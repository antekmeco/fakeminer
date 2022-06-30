import platform
import random
import string
from time import sleep

import pyfiglet
from colorama import init, Fore

print(Fore.GREEN + pyfiglet.figlet_format("ExoMiner"))
letters = string.punctuation
if platform.system() == "Windows":
    init(convert=True)
eth = 0
while True:
    sleep(0.50)
    thing = ''.join(random.choice(string.ascii_letters) for i in range(25))
    print(" | " + Fore.RED + thing + Fore.YELLOW + f" |  ETH {round(eth, 4)} | ")
    eth += 0.00001
    if eth > 1:
        with open("hit.txt", "w") as f:
            f.write(thing)
        print("Mined 1 eth!")
        print("Sending to hit.txt")
        break
