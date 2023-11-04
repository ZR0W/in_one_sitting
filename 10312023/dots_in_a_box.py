# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 20:59:01 2023

@author: Rowland
"""

"""
reference
https://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/
"""

# imports
import numpy as np
from scipy.spatial.distance import pdist, squareform

import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation


if __name__ == "__main__":
    print("Hello World")
    
    # TODO: define box and particle classes
    
    fig = plt.figure()
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    ax = fig.add_subplot(111, aspect='equal', autoscale_on=False, xlim=(-3.2, 3.2), ylim=(-2.4, 2.4))
    
    particles, = ax.plot([], [], 'bo', ms=6)
    text = ax.text(-1,-1,'oops', fontsize=10)
    
    start = [0,0]
    angle = 0
    rect = plt.Rectangle(start, 2, 2, angle, ec='none', lw=2, fc='none')
    rect.set_edgecolor('green')
    ax.add_patch(rect)
    
    def init():
        # initialize animation
        global particles, rect, angle, text
        start = [-2,-2]
        rect.set_edgecolor('r')
        rect.set_xy = start
        rect.angle = angle
        text.text = 'hi'
        return text, rect
    
    def animate(i):
        global particles, rect, angle, text
        rect.set_edgecolor('b')
        rect.angle = angle+i
        text.text = str(i)
        print(i)
        return text, rect
    
    ani = animation.FuncAnimation(fig, animate, frames=600, interval=10, blit=True, init_func=init)
        
    plt.show()
