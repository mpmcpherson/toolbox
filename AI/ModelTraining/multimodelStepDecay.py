from keras.callbacks import Callback
import math

class MultiModelStepDecay(Callback):
    def __init__(self, model_lr_pairs, drop, epochs_drop):
        super(MultiModelStepDecay, self).__init__()
        self.model_lr_pairs = model_lr_pairs
        self.drop = drop
        self.epochs_drop = epochs_drop
        self.lr = 0.00

    def on_epoch_begin(self, epoch, logs=None):
        for model, initial_lr in self.model_lr_pairs:
            lr = initial_lr * math.pow(self.drop, math.floor((1 + epoch) / self.epochs_drop))
            model.optimizer.lr.assign(lr)
            self.lr = model.optimizer.lr.numpy()

