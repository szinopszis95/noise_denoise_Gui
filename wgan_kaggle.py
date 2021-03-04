import numpy as np # linear algebra

import os
import sys
from tqdm import tqdm, tqdm_notebook
import glob
import shutil
import time      # time.perf_counter()
import random

import matplotlib.pyplot as plt
import tensorflow as tf
import xml.etree.ElementTree as ET
from u_net import unet_build
from keras.layers import Input, Dense, Reshape, Flatten
from keras.layers import BatchNormalization, Activation
from keras.layers.advanced_activations import LeakyReLU
from keras.layers.convolutional import UpSampling2D, Conv2D
from keras.models import Model
from keras import backend as K
from keras.optimizers import Adam
from neural_net_training.batch_generator import BatchDataGenGAN
from rand_functions.helper_functions import gen_file_list
from neural_net_training.save_load_model import save_model
from dists_loss import DISTS

tf.compat.v1.disable_eager_execution()

img_shape = (512,512,1)
batch_size = 4
train_data_path = "./2dprojections/selected_60"
train_mask_path = "./2dprojections/selected_gt"
file_list_length = len(gen_file_list(train_data_path))
train_datagen = BatchDataGenGAN(train_data_path, train_mask_path, batch_size).gen_batch()
predict_gen = BatchDataGenGAN(train_data_path, train_mask_path, batch_size).gen_batch()
x_batch, y_batch = next(train_datagen)
num_files_per_nrrd = 128
num_epochs = 100

steps_per_epoch_calc = file_list_length*num_files_per_nrrd//batch_size

penaltyLambda = 10    # d_loss = f_loss - r_loss + λ･penalty
gen_lambda = 1e-3

# critic(discriminator) iterations per generator iteration
trainRatio = 5
rec_interval = 10000
alpha = 0.84
_dists_init = DISTS()

def build_discriminator():
    input = Input(shape=img_shape)
    x = Conv2D(64, kernel_size=4, strides=2, padding="same", use_bias=False)(input)
    x = LeakyReLU(0.2)(x)
    x = Conv2D(128, kernel_size=4, strides=2, padding="same", use_bias=False)(x)
    x = LeakyReLU(0.2)(x)
    x = Conv2D(256, kernel_size=4, strides=2, padding="same", use_bias=False)(x)
    x = Conv2D(256, kernel_size=3, strides=1, padding="same", use_bias=False)(x)
    x = LeakyReLU(0.2)(x)
    x = Conv2D(256, kernel_size=3, strides=1, padding="same", use_bias=False)(x)
    x = LeakyReLU(0.2)(x)
    x = Conv2D(512, kernel_size=4, strides=2, padding="same", use_bias=False)(x)
    x = LeakyReLU(0.2)(x)
    x = Conv2D(1, kernel_size=1, strides=1, padding="same", use_bias=False)(x)
    x = Flatten()(x)
    x = Dense(units=1, activation=None)(x)  # activation = None

    model = Model(input, x)
    print("●discriminator")
    model.summary()
    return model


def build_WGANgp(generator, discriminator):
    #### model
    # generator image(fake image)
    generator_input = Input(shape=x_batch[0].shape)
    f_img = generator(generator_input)
    f_out = discriminator(f_img)
    # real image
    r_img = Input(shape=img_shape)
    r_out = discriminator(r_img)
    # average image
    epsilon = K.placeholder(shape=(None, 1, 1, 1))
    a_img = Input(shape=(img_shape),
                  tensor=epsilon * r_img + (1 - epsilon) * f_img)
    a_out = discriminator(a_img)

    #### loss
    # original critic(discriminator) loss
    r_loss = K.mean(r_out)
    f_loss = K.mean(f_out)
    r_gen = K.mean(r_img)
    f_gen = K.mean(f_img)
    # gradient penalty  <this is point of WGAN-gp>
    grad_mixed = K.gradients(a_out, [a_img])[0]
    norm_grad_mixed = K.sqrt(K.sum(K.square(grad_mixed), axis=[1, 2, 3]))
    grad_penalty = K.mean(K.square(norm_grad_mixed - 1))
    penalty = penaltyLambda * grad_penalty
    # d loss
    d_loss = f_loss - r_loss + penalty
    L1 = K.mean(K.abs(f_img-r_img))
    MS_SSIM = 1 - tf.reduce_mean(tf.image.ssim_multiscale(r_img, f_img, 2.0))
    NVIDIA = alpha*(1 - (tf.reduce_mean(tf.image.ssim_multiscale(r_img, f_img, 2.0)))) + ((1-alpha)*K.mean(K.abs(f_img -r_img)))
    SSIM = 1 - tf.reduce_mean(tf.image.ssim(r_img, f_img, 2.0))
    dist_loss = _dists_init.get_score(r_img, f_img)

    #### discriminator update function
    d_updates = Adam(lr=1e-4, beta_1=0.5, beta_2=0.9). \
        get_updates(params=discriminator.trainable_weights, loss=d_loss)
    d_train = K.function([r_img, generator_input, epsilon],
                         [r_loss, f_loss, penalty, d_loss],
                         d_updates)

    #### generator update function
    g_loss = SSIM - (1e-3*f_loss)
    g_updates = Adam(lr=1e-4, beta_1=0.5, beta_2=0.9). \
        get_updates(params=generator.trainable_weights, loss=g_loss)
    g_train = K.function([generator_input, r_img], [r_gen, f_gen, g_loss], g_updates)

    return g_train, d_train

