def kwargs_test(**kwargs): # 가변인수 **
    print(kwargs)
    # 개별 변수명을 불러냄
    print("First value is {first}".format(**kwargs))
    print("Second value is {second}".format(**kwargs))
    print("Third value is {third}".format(**kwargs))

kwargs_test(first=3, second=4, third=5) # 3개의인수를 넣음 {'first': 3, 'second': 4, 'third': 5}