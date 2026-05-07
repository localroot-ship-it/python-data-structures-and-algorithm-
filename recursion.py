 #print name "naveed " four times using recursion
#head recursion
def Func():
    if count==4:
        return
    print("naveed")
    count=1
    
Func()

#print name n times using recursion 
#tail recursion or (back tracking)
def func():
    if count==4:
      return
    count=1
    func()
    print("naveed")
#recursion using parametres(and print numbers)
def func(x,n):
    if n==0:
        return
    print(x)
    func(n,n-1)
func(15,5)

