# i=1
# while i<=10:
#     print(i)
#     i+=1

# i=10
# while i>=1:
#     print(i)def
#     i-=1 

# i=0
# while i<=20:
#     print(i)
#  i+=1 


# n = int(input("number: "))
# i=1
# while i<=10:
#     print(n*i)
#     i+=1

# n = int(input("number: "))
# sum=0
# i = 1
# while i<=n:
#     sum +=i
#     i+=1
# print(sum)


# num = int(input("number: "))
# count = 0
# if num == 0:
#   count = 1
# else:
#   while num!=0:
#     num = num//10
#     count=count+1
    

# print("total number of digits is",count)

#FIND SUM OF N NUMBERS
# def AP(n):
#     sum = (n+1)
#     sum1= sum*n
#     sum2=sum1//2
#     print(sum2)


# AP(12345)
# print(AP)

# n= int(input("number"))
# sum = 0
# i=0
# while i<=n:
#     sum+=i
# print(sum)
    
# = int(input("number"))
# count =0 n
# while n>0:          # jab tak nuber devide karte karte 0 se chota na ho
#     n=n//10         # ye divide karega 
#     count+=1        # jitni baar loop chaelga utni baar count +1 se barta jayega

# FIBONACCI SERIES

# n=0
# while n<5:
#     print(n*"*")
#     n+=1

# n=int(input("num"))
# i=1
# while i<=n:
#     i+=1
#     print(i)

#for  n in range (0,10,1):
 #   print("*"*n)

# num=int(input("Number:- "))
# for i in range(0,num+1):
#     print(i)   

# num=int(input("number:- "))
# for  n in range (num,0,-1):
#     print(n)


# num = [25, 98, 21, 54, 36, 54, 54, 12, 99, 1452]
# larger = num[0]

# for i in num:
#     if i > larger:
#         larger = i
# print(larger)

# num = [25,98,21,54,36,54,54,12,99,1452]
# print(min(num))
# num = [25,98,21,54,36,54,54,12,99,1452]
# print(max(num))

# n = int(input("num"))
# i=0
# while i<n:
#     i+=1
#     print(i)

num = 12345
count =0
while num>0:

    reminder=num%10
    count=(count*10)+reminder
    num=num//10
print(count)
