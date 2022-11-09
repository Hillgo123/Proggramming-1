list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


list.sort()


def check():
    for n in range(0, len(list)):
        if n > 0:
            if list[n] == list[n - 1]:
                list.pop(n)
                break


if __name__ == '__main__':
    for n in range(len(list)):
        check()

    print(list)
