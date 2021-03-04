from os.path import join

import nrrd
import numpy as np
from skimage.transform import resize, iradon
import matplotlib.pyplot as plt

from rand_functions.helper_functions import gen_file_list, random_shuffle


class BatchDataGen:
    def __init__(self, file_path, mask_path, batch_size):
        self.file_path = file_path
        self.mask_path = mask_path
        self.batch_size = batch_size

    def gen_batch(self):
        file_list = gen_file_list(self.file_path)
        mask_list = gen_file_list(self.mask_path)

        while True:
            # file_list, mask_list = random_shuffle(file_list, mask_list)
            for (file, mask) in zip(file_list, mask_list):

                X = load_data(file, self.file_path)
                Y = load_data(mask, self.mask_path)
                # X, Y = random_shuffle(X, Y)
                X = np.array(X)
                Y = np.array(Y)
                for i in range(X.shape[0] // self.batch_size):
                    x_batch = X[i * self.batch_size:(i + 1) * self.batch_size, ...]
                    y_batch = Y[i * self.batch_size:(i + 1) * self.batch_size, ...]

                    yield x_batch, y_batch



def load_data(data, data_path):
    data, header = nrrd.read(join(data_path, data), index_order='C')
    output_size = data.shape[1]
    radius = output_size // 2
    xpr, ypr = np.mgrid[:output_size, :output_size] - radius
    img_stack = np.zeros((len(data), 512,512))
    for idx in range(len(data)):
        masked = data[idx,:,:]
        # resized = resize(orig, (512,512), order=1)
        mask_circle = (xpr ** 2 + ypr ** 2) > radius ** 2
        masked[mask_circle] = 0
        img_stack[idx,:,:] = masked
    # data = np.array(data).transpose(2, 1, 0)  # nrrd read/write order shenanigans

    data = img_stack[:, :, :, np.newaxis]
    # np.clip(data, -1., 1., out=data)
    data = 2. * (data - np.min(data)) / np.ptp(data) - 1
    return data

def load_dataGAN(data, data_path):
    data, header = nrrd.read(join(data_path, data), index_order='C')

    # data = np.array(data).transpose(2, 1, 0)  # nrrd read/write order shenanigans
    # data = (data - np.min(data)) / np.ptp(data)
    data = 2.*((data - np.min(data))  / np.ptp(data))-1
    data = data.transpose(0, 2, 1)
    # np.clip(data, -1., 1., out=data)
    # data = data[:, :, :, np.newaxis]

    return data

class BatchDataGenGAN:
    def __init__(self, file_path, mask_path, batch_size=1):
        self.file_path = file_path
        self.batch_size = batch_size
        self.mask_path = mask_path

    def gen_batch(self):
        file_list = gen_file_list(self.file_path)
        mask_list = gen_file_list(self.mask_path)

        while True:
            #file_list, mask_list = random_shuffle(file_list, mask_list)

            file_list, mask_list = random_shuffle(file_list, mask_list)
            for (file, mask) in zip(file_list, mask_list):
                X = load_dataGAN(file, self.file_path)
                Y = load_data(mask, self.mask_path)

                # X, Y = random_shuffle(X, Y)
                X = np.array(X)
                Y = np.array(Y)
                for i in range(X.shape[0] // self.batch_size):
                    y_batch = Y[i * self.batch_size:(i + 1) * self.batch_size, ...]
                    x_batch = X[i * self.batch_size:(i + 1) * self.batch_size, ...]
                    # dict = {}
                    temp_batch = []
                    # it = 1
                    for j in range(self.batch_size):
                        it = 0

                        # it2 = 1
                        # output_name = 'output_{:03d}'.format(it)
                        num_proj = x_batch[j].shape[1]
                        temp_projections = np.zeros((Y.shape[1], Y.shape[2], num_proj))
                        # print(temp_projections.shape)
                        if num_proj == 2:
                            theta = np.linspace(0, 180, num_proj, False)
                        else:
                            theta = np.linspace(0, 180, num_proj, True)
                        rec = iradon(x_batch[j], theta=theta, output_size=Y.shape[1], gen_individual_backprojections=True,
                                     filter=None)
                        for image in rec:
                            # name = 'img_{:03d}_{:03d}'.format(it, it2)
                            # dict = {name : image_new, output_name : Y[(it-1)*self.batch_size]}
                            # dict[name] = image_new
                            # it2 +=
                            temp_projections[:,:,it] = image
                            it += 1
                        # dict[output_name] = Y[(it-1)*self.batch_size]
                        # it+=1
                        temp_batch.append(temp_projections)
                    # temp_batch = 2. * (temp_batch - np.min(temp_batch)) / np.ptp(temp_batch) - 1
                    # np.clip(temp_batch, -1., 1., out=temp_batch)
                    # print(temp_batch.shape)
                # for y in y_batch:
                #     z = np.squeeze(y)
                #     plt.imshow(z, cmap='gray')
                #     plt.show()
                    # for t in temp_batch:
                    #     g = np.transpose(t, (2,1,0))
                    #     for data in g:
                    #         plt.imshow(data, cmap='gray')
                    #         plt.show()
                    # for projections in temp_batch:
                    # print(y_batch.shape)

                    yield np.asarray(temp_batch), y_batch


# sinogram_path = "../2dprojections/test_sino"
# gt_path = "../2dprojections/test_gt"
# proba = BatchDataGenGAN(sinogram_path, gt_path, 4).gen_batch()
# while True:
#     batchx, batchy = next(proba)
#     for img in batchy:
#         im = np.squeeze(img)
#         plt.imshow(im, cmap='gray')
#         plt.show()
# print(batch)

