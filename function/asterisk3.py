def asterisk_test_2(*args):
    x,y,*z=args # 언패킹
    return x,y,z
print(asterisk_test_2(3,4,5)) # 수 더 많이 넣어도 가변인수z에 다 들어감