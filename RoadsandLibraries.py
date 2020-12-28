#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
    min_cost=0
    preKey = None
    if c_lib <=c_road:
        min_cost= c_lib*n
    else:
        graph =dict()
        visited =set() #Set is a unique list of elements
    
        for connections in cities:
            c0=connections[0] ##Creates new instances of cities
            c1 =connections[1]
            if c0 in visited and c1 in visited: 
                continue

            if c0 in visited:
                c0_val =graph.get(c0)
                if c0_val:  ##Checks if the value is empty
                    graph[c0]= c0_val + [c1]
                    preKey = c0
                    print(preKey)
        
                else:
                    prev_vals= graph.get(preKey)
                    graph[prev_vals] =preKey.append(c1) ##Append to previous key and append
                    print("c0 is not a key, appending to prev")

                visited.add(c0)

            elif c1 in visited:
                c1_val = graph.get(c1)
                if c1_val:
                    graph[c1] =c1_val + [c0]
                    preKey= c1
                else:
                    prev_vals =graph.get(preKey)
                    graph[preKey]= prev_vals +[c0]

                visited.add(c0)
            else:
                #Checks for any previous values at c0
                pre_vals =graph.get(c0)
                print("c0_vals",pre_vals) #Prints out c0_vals

                #Options are to append c1 to pre_vals or create new list of items
                graph[c0] =pre_vals+ [c0] if pre_vals else [c1]

                preKey = c0

                visited.add(c0)
                visited.add(c1)

    for k, v in graph.items():
        print("k: ", k, "v: ",v)
    num_libs= len(graph.keys())
    min_cost = (len(graph.keys())*c_lib) +((n-num_libs)+c_road)
    return min_cost


if __name__ == '__main__':
    print(roadsAndLibraries(5,6,1, [[1,2],[1,3],[1,4]]))
