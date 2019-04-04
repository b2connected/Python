def print_something(my_name, your_name):
    print("Hello {0}, My name is {1}".format(your_name, my_name))

print_something("AJ", "be")  # 순서대로 {0}{1}에 들어감
print_something(your_name="AJ", my_name="be") # 바꿔서 전해짐