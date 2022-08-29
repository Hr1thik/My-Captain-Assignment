#Write a Python program to print all positive numbers in a range.
li=[]
n=int(input("Enter size of list "))
for i in range(0,n):
    e=int(input("Enter element of list "))
    li.append(e)

print("Positive numbers in",li,"are: ")

for i in li:   
    
    if i >= 0:
       print(i, end = " ")
