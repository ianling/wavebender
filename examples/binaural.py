#!/usr/bin/env python3
from sys import stdout

from wavebender import *

channels = ((sine_wave(170.0, amplitude=0.1),),
            (sine_wave(178.0, amplitude=0.1),))

samples = compute_samples(channels)
write_wavefile(stdout.buffer, samples)
