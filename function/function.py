def f(x):
    return 2*x+7 # 11
def g(x):
    return x**2 # x의 2제곱: 4
x=2
print(f(x) + g(x) + f(g(x)) + g(f(x)))
# 11, 4, 15, 121