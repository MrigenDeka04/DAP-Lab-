import numpy as np

a = np.array([[1,2],[4,5]])
b = np.array([[1,2],[4,5]])
while True:
    print("1.Add , 2.Subtract , 3.Multiply , 4.Divide , 5.Dot product , 6.Exponentiation , 7.Logarithm , 8.Natural logarithm , 9.Exit")
    n = int(input("Enter the option number : "))
    if not n < 1 and not n > 8:
        if n == 1:
            c = np.add(a,b)
            print("Sum",c)
        elif n == 2:
            d = np.subtract(a,b)
            print("Difference",d)
        elif n == 3:
            e = np.multiply(a,b)
            print("Product",e)
        elif n == 4:
            f = np.divide(a,b)
            print("Remainder",f)
        elif n == 5:
            g = np.dot(a,b)
            print("Dot product",g)
        elif n == 6:
            h, i = np.exp(a), np.exp(b)
            print("Exponentiation for array a :", h)
            print("Exponentiation for array b : ", i)
        elif n == 7:
            l, m = np.log(a), np.log(b)
            print("Logarithm for array a : ", l)
            print("Logarithm for array b : ", m)
        elif n == 8:
            x, y = np.log10(a), np.log10(b)
            print("Natural logarithm for array a : ", x)
            print("Natural logarithm for array b : ", y)
    elif n == 9:
        break
    else:
        print("No such option exist, please enter existing options.\n")