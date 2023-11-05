# Configuration Class
# The `Config` class is a central place to manage all configuration settings for the audio classification model. 
# It encapsulates various parameters that will be used throughout the data preprocessing and model training processes.

import os
class Config: 
    def __init__(self, mode='conv', nfilt=26, nfeat=13, nfft=512, rate=16000): 
        self.mode = mode   # The mode of processing ('conv' for CNN, 'time' for RNN)
        self.nfilt = nfilt # The number of filters in the Mel filterbank
        self.nfeat = nfeat # The number of features to be extracted
        self.nfft = nfft   # The window size for the FFT
        self.rate = rate   # The sample rate of the audio files
        self.step = int(rate/10)  # The step size for feature extraction 
        self.model_path = os.path.join('models', mode + '.model')
        self.p_path = os.path.join('pickles', mode + '.p') 