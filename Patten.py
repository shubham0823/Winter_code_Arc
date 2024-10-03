# colors = ["red" , "blue" , "green" , "black" ]
# for color in colors :
#     print (color)
#     for SingleAlphabet in color:
#         print (SingleAlphabet)

# for number in range (0, 21 , 5) :
#     print(number)

# for patten1 in range (1, 6):
#     for patten2 in range (1,6):
#         if patten2<= patten1:
#             print("*" ,end='')
#         else :
#             print("")
#     print()
 

# n = int(input("number"))
# #    *
# #   **
# #  ***
# # ****
# for i in range (1,n):
#     for j in range (1,n):
#         if j<=i:
#             print(" " ,end='')
#         else :
#             print("*",end='')
#     print()


# for patten1 in range (1 ,5):
#    for patten2 in range (1,5):
#        if patten1<=patten2:
#            print ("*",end='')
        
# n = 4

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j < n+1-i:
#             print(" ", end="")
#         else:
#             print("*", end="")
#     print()


# n=4
# while ( n >= 0):
#    print(n)
#    n = n-1
# else:


# import time
# t = time.strftime('%H:%M:%S')
# hour = int (time.strftime('%H'))
# print (hour)

# if hour>5 or hour<12:
#    print ("Good Morning")

# else :
#    print ("good evening")

# n = [1,4,0,6,0,5,3,0,7]
# for x in n:
#    if x==0:
#       n.remove (x)
#       n.append(x)
# print (n)

# https://www.youtube.com/shorts/R4CviXUChxQ
# https://www.youtube.com/watch?v=rkMSVGkw0dI


#fabonacci(n)
num = int(input("enter the number ") )
num1=0
num2=1

print()   
for i in range (num):
      
   sum= num1+num2
   num1=num2
   num2=sum
   print(sum,end =" ")



   