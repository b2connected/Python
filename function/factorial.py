def factorial(n): # 매개변수로 사용자가 보낸값을 받음
    if n==1: # 1이면 1을 리턴
        return 1
    else: # 아니면 
        return n*factorial(n-1)


print(factorial(int(input("Input Number for Factorial Calculation: "))))
# 사용자에게 받은 값을 인수로