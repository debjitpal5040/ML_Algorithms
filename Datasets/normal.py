from math import exp, pi, sqrt
def f(mean,std,x):
    coeff = 1.0 / (std * sqrt(2 * pi))
    expon = -((x-mean)/std)**2 / 2.0
    return coeff * exp(expon)

print(f(49.89814749172261,4.763430142249043,35))



