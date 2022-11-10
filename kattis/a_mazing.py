# https://open.kattis.com/problems/amazing
import random
from sys import stdout

maze_size = random.randint(5, 15)
maze = []


def create_maze():
    maze_outcome = ['no exit', 'exit', 'exit', 'exit']
    maze_contents = ['right', 'left', 'up', 'down']
    for n in range(maze_size):
        maze.append(maze_contents[random.randint(0, len(maze_contents) - 1)])
    maze.append(maze_outcome[random.randint(0, len(maze_outcome) - 1)])


def player():
    playing = True
    player_location = []

    while playing == True:
        stdout.flush()
        if maze[len(player_location)] == 'exit':
            print('You escaped')
            playing = False

            break

        elif 'no exit' in maze:
            print('There is no escape!')
            playing = False

            break

        move = str(
            input('Where do you want to move? (up/down/right/left)')).lower()

        if move == maze[len(player_location)]:
            player_location.append('')
            print('ok')
            move = ''

        elif move != maze[len(player_location)]:
            print('wall')
            move = ''

        else:
            print('Invalid input')


def main():
    create_maze()
    print(maze)

    player()


if __name__ == '__main__':
    main()
