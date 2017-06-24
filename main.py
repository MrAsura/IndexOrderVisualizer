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
Create order data based on the format
"""
def createIndexOrderInfo(frmt):
    #Count  number of bits in y and x coordinate
    xbits = 0
    ybits = 0
    for b in frmt:
        if b is '0':
            xbits += 1
        else:
            ybits += 1
            
    if xbits is 0 or ybits is 0:
        raise ValueError("Format needs to have at least one x bit and y bit.")
    
    xticks = [ ("{{0:^}}\n{{0:0{len}b}}").format(len=xbits).format(i) for i in range(2**xbits) ]
    yticks = [ ("{{0:^}}\n{{0:0{len}b}}").format(len=ybits).format(i) for i in range(2**ybits) ]
    
    xs = []
    ys = []

    for i in range(2**len(frmt)):
        x = 0
        y = 0
        for (fb,ib) in zip(frmt,"{{0:0{len}b}}".format(len=len(frmt)).format(i)):
            if fb is '0':
                x = (x << 1) + int(ib,2)
            else:
                y = (y << 1) + int(ib,2)
        xs.append(x)
        ys.append(y)
  
    return (xs,ys,xticks,yticks)

"""
Create a plot for the index order for the given parameters
"""
def printIndexOrder(frmt, xs, ys, xticks, yticks):
    pp.figure(figsize=(len(xticks),len(yticks)))
    pp.plot(xs,ys)
    pp.title(frmt, y=(1 + 1/len(yticks)))
    pp.xlabel("x")
    pp.ylabel("y")
    pp.xticks(range(len(xticks)), xticks, rotation='horizontal')
    pp.yticks(range(len(yticks)), yticks, rotation='vertical')
    
    ax = pp.gca()
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position('top')
    ax.invert_yaxis()
    #ax.tick_params(axis='x',which='major',pad=len(xticks))
    #ax.tick_params(axis='y',which='major',pad=len(yticks))
    
    pp.margins(1/(len(xticks)+len(yticks)))
    pp.subplots_adjust(bottom=0.15)

if __name__ == "__main__":
    
    frmt = input("Give indexing format: ")
    if(not re.match(r"^[10]*$",frmt)):
        raise ValueError("Incorrect format. Only use 1s and 0s.")
    """
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
    """
    
    printIndexOrder(frmt, *createIndexOrderInfo(frmt))