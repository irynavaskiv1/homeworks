from random import randrange as rnd, choice
import tkinter as tk
import math
import time


def main():
    global root, canvas, gun1
    root = tk.Tk()
    root.geometry('800x600')
    canvas = tk.Canvas(root, bg='white')
    canvas.pack(fill=tk.BOTH, expand=1)


class Ball:
    def __init__(self, x=40, y=450, vx=0, vy=0):
        """
        Args:
        x - початкове розположення кульки по горизонталі
        y - початкове розположення кульки по вертикалі
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = vx
        self.vy = vy
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canvas.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = 30

    def set_cords(self):
        canvas.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move(self):
        """Перемістити м'яч після одиниці часу.
         Метод описує переміщення м'яча за один кадр перемальовування.
         Тобто, оновлює значення self.x і self.y з урахуванням швидкостей
         self.vx і self.vy, сили гравітації, що діє на м'яч,
         і стін по краях вікна (розмір вікна 800х600).
        """
        # FIXME
        if self.x + self.vx < 0:
            self.vx *= -1
        if self.x + self.vx > 800:
            self.vx *= -1
        if self.y - self.vy < 0:
            self.vy *= -1
        if self.y - self.vy > 600:
            self.vy *= -1

        self.vy -= 1
        if 0 < self.x + self.vx < 800:
            self.x += self.vx
        if 0 < self.y - self.vy < 600:
            self.y -= self.vy
        self.set_cords()

        self.vx -= 0.05 * self.vx / abs(self.vx)
        self.vy -= 0.05 * self.vy / abs(self.vy)

        if abs(self.vx) - 0.05 < 0 and abs(self.vy) - 0.05 < 0:
            canvas.delete(self.id)

    def hittest(self, obj):
        """ Функція перевіряє чи зіткнулися обєкт і ціль
        Args:
            obj: Обєкт в якому перевіряється зіткнення
        Returns:
            Повертає True якщо ціль зіткнулася, якщо  ні, то False.
        """
        # FIXME
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 > \
                (self.r + obj.r) ** 2:
            return False
        else:
            return True


class Gun:
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.angle = 1
        self.x = 20
        self.y = 450
        self.id = canvas.create_line(self.x, self.y, 50, 420, width=7)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Постріл м'ячем.
         Відбувається при відпуску кнопки миші.
         Початкові значення компонент швидкості м'яча vx і vy
         залежать від положення миші.
        """
        global balls, bullet
        bullet += 1
        r = 5
        self.angle = math.atan((event.y - self.y) / (event.x - self.x))
        self.x = 20 + max(self.f2_power, 20) * math.cos(self.angle),
        self.y = 450 + max(self.f2_power, 20) * math.sin(self.angle)
        vx = self.f2_power * math.cos(self.angle)
        vy = - self.f2_power * math.sin(self.angle)
        new_ball = Ball(x, y, vx, vy)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Ціль, залежить від розположення мишки"""
        if event:
            self.angle = math.atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            canvas.itemconfig(self.id, fill='red')
        else:
            canvas.itemconfig(self.id, fill='black')
        canvas.coords(self.id, 20, 450,
                      20 + max(self.f2_power, 20) * math.cos(self.angle),
                      450 + max(self.f2_power, 20) * math.sin(self.angle)
                      )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canvas.itemconfig(self.id, fill='orange')
        else:
            canvas.itemconfig(self.id, fill='black')


class Target:
    def __init__(self, x, y, R):
        self.points = 0
        self.live = 1

        # FIXME: don't work! How to call this functions when object is created?
        self.id = canvas.create_oval(0, 0, 0, 0)
        self.id_points = canvas.create_text(30, 30, text=self.points,
                                            font='28')
        self.new_target()

    def new_target(self):
        """ Ініціалізація нової цілі """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        color = self.color = 'red'
        canvas.coords(self.id, x - r, y - r, x + r, y + r)
        canvas.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        """Попадання шаріка в ціль"""
        canvas.coords(self.id, -10, -10, -10, -10)
        self.points += points
        canvas.itemconfig(self.id_points, text=self.points)


screen1 = canvas.create_text(400, 300, text='', font='28')
gun1 = Gun()
bullet = 0
balls = []


def new_game(event=''):
    global gun1, target, screen1, balls, bullet
    targets = []
    for i in range(2):
        targets.append(Target())
    bullet = 0
    balls = []
    canvas.bind('<Button-1>', gun1.fire2_start)
    canvas.bind('<ButtonRelease-1>', gun1.fire2_end)
    canvas.bind('<Motion>', gun1.targetting)


def time_handler():
    target.live = 1
    while target.live or balls:
        for ball in balls:
            if ball.vx == 0 and ball.vy == 0:
                canvas.delete(ball.id)
            ball.move()
            for i in target:
                if ball.hittest(i) and i.live:
                    i.live = 0
                    i.hit()
                    target.remove(i)
        if len(target) == 0:
            canvas.bind('<Button-1>', '')
            canvas.bind('<ButtonRelease-1>', '')
            canvas.itemconfig(screen1, text='Ціль знщена за ' +
                                            str(bullet) + ' вистрілів')
        canvas.update()
        time.sleep(0.03)
        gun1.targetting()
        gun1.power_up()
    canvas.itemconfig(screen1, text='')
    canvas.delete(Gun)
    root.after(750, new_game)


main()
new_game()
root.mainloop()
