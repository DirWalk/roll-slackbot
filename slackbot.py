import sys
import random
import os
import secrets

#ver_token = secrets.VERIFICATION_TOKEN


def roll(arg, mod=0):
    rolls = int(arg.split('d')[0])
    sides = int(arg.split('d')[1]) + 1
    modifier = int(mod)
    for _ in range(rolls):
        rand_number = random.choice(range(modifier + 1, sides + modifier))
        print("Your roll is: {}".format(rand_number))


def run():
    if len(sys.argv) == 3:
        roll(sys.argv[1], int(sys.argv[2]))
    else:
        roll(sys.argv[1])


#if __name__ == '__main__':
#    run()


if __name__ == '__main__':
    for _ in range(sys.argv[3]):
        run()