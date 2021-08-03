from numpy import *
#Declraing and defining Matrices
a_a=[]
b_b=[]
def get_1():
    print("Enter parameters for first matrix.")
    r1=int(input("Enter the number of rows: "))
    c1=int(input("Enter the number of columns: "))
    for i1 in range(c1):
        a=[]
        for j1 in range(r1):
            n1=int(input("Enter element: "))
            a.append(n1)
        a_a.append(a)
def get_2():
    print("Enter parameters for second matrix.")
    r2=int(input("Enter the number of rows: "))
    c2=int(input("Enter the number of columns: "))
    for i2 in range(c2):
        b=[]
        for j2 in range(r2):
            n2=int(input("Enter element: "))
            b.append(n2)
        b_b.append(b)
#Matrix Operations
def mult():
    s1=aa.shape
    s2=bb.shape
    if(s1[1]==s2[0]):
        print("Multiplication= ",aa*bb)
    else:
        print("Matrix has to be reshaped for it to be multiplied.")
def tran():
    print("Transpose of first matrix: ",aa.T)
    print("Transpose of second matrix: ",bb.T)
def m_sum():
    print("Addition= ",aa+bb)
def change():
    row=int(input("Enter the new number of rows: "))
    col=int(input("Enter the new number of columns: "))
    print("Matrices:- ")
    print("1.First Matrix")
    print("2.Second Matrix")
    sel=int(input("Enter the matrix to be reshaped: "))
    if sel==1:
        aa.reshape(row,col)
        print("First Matrix: ",aa)
    elif sel==2:
        bb.reshape(row,col)
        print("Second Matrix: ",bb)
    else:
        print("Invalid Input Given!!")
get_1()
get_2()
aa=matrix(a_a)
bb=matrix(b_b)
print("Matrix Operations")
print("1.Multiplication")
print("2.Transpose")
print("3.Addition")
print("4.Reshape")
print("5.Exit")
c=0
while c==0:
    ch=int(input("Enter you choice: "))
    if ch==1:
        mult()
        c=0
    elif ch==2:
        tran()
        c=0
    elif ch==3:
        m_sum()
        c=0
    elif ch==4:
        change()
        c=0
    elif ch==5:
        print("Code execution ends here.")
        c=1
#changed
#Name : Tirthesh
