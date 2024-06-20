import curses
import time
import random

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)
    sh, sw = stdscr.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)
    w.keypad(1)

    # Initial bird position
    bird_y = sh // 2
    bird_x = sw // 4

    # Gravity and jump velocity
    gravity = 1
    jump_velocity = -2
    velocity = 0

    # Pipe parameters
    pipe_interval = 20
    pipe_height = 10
    pipe_width = 3
    pipes = []

    score = 0

    while True:
        w.clear()

        # Check for user input
        key = w.getch()
        if key == ord('q'):
            break
        elif key == ord(' '):
            velocity = jump_velocity

        # Update bird position
        velocity += gravity
        bird_y += velocity

        # Draw bird
        w.addch(int(bird_y), bird_x, '*')

        # Generate pipes
        if random.randint(0, 9) == 0:
            pipe_gap = random.randint(2, 6)
            pipes.append((sw, pipe_gap))

        # Move pipes and check for collisions
        new_pipes = []
        for pipe_x, pipe_gap in pipes:
            w.addch(0, pipe_x, '|')
            w.addch(pipe_gap, pipe_x, '|')
            w.addch(pipe_gap + pipe_height, pipe_x, '|')
            if bird_x == pipe_x and (bird_y < pipe_gap or bird_y > pipe_gap + pipe_height):
                w.addstr(sh // 2, sw // 2 - 5, "Game Over")
                w.addstr(sh // 2 + 1, sw // 2 - 8, "Score: {}".format(score))
                w.refresh()
                time.sleep(2)
                return

            if pipe_x > 0:
                new_pipes.append((pipe_x - 1, pipe_gap))

        pipes = new_pipes

        # Update score
        if pipes and bird_x == pipes[0][0]:
            score += 1

        w.addstr(0, 2, "Score: {}".format(score))

        w.refresh()

if __name__ == "__main__":
    curses.wrapper(main)
