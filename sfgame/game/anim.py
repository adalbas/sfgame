# Filename: anim.py
# 
# Add license here

# Author: Adalberto Medeiros (adalbas@gmail.com)
# Code references: spritesheet from pygame docs


class BaseAnimation(object):
    """sprite strip animator
    
    This class provides an iterator (iter() and next() methods), and a
    __add__() method for joining strips which comes in handy when a
    strip wraps to the next row.
    """
    def __init__(self, images, loop=False, frames=1):
        """
        BaseAnimation class
        
        Receives an array (images) and iterates it considering the frame rate
        and loop
        
        loop is a boolean that, when True, causes the next() method to
        loop. If False, the terminal case raises StopIteration.
        
        frames is the number of ticks to return the same image before
        the iterator advances to the next image.
        """
        self.i = 0
        self.loop = loop
        self.frames = frames
        self.f = frames
        self.images = images
  
    def iter(self):
        self.i = 0
        self.f = self.frames
        return self
    
    def next(self):
        if self.i >= len(self.images):
            if not self.loop:
                raise StopIteration
            else:
                self.i = 0
        image = self.images[self.i]
        self.f -= 1
        if self.f == 0:
            self.i += 1
            self.f = self.frames
        return image
    
    def __add__(self, ss):
        self.images.extend(ss.images)
        return self
    
    def start(self):
        pass
    
    def stop(self):
        pass
    
    def pause(self):
        pass
    
    def resume(self):
        pass
        