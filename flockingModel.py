#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import random as rd
import sys

class flock():
    def __init__(self,bird_array):
        self.birds = bird_array
        self.numBirds = len(bird_array)
    def get_center(self,i):
        pos = np.array([0.,0.])
        for n in range(0,self.numBirds):
            if n != i:
                pos += self.birds[n].pos
        pos /= (self.numBirds-1)
        return pos            
    def update(self):
        old_birds = self.birds
        for n in range(0,self.numBirds):
            goto = self.get_center(n)
            if np.linalg.norm(goto - self.birds[n].pos) > 1.:
                self.birds[n].orient(goto)
            self.birds[n].update()      
    def show_flock(self):
        for bird in self.birds:
            plt.plot(bird.pos[0],bird.pos[1],'.')
        #xmin = min([bird.pos[0] for bird in self.birds])-1
        #xmax = max([bird.pos[0] for bird in self.birds])+1
        #ymin = min([bird.pos[1] for bird in self.birds])-1
        #ymax = max([bird.pos[1] for bird in self.birds])+1
        #plt.xlim([xmin,xmax])
        #plt.ylim([ymin,ymax])
        plt.xlim([-10,15])
        plt.ylim([-10,15])
        plt.draw()

class bird():
    def __init__(self,pos,vel=[0.,0.],speed=1.):
        self.pos = np.array(pos)
        self.vel = np.array(vel)
        self.speed = speed
        self.vel *= speed/np.linalg.norm(self.vel)
    def orient(self,target):
        self.vel += (target - self.pos)*.1
        self.vel *= self.speed/np.linalg.norm(self.vel)
    def update(self):
        self.pos += self.vel*.2


if __name__ == '__main__':
    print sys.argv
    if len(sys.argv)!=3: 
        print('need two args: number_of_birds length_of_simulation')
    else:
        numBirds = int(sys.argv[1]); T = int(sys.argv[2])
        myFlock = flock([bird([rd.uniform(0,5),rd.uniform(0,5)],[rd.uniform(0,1),rd.uniform(0,1)],1.) for n in range(0,numBirds)])
        for t in range(0,T):
            plt.clf()
            myFlock.show_flock()
            myFlock.update()
            plt.pause(.001)
