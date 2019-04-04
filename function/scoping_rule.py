def test(t): # x를 받아와서 t로 치완하여 사용
    print(x) # 여기서 x는 재정의 되지 않았으므로 전역변수임
    t=20  
    print("In function:", t) # 20출력

x=10
test(x)
print("In Main:", x) # 10출력
print("In Main: ", t)  
# t는 test()함수 내에서만 사용할 수 있는 지역변수라서 오류남