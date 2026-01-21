#Palindrome
s = input("Enter a string: ")

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
    
# * Pattern
n = 5
for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()
    
# Number pattern 
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
    
# Reverse string 
s = input("Enter a string: ")
rev = s[::-1]
print("Reversed string:", rev)

# Reverse Number 
num = int(input("Enter a number: "))
rev = 0
while num > 0:
    digit = num % 10     
    rev = rev * 10 + digit
    num = num // 10       
print("Reversed number:", rev)

# Positive, Negative , Zero 
num = int(input("Enter a number: "))
if num > 0 and num != 0:
    print("Positive number")
elif num < 0 and num != 0:
    print("Negative number")
else:
    print("Zero")
    
 # Bit in a number 
 num = int(input("Enter a number: "))
pos = int(input("Enter bit position: "))
bit = (num >> pos) & 1
print("Bit at position", pos, "is:", bit)

#Swap Numbers 
a = int(input("Enter a: "))
b = int(input("Enter b: "))
a, b = b, a
print("After swapping:")
print("a =", a)
print("b =", b)