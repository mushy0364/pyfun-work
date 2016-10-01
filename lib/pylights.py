'''Colorful holiday lights for coding loops of all kinds'''

import colors as c
import time

LEFT = '''
       
       
       
       
       
       
       
       
'''

WIRE = '''
c.--._.--
'''

BASE = '''
c   _Y_  
c  [___] 
'''

BULB = '''
c  /:' \ 
c |::   |
c \::.  /
c  \::./ 
c   '='  
'''

def join_ascii(join,sep=""):
    joined = ""
    join = [LEFT] + join
    tjoin = [str(i).split("\n") for i in join]
    longest = 0
    for t in tjoin:
        l = len(t)
        if l > longest: longest = l
    for i in range(longest):
        for j in range(len(tjoin)):
            joined += tjoin[j][i] + sep
        joined += "\n"
    return joined


class Bulb():
    base_color = c.base00
    wire_color = c.base03

    def __init__(self,color=c.base00):
        self.text = BULB
        self.color = color

    def __str__(self):
        lit = WIRE.replace("c",self.base_color).rstrip('\n')
        lit += BASE.replace("c",self.wire_color).rstrip('\n')
        lit += self.text.replace("c",self.color)
        return lit

class Set(list):

    def __init__(self,color=c.base00):
        self._color = color
        for i in range(8):
            self.append(Bulb(color))

    @property
    def color(self):
        return self._color 

    @color.setter
    def color(self,val):
        for i in self:
            i.color = val

    def randomize(self):
        for i in self:
            i.color = c.random()

    def update(self):
        print(c.clear)
        print(join_ascii(self) + c.reset)

    def demo(self):
        try: 
            while True:
                self.randomize()
                self.update()
                time.sleep(0.25)
        except KeyboardInterrupt:
            exit()

if __name__ == '__main__':
    import pylights
    pylights.Set().demo()



