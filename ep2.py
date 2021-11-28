import numpy as np
import os
from moving_average import *
import matplotlib.pyplot as plt

file_num = input('Введите номер файла: ')
sig = np.genfromtxt(os.path.join('signals', f'signal0{file_num}.dat'),  delimiter="\n")

fig, axs = plt.subplots(1, 2)
x = np.arange(sig.size)
axs[0].plot(x, sig)
axs[0].minorticks_on()
axs[0].grid(which='major',
            color='k',
            linewidth=1)
axs[0].grid(which='minor',
            color='grey',
            linestyle=':')
axs[0].set_title('Сырой сигнал')

sig_filtered = moving_average(sig, 10)
axs[1].plot(x, sig_filtered)
axs[1].minorticks_on()
axs[1].grid(which='major',
            color='k',
            linewidth=1)
axs[1].grid(which='minor',
            color='grey',
            linestyle=':')
axs[1].set_title('После фильтра')

fig.savefig(os.path.join('filtered_signals', f'filtered_signal0{file_num}.png'))
plt.show()
