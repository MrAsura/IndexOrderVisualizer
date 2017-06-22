# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 19:54:08 2017

Program for visualizing index order of custom schemas in 2D arrays

@author: Jaakko
"""
import re
import matplotlib.pyplot as pp

#%%
"""
Create a plot for the index order for the given parameters
"""
def printIndexOrder(frmt, xs, ys, xticks, yticks):
    pp.plot(xs,ys)
    pp.title(frmt, y=1.2)
    pp.xlabel("x")
    pp.ylabel("y")
    pp.xticks(range(len(xticks)), xticks, rotation='horizontal')
    pp.yticks(range(len(yticks)), yticks, rotation='vertical')
    
    ax = pp.gca()
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position('top')
    ax.invert_yaxis()
    
    pp.margins(0.2)
    pp.subplots_adjust(bottom=0.15)

if __name__ == "__main__":
    
    frmt = "11"#input("Give indexing format: ")
    if(not re.match(r"^[10]*$",frmt)):
        raise ValueError("Incorrect format. Only use 1s and 0s.")
    
    xs = [0, 1, 2, 3, 4,
          0, 1, 2, 3, 4,
          0, 1, 2, 3, 4]
    
    ys = [0, 0, 0, 0, 0,
          1, 1, 1, 1, 1,
          2, 2, 2, 2, 2,]
    lenx = 5
    leny = 3
    xticks = [ ("{0:^}\n{0:0"+str(lenx)+"b}").format(i) for i in range(lenx) ]
    yticks = [ ("{0:^}\n{0:0"+str(leny)+"b}").format(i) for i in range(leny) ]
    
    printIndexOrder(frmt, xs, ys, xticks, yticks)