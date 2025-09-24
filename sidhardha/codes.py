colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']
text = "Python is Awesome!"

while True:
    for color in colors:
        print(f"{color}{text}\033[0m", end="\r")


vs = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

snk = [[sh//2, sw//4 + i] for i in range(3)][::-1]
food = [sh//2, sw//2]
w.addch(food[0], food[1], 'O')

key = curses.KEY_RIGHT
while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    head = [snk[0][0] + (key == curses.KEY_DOWN and 1) + (key == curses.KEY_UP and -1),
            snk[0][1] + (key == curses.KEY_LEFT and -1) + (key == curses.KEY_RIGHT and 1)]

    if head in snk or head[0] in [0, sh] or head[1] in [0, sw]:
        curses.endwin()
        quit()

    snk.insert(0, head)
    if head == food:
        food = None
        while food is None:
            nf = [random.randint(1, sh-1), random.randint(1, sw-1)]
            food = nf if nf not in snk else None
        w.addch(food[0], food[1], 'O')
    else:
        tail = snk.pop()
        w.addch(tail[0], tail[1], ' ')

    w.addch(snk[0][0], snk[0][1], '#')

#turtle drawing

t = turtle.Turtle()
t.speed(0)
colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']

for i in range(360):
    t.pencolor(colors[i % 6])
    t.forward(i)
    t.left(59)

turtle.done()

