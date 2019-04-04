def print_something_2(my_name, your_name="be"):
    print("Hello {0}, My name is {1}".format(your_name, my_name))
    
print_something_2("aj", "be2")  #이렇게 하면 덮어씌워진당
print_something_2("aj") # 디폴트값이 있어서 하나만 줘도 오류 안남