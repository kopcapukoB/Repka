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