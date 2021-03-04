from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping

from neural_net_training.batch_generator import BatchDataGen
from neural_net_training.models import *
from neural_net_training.plot_loss_progress import PlotLosses


class TrainNetwork:
    def __init__(self, train_data_path, train_mask_path, batch_size, valid_data_path, valid_mask_path, model_index,
                 num_epochs, progressbar, label, learning_rate, lr_index, steps_per_epoch):
        self.train_data_path = train_data_path
        self.train_mask_path = train_mask_path
        self.batch_size = batch_size
        self.valid_data_path = valid_data_path
        self.valid_mask_path = valid_mask_path
        self.model_index = model_index
        self.num_epochs = num_epochs
        self.progressbar = progressbar
        self.label = label
        self.learning_rate = learning_rate
        self.lr_index = lr_index
        self.steps_per_epoch = steps_per_epoch


    def training(self):
        x_batch, y_batch = next(BatchDataGen(self.train_data_path, self.train_mask_path, self.batch_size).gen_batch())

        model = simple_autoencoder(x_batch)
        train_generator = BatchDataGen(self.train_data_path, self.train_mask_path, self.batch_size).gen_batch()
        validation_generator = BatchDataGen(self.valid_data_path, self.valid_mask_path, self.batch_size).gen_batch()
        if self.model_index == 0:
            model = simple_autoencoder(x_batch)
        if self.model_index == 1:
            model = u_net(x_batch)

        # steps per epoch
        # dcm_filenames = sorted(list(os.listdir(SINOGRAM_PATH)))
        # file, header = nrrd.read(os.path.join(SINOGRAM_PATH, dcm_filenames[-1]), index_order='C')
        # last_size = len(file)
        # length = (len(dcm_filenames) - 1) * 4 + last_size

        callbacks = [
            ModelCheckpoint('best_model_testing.h5', monitor='val_loss', mode='min', save_best_only=True),
            EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=50),
            PlotLosses(self.num_epochs, self.progressbar, self.label)
        ]

        lr = self.learning_rate
        optim = opt(self.lr_index, lr)
        model.compile(optim, loss=SSIM)
        model.summary()
        trained_model = model.fit(train_generator, steps_per_epoch=self.steps_per_epoch, epochs=self.num_epochs,
                                  validation_data=validation_generator, validation_steps=1, verbose=1,
                                  callbacks=callbacks)
