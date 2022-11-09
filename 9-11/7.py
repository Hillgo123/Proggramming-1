import time

list = [1, 1]


def fibbonaci(n):
    for n in range(n):
        for i in range(1, 2):
            new = list[i] + list[i - 1]
            list.append(new)
            list.pop(0)

            yield new


if __name__ == '__main__':
    start = time.time()
    for i in fibbonaci(100000000000000000):
        print(i)
    print(f'It took {time.time() - start} seconds to execute code')