#!/usr/bin/env python3
from sys import stdout

from wavebender import *

channels = ((white_noise(amplitude=0.1),),)

samples = compute_samples(channels, 44100 * 60 * 1)
write_wavefile(stdout.buffer, samples, 44100 * 60 * 1, nchannels=1)
