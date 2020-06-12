#Objective: Dive deeper into Numpy

import pandas as pd #Import needed to work with Pandas
import numpy as np #Import needed to work with Numpy

arr = np.array([[1,2,3],[4,5,6]]) #2 Dimensional numpy array
print("Array dimensions are: ",arr.ndim) #Print array dimensions
print("Array shape is: ",arr.shape) #Print array coordinates
print("Array size is: ",arr.size) #Print total number of array elements
print("Array datatype(s) includes: ",arr.dtype,"\n\n") #Prints datatype of array elements

print("List of values from 0 - 30 incremented by 5")
arr2 = np.arange(0,30,5) #Create an array with values from 0 to 30 in 5 step increments
print(arr2,"\n\n")

print("List of 11 values from 0 - 10")
arr3 = np.linspace(0,10,11) #Create a list of 11 values from 0 to 10
print(arr3,"\n\n")

print("New resized numpy array")
arr_reshape = arr.reshape(3,1,2) #Transforms the numpy array to a 3x1x2
print(arr_reshape,"\n\n")

print("New flattened array")
flatten_arr = arr_reshape.flatten() #Transforms the reshaped array to a Y x 1 array
print(flatten_arr,"\n\n")

print("Slicing numpy arrays")
sliced_arr = arr_reshape[:2]
print(sliced_arr,"\n\n")

print("Conditional indexing")
cond = flatten_arr < 3 #stores the condition for indexing
index_arr = flatten_arr[cond] #Only stores values where the condition is true
print(index_arr,"\n\n")

print("Transpose operation")
transpose_sliced_arr = sliced_arr.T #Rotate sliced_arr on axis
print(transpose_sliced_arr,"\n\n")

print("Max value in flatten arr:")
max_flatten_arr = flatten_arr.max(axis =0) #Stores the max value in the array column-wise
print(max_flatten_arr,"\n\n")


print("Min value in sliced arr:")
min_sliced_arr = sliced_arr.min(axis = 0) #Stores the min value in the array column-wise
print(min_sliced_arr,"\n\n")

print("Sum value in flatten arr:")
sum_flatten_arr = flatten_arr.sum() #Stores the sum of values in the array
print(sum_flatten_arr,"\n\n")

print("Numpy arrays can be sorted","\n\n")

print("Select values based on condition")
condlist = [flatten_arr<3] #Create condition for selection
choicelist = [flatten_arr] #Define what the condition will be applied to
print(np.select(condlist, choicelist),"\n\n") #Performs select function

print("Where: chose elements depending on the conditions")
condition = flatten_arr < 5 #Condition to print values from flatten_arr
print(np.where(condition,flatten_arr,0),"\n\n")#Performs where function, when not in the condition prints 0


print("Floor: floor of the values in the numpy array")
floor_arr = np.array([3.5,4.3,2.2,5.9]) #Create generic array
print(np.floor(floor_arr),"\n\n") #performs floor function on the array

