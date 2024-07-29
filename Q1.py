#Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i. 
#This was asked by Uber. Example array=[1,2,3,4] output is [24,12,8,6]


import math

def product_of_integers(lst1): 
    result = [] #Iniitalise a new array
    for i in range(len(lst1)):
        left = lst1[:i] #take all the elements before i (not inclusive)  
        right = lst1[i+1:] #take all elements after i
        left_product = math.prod(left) #product of left side
        right_product = math.prod(right) #product of right side
        result.append(left_product * right_product) #append the final product by * both left_prod and right_prod
    return result
