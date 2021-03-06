from distributions import get_distributions
from math import sqrt


def selection(dist, n: int):
    return sorted(dist.x() for i in range(n))


def char(sel: list, ch_type: str):
    if len(sel) == 0:
        raise ValueError("Empty selection!")
    if ch_type == 'avr':
        return sum(sel) / len(sel)
    elif ch_type == 'med':
        l = len(sel) // 2
        if len(sel) % 2 == 0:
            return (sel[l - 1] + sel[l]) / 2
        else:
            return sel[l]
    elif ch_type == 'zr':
        return (sel[0] + sel[-1]) / 2
    elif ch_type == 'zq':
        n = len(sel)
        z = 0
        if n % 4 == 0:
            z += sel[n // 4 - 1]
        else:
            z += sel[n // 4]
        if 3 * n % 4 == 0:
            z += sel[3 * n // 4 - 1]
        else:
            z += sel[3 * n // 4]
        return z / 2
    elif ch_type == 'ztr':
        r = len(sel) // 4
        selr = sel[r:-r]
        return sum(selr) / len(selr)
    else:
        raise ValueError("Wrong characteristic name: " + ch_type)


N = 1000
ns = [10, 50, 1000]
ds = get_distributions()
chars = ['avr', 'med', 'zr', 'zq', 'ztr']
for d in ds:
    print(d.name)
    for n in ns:
        print(f'n={n}')
        data = {}
        for c in chars:
            data[c] = [0, 0]
        for i in range(N):
            s = selection(d, n)
            for k in data:
                z = char(s, k)
                data[k][0] += z / N
                data[k][1] += z * z / N
        for c in chars:
            data[c][1] = data[c][1] - data[c][0] ** 2
            print(c, data[c], sqrt(data[c][1]))
