x = input("Enter a character : ")

if(len(x)==1 and ('A'<=x<='Z' or 'a'<=x<='z')):
    print(x,"is an alphabet")
else :
    print(x,"is not an alphabet")