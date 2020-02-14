import pickle
from attn_decoder import AttnDecoderRNN
from encoder import EncoderRNN

def dumpObjectToFile(object, location):
    with open(location, 'wb') as object_file:
        pickle.dump(object, object_file)

def loadObjectFromFile(location):
    with open(location, 'rb') as object_file:
        return pickle.load(object_file)

def saveModel(encoder, decoder):
    dumpObjectToFile(encoder, encoder_file_location)
    dumpObjectToFile(decoder, decoder_file_location)
