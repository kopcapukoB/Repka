import numpy
import time
import pwm_dac
import triangle_generator as tg

amplitude = 3.0
signal_frequency = 200.0
sampling_frequency = 1000.0
tim = 0.0

if __name__ == "__main__":
    try:
        while True:
            try:
                voltage = amplitude * tg.get_triangle_wave_amplitude(signal_frequency, tim)
                pwm_dac.dac.set_voltage(voltage)
                tg.wait_for_sampling_period(sampling_frequency)
                tim = tim + 1 / sampling_frequency

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз \n")

    finally:
        pwm_dac.dac.deinit()
