import numpy as np
import matplotlib.pyplot as plt
class Manager:

    def __init__(self, universe):

        self.uni = universe
        self.history=dict()
        self.figure=plt.figure('Stats')

    def plot_and_update(self):

    	stats=self.uni.get_stats()
    	for key,value in stats.items():
    		self.history[key] = self.history.get(key, list()) + [value]


    	self.figure.clf()
    	for key,value in self.history.items():
    		plt.plot(range(len(value)),value,'-+',label=key)

    	plt.legend()
    	plt.show()
    	self.uni.update()
    
