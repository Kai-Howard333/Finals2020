from random import randint
import random
class PWGenerator:
    def __init__(self):
        self.caps = random.randint(1,5)
        self.lows = random.randint(1,5)
        self.n = random.randint(1,5)
        self.symbol = random.randint(1,5)
        self.password = ''
        self.special = 0

    def createPW(self):

        for i in range(self.caps):
            self.password += chr(randint(65,90))
        for i in range(self.lows):
            self.password += chr(randint(97,122))
        for i in range(self.n):
            self.password += chr(randint(48,57))

        while self.symbol != 0:     # this makes python search for the special characters on the keypad 1-0 !-)
            self.special = randint(33,64)
            if self.special == 33 \
            or self.special == 35 \
            or self.special == 36 \
            or self.special == 37 \
            or self.special == 38 \
            or self.special == 40 \
            or self.special == 41 \
            or self.special == 42 \
            or self.special == 64:
                self.password += chr(self.special)
                self.symbol -= 1
        self.password = ''.join(random.sample(self.password, len(self.password)))   #randomizes the password even more
        return str(self.password)

print(f'Here is your new generated password:\n{PWGenerator().createPW()}')