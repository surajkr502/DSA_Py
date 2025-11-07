# 1. Give an array with some integer type value.Write a python script to short array.
from array import *
# arr=array('i',[6,4,9,7,12,9,33,67,92,100,45,78,234,578,3556,7543])
# a_list=list(arr)
# print(sorted(a_list))

# 2. Give an array with some integer type value.Write a python script to short array without using in built fn and method.
arr=array('i',[45,74,67,25,96,4,99,23,75,96,53,28,85,30])
n=len(arr)
for i in range(n):
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print('sorted arr is:',arr)

# 3. Give a list of heterogenous elements.Write a python scripts to remove all the non int value from the list.
# list=(1,3,'python','@',53,'java')
# li_int=()
# for i in list:
#     if i ==int:
#         print(i)
    