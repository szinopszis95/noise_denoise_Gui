import nrrd
import numpy as np
from neural_net_training.models import u_net, SSIM, simple_autoencoder
from neural_net_training.save_load_model import save_model
import tensorflow as tf
import functools
import matplotlib.pyplot as plt
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import AveragePooling2D, AveragePooling3D, UpSampling2D, UpSampling3D
from tensorflow.keras.layers import Input, Conv2D, Conv3D, BatchNormalization, Concatenate
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam

from neural_net_training.batch_generator import BatchDataGen, BatchDataGenGAN, load_data, gen_file_list
from rand_functions.helper_functions import random_shuffle

# train_data_path = "./train_data/reconstructed"
# train_mask_path = "./train_data/ground_truth"
# valid_data_path = "./valid_data/reconstructed"
# valid_mask_path = "./valid_data/ground_truth"

train_data_path = "./2dprojections/selected_sino"
train_mask_path = "./2dprojections/selected_gt"
valid_data_path = "./2dprojections/test_sino"
valid_mask_path = "./2dprojections/test_gt"


def UnetConv(dim, input, filtersnum, is_batchnorm, actfn, name, res=True):
    block = tf.keras.models.Sequential(name=name)

    block.add(ConvSolution(dim, filtersnum, kernel_initializer="glorot_normal", padding="same", name=name + '_1'))
    if is_batchnorm:
        block.add(BatchNormalization(name=name + '_1_bn'))
        block.add(Activation(actfn, name=name + '_1_act'))
        block.add(ConvSolution(dim, filtersnum, kernel_initializer="glorot_normal", padding="same", name=name + '_2'))
    if is_batchnorm:
        block.add(BatchNormalization(name=name + '_2_bn'))
        block.add(Activation(actfn, name=name + '_2_act'))
    if (res):
        if (dim == 2):
            projected_input = Conv2D(filtersnum, (1, 1), strides=(1, 1), kernel_initializer="glorot_normal",
                                     padding="same", name=name + '_proj')(input)
        elif (dim == 3):
            projected_input = Conv3D(filtersnum, (1, 1, 1), strides=(1, 1, 1), kernel_initializer="glorot_normal",
                                     padding="same", name=name + '_proj')(input)
        x = block(input) + projected_input
        x = Activation(actfn, name=name + '_res_act')(x)
    else:
        x = block(input)

    return x


def ConvSolution(dim, filtersnum, kernel_initializer, padding, name):
    if (dim == 2):
        return Conv2D(filtersnum, (3, 3), strides=(1, 1), kernel_initializer=kernel_initializer, padding=padding,
                      name=name)
    elif (dim == 3):
        return Conv3D(filtersnum, (3, 3, 3), strides=(1, 1, 1), kernel_initializer=kernel_initializer, padding=padding,
                      name=name)


def PoolingSolution(dim):
    if (dim == 2):
        return AveragePooling2D(pool_size=(2, 2))
    elif (dim == 3):
        return AveragePooling3D(pool_size=(2, 2, 2))


def UpsamplingSolution(dim):
    if (dim == 2):
        return UpSampling2D()
    elif (dim == 3):
        return UpSampling3D()


def unet_build(dim, input_size, filters, actfn, is_batchnorm, lastActivation=None, residual=False):
    '''
    Direct 3D analogue of the above defined unet.
    '''
    m = {}


    m["inputs"] = Input(shape=input_size)

    last = m["inputs"]
    for d in range(len(filters) - 1):
        m[f"conv{d}_l"] = UnetConv(dim, last, filters[d], is_batchnorm, actfn, name=f"conv{d}_l", res=residual)
        m[f"pool{d}"] = PoolingSolution(dim)(m[f"conv{d}_l"])
        last = m[f"pool{d}"]
        d += 1
        m[f"conv{d}_r"] = UnetConv(dim, last, filters[d], is_batchnorm, actfn, name=f"conv{d}_r", res=residual)

    for d in range(len(filters) - 1, 0, -1):
        m[f"up{d - 1}_r"] = Concatenate(axis=-1)([UpsamplingSolution(dim)(m[f"conv{d}_r"]), m[f"conv{d - 1}_l"]])
        m[f"conv{d - 1}_r"] = UnetConv(dim, m[f"up{d - 1}_r"], filters[d - 1], is_batchnorm, actfn,
                                       name=f"conv{d - 1}_r",
                                       res=residual)
    if (dim == 2):
        m[f"conv{0}_r"] = Conv2D(1, (1, 1), activation=lastActivation, name='final', dtype='float32')(
            m[f"conv{d - 1}_r"])  # mixed precision training
    elif (dim == 3):
        m[f"conv{0}_r"] = Conv3D(1, (1, 1, 1), activation=lastActivation, name='final', dtype='float32')(
            m[f"conv{d - 1}_r"])  # mixed precision training

    model = Model(inputs=[m["inputs"]], outputs=[m[f"conv{0}_r"]])
    return model

