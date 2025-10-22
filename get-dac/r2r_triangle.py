import r2r_dac as r2r
import triangle_generator as tg
import time
  
amplitude = 1.0
signal_frequency = 1.0
sampling_frequency = 1000.0
tim = 0.0

if __name__ == "__main__":
    try:
        while True:
            try:
                voltage = amplitude * tg.get_triangle_wave_amplitude(signal_frequency, tim)
                r2r.dac.set_voltage(voltage)
                tg.wait_for_sampling_period(sampling_frequency)
                tim = tim + 1 / sampling_frequency

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз \n")

    finally:
        r2r.dac.deinit()
