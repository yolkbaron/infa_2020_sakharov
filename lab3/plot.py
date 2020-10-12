import numpy as np
import matplotlib.pyplot as plt

t = np.arange(5, 6, 0.01)
x = [142500, 190530, 255760, 319390, 379390, 457140, 501370]
y = [3.14 - 3.0770, 3.14 - 3.0447, 3.14 - 3.0122, 3.14 - 2.9402, 3.14 - 2.9796, 3.14 - 2.9061, 3.14 - 2.8717]
plt.figure(figsize = (10, 5))
g, w = np.polyfit(np.log10(x), y, deg=2, cov=True)
g_f = np.poly1d(g)
plt.errorbar(np.log10(x), y, xerr = 0.00003, yerr = 0.07, fmt='none')
plt.plot(t, g_f(t), label=r'$P_2(t) = a_2+b_2t+c_2t^2$')
plt.xlabel(r'$lg(f)$')
plt.ylabel(r'$phi$')
plt.title(r'$f(x)$')
plt.grid(True)
plt.show()