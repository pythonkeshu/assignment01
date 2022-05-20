# Q2 Python program to count the number of vowels in a given string.
given_statement = input("enter the statement you want to check no of vowels present in it :  ")
new_statement = given_statement.lower()
vowels = "aeiou"
count = 0
for i in new_statement:
    if i in vowels:
        count= count+1
print("Total number of vowels present in given statement is : ",count) 
