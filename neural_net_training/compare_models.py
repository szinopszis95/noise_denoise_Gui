from neural_net_training.batch_generator import BatchDataGen
from neural_net_training.save_load_model import load_model


class CompareModels:
    def __init__(self, x_path, y_path, batch_size, model_1_index, model_2_index, scrollbar, canvas_1, canvas_2,
                 canvas_3, canvas_4, x_batch, y_batch, y1_hat, y2_hat):
        self.x_path = x_path
        self.y_path = y_path
        self.batch_size = batch_size
        self.model_1_index = model_1_index
        self.model_2_index = model_2_index
        self.scrollbar = scrollbar
        self.canvas_1 = canvas_1
        self.canvas_2 = canvas_2
        self.canvas_3 = canvas_3
        self.canvas_4 = canvas_4
        self.x_batch = x_batch
        self.y_batch = y_batch
        self.y1_hat = y1_hat
        self.y2_hat = y2_hat

    def predict(self):

        x_batch, y_batch = next(BatchDataGen(self.x_path, self.y_path,
                                             self.batch_size).gen_batch())

        if self.model_1_index == 0:
            model1 = load_model('denoising_encoder_100')
        else:
            model1 = load_model('denoising_ssim_100')

        if self.model_2_index == 0:
            model2 = load_model('denoising_encoder_100')
        else:
            model2 = load_model('denoising_ssim_100')

        y1_hat = model1.predict(y_batch)
        y2_hat = model2.predict(y_batch)

        self.scrollbar.setMinimum(0)
        self.scrollbar.setMaximum(len(x_batch) - 1)
        self.scrollbar.setValue(0)
        self.draw_canvas(self.canvas_1, y_batch, 0)
        self.draw_canvas(self.canvas_2, x_batch, 0)
        self.draw_canvas(self.canvas_3, y1_hat, 0)
        self.draw_canvas(self.canvas_4, y2_hat, 0)

        return x_batch, y_batch, y1_hat, y2_hat

    def scroll_value(self):
        value = self.scrollbar.value()
        self.draw_canvas(self.canvas_1, self.y_batch, value)
        self.draw_canvas(self.canvas_2, self.x_batch, value)
        self.draw_canvas(self.canvas_3, self.y1_hat, value)
        self.draw_canvas(self.canvas_4, self.y2_hat, value)

    def draw_canvas(self, canvas, data, value):
        canvas.canvas.axes.clear()
        canvas.canvas.axes.axis('off')
        canvas.canvas.axes.imshow(data[value, :, :, 0], cmap='gray')
        canvas.canvas.draw()
