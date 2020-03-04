import math
 
 
def quadratic(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                print('方程有任意解')
            else:
                print('方程无解')
        else:
            x = -c / b
            print('方程有解：x=%.2f' % x)
    else:
        q = b * b - 4 * a * c
        if q > 0:
            x1 = (-b + math.sqrt(q)) / a / 2
            x2 = (-b - math.sqrt(q)) / a / 2
            print("一元二次方程的解为x1=%.2f，x2=%.2f" % (x1, x2))
            return ()
        elif q == 0:
            x1 = -b / a / 2
            x2 = x1
            print("一元二次方程的解相同，x1=x2=%.2f" % (x1))
            return x1, x2
        else:
            pass
            print("一元二次方程无解")
            return ()
 
 
print('input a,b,c :')
a = float(input('a:'))
b = float(input('b:'))
c = float(input('c:'))
q = quadratic(a, b, c)
