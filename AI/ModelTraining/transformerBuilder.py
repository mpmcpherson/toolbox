import tensorflow as tf
from keras.layers import Input, Embedding, MultiHeadAttention, Dense, Dropout, LayerNormalization
from keras import Model
from keras.optimizers import Adam
from keras.optimizers.schedules import ExponentialDecay # stepdecay needs to be pulled in
from  multimodelStepDecay import MultiModelStepDecay
import numpy as np


# Define the memory network model architecture
class MemoryNetwork(Model):
    def __init__(self, max_memory_size, memory_dim):
        super(MemoryNetwork, self).__init__()
        self.memory_matrix = tf.Variable(tf.zeros((max_memory_size, memory_dim)), trainable=False)

    def read_memory(self, indices):
        return tf.gather(self.memory_matrix, indices)

    def write_memory(self, indices, values):
        self.memory_matrix.scatter_update(indices, values)

# Define the transformer model architecture
class Transformer(Model):
    def __init__(self, vocab_size, max_length, d_model, num_heads, num_layers, num_classes, dropout_rate=0.1):
        super(Transformer, self).__init__()
        self.embedding = Embedding(input_dim=vocab_size, output_dim=d_model)
        self.attention_blocks = [MultiHeadAttention(num_heads=num_heads, key_dim=d_model) for _ in range(num_layers)]
        self.layer_norms = [LayerNormalization() for _ in range(num_layers)]
        self.dropout = Dropout(rate=dropout_rate)
        self.fc = Dense(num_classes, activation='softmax')

    def call(self, inputs, training=False):
        embeddings = self.embedding(inputs)
        attention_output = embeddings  # Initialize with embeddings

        for attention_block, layer_norm in zip(self.attention_blocks, self.layer_norms):
            attention_output = attention_block(attention_output, attention_output)
            attention_output = layer_norm(attention_output)

        attention_output = self.dropout(attention_output, training=training)
        output = self.fc(attention_output)
        return output
