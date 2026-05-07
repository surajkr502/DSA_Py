# n=input('enter any no.')
# n=10
# i,count=1,0
# for i in range(n): 
#     for j in range(n):
#         count=count+1

# print(count)

# n=input('enter any no.')


# n=1000
# i,count=1,0
# while i<=n: 
#     count=count+1
#     i=i*2           #o(logn base 2)
# print(count)

# n=int(input('enter a no.'))
# i,count=1,0
# while i>=n: 
#     count=count+1
#     i=i//2           #o(logn base 2)
# print(count)


# Stack (push)
# stack=[]
# element=int(input('enter element:'))
# stack.append(element)
# print(stack)


# stack=[]
# n=int(input('enter no. of element:'))
# for i in range(n): 
#     element=int(input('enter element:'))
#     stack.append(element)
# print(stack)
# x=stack.pop()
# print(x,stack)

# stack=[]
# n=int(input('enter no. of element:'))
# for i in range(n): 
#     element=int(input('enter element:'))
#     stack.append(element)
# print(stack)
# t=stack[-1]
# print(t)
# if len(stack)==0: 
#     print('stack is empty')

# max_stack_len=int(input('enter max length:'))
# stack=[]
# t=int(input('enter no. of '))

def stack(): 
    stack=[]
    return stack
# print(stack())
def push (stack,element): 
    if stack is not None: 
        stack.append(element,stack)
        return 
    stack=stack()
    element=int(input('enter element'))
    push(element)
    print(stack)


# def pop(stack): 
#     if len(stack)>0: 
#         return stack.pop()
#     else: 
#         Exception('stack under flow')  #raise exception
#         print('stack under flow is empty')
# def top(stack):
#     if len(stack)>0: 
#         return stack[-1]
#     else: 
#         raise IndexError('stack is under flow')


# def isEmpty(stack): 
#     if len(stack)==0: 
#         return True
#     else: 
#         return False
# def isFull(stack,max_len):
#     if len(stack)==max_len:
#         return True
#     else: 
#         return False
