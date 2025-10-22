import RPi.GPIO as GPIO
import time
import r2r_adc as r2r
import adc_plot

voltage_values = []
time_values = []
duration = 10.0
act_time = 0.0
max_voltage = 0.0

if __name__ == "__main__":
    dac = r2r.R2R_ADC(3.157, 0.005, True)
    try:
        while True:
            try:
                while act_time < duration:
                    number = dac.sequential_counting_adc()
                    act_time = act_time + number * dac.compare_time
                    voltage = float(dac.dynamic_range * number / 256)
                    if voltage > max_voltage:
                        max_voltage = voltage
                    time_values.append(act_time)
                    voltage_values.append(voltage)
                
                adc_plot.plot_voltage_vs_time(time_values, voltage_values, max_voltage)
                break

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз \n")

    finally:
        dac.deinit()