import time
import random

print('Welcome to Rolling Dice\n\n')

while True:
    rolled_num = random.randint(1,6)
    print('rolling dice...')
    time.sleep(1)
    print('you got a', rolled_num)
    input('Press a key to roll again')
