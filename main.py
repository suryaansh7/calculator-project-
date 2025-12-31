def add(n1, n2):
    return n1 + n2
def multiply(n1,n2):
    return n1*n2
def subtract(n1,n2):
    return n1-n2
def divide(n1,n2):
    return n1/n2
p="False"
a = input("enter no.1")
b = input("enter no.2")
while p=="False":

    calc={
    "+":add(int(a),int(b)),
    "*":multiply(int(a),int(b)),
    "-":subtract(int(a),int(b)),
    "/":divide(int(a),int(b)),
    }
    c=input("enter operation")
    if c=="+":
        print (calc["+"])
    elif c=="-":
        print(calc["-"])
    elif c=="*":
        print(calc["*"])
    else:
        print(calc["/"])
    d=input("enter y if u want to continue with same or enter n for new")
    if d=="y":
        a=calc[c]
        b = input("enter no.2")
    elif d=="n":
        a = input("enter no.1")
        b = input("enter no.2")
    e=input("enter stop to stop")
    if(e=="stop"):
        p="True"



