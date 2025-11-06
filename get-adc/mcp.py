import RPi.GPIO as GPIO
import time
import mcp3021_driver as driver
import adc_plot

voltage_values = []
time_values = []
duration = 10.0
act_time = 0.0
max_voltage = 5.5

if __name__ == "__main__":
    mcp = driver.MCP3021(3.278, True)
    try:
        while True:
            try:
                while act_time < duration:
                    act_time = act_time + 0.01
                    voltage = mcp.get_voltage()
                    time_values.append(act_time)
                    voltage_values.append(voltage)
                    time.sleep(0.01)
                
                adc_plot.plot_voltage_vs_time(time_values, voltage_values, max_voltage)
                adc_plot.plot_sampling_period_hist(time_values)
                break

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз \n")

    finally:
        mcp.deinit()