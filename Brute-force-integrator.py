def f(x):
    return 1/((x**2) + 1) # define the function

a = -1 # define the lower integration bound
b = 1 # upper integration bound

n = 300000 # number of subintervals

delta_x = (b-a)/n
sum = 0
i = 1

for i in range (1,n):
    rep_x = -3 + (3*i - 3)/n
    sum = sum + f(rep_x)

sum = sum*delta_x

print(f"Area under this graph is about {sum}")