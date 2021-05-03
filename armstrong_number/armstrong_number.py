usrinput=input("Enter a number")
k = []
for i,c in enumerate(usrinput):
    m = int(c)
    a = m**3
    k.append(a)


add=sum(i for i in k)
if add == int(usrinput):
    print("The number is an armstrong number")
else:
    print("The number is not an armstrong number")