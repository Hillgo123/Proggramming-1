from termcolor import colored
import random


colors = ['green', 'red', 'yellow', 'blue', 'white', 'magenta', 'cyan']
color_attrs = ['bold', 'reverse', 'dark', 'underline', 'blink', 'concealed']


def prime(n):
    for i in range(2, n+1):
        for x in range(2, i):
            if i % x == 0:
                break
        else:
            yield i


list = []
if __name__ == '__main__':
    for i in prime(100000000):
        print(colored(i, colors[random.randint(0, len(colors) - 1)],
            attrs=[color_attrs[random.randint(0, len(color_attrs) - 1)]]))
    #     list.append(i)
    #     if len(list) == 5:
    #         break
    # print(list)