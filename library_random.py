import numpy as np
import time

class RandomGen(object):

    number = None

    def __init__(self):
        pass

    def run(self):

        while True:
            self.number = np.random.rand()
            print(self.number)
            time.sleep(3);


if __name__ == "__main__":

    rand = RandomGen()

    rand.run()