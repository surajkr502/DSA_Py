# 1. Give an array with some integer type value.Write a python script to short array.
from array import *
# arr=array('i',[6,4,9,7,12,9,33,67,92,100,45,78,234,578,3556,7543])
# a_list=list(arr)
# print(sorted(a_list))

# 2. Give an array with some integer type value.Write a python script to short array without using in built fn and method.
# arr=array('i',[45,74,67,25,96,4,99,23,75,96,53,28,85,30])
# n=len(arr)
# for i in range(n):
#     for j in range(0,n-i-1):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]
# print('sorted arr is:',arr)

# 3. Give a list of heterogenous elements.Write a python scripts to remove all the non int value from the list.
# list=[1,5.5,'java',6,True,28,False,9.0,'cpp']
# print('original heterogenous list:',list)
# int_arr=[]
# for i in list:
#     if type(i)==int:
#         int_arr.append(i)
# print(int_arr)

# Shorter version (using list comprehension)
# int_arr=[i for i in list if type(i)==int]
# print(int_arr)

#
# 4. Give a list of heterogenous elements.Write a python scripts to remove all the non int value from the list without using method or fn.
# n=len(list)
# for i in range(n):
#     try:
#         if list[i]==int (list[i]):
#             if not(list[i] is True or list[i] is False):
#                 int_arr=int_arr+[list[i]]
#     except:
#         # Ignore elements that cannot be converted to int
#         pass
# print(int_arr)

# 5. Write a python script  to calculate average of elements of list.
list=[54,67,12,96,50,36,74,38,65]
# if list==0:
#     print('list is empty')
# else:
#     total=sum(list)
#     count=len(list)
# average=total/count
# print(round(average,2))

# 6. Write a python script  to calculate average of elements of list without using any method.
# total=0
# count=0
# for i in list:
#     total=total+i
#     count=count+1
# average=total/count
# print(round(average,2))


# Write a python script to create a list to first  n prime numbers.
n=int(input('Enter how many prime numbers you want:'))
prime=[]
# if n%1==0 &
# Write a python script to create a list to first n term of fibonacci series.