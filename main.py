from new import signal, get_F, get_F_optimized
import matplotlib.pyplot as plt

# option values
n = 12
omega = 1800
N = 64

range_min = 0
range_max = 1

x_gen = signal(n, omega, range_min, range_max)
x = [x_gen(i) for i in range(N)]
(FR, Fi) = get_F(x)
(FR1, Fi1) = get_F_optimized(x)
# print(get_F_optimized(x))

F = [FR[i] + Fi[i] for i in range(N)]

fig = plt.figure()

ax_1 = fig.add_subplot(3, 2, 1)
ax_2 = fig.add_subplot(3, 2, 2)
ax_3 = fig.add_subplot(3, 2, 3)
ax_4 = fig.add_subplot(3, 2, 4)
ax_5 = fig.add_subplot(3, 2, 5)
ax_6 = fig.add_subplot(3, 2, 6)


ax_1.plot(range(N), FR)
ax_2.plot(range(N), Fi)
ax_3.plot(range(N), FR1)
ax_4.plot(range(N), Fi1)
ax_5.plot(range(N), x)
ax_6.plot(range(N), F)

ax_1.set(title='FR')
ax_2.set(title='Fi')
ax_3.set(title='FR_opt')
ax_4.set(title='Fi_opt')
ax_5.set(title='x')
ax_6.set(title='F')

plt.show()