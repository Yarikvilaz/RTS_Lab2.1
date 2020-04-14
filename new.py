import random
import math
import time
import os
SHOW_TIME = True


def get_func_time(f):
    """Show function execute time."""
    if not SHOW_TIME:
        return f

    def func(*args):
        start = time.time()
        a = f(*args)
        print(f"({f.__name__})час:", time.time() - start)
        return a
    return func


@get_func_time
def signal(n, omega, min_value=0, max_value=1):
    """Return signal function."""
    A = [min_value + (max_value - min_value) * random.random() for _ in range(n)]
    phi = [min_value + (max_value - min_value) * random.random() for _ in range(n)]

    def f(t):
        x = 0
        for i in range(n):
            x += A[i]*math.sin(omega/n*t*i + phi[i])
        return x
    return f


@get_func_time
def get_m_D(x):
    """Return expected value(m) and dispersion."""
    m = sum(x)/len(x)
    return m, sum([(i - m) ** 2 for i in x]) / (len(x) - 1)


@get_func_time
def get_m(x):
    """Return expected value."""
    return sum(x)/len(x)


@get_func_time
def get_D(x, m=None):
    """return dispersion."""
    if m is None:
        m = get_m(x)
    return sum([(i - m) ** 2 for i in x]) / (len(x) - 1)


@get_func_time
def get_R(x_gen, y_gen, N, tau=0):
    """Return correlation between x(t) and y(t+tau), t=0..N."""
    x = [x_gen(i) for i in range(N)]
    y = [y_gen(i+tau) for i in range(N)]
    m_x, D_x = get_m_D(x)
    m_y, D_y = get_m_D(y)

    R = 0
    for i in range(N//2-1):
        R += (x[i] - m_x)*(y[i+tau] - m_y)/(N//2-1)
    R /= (D_x*D_y)**(1/2)
    return R


@get_func_time
def get_F(x):
    N = len(x)
    FR = []
    Fi = []
    for p in range(N):
        FR.append(0)
        Fi.append(0)
        for k in range(N):
            FR[p] += x[k]*math.cos(-2*math.pi*p*k/N)
            Fi[p] += x[k]*math.sin(-2*math.pi*p*k/N)
    return FR, Fi


@get_func_time
def get_F_optimized(x):
    N = len(x)
    w = []
    for i in range(N):
        if i < N//4:
            w.append((math.cos(-2*math.pi*i/N),
                      math.sin(-2*math.pi*i/N)))
        elif i < N//2:
            w.append((w[i-N//4][1],
                      -w[i-N//4][0]))
        else:
            w.append((-w[i-N//2][0], -w[i-N//2][1]))
    FR = []
    Fi = []
    for i in range(N):
        FR.append(sum([w[(i*j)%N][0]*x[j] for j in range(N)]))
        Fi.append(sum([w[(i*j)%N][1]*x[j] for j in range(N)]))
    return FR, Fi