generator = unet_build(2, x_batch.shape[1:], filters=[32, 64, 128, 256, 512], actfn='relu', is_batchnorm=False,
             lastActivation='tanh', residual=True)
generator.summary()
discriminator = build_discriminator()

#generator.load_weights("./saved_models/resnet_wgangp_gen_ms_nvidia2_weights.h5")
#discriminator.load_weights("./saved_models/resnet_wgangp_disc_ms_nvidia2_weights.h5")
G_train, D_train = build_WGANgp(generator, discriminator)

g_loss_list = []
r_loss_list = []
f_loss_list = []
f_r_loss_list = []
penalty_list = []
d_loss_list = []
g_loss_list = []

kernel_start = time.perf_counter()
kernel_time_limit = 60*60*8.5


import matplotlib

matplotlib.use("Agg")
from matplotlib import colors, gridspec, pyplot as plt
def plot_img(img):

    norm = colors.Normalize(-1, 1)
    plt.imshow(img, norm=norm, interpolation='nearest',
               cmap='gray')
    plt.gca().tick_params(left=False, bottom=False,
                          labelleft=False, labelbottom=False)


def plot_samples(gen, batch_gen,
                 num_samples=16, samples_per_row=8, out_fn=None):
    fake_images, real_images = next(predict_gen)
    num_samples = min(num_samples, real_images.shape[0])
    generated_images = gen.predict(fake_images)

    num_rows = int(np.ceil(num_samples / samples_per_row))
    num_cols = samples_per_row
    plt.figure(figsize=(1.5 * num_cols, 2 * 1.5 * num_rows))
    gs = gridspec.GridSpec(2, 1, hspace=0.1)
    gs_real = gridspec.GridSpecFromSubplotSpec(num_rows, num_cols,
                                               hspace=0.02, wspace=0.02, subplot_spec=gs[0, 0])
    gs_gen = gridspec.GridSpecFromSubplotSpec(num_rows, num_cols,
                                              hspace=0.02, wspace=0.02, subplot_spec=gs[1, 0])

    for k in range(num_samples):
        i = k // samples_per_row
        j = k % samples_per_row

        plt.subplot(gs_real[i, j])
        plot_img(real_images[k, :, :, 0])

        plt.subplot(gs_gen[i, j])
        plot_img(generated_images[k, :, :, 0])

    if out_fn is not None:
        plt.savefig(out_fn, bbox_inches='tight')
        plt.close()

for i in range(num_epochs):
    plot_fn = "./figures/wgan_try_samples_{:03d}.png".format(i)
    print("Epoch {}/{}".format(i + 1, num_epochs))
    progbar = tf.keras.utils.Progbar(
        steps_per_epoch_calc * batch_size)
    for step in range(steps_per_epoch_calc):

        #### Discriminator
        for j in range(trainRatio):
            # Generator in
            image_batch_fake, image_batch_real = next(train_datagen)
            # Generator out Images
            f_imgs = generator.predict(image_batch_fake)
            # Real Images
            r_imgs = image_batch_real
            # train the discriminator
            epsilon = np.random.uniform(size=(batch_size, 1, 1, 1))
            r_loss, f_loss, penalty, d_loss = D_train([r_imgs, image_batch_fake, epsilon])

        #### Generator
        # Generator in
        image_batch_fake, image_batch_real = next(train_datagen)
        # train the generator
        r_gen, f_gen, g_loss = G_train([image_batch_fake, image_batch_real])

        if (step % 50 == 0):
            save_model(generator, 'resnet_wgangp_gen_try')
            save_model(discriminator, 'resnet_wgangp_disc_try')



        #### Record of learning progress
        # loss
        r_loss_list.append(r_loss)
        f_loss_list.append(f_loss)
        f_r_loss_list.append(f_loss - r_loss)
        penalty_list.append(penalty)
        d_loss_list.append(d_loss)
        g_loss_list.append(g_loss)

        losses = []
        losses.append(("D1", r_loss))
        losses.append(("D2", f_loss))
        losses.append(("D3", d_loss))
        losses.append(("penalty", penalty))
        losses.append(("G0", g_loss))
        progbar.add(batch_size, values=losses)

    plot_samples(generator, predict_gen, out_fn=plot_fn)
        # print(f'iteration:{i} / d_loss:{d_loss:.3f} / g_loss:{sum(g_loss) / len(g_loss):.3f}')




# def sumple_images(imgs, rows=3, cols=3, figsize=(12, 10)):
#     fig, axes = plt.subplots(nrows=rows, ncols=cols, figsize=figsize)
#     for indx, axis in enumerate(axes.flatten()):
#         img = image.array_to_img(imgs[indx])  # ndarray → PIL
#         imgplot = axis.imshow(img)
#         axis.set_axis_off()
#     plt.tight_layout()
    # generated image sumple
    # if (iteration in [100, 1000]) or (iteration % rec_interval == 0):
    #     print(f'iteration:{iteration} / d_loss:{d_loss:.3f} / g_loss:{sum(g_loss) / len(g_loss):.3f}')
    #     g_imgs = generator.predict(z_fix)
    #     imgs = g_imgs * 127.5 + 127.5
    #     sumple_images(imgs, rows=1, cols=7)
    #     plt.show()

    i += 1

print("last iteration:", i - 1)