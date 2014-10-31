from multiprocessing import *
import ctypes

num = Value(ctypes.c_int, 0)


def A():
    global num

    print('Mi funcion concurrente %s' % num.value)

    num.value += 1

pool = Pool(processes=10)

if __name__ == "__main__":
    for p in range(20):
        pool.apply_async(A, ())

    pool.close()
    pool.join()
