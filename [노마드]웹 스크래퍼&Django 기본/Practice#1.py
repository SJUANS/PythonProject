# Make a calculator : plus, minus, times, division, negation, power

def validation(a):
    if type(a) is int:
        return a
    else:
        print("Please write all the arguments as integers")

def plus(a,b):
   a = validation(a)
   b = validation(b)
   return a + b

#print(plus(3,5.5)) # 연산자는 str 들어가면 무조건 error 나게 되어있음
# True와 False를 넣으면 각각 수 1,0으로 인식되어 계산이 된다...!

def minus(a,b):
   a = validation(a)
   b = validation(b)
   return a - b

def times(a,b):
   a = validation(a)
   b = validation(b)
   return a * b

def division(a,b):
   a = validation(a)
   b = validation(b)
   return a / b

def negation(a):
   a = validation(a)
   return -a

def power(a,b):
   a = validation(a)
   b = validation(b)
   return a ** b

print(plus(6,3),minus(6,3),division(6,3),negation(6),power(6,3))