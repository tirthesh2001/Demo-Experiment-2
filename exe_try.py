class just_because_error(Exception):
    pass

n=int(input("Enter a Numer= "))
fact=1
try:
    assert n>4 and n<10, "The number should be 5.(Don't ask why)"
    if(n==5):
        for i in range(1,n+1):
            fact*=i
        print("Factorial= ",fact)
    elif(n>5 and n<7):
        num=int(input("Enter another number: "))
        print("Multiplaication Table of ",n)
        for i in range(1,num+1):
            print(n,"*",i,"=",(n*i))
    else:
        raise(just_because_error("User Defined error"))
except AssertionError:
    print("Input beyond expectations.")
except just_because_error as e:
    print("To show implementation of 'raise'.")
except TypeError:
    print("Only integer values allowed.")
else:
    print("All good!!")
finally:
    print("The code ends here")
    
    
