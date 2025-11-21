import os
import time
import shutil

# Clear screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Get terminal size
def get_terminal_size():
    size = shutil.get_terminal_size((80, 20))
    return size.columns, size.lines

# Red heart ASCII
HEART = [
    "\033[31m  **   **  \033[0m",
    "\033[31m ****** ** \033[0m",
    "\033[31m***********\033[0m",
    "\033[31m ********* \033[0m",
    "\033[31m  *******  \033[0m",
    "\033[31m   *****   \033[0m",
    "\033[31m    ***    \033[0m",
    "\033[31m     *     \033[0m"
]

# Heart animation
def animate_heart(frames=300, delay=0.08):
    cols, rows = get_terminal_size()
    w = len(HEART[0])
    h = len(HEART)

    x = 0
    y = 0
    dx = 1
    dy = 1

    for _ in range(frames):
        clear()

        # Bounce logic
        if x + w >= cols - 1: 
            dx = -1
        if x <= 0: 
            dx = 1
        if y + h >= rows - 2: 
            dy = -1
        if y <= 0: 
            dy = 1

        x += dx
        y += dy

        # Print empty lines above heart
        for _ in range(y):
            print()

        # Print heart at location
        for line in HEART:
            print(" " * x + line)

        time.sleep(delay)

# Run animation
try:
    animate_heart()
except KeyboardInterrupt:
    clear()
    print("❤ Animation stopped.")
