import random

class Password:
    def __init__(self):
        self.cl='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.sm='abcdefghijklmnopqrstuvwxyz'
        self.symbol='!@#$%^&*()_-+={}[]<>?'
        self.digit='1234567890'

    def get(self):
        n=random.randint(8,12)
        p=[]
        a=n//4
        for i in range(a):
            p.append(random.choice(self.cl))
        for i in range(a):
            p.append(random.choice(self.sm))
        for i in range(a):
            p.append(random.choice(self.symbol))
        for i in range(n-(3*a)):
            p.append(random.choice(self.digit))
        random.shuffle(p)
        return "".join(p)


    
