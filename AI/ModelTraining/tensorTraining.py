import tensorflow as tf
from keras.layers import Input, Embedding, MultiHeadAttention, Dense, Dropout, LayerNormalization
from keras import Model
from keras.optimizers import Adam
from keras.optimizers.schedules import ExponentialDecay # stepdecay needs to be pulled in
from  multimodelStepDecay import MultiModelStepDecay
from transformerBuilder import Transformer, MemoryNetwork
import numpy as np


# Create a synthetic dataset
vocab_size = 10000
max_length = 50
num_samples = 1000
num_classes = vocab_size  # Example: Language modeling task

X = np.random.randint(0, vocab_size, size=(num_samples, max_length))
y = X

# Model hyperparameters
d_model = 128
num_heads = 4
num_layers = 2
dropout_rate = 0.2
initial_learning_rate = 0.001
decay_steps = 1000
end_learning_rate = 0.0001

# Build and compile the model
model = Transformer(vocab_size, max_length, d_model, num_heads, num_layers, num_classes, dropout_rate)

# Gradient Clipping
clip_value = 1.0
optimizer = Adam(learning_rate=initial_learning_rate, clipvalue=clip_value)

# Learning Rate Scheduling (Step Decay)
step_decay = MultiModelStepDecay(initial_learning_rate, step_size=decay_steps, gamma=0.5)
optimizer = Adam(learning_rate=step_decay.lr)

# Learning Rate Scheduling (Exponential Decay)
exp_decay = ExponentialDecay(initial_learning_rate, decay_steps, decay_rate=0.5)
optimizer = Adam(learning_rate=exp_decay.decay_rate)

model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
batch_size = 32
epochs = 10
model.fit(X, y, batch_size=batch_size, epochs=epochs)
