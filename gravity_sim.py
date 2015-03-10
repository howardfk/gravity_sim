#!/usr/bin/env python
import matplotlib.pylab as plt 
import numpy as np
import matplotlib.animation as ani

class Force(object):
   def __init__(self,p1, p2):
      #self.force=np.array([0,0,0])
      self.update(p1,p2)

   def update(self, p1,p2):
      """Force on p1 from p2"""
      sep = p1.pos - p2.pos
      mag = np.linalg.norm(sep)
      self.force = -(p1.mass*p2.mass)*sep/mag**3
   


class Partical(object):
   dt = 0.3
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

def makemovie(p1,p2):   
   FFMpegWriter = ani.writers['ffmpeg']
   metadata = dict(title = 'Gravity simulation')
   writer = FFMpegWriter(fps = 15, metadata = metadata)

   fig = plt.figure()
   l, = plt.plot([],[], 'o')
   l2, = plt.plot([],[], 'o')

   plt.xlim([min(p1.pos[0],p2.pos[0])-3,max(p1.pos[0],p2.pos[0])+3])
   plt.ylim([min(p1.pos[1],p2.pos[1])-3,max(p1.pos[1],p2.pos[1])+3])

   with writer.saving(fig, "grav_sim_bigstep.mp4", 100): #100 is the dpi
      for n in range(0,4000):
         plt.xlim([min(p1.pos[0],p2.pos[0])-3,max(p1.pos[0],p2.pos[0])+3])
         plt.ylim([min(p1.pos[1],p2.pos[1])-3,max(p1.pos[1],p2.pos[1])+3])
         if n%9==0:
            l.set_data(p1.pos[0],p1.pos[1])
            l2.set_data(p2.pos[0],p2.pos[1])
            writer.grab_frame()
         p1.update(grav.force)
         p2.update(-grav.force)
         grav.update(p1,p2)
      
      

pos1 = np.array([1.0,0.0,0.0])      
pos2 = np.array([0.0,0.0,0.0])      

vel1 = np.array([0.3,0.5,0.0])      
vel2 = np.array([0.0,-0.5,0.0])      

p1 = Partical(pos1, vel1)
p2 = Partical(pos2, vel2)
grav = Force(p1,p2)

makemovie(p1,p2)

"""
for n in range(0,90):
   #plt.clf()
   plt.xlim([min(p1.pos[0],p2.pos[0])-3,max(p1.pos[0],p2.pos[0])+3])
   plt.ylim([min(p1.pos[1],p2.pos[1])-3,max(p1.pos[1],p2.pos[1])+3])
   plt.plot(p1.pos[0],p1.pos[1],'o')
   plt.plot(p2.pos[0],p2.pos[1],'o')     
   if n%9==0:
      plt.draw()
   plt.pause(0.01)
   p1.update(grav.force)
   p2.update(-grav.force)
   grav.update(p1,p2)
#   print grav.force, p1.velc
"""
