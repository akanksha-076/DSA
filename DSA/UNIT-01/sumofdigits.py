
# number=input("enter a number")
# s=0
# for i in number:
#     s=s+int(i)
# print(s)

# Program to find the sum of digits using arithmetic operations

num = int(input("Enter a number: "))

digit_sum = 0
while num > 0:
    digit = num % 10      # get last digit
    digit_sum += digit
    num //= 10            # remove last digit

print("Sum of digits:", digit_sum)