import numpy
import time
import math

def get_triangle_wave_amplitude(freq, tim):
    k = int(tim * freq)
    A = tim * freq - int(tim * freq)
    return float(A + (1 - 2 * A) * (k % 2))

def wait_for_sampling_period(sampling_frequency):
    time.sleep(float(1 / sampling_frequency))