def maxDepth(input_shape):
    max_depths = []
    for n in input_shape:
        c = 0
        while n > 1:
            if n % 2 == 0:
                n /= 2
                c += 1
            else:
                break
        max_depths.append(c)
    return max_depths


def gen_batch_alter(file_list, mask_list, batch_size):
    while True:
        file_list, mask_list = random_shuffle(file_list, mask_list)
        for (file, mask) in zip(file_list, mask_list):

            X = load_data(file, train_data_path)
            Y = load_data(mask, train_mask_path)
            X, Y = random_shuffle(X, Y)
            X = np.array(X)
            Y = np.array(Y)
            for i in range(X.shape[0] // batch_size):
                x_batch = X[i * batch_size:(i + 1) * batch_size, ...]
                y_batch = Y[i * batch_size:(i + 1) * batch_size, ...]

                yield x_batch, y_batch


# train_mask_path = "./train_data/selected_gt"
# train_data_path = "./train_data/selected_recon"
# num_files_per_nrrd = 128
# batch_size = 4
# #
# list_data = gen_file_list(train_data_path)
# x_batch, y_batch = next(BatchDataGen(train_data_path, train_mask_path, batch_size).gen_batch())
# train_datagen = BatchDataGen(train_data_path, train_mask_path, batch_size).gen_batch()
# # # valid_datagen = BatchDataGenGAN(valid_data_path, valid_mask_path, batch_size).gen_batch()
# # #
# # #
# _callbacks = [
#     ModelCheckpoint(filepath='unet_new_ssim_100_{epoch:02d}.h5', monitor='loss', mode='min', save_best_only=True, save_freq=10),
#     EarlyStopping(monitor='loss', mode='min', verbose=1, patience=10)
# ]
# # # # #
# model = unet_build(2, (512,512,1), filters=[32, 64, 128, 256, 512], actfn='relu', is_batchnorm=False,
#                lastActivation='tanh', residual=True)
# # #
# # model = u_net(x_batch)
# model.load_weights("unet_new_ssim_100_59.h5")
# # # model = tf.keras.models.load_model("resnet_50_21.h5", custom_objects={'loss':SSIM}, compile=False)
# model.summary()
# opt = tf.keras.optimizers.Adam(1e-4)
# model.compile(optimizer=opt, loss=SSIM)
# # # # #
# trained_model = model.fit(train_datagen, steps_per_epoch=len(list_data)*num_files_per_nrrd//batch_size, epochs=42, callbacks=_callbacks)
# # # # #
# save_model(model, 'unet_new_ssim_100')

#####

#
# _callbacks2 = [
#     ModelCheckpoint(filepath='unet_new_mse_100_{epoch:02d}.h5', monitor='loss', mode='min', save_best_only=True, save_freq=10),
#     EarlyStopping(monitor='loss', mode='min', verbose=1, patience=10)
# ]
#
# model2 = unet_build(2, (512,512,1), filters=[32, 64, 128, 256, 512], actfn='relu', is_batchnorm=False,
#                lastActivation='tanh', residual=True)
# model2.compile(optimizer=opt, loss='mse')
# trained_model2 = model2.fit(train_datagen, steps_per_epoch=len(list_data)*num_files_per_nrrd//batch_size, epochs=100, callbacks=_callbacks2)
# save_model(model2, 'unet_new_mse_100')
# #####
#
#
#
# _callbacks3 = [
#     ModelCheckpoint(filepath='autoencoder_new_mse_100_{epoch:02d}.h5', monitor='loss', mode='min', save_best_only=True, save_freq=10),
#     EarlyStopping(monitor='loss', mode='min', verbose=1, patience=10)
# ]
#
# model3 = simple_autoencoder(x_batch)
# model3.compile(optimizer=opt, loss='mse')
# trained_model3 = model3.fit(train_datagen, steps_per_epoch=len(list_data)*num_files_per_nrrd//batch_size, epochs=100, callbacks=_callbacks3)
# save_model(model3, 'autoencoder_new_mse_100')
#

#######
# _callbacks4 = [
#     ModelCheckpoint(filepath='autoencoder_new_ssim_100_{epoch:02d}.h5', monitor='loss', mode='min', save_best_only=True, save_freq=10),
#     EarlyStopping(monitor='loss', mode='min', verbose=1, patience=10)
# ]
#
# model4 = simple_autoencoder(x_batch)
# model4.compile(optimizer=opt, loss=SSIM)
# trained_model3 = model4.fit(train_datagen, steps_per_epoch=len(list_data)*num_files_per_nrrd//batch_size, epochs=100, callbacks=_callbacks4)
# save_model(model4, 'autoencoder_new_ssim_100')



# plt.plot(trained_model.history['loss'])
# plt.plot(trained_model.history['val_loss'])
# plt.title('model loss')
# plt.ylabel('loss')
# plt.xlabel('epoch')
# plt.legend(['train', 'test'], loc='upper left')
# plt.savefig('10_epoch')
# plt.show()
#
# model = load_model("resnet_new_epoch")
# model = tf.keras.models.load_model("unet_new_none_checkpoint.h5", custom_objects={'loss':SSIM}, compile=False)
#
# proba = BatchDataGenGAN(train_data_path, train_mask_path, 4).gen_batch()
# for i in range(10):
#     x_pred, y_pred = next(proba)
#     y_hat = model.predict(x_pred)
#     y_hat = np.squeeze(y_hat)
#     y_pred = np.squeeze(y_pred)
#     x_pred = np.squeeze(x_pred)
#     nrrd.write('pred_15_angles{:02d}.nrrd'.format(i), y_hat, compression_level=1, index_order='C')
    # nrrd.write('gt_{:02d}.nrrd'.format(i), y_pred, compression_level=1, index_order='C')
    # nrrd.write('valami2_noise.nrrd', x_pred, compression_level=1, index_order='C')

# class UnetBuilder():
#     def __init__(self, input_size, targetdepth):
#         self.maxDepths = maxDepth(input_size)
#         print(targetdepth, self.maxDepths)
#
#
# def discriminator_model(input_size, actfn, is_batchnorm):
#     inputs = Input(shape=input_size)
#     conv1 = UnetConv3D(inputs, 16, is_batchnorm, actfn, name='conv1')
#     pool1 = AveragePooling3D(pool_size=(2, 2, 2))(conv1)
#     conv2 = UnetConv3D(pool1, 32, is_batchnorm, actfn, name='conv2')
#     pool2 = AveragePooling3D(pool_size=(2, 2, 2))(conv2)
#     conv3 = UnetConv3D(pool2, 64, is_batchnorm, actfn, name='conv3')
#     pool3 = AveragePooling3D(pool_size=(2, 2, 2))(conv3)
#     conv4 = UnetConv3D(pool3, 128, is_batchnorm, actfn, name='conv4')
#     pool4 = AveragePooling3D(pool_size=(2, 2, 2))(conv4)
#     conv5 = UnetConv3D(pool4, 16, is_batchnorm, actfn, name='conv5')
#     f = Flatten()(conv5)
#     d = Dense(1, dtype='float32')(f)
#     model = Model(inputs=[inputs], outputs=[d])
#     return model

# def laplacianFilter(alpha):
#     laplacian = np.array([
#         [alpha/4, (1-alpha)/4, alpha/4],
#         [(1-alpha)/4, -1, (1-alpha)/4],
#         [alpha/4, (1-alpha)/4, alpha/4]
#     ])
#     laplacian = (4/(alpha+1)) * laplacian
#     return laplacian
#
#
# kernel = -1/256 * np.array([
#         [1, 4, 6,4,1],
#         [4,16,24,16,4],
#         [6,24,-476,24,6],
#         [4,16,24,16,4],
#         [1,4,6,4,1]
#     ])
# alpha = 0.5
# laplacian = laplacianFilter(alpha)
#
# phi = 2
# theta = 2
# maxIntensity = 1
#
# def enhance_edge(file):
#     file, header = nrrd.read(file, index_order='C')
#     file_enhanced = []
#     for i in range(file.shape[0]):
#         enhanced = scipy.ndimage.convolve(file[i], kernel, mode='nearest')
#         # enhanced[enhanced < 0.005] = 0
#         # enhanced = file[i] - enhanced
#         # enhanced = (maxIntensity / phi) * (enhanced / (maxIntensity / theta)) ** 2
#         file_enhanced.append(enhanced)
#     nrrd.write('valami2_enhanced.nrrd', np.array(file_enhanced), index_order='C', compression_level=1)
#
# enhance_edge('valami2.nrrd')
#
# generator_optimizer = Adam(
#     learning_rate=0.0002, beta_1=0.5, beta_2=0.9)
# discriminator_optimizer = Adam(
#     learning_rate=0.0002, beta_1=0.5, beta_2=0.9)
#
#
# # Define the loss functions to be used for discrimiator
# # This should be (fake_loss - real_loss)
# # We will add the gradient penalty later to this loss function
# def discriminator_loss(real_img, fake_img):
#     real_loss = tf.reduce_mean(real_img)
#     fake_loss = tf.reduce_mean(fake_img)
#     return fake_loss - real_loss
#
#
# # Define the loss functions to be used for generator
# def generator_loss(fake_img):
#     return -tf.reduce_mean(fake_img)
#
#
# # Epochs to train
# epochs = 20
#
# # Get the wgan model
# noise_dim = 128
# d_model = get_discriminator_model(x_batch)
# g_model = get_generator_model(noise_dim)
# d_model.summary()
# g_model.summary()
#
# wgan = WGAN(
#     discriminator=d_model,
#     generator=g_model,
#     latent_dim=noise_dim,
#     discriminator_extra_steps=3,
# )
#
# # Compile the wgan model
# wgan.compile(
#     d_optimizer=discriminator_optimizer,
#     g_optimizer=generator_optimizer,
#     g_loss_fn=generator_loss,
#     d_loss_fn=discriminator_loss,
# )
#
# # Start training
# trained_model = wgan.fit(x_batch, steps_per_epoch=2, epochs=50)
