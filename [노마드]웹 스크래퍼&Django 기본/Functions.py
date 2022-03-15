# 파이썬 함수 정의
def this_is_py_function(parameter):
    print("Received argument:",parameter) # 들여쓰기로 함수의 body 표시
    # print 안에서 합쳐서 나오게 하려면 + 대신 ,를 써야 함!
    # print("Received argument:" + parameter) --> Error 출력
this_is_py_function("hello")
this_is_py_function(1)
this_is_py_function(True)

# Defalut value 설정:
def set_default_value(arg="you didn't send an argument"):
    print(arg)
set_default_value() #파라미터에 설정한 default value 출력

# 함수의 return
def this_prints(a,b):
    print(a * b)

def this_returns(a,b):
    return a * b #()로 묶지 않아도 됨
    print(a - b) #return과 함께 함수 종료되므로 이후 코드는 실행되지 않음

printed_value = this_prints(4,3)
returned_value = this_returns(3,4)
print(printed_value,returned_value) #None, 12

# Positional vs Keyworded argument
def chr_info(name,race,Class,level): #주의:class로 파라미터 설정하지 말 것
    return f"The {race} {Class}, {name} has reached lv.{level}!" #f=format
    # 문자열 여러개와 변수를 +로 묶을수도 있음(불편함)

Positional_arg = chr_info("PawPaw","human","warrior",4)
Keyworded_arg = chr_info(level=10,name="Byul",Class="mage",race="Khajiit")

print(Positional_arg)
print(Keyworded_arg)

