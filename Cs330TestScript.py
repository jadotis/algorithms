# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 12:26:28 2017

@author: Jadotis
"""

    
def valueCalc(array):
    #These values are arbitrary to the function
    i = array[0]
    j = array[1]
    k = array[2]
    
    Total = i[0] * i[1]
    Total += j[0] *(i[1] + j[1])
    Total += k[0] * (i[1] + j[1] + k[1])
    print(Total)
    return Total
    
    
#Test Cases:
#(weight, Time)
print("Ascending T/W")
valueCalc([(9,1), (6,7), (2,6)])  #1/9 7/6 3
valueCalc([(11,1), (9,2), (14,28)]) #1/11 2/9 2
valueCalc([(2,3), (24,67), (12,232)]) #3/2 large larger

print("Descending T/W")
valueCalc([(2,6), (6,7), (9,1)]) #3  7/6 1/9
valueCalc([(14,28), (9,2), (11,1)]) # 2 2/9 1/11
valueCalc([(12,232), (24,67), (2,3)]) #Reverse of 3



print("Now testing W/T")


print("Ascending W/T")
valueCalc([(11,11), (12, 7), (12,2)]) #1 12/7 6
valueCalc([(11,1), (144, 12), (100,1)]) #11 12 100
valueCalc([(1,7), (2, 7), (1,1)]) # 1/7 2/7 1

print("Descending W/T")
valueCalc([(12,2), (12, 7), (11,11)])
valueCalc([(100,1), (144, 12), (11,1)])
valueCalc([(1,1), (2,7), (1,7)])

print("Finished")
    