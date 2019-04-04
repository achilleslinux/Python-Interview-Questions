usrinput=input("Please enter a word \n")
print(type(usrinput))
l = ['a','e','i','o','u','A','E','I','O','U']

if l in usrinput:
    print("It contains vowels")
else:
    print("It doesn't contains vowels")