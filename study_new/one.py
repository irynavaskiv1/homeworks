import tkinter as tk
from random import randint

WIDTH = 400
HEIGHT = 500


def canvas_click_handler(event):
    print('Hello! x= ', event.x, 'and y= ', event.y )


def tick():
    global x, y, dx, dy, R
    x += dx
    y += dy
    if x + R > WIDTH or x - R < 0:
        dx = -dx

    canvas.move(ball_id, +1, +1)
    root.after(50, tick)


def main():
    global root, canvas
    global ball_id, x, y, dx, dy, R

    root = tk.Tk()
    root.geometry(str(WIDTH) + 'x' + str(HEIGHT))
    canvas = tk.Canvas(root)
    canvas.pack(anchor = 'rw', fill =tk.BOTH)
    canvas.bind('<Button-1>', canvas_click_handler)

    R = randint(20, 50)
    x = randint(R, WIDTH, R)
    y = randint(R, HEIGHT, R)
    dx, dy = +1, +1
    ball_id = canvas.create_oval(x + R, y + R,
                                 x - R, y - R, fill='green')

    tick()
    root.mainloop()


if __name__ == '__main__':
    main()

