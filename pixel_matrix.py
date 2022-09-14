import numpy as np
from matplotlib import pyplot as plt

class PixelMatrix:
    pixels = []
    
    def loadMatrix(self, resolution):
        self.pixels = np.zeros(shape=resolution)
        

    def showMatrix(self):
        image = np.array(self.pixels, dtype=np.uint8)
        plt.imshow(image, interpolation='none')
        plt.show()

