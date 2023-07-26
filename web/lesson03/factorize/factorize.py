from multiprocessing import Process
from time import time


def factorize(*number):
    l = []
    l2 = []

    for i in number:
        for k in filter(lambda j: (i % j) == 0, range(1, i + 1)):
            l.append(k)

        l2.append(l)
        l = []

    return l2


if __name__ == '__main__':
    a, b, c, d = factorize(128, 255, 99999, 10651060)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158,
                 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212,
                 2662765, 5325530, 10651060]

    timer = time()
    factorize(128, 255, 99999, 10651060)
    print(f'Time for 1 process: {time() - timer}')

    processes = [
        Process(target=factorize, args=(128, 255)),
        Process(target=factorize, args=(99999, )),
        Process(target=factorize, args=(10651060, ))
    ]

    timer = time()

    [pr.start() for pr in processes]
    [pr.join() for pr in processes]
    [pr.close() for pr in processes]

    print(f'Time for 3 processes: {time() - timer}')
