import math

course = 'python'
len(course)
x = -2.3
print(round(x))  #四舍五入
print(abs(x))   #绝对值

print(math.ceil(2.1))

is_hot = False
is_code = False
if is_hot:
    print('天气很热')
elif is_code:
    print('天气很冷')
else:
    print('天气不冷也不热')

print(f"天气: is_hot : {is_hot} is_code :{is_code}")

name = input("请输入姓名:")
print(f'hi {name}')
