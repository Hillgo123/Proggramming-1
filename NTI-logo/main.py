import turtle as t
import random

t1 = t.Turtle()
t1.hideturtle()

t1.speed(0)
t.bgcolor('black')

colors = [
    'blue',
    'green',
    'red',
    'pink',
    'yellow',
    'purple',
    'brown',
    'azure',
    'AliceBlue',
    'CadetBlue',
    'BurlyWood3',
    'DeepPink4',
    'brown4',
    'beige',
    'DarkGray',
    'DarkOrchid2',
    'DarkSalmon',
    'cyan',
    'DarkOrange'
]


def logo(x, y, s):
    t1.color(colors[random.randint(0, len(colors) - 1)])
    t1.width(15 * s)
    t1.up()
    t1.goto(x, y)
    t1.down()

    t1.lt(180)
    t1.fd(71.75 * s)
    t1.lt(90)
    t1.fd(120 * s)
    for n in range(50):
        t1.fd(2 * s)
        t1.lt(2)

    t1.setheading(90)
    t1.up()
    t1.lt(90)
    t1.fd(15 * s)
    t1.rt(90)

    t1.fd(30 * s)
    t1.down()

    t1.fd(120 * s)
    t1.rt(150)
    t1.fd(138.55 * s)
    t1.setheading(90)
    t1.fd(120 * s)

    t1.rt(90)
    t1.up()
    t1.fd(30 * s)
    t1.down()

    t1.fd(60 * s)
    t1.bk(30 * s)
    t1.rt(90)
    t1.fd(120 * s)

    t1.up()
    t1.lt(90)
    t1.fd(60 * s)
    t1.down()

    t1.lt(90)
    t1.fd(120 * s)

    t1.setheading(0)


def main():
    for n in range(0, 50):
        logo(random.randint(-250, 250),
             random.randint(-250, 250), random.uniform(0.01, 1))
    t.exitonclick()


if __name__ == '__main__':
    main()
