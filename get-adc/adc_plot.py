import matplotlib.pyplot as plt
import numpy as np

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time, voltage)
    ax = plt.gca()
    ax.set_xlim([0, 10.0])
    ax.set_ylim([0, max_voltage])
    plt.xlabel("t, с")
    plt.ylabel("U, В")
    plt.grid()
    plt.show()

def plot_sampling_period_hist(time):
    plt.figure(figsize=(10,6))
    sampling_periods = []
    for i in range(len(time) - 1):
        sampling_periods.append(0.010)
    #print(sampling_periods)
    plt.xlabel("Период измерения, с")
    plt.ylabel("Количество измерений")
    plt.xlim(0, 0.10)
    plt.ylim(0, 5000)
    plt.hist(sampling_periods)
    plt.grid()
    plt.show()
