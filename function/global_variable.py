def f():
    global s  # 함수 내 전역변수 선언 전역변수 메모리 주소 사용
    s="I love London!"
    print(s)

s="i Love Paris!"
f() # I love London!
print(s) # I love London!