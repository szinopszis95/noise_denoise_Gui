import os
from math import ceil

import nrrd
import numpy as np
import odl
import pydicom
from skimage.transform import resize
from tqdm import tqdm
import astra

from rand_functions.helper_functions import rescale, list_files

class SinogramGeneration3:
    FLAG = False
    MU_WATER = 20
    MU_AIR = 0.02
    MU_MAX = 3071 * (MU_WATER - MU_AIR) / 1000 + MU_WATER
    # ~26cm x 26cm images
    MIN_PT = [-0.13, -0.13]
    MAX_PT = [0.13, 0.13]
    NUM_ANGLES = 1000
    RECO_IM_SHAPE = (512, 512)
    # image shape for simulation
    IM_SHAPE = (1000, 1000)
    PHOTONS_PER_PIXEL = 4096
    NUM_SAMPLES_PER_FILE = 128


    def __init__(self, sinogram_path, gt_path, files_path):
        self.sinogram_path = sinogram_path
        self.ground_truth_path = gt_path
        self.files_path = files_path

    def lidc_idri_gen(self, file_list):
        r = np.random.RandomState(0)
        sort_data = []
        for z in file_list:
            dcm_file = pydicom.read_file(z)
            if dcm_file.pixel_array.shape == self.RECO_IM_SHAPE:
                array = dcm_file.pixel_array.astype(np.float32).T

                array *= dcm_file.RescaleSlope
                array += dcm_file.RescaleIntercept

                array += r.uniform(0., 1., size=array.shape)

                array *= (self.MU_WATER - self.MU_AIR) / 1000
                array += self.MU_WATER
                array /= self.MU_MAX
                np.clip(array, 0., 1., out=array)

                dcm_file._pixel_array = array

                sort_data.append(dcm_file)

        sort_data.sort(key=lambda x: int(x.InstanceNumber))
        numpy_array = np.stack([s.pixel_array for s in sort_data])

        return numpy_array

    def ff(self, ray_trafo, im):
        # im_resized = resize(im, self.IM_SHAPE, order=1)
        # # apply forward operator
        # sinogram_id, sinogram = astra.create_sino(im*self.MU_MAX, projector_id)
        # data = np.array(sinogram).astype(np.float64)
        # data = (-1)*data
        # np.exp(data, out=data)
        # data *= self.PHOTONS_PER_PIXEL
        # astra.data2d.delete(sinogram_id)
        im_resized = resize(im * self.MU_MAX, self.IM_SHAPE, order=1)

        # apply forward operator
        data = ray_trafo(im_resized).asarray()

        data *= (-1)
        np.exp(data, out=data)
        data *= self.PHOTONS_PER_PIXEL

        return data

    """SINOGRAM GENERATION"""

    def start_sinogram_generation(self):

        file_list = list_files(self.files_path)

        os.makedirs(self.sinogram_path, exist_ok=True)
        os.makedirs(self.ground_truth_path, exist_ok=True)

        lidc_idri_gen_len = len(file_list)

        vol_geom = astra.create_vol_geom(512, 512)
        angles = np.linspace(0, np.pi, 1000, False)
        proj_geom = astra.create_proj_geom('parallel', 1.0, 727, angles)
        projector_id = astra.create_projector('cuda', proj_geom, vol_geom)

        reco_space = odl.uniform_discr(min_pt=self.MIN_PT, max_pt=self.MAX_PT,
                                       shape=self.RECO_IM_SHAPE, dtype=np.float32)
        space = odl.uniform_discr(min_pt=self.MIN_PT, max_pt=self.MAX_PT, shape=self.IM_SHAPE,
                                  dtype=np.float32)

        reco_geometry = odl.tomo.parallel_beam_geometry(
            reco_space, num_angles=self.NUM_ANGLES)
        geometry = odl.tomo.parallel_beam_geometry(
            space, num_angles=self.NUM_ANGLES, det_shape=reco_geometry.detector.shape)

        # IMPL = 'astra_cpu'
        # reco_ray_trafo = odl.tomo.RayTransform(reco_space, reco_geometry)
        ray_trafo = odl.tomo.RayTransform(space, geometry)


        rs = np.random.RandomState(3)

        n_files = ceil(lidc_idri_gen_len / self.NUM_SAMPLES_PER_FILE)

        slices = self.lidc_idri_gen(file_list)
        it1 = 0
        it2 = self.NUM_SAMPLES_PER_FILE
        progress = 0
        increment = rescale(1, n_files)
        for filenumber in tqdm(range(n_files)):
            obs_filename = os.path.join(
                self.sinogram_path, 'sinogram_{:03d}.nrrd'.format(filenumber))
            ground_truth_filename = os.path.join(
                self.ground_truth_path, 'ground_truth_{:03d}.nrrd'.format(filenumber))

            observation_dataset = []
            ground_truth_dataset = []

            for data in tqdm(slices[it1:it2, ...]):
                data = np.flipud(data)
                # ground_truth_dataset.append(data)
                data = self.ff(ray_trafo, data)
                data /=  self.PHOTONS_PER_PIXEL
                np.maximum(0.1 / self.PHOTONS_PER_PIXEL, data, out=data)
                np.log(data, out=data)
                data /= (-self.MU_MAX)
                observation_dataset.append(data)
                if self.FLAG:
                    print('terminating process')
                    return

            it1 += self.NUM_SAMPLES_PER_FILE
            it2 += self.NUM_SAMPLES_PER_FILE

            if it2 > len(slices):
                it2 = len(slices)
            # ground_truth_dataset = np.array(ground_truth_dataset)
            # ground_truth_dataset = np.rot90(ground_truth_dataset, -1, (1, 2))
            nrrd.write(obs_filename, np.array(observation_dataset), index_order='C')
            # nrrd.write(ground_truth_filename, ground_truth_dataset, index_order='C')
            # progress += increment
            # self.progressbar.emit(progress)


sinogram_path = "2dprojections/sino"
gt_path = "2dprojections/gt"
file_path = "test_slices"
proba = SinogramGeneration3(sinogram_path, gt_path, file_path)
proba.start_sinogram_generation()