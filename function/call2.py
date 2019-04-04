def spam(eggs):
    eggs.append(1)  # 기존 객체의 주소값에 [1]추가 따라서 ham=[0, 1]

    eggs=[2, 3] # eggs는 자신만의 메모리 주소를 가지게 됨

ham=[0]
spam(ham) # ham을 인수로 줌
print(ham) # 객체 호출(함수 안 변수 호출)