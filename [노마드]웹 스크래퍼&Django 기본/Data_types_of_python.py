
this_is_string = "문자열"
this_is_int = 3
this_is_float = 3.14
this_is_boolean = True
this_is_nonetype = None
# 파이썬의 Boolean(True,False)와 None은 꼭 대문자로 시작해야 함!
# None은 파이썬만 갖고 있는 자료형. JS의 null/undefined. 값이 존재하지 않음.
# 변수 선언하고 끝에 ,를 붙이면 tuple 자료형이 됨!

print(type(this_is_string))
print(type(this_is_int))
print(type(this_is_float))
print(type(this_is_boolean))
print(type(this_is_nonetype))
# type:자료형을 반환하는 함수

str_123 = "123"
n_123 = int(str_123)
print(str_123)
print(n_123)
# 여기까지 print된 두 값의 차이는 없음
print(type(str_123)) #<class 'str'>
print(type(n_123)) #<class 'int'>
