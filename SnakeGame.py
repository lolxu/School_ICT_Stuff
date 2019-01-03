import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint

with open("UserData.txt") as f: #in read mode, not in write mode, careful
    rd = f.readline()
    MaxName = rd
    rs = f.readline()
    MaxScore = int(rs)
    
print("\n" + MaxName + "has the Highest Score of " + rs)
print("\n")
name = raw_input("Please Input your user name : ")
print("\n")
a = raw_input("Press any key to continue...")

curses.initscr()

BIGX = 60
BIGY = 20

win = curses.newwin(BIGY, BIGX, 0, 0)
win.keypad(1)

curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

key = KEY_RIGHT                                                    # Initializing values
score = 0

snake = [[4,10], [4,9], [4,8]]                                     # Initial snake co-ordinates
food = [10,20]                                                     # First food co-ordinates

win.addch(food[0], food[1], '0')                                   # Prints the food

while key != 27:                                                   # While Esc key is not pressed
    win.border(0)
    win.addstr(0, 2, 'Score : ' + str(score) + ' ')                # Printing 'Score' and
    win.addstr(0, BIGX/2, ' SNAKE ')                               # 'SNAKE' strings
    win.timeout(150 - (len(snake)/5 + len(snake)/10)%120)          # Increases the speed of Snake as its length increases
    
    prevKey = key                                                  # Previous key pressed
    event = win.getch()
    key = key if event == -1 else event 

    if key == ord(' '):                                            # If SPACEis pressed, wait for another
        key = -1                                                   # one (Pause/Resume)
        while key != ord(' '):
            key = win.getch()
        key = prevKey
        continue

    if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:     # If an invalid key is pressed
        key = prevKey

    snake.insert(0, [snake[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1), snake[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)])

    if event in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN]:
        score -= 1
    
    
    if snake[0][0] == 0: snake[0][0] = BIGY-2
    if snake[0][1] == 0: snake[0][1] = BIGX-2
    if snake[0][0] == BIGY-1: snake[0][0] = 1
    if snake[0][1] == BIGX-1: snake[0][1] = 1

    # Exit if snake crosses the boundaries
    #if snake[0][0] == 0 or snake[0][0] == 19 or snake[0][1] == 0 or snake[0][1] == 59: break

    # Snake dies...
    if snake[0] in snake[1:]: break

    
    if snake[0] == food:                                            
        food = []
        score += 5
        while food == []:
            food = [randint(1, BIGY-2), randint(1, BIGX-2)]         
            if food in snake: food = []
        win.addch(food[0], food[1], '0')
    else:    
        last = snake.pop()                                          
        win.addch(last[0], last[1], ' ')
    win.addch(snake[0][0], snake[0][1], '#')
    
curses.endwin()

if score > MaxScore:
    print("************************")
    print("**                    **")
    print("**  New High Score !  **")
    print("**                    **")
    print("************************")
    
    with open("UserData.txt","w") as f:
        f.write(format(name))
        f.write("\n")
        f.write(format(score))

print("\nYour Score - " + str(score))


