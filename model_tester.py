from u_net import unet_build
from neural_net_training.save_load_model import load_model
from neural_net_training.batch_generator import BatchDataGenGAN, BatchDataGen
from neural_net_training.models import SSIM, simple_autoencoder
from rand_functions.helper_functions import gen_file_list
import numpy as np
import tensorflow as tf
import nrrd
from tqdm import tqdm
import matplotlib.pyplot as plt

num_files_per_nrrd = 128
batchsize = 4

train_data_path = "./2dprojections/test_sino"
train_mask_path = "./2dprojections/test_gt"
valid_data_path = "./results_statistics/sparse_view_sino/15_angles"
valid_mask_path = "./results_statistics/sparse_view_ground_truth"
proba = BatchDataGenGAN(train_data_path, train_mask_path, batchsize).gen_batch()
# x_batch, y_batch = next(proba)

valid_list = gen_file_list(valid_data_path)

model = unet_build(2, (512,512,15), filters=[32, 64, 128, 256, 512], actfn='relu', is_batchnorm=False,
                lastActivation='tanh', residual=True)
# model = simple_autoencoder()
model.load_weights("eeeh_100.h5")

# model = tf.keras.models.load_model("unet_only_56.h5", custom_objects={'loss':SSIM}, compile=False)
results = []
gt = []
noisy = []
# for i in tqdm(range(len(valid_list)*num_files_per_nrrd // batchsize)):
for i in tqdm(range(5)):

    x_pred, y_pred = next(proba)
    y_hat = model.predict(x_pred)
    y_hat = np.squeeze(y_hat)
    y_pred = np.squeeze(y_pred)
    x_pred = np.squeeze(x_pred)


    for j in range(y_pred.shape[0]):
        # plt.imshow(y_hat[j])
        # plt.show()
        noisy.append(x_pred[j])
        results.append(y_hat[j])
        gt.append(y_pred[j])
        # nrrd.write('./test_figures/nvidia_{:02d}.nrrd'.format(i), y_hat, compression_level=1, index_order='C')
        # nrrd.write('./test_figures/gt{:02d}.nrrd'.format(i), y_pred, compression_level=1, index_order='C')
noisy = np.array(noisy)
results = np.array(results)
# results = np.roll(results, 128, 0)
gt = np.array(gt)
nrrd.write('./results_statistics/sparse_view_recon/15_angles_unet/15_unet.nrrd', results, compression_level=1, index_order='C')
nrrd.write('./results_statistics/sparse_view_noisy/15_angles/15_noisy_full.nrrd', noisy, compression_level=1, index_order='C')
nrrd.write('./results_statistics/sparse_view_gt_concat/sparse_15_gt.nrrd', gt, compression_level=1, index_order='C')
print(noisy.shape)