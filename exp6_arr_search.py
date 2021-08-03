from numpy import *
def get_arr():
    global tot_ele
    global arr
    tot_ele=int(input("Enter the number of elements to be entered: "))
    arr=array(arange(0,tot_ele))
    for i in range(0,tot_ele):
        print("Enter element at",i,":")
        ele=int(input())
        arr[i]=ele
def search_ele():
    to_find=int(input("Enter the element to be search: "))
    for i in range(0,tot_ele):
        if arr[i]==to_find:
            print("The element ",to_find,"is present at ",i,".")
            break
def search_inx():
    to_find=int(input("Enter the index to find: "))
    if to_find<tot_ele:
        print("The element present at ",to_find," is ",arr[to_find])
    else:
        print("Entered index is invalid")
print("Array Searches: ")
print("1.Define array")
print("2.Search an element")
print("3.Search an index")
print("4.Exit")
c=0
while c==0:
    ch=int(input("Enter your choice: "))
    if ch==1:
        get_arr()
        c=0
    elif ch==2:
        search_ele()
        c=0
    elif ch==3:
        search_inx()
        c=0
    elif ch==4:
        print("Execution ends here.")
        c=1
    else:
        print("Invalid choice.")
