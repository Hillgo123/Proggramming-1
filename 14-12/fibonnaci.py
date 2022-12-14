fib_2 = [0, 1]
fib_3 = [0, 1, 1]


def fibbonaci_2(i):
    for n in range(0, i + 1):
        yield fib_2[1]

        fib_2.append(fib_2[0] + fib_2[1])
        fib_2[0] = fib_2[1]
        fib_2[1] = fib_2[2]
        fib_2.pop(2)


def fibbonaci_3(i):
    for n in range(0, i + 1):
        yield fib_3[1]

        fib_3.append(fib_3[0] + fib_3[1] + fib_3[2])
        fib_3[0] = fib_3[1]
        fib_3[1] = fib_3[2]
        fib_3[2] = fib_3[3]
        fib_3.pop(3)


if __name__ == '__main__':
    fib_1 = int(input(
        'Would you like to try the two number fibbonaci or the three number fibbonaci? (2/3)'))
    if fib_1 == 2:
        stop = input('Would you like to have a stop? (y/n)').lower()
        if stop == 'y':
            stop_number = int(input('When do you want it to stop?'))
            for n in fibbonaci_3(int(input('How many numbers would you like to test?'))):
                if n < stop_number:
                    print(n)

        elif stop == 'n':
            for n in fibbonaci_3(int(input('How many numbers would you like to test?'))):
                print(n)

    elif fib_1 == 3:
        stop = input('Would you like to have a stop? (y/n)').lower()
        if stop == 'y':
            stop_number = int(input('When do you want it to stop?'))
            for n in fibbonaci_2(int(input('How many numbers would you like to test?'))):
                if n < stop_number:
                    print(n)

        elif stop == 'n':
            for n in fibbonaci_2(int(input('How many numbers would you like to test?'))):
                print(n)
