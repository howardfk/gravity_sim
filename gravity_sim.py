#!/usr/bin/env python
import matplotlib.pylab as plt 
import numpy as np

class Force(object):
   def __init__(self,p1, p2):
      #self.force=np.array([0,0,0])
      self.update(p1,p2)

   def update(self, p1,p2):
      """Force on p1 from p2"""
      sep = p1.pos - p2.pos
      mag = np.linalg.norm(sep)
      print mag
      self.force = -(p1.mass*p2.mass)*sep/mag**3
   


class Partical(object):
   dt = 0.1
   """
   Attributes:
   positoin
   velocity
   acceleration
   mass
   """
   def __init__(self, pos=np.array([0.,0.,0.]),velc = np.array([0.,0.,0.]), mass = 1.0):
      self.pos = pos
      self.velc = velc
      self.mass = float(mass)

   def update(self, force):
      self.velc +=  force*Partical.dt/self.mass
      self.pos += self.velc*Partical.dt
      
pos1 = np.array([10.0,0.0,0.0])      
vel1 = np.array([0.0,1.2,0.0])      
pos2 = np.array([0.0,0.0,0.0])      
vel2 = np.array([0.0,0.0,0.0])      

p1 = Partical(pos1, vel1)
p2 = Partical(pos2, vel2, 90.9)
grav = Force(p1,p2)

for n in range(0,150):
   plt.clf()
   plt.xlim([min(p1.pos[0],p2.pos[0])-1,max(p1.pos[0],p2.pos[0])+1])
   plt.ylim([min(p1.pos[1],p2.pos[1])-1,max(p1.pos[1],p2.pos[1])+1])
   plt.plot(p1.pos[0],p1.pos[1],'o')
   plt.plot(p2.pos[0],p2.pos[1],'o')     
   plt.draw()
   plt.pause(0.03)
   p1.update(grav.force)
   p2.update(-grav.force)
   grav.update(p1,p2)
   print grav.force, p1.pos


