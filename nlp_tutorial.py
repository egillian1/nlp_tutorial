import random
import torch
import torch.nn as nn
from torch import optim

from data_processing import *
from helpers import *
from attn_decoder import AttnDecoderRNN
from encoder import EncoderRNN
from evaluation import *
from lang import Lang

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
if torch.cuda.is_available():
    print("Using CUDA.")
else:
    print("CUDA not available. Switching to CPU.")

encoder_file_location = 'data/encoder.dictionary'
decoder_file_location = 'data/decoder.dictionary'

# Load model from files
encoder = loadObjectFromFile(encoder_file_location)
decoder = loadObjectFromFile(decoder_file_location)
if encoder and decoder:
    evaluateRandomly(encoder, decoder)
    print(evaluate(encoder, decoder, 'c est un jeune directeur plein')[0])

# Create wod embeddings
input_lang, output_lang, pairs = prepareData('eng', 'fra', True)
print(random.choice(pairs))
print(input_lang)

# Create and train new model
hidden_size = 256
encoder1 = EncoderRNN(input_lang.n_words, hidden_size).to(device)
attn_decoder1 = AttnDecoderRNN(hidden_size, output_lang.n_words, dropout_p=0.1).to(device)
trainIters(encoder1, attn_decoder1, 75000, print_every=5000)
