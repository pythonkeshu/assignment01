# Q 1. python program to capitalize first and last program the first and last character of each word in a string.
given_data = str(input("Enter the data you want to change : "))
given_data = given_data.title()
given_data = given_data.split()
processed_data = ""
for i in given_data:
    processed_data+=i[:-1]+i[-1].upper()+" "
print("Processed data : ",processed_data)
