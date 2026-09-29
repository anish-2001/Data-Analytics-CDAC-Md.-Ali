import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8_whitegrid' if 'seaborn-v0_8_whitegrid' in plt.style.available else 'default')

plt.rcParams["figure.dpi"] = 100

x_linear, step_size = np.linspace(start = 0.0, stop = 10.0, num = 15, retstep= True)
print("Linear space array: ",x_linear)
print("Step size: ", step_size)

plt.figure(figsize= (9, 2.5))
plt.scatter(x_linear, np.zeros_like(x_linear), color = '#1f77b4', s = 60, zorder = 4, label = f'Linear Space (h = {step_size:.2f})')

plt.vlines(x_linear, ymin = -0.1, ymax= 0.1, color = '#1f77b4', alpha = 0.5, linestyles= '--')

plt.title("1D Uniform Grid Linear Space with Vertical Lines", fontsize = 12, fontweight = 'bold')
plt.xlabel("value", fontsize = 15, fontweight = 'bold')
plt.show()
