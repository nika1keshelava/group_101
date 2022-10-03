# my_sentence = " aa {1} bb {0} cc {2} ".format("zz", "yy", "xx")


# print(my_sentence)


# if 10<5:
#     print("a")
# else:
#     print("b")


# if False:
#     print("10")
# else:
#     print("20")

#print -  output
#input()   - input

# my_age = input("how old are you: ")
# # print(type(my_age))

# my_age += 2

# print("i am " + my_age + " years old")


# age = 22
# age += 5 #incrementation  გაზრდა


# print(age)


# a = "20"
# b = "30"
# c = "40"

# print(int(a)+int(b)+int(c))

# მომხმარებელს ტერმინალიდან შემოატანინეთ ორი რიცხვი და დამიპრინტეთ მათი ჯამი

# num1 = int(input("enter number1: "))
# num2 = int(input("enter number2: "))

# print("their sum is " + str(num1+num2))

# მომხმარებელს შემოატანინეთ ორი რიცხვი
# გამოითვალეთ მათი ნამრავლი
# თუ ნამრავლი მეტია 100-ზე, დაპრინტეთ "xxx", თუ არადა - "yyy"

# num1 = int(input("enter number1: "))
# num2 = int(input("enter number2: "))

# product = num1 * num2

# if product > 100:
#     print("xxx")
# else:
#     print("yyy")


a = 7
b = 3

# print(a + b)
# print(a * b)
# print(a / b)
# print(a - b)

# print(13 % 5)

# print(b % a)  # რამდენი დარჩება ნაშთი გაყოფის შემდეგ
# print(a ** b) #ხარისხში აყვანა
# print(a/b)
# print(a//b)



# მომხმარებელმა ტერმინალიდან შემოიტანოს 3 რიცხვი
# აქედან მხოლოდ კენტები შეკრიბოს და დაპრინტოს ჯამი

#input, %, if , += 

#20
#7
#3


# 7+3 = 10


#  5 % 2 = 1
#  13 % 2 = 1
#  10 % 2 = 0
#  16 % 2 = 0

num1 = int(input("enter num 1: "))
num2 = int(input("enter num 2: "))
num3 = int(input("enter num 3: "))

#for each number if number kentia, 0 + number 

# 20, 13, 5

my_sum = 0

if num1 % 2 == 1:
    my_sum += num1 
    
if num2 % 2 == 1:
    my_sum += num2 
# my_sum = 13  

if num3 % 2 == 1:
    my_sum += num3 

#my_sum-ს რომელიც ბოლო ვერსიის მიხედვით უდრიდა 13-ს, კიდევ დაემატა 5, და გახდა 18

print("the sum of odd numbers is {}".format(my_sum))