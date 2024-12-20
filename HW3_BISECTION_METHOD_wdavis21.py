def f(x): # This method is used to define our function
    return (x**3)+(4*x**2)-10

a=1  #Value of a
b=2  #Value of b
tol=10**(-6)  #Value of tolerance
max_it = 50  #Value of max iteration
FA = f(a)  #Variable equals function of a

#For loop includes nested if-else loop which will run the iterations from range 1 through value of max_it
for i in range (1,max_it):
    p = a+(b-a)/2
    FP = f(p)
    print("i={}, a={}, b={}, p={}, FP={}".format(i,a,b,p,FP))
    if(FP==0 or (b-a)/2<tol):
        print(p)
        break
    if (FA*FP>0):
        a=p
        FA=FP
    else:
        b=p






