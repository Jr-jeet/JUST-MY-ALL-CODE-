





# # small calculator
# a = int(input("first "))
# b = int(input("second "))
# operation = (input(" "))
# if operation=="+":
#    print(a + b)
# if operation=="-":
#    print(a-b) 
# if operation=="*":
#    print(a*b)
# if operation=="/":
#    print(a/b)


# num = int(input("number "))
# if num % 2 == 0:
#     print("even")
# else:
#     print("odd")

# A = int(input(" check "))
# if A % 7 == 0:
#     print("yess divisble by 7")
# else:
#    print(" not divisble by 7")

# tup = (1,2,3,2,4,8,7,9,0,5,2)
# print(tup.index(5))
# tup = (1,2,3,2,4,8,7,9,0,5,2)
# print(tup.count(5))
# tup = (1,2,3,2,4,8,7,9,0,5,2)
# print(tup.index(5))
# print(tup[1:4])

# # WAP of 3 movie and  them in  LIST
# movie =[]
# list1 = input("1st movie: ")
# list2 = input("2nd movie: ")
# list3 = input("3rd movie: ")
# movie.append(list1)
# movie.append(list2)
# movie.append(list3)
# print(movie)

# WAP COUNT "A" IN FOLLOWING
# list =("C","D","A","A","B","B","A")
# list1 = list.count("A")
# print(list1)
# list1 = []
# list2 = ("A")
# list3 = ("B")
# list4 = ("C")
# list5 = ("A")
# list1.append(list2)
# list1.append(list3)
# list1.append(list4)
# list1.append(list5)
# # list1.sort()
# print(list1)
# # take 3 input with user and print 
# marks={}
# phy =input("number: ")
# chem =input("number: ")
# math =input("number: ")
# marks.update({"phy": phy})
# marks.update({"chem":chem})
# marks.update({"math":math})
# print(marks)
# # print 1 to 100
# num = 1
# while  num<=100:
#     num+=1
#     print(num)
# i = 9 
# while i >= 90:
#     print(i)
#     i+=9

#     # print the multiplication table of a number n
# n = int(input("number: "))
# i = 1
# while i<=10:
#     print(n*i)
#     i+=1
# # PRINT THE MULTIPLICATION OF A OF N
# n = int(input("enter: "))
# for i in range(1,11):
#     print(n*-i)
# # until user input 0
# while True:
#     n=int(input("number: "))
#     if n==0:
#         print("end")
# def calc_sum(a,b,c):
#     sum = a+b+c
#     avg = sum/3
#     print(avg)


# calc_sum(23,83,-34)
# calc_sum(67627,92782,87)

# list = [ "me", "you", "hyt", "kiu"]


# def printlen(list):
#     print(len(list))




# def printall(list):
#     for item in list:
#         print(item , end=" ")


# printall(list)
# printlen(list)

# usd in inr

# def    converter(a):
#     inr = a*83.12
#     print(a,"usd=" ,inr,"inr")


# converter(400)

# odd and even
# def eo (a):
#   if a%2==0:
#     print("even")
#   else:
#     print("odd")



# eo(int(input("number: ")))

# # recusion    print list items
# def jr(list , idx=0):
#     if idx == len(list):
#         return 
#     print(list[idx])
#     jr(list,idx+1)



# fruits = [ "apple", "banana","orange","gwabha","mango"]
# jr(fruits)
# list =[ 12,34,65,76,543,77,90,96,]
# largest = list[0]
# for num in list:
#     if num>largest:
#         largest = num
# print(largest)

# with open ("practice.txt","w") as f:
#     data = f.write(" Hi everyone \n we are learning python \n with toutube")
#     print(data)
# with open ("practice.txt","r") as f:
#     data = f.read()

# new_data=data.replace("we","iam")
# print(data)
# with open("practice.txt","w") as f:
#     f.write(new_data)


# class student:
#     def __init__(self,name,marks):              # if we can't create a function then python can done by deafult
                                                  # khud se add kiya instruction then ("parameterized constructor")
#         self.name = name
#         self.marks=marks

# s1=student("Jeet","95")
# s2=student("Dimple","91")
# print(s1.name)
# print(s2.marks)

# import random
# target=random.randint(1,100)
# while True:
#     user=int(input("guess the num"))
#     if user==target:
#         print("you guues the target")
#         break
#     elif user<target:
#         print("you guess the lowest target")
#     elif user>target:
#         print("you guess the higher target")
#     else:
#         print("error")

# create class student  that takes 3 marks and has a method average   1 METHOD
# class student:
#     Schoolname="Kids garden school"
#     def __init__(self,name,phy,che,bio):
#         self.name=name
#         self.phy=phy
#         self.che=che
#         self.bio=bio
#         self.sum= self.phy+self.che+self.bio
#         self.per= self.sum/3

# s1=student("Jeet",98,93,89)
# s2=student("Junior",97,95,87)
# s3=student("Ricky",78,45,89)

# print(s1.per)
# print(s2.per)
# print(s3.per)

# class student:
#     Schoolname="Kids garden school"
#     def __init__(self,name,phy,che,bio):
#         self.name=name
#         self.phy=phy
#         self.che=che
#         self.bio=bio
#     def avg_cal(self):
#         sum=self.phy+self.che+self.bio
#         avg=sum/3
#         return avg
# s1=student("Jeet",98,93,89)
# s2=student("Junior",97,95,87)
# s3=student("Ricky",78,45,89)

# print (s1.avg_cal())
# print (s2.avg_cal())
# print (s3.avg_cal())
