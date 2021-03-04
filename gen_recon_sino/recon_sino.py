import os

import astra
import nrrd
import numpy as np
import odl
from tqdm import tqdm
from scipy import stats

from rand_functions.helper_functions import rescale


class ReconSino:
    def __init__(self, sinogram_path, reconstructed_path, padding, progressbar, _case):
        self.sinogram_path = sinogram_path
        self.padding = padding
        self.progressbar = progressbar
        self.reconstructed_path = reconstructed_path
        self._case = _case

    """RECONSTRUCT USING ASTRA"""

    def reconstruct_astra(self, sinogram, progress, increment):
        slices, header = nrrd.read(sinogram, index_order='C')
        print(slices.shape)
        geom_1 = 727
        geom_2 = 1000
        eh = []
        rec = []
        if self.padding:
            slices = np.pad(slices, ((0, 0), (1, 1), (1, 1)), 'edge')
            geom_1 += 2
            geom_2 += 2
        for i in range(slices.shape[0]):
            vol_geom = astra.create_vol_geom(512, 512)

            proj_geom = astra.create_proj_geom('parallel', 1.0, geom_1, np.linspace(0, np.pi, geom_2))
            sinogram_id = astra.data2d.create('-sino', proj_geom, slices[i, :, ])

            proj_id = astra.create_projector('cuda', proj_geom, vol_geom)

            rec_id = astra.data2d.create('-vol', vol_geom)

            # id_,try_ = astra.create_backprojection(sinogram_id, proj_id)

            cfg = astra.astra_dict('FBP')
            cfg['ProjectorId'] = proj_id
            cfg['ProjectionDataId'] = sinogram_id
            cfg['ReconstructionDataId'] = rec_id
            alg_id = astra.algorithm.create(cfg)
            astra.algorithm.run(alg_id)
            fbp_reconstruction = astra.data2d.get(rec_id)
            fbp_reconstruction = np.fliplr(fbp_reconstruction)
            fbp_reconstruction = np.flipud(fbp_reconstruction)
            # try_ = np.fliplr(try_)
            # try_ = np.flipud(try_)
            Y, X = np.ogrid[:512, :512]
            dist_from_center = np.sqrt((X - 256) ** 2 + (Y - 256) ** 2)
            mask = dist_from_center <= 256

            fbp_reconstruction[~mask] = np.min(fbp_reconstruction)
            np.clip(fbp_reconstruction, 0., 1., out=fbp_reconstruction)
            rec.append(fbp_reconstruction)

            progress += increment
            self.progressbar.emit(progress)
            # eh.append(try_)
            # nrrd.write('eh.nrrd', np.array(eh), index_order='C', compression_level=1)

        rec = np.array(rec)
        return rec

    """RECONSTRUCT USING ODL"""

    def reconstruct_odl(self, sinogram, progress, increment):
        slices, header = nrrd.read(sinogram, index_order='C')
        rec = []
        for i in range(slices.shape[0]):
            reco_space = odl.uniform_discr(min_pt=[-0.13, -0.13], max_pt=[0.13, 0.13],
                                           shape=[512, 512], dtype=np.float32)
            reco_geometry = odl.tomo.parallel_beam_geometry(
                reco_space, num_angles=1000)

            # Ray transform (= forward projection).
            ray_trafo = odl.tomo.RayTransform(reco_space, reco_geometry, impl='astra_cuda')

            # Create filtered back-projection operator
            fbp = odl.tomo.fbp_op(ray_trafo, padding=self.padding)

            # Calculate filtered back-projection of data
            fbp_reconstruction = fbp(slices[i, :, :])
            fbp_reconstruction = fbp_reconstruction.asarray()

            # Y, X = np.ogrid[:512, :512]
            # dist_from_center = np.sqrt((X - 256) ** 2 + (Y - 256) ** 2)
            # mask = dist_from_center <= 256
            #
            # fbp_reconstruction[~mask] = np.min(fbp_reconstruction)
            np.clip(fbp_reconstruction, 0., 1., out=fbp_reconstruction)
            # print(np.mean(fbp_reconstruction))
            # fbp_reconstruction = (fbp_reconstruction - np.min(fbp_reconstruction)) / np.ptp(fbp_reconstruction)

            rec.append(fbp_reconstruction)

            progress += increment
            self.progressbar.emit(progress)

        rec = np.array(rec)
        rec = np.rot90(rec, -1, (1, 2))
        return rec

    def image_histogram_equalization(self, image, number_bins=256):
        image_histogram, bins = np.histogram(image.flatten(), number_bins, density=True)
        cdf = image_histogram.cumsum()  # cumulative distribution function
        cdf = cdf / cdf[-1]  # normalize
        # use linear interpolation of cdf to find new pixel values
        image_equalized = np.interp(image.flatten(), bins[:-1], cdf)

        return image_equalized.reshape(image.shape)

    def start_reconstruction(self):
        os.makedirs(self.reconstructed_path, exist_ok=True)
        dcm_filenames = sorted(list(os.listdir(self.sinogram_path)))
        file, header = nrrd.read(os.path.join(self.sinogram_path, dcm_filenames[-1]), index_order='C')
        last_size = len(file)
        length = (len(dcm_filenames) - 1) * 128 + last_size

        progress = 0
        increment = rescale(1, length)
        it = 0
        for dcm_file in tqdm(dcm_filenames):
            if dcm_file.endswith('.nrrd'):
                if self._case == 0:
                    recon_filename = os.path.join(self.reconstructed_path, 'noisy_astra_{:03d}.nrrd'.format(it+101))
                    nrrd.write(recon_filename,
                               self.reconstruct_astra(os.path.join(self.sinogram_path, dcm_file), progress, increment),
                               index_order='C')
                if self._case == 1:
                    recon_filename = os.path.join(self.reconstructed_path, 'noisy_odl_{:03d}.nrrd'.format(it+101))
                    nrrd.write(recon_filename,
                               self.reconstruct_odl(os.path.join(self.sinogram_path, dcm_file), progress, increment),
                               index_order='C')
                it += 1
                progress += 100 / len(dcm_filenames)

        self.progressbar.emit(100)
