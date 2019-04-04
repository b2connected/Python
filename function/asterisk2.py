def asterisk_test(a, b, *args):  #a=1 b=2 args(3,4,5)가 들어감 *args는 가변인수
    print(args) #(3,4,5) 튜플 반환

print(asterisk_test(1, 2, 3, 4, 5)) #인수로 5개의 값을 줌 출력하면 None나옴
