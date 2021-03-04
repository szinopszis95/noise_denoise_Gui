import matplotlib.pyplot as plt
from skimage.metrics import peak_signal_noise_ratio, structural_similarity, mean_squared_error
import numpy as np
from scipy import stats
from rand_functions.helper_functions import gen_file_list
import tensorflow as tf
from tensorflow.keras.backend import get_value
from os.path import join

import nrrd

def _MSE(ground_truth, prediction):
    return mean_squared_error(ground_truth, prediction)

def PSNR(ground_truth, prediction):
    return peak_signal_noise_ratio(ground_truth, prediction)


def SSIM(ground_truth, prediction):
    return structural_similarity(ground_truth, prediction)


def visualize(ground_truth, reconstructed, prediction, i):
    ground_truth = np.squeeze(ground_truth)
    reconstructed = np.squeeze(reconstructed)
    prediction = np.squeeze(prediction)

    ground_truth = ground_truth[i, :, :]
    reconstructed = reconstructed[i, :, :]
    prediction = prediction[i, :, :]

    reconstructed_ssim = SSIM(ground_truth, reconstructed)
    reconstructed_psnr = PSNR(ground_truth, reconstructed)
    prediction_ssim = SSIM(ground_truth, prediction)
    prediction_psnr = PSNR(ground_truth, prediction)

    fig, ax = plt.subplots(1, 3, figsize=(12, 6))
    ax[0].title.set_text('Ground truth')
    ax[1].title.set_text('Reconstructed \n PSNR: {:.3f} \n SSIM: {:.3f}'.format(reconstructed_psnr, reconstructed_ssim))
    ax[2].title.set_text('Autoencoder - MSE loss\n PSNR: {:.3f} \n SSIM: {:.3f}'.format(prediction_psnr, prediction_ssim))

    ax[0].imshow(ground_truth, cmap='gray')
    ax[1].imshow(reconstructed, cmap='gray')
    ax[2].imshow(prediction, cmap='gray')
    plt.show()
    # plt.savefig('autoencoder_mse_{:03d}.png'.format(i))
    return prediction_ssim, prediction_psnr
    # plt.show()


def make_stat(file):
    array = np.load(file)
    min = np.min(array)
    max = np.max(array)
    mean = np.mean(array)
    std = np.std(array)
    var = np.var(array)
    sem = stats.sem(array)

    print(np.around(min, 3), np.around(max, 3), np.around(mean, 3), np.around(std, 3), np.around(var, 3),
          np.around(sem, 3))

def calc_stats(array):
    min = np.min(array)
    max = np.max(array)
    mean = np.mean(array)
    std = np.std(array)
    var = np.var(array)
    sem = stats.sem(array)

    return np.array((min, max, mean, std, var, sem))


def load_data(data, data_path):
    data, header = nrrd.read(join(data_path, data), index_order='C')
    data = np.array(data).astype(np.float32)
    return data

# make_stat('encoder_ssim_ssim_values.npy')
def gen_stats(gt_path, recon_path, noisy_path, name):
    gt_list = gen_file_list(gt_path)
    recon_list = gen_file_list(recon_path)
    noisy_list = gen_file_list(noisy_path)

    _mse_array = []
    _psnr_array = []
    _ssim_array = []
    _ms_ssim_array = []
    current_best = 0
    current_worst = 1


    for (gt, recon, noisy) in zip(gt_list, recon_list, noisy_list):
        X = load_data(gt, gt_path)
        Y = load_data(recon, recon_path)
        Z = load_data(noisy, noisy_path)

        X = np.array(X)
        Y = np.array(Y)
        Z = np.array(Z)
        X = np.squeeze(X)
        Y = np.squeeze(Y)
        Z = np.squeeze(Z)


        for i in range(X.shape[0]):
            _mse_array.append(_MSE(X[i], Y[i]))
            _psnr_array.append(PSNR(X[i], Y[i]))
            _ssim_array.append(SSIM(X[i], Y[i]))
            # fig, ax = plt.subplots(1, 2, figsize=(12, 6))
            # ax[0].imshow(X[i], cmap='gray')
            # ax[1].imshow(Y[i], cmap='gray')
            # plt.show()

            x = X[i, :, :, np.newaxis]
            y = Y[i, :, :, np.newaxis]
            _ms_ssim = get_value(tf.image.ssim_multiscale(x, y, 2))
            _ms_ssim_array.append(_ms_ssim)

            if(_ms_ssim > current_best):
                 current_best = _ms_ssim
                 best_x = X[i]
                 best_y = Y[i]
                 best_z = Z[i]
            if(_ms_ssim < current_worst):
                 current_worst = _ms_ssim
                 worst_x = X[i]
                 worst_y = Y[i]
                 worst_z = Z[i]
    nrrd.write(recon_path + '/best_gt_{}.nrrd'.format(name), best_x, compression_level=1, index_order='C')
    nrrd.write(recon_path +'/best_recon_{}.nrrd'.format(name), best_y, compression_level=1, index_order='C')
    nrrd.write(recon_path +'/best_noisy_{}.nrrd'.format(name), best_z, compression_level=1, index_order='C')

    nrrd.write(recon_path +'/worst_gt_{}.nrrd'.format(name), worst_x, compression_level=1, index_order='C')
    nrrd.write(recon_path +'/worst_recon_{}.nrrd'.format(name), worst_y, compression_level=1, index_order='C')
    nrrd.write(recon_path +'/worst_noisy_{}.nrrd'.format(name), worst_z, compression_level=1, index_order='C')

    stats = np.empty((6, 4))
    stats[:,0] = calc_stats(_mse_array)
    stats[:,1] = calc_stats(_psnr_array)
    stats[:,2] = calc_stats(_ssim_array)
    stats[:,3] = calc_stats(_ms_ssim_array)

    np.savetxt(recon_path+ '/nvidia.csv', stats, delimiter=',')

gt_path = "./results_statistics/sparse_view_gt_concat"
recon_path = "./results_statistics/sparse_view_recon/nvidia"
noisy_path = "./results_statistics/sparse_view_noisy"
gen_stats(gt_path, recon_path, noisy_path, 'nvidia')


