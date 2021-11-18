import numpy as np
import os
import numpy as np
from moving_average import *
import matplotlib.pyplot as plt

file_num = input('Введите номер файла: ')
with open(os.path.join('signals', f'signal0{file_num}.dat')) as f:
    sig = filter(lambda x: x, f.read().split('\n'))
    sig = np.array([float(i) for i in sig])

fig, axs = plt.subplots(1, 2)
x = [i for i in range(sig.size)]
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
