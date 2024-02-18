print("hello world")
# 1. 변수와 데이터타입

a=100

print(a)

# 데이터타입

# 정수형(int), 실수형(float), 문자열(str), 논리형(bool)

# type() : 데이터타입
a=100

b=8907.25

c = "python"

d = True

print("정수형 : ",a, "타입 : ", type(a))

print("실수형 : ", b)

print("문자열 : ",c)

print("논리형 : ", d)

print(type(c))

# a에 타입을 float으로 변환해서 출력하시오
print(type(a),type(float(a)))

# a의 타입을  논리형으로 바꾸어서 출력하시오.
# 타입도 출력하시오
print(type(a), bool(a))
print(bool("python"))

#bool이 false인 경우

print("*"*20)

print(bool(0))

print(bool("")) 

print(bool(0.0))
d
# [Test] 혼자해보기
# +, -, *, /(2.1),//(몫, 2), %(1) , ** (거듭제곱), "문자열"*횟수
a=7
b=3
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(a**b)
print("졸려"*100)

# 입력문 : input()  - 터미널에서 python 실행 후 실습
#map(적용시킬 함수, 적용할 값들) 
# map(int, 리스트)
# 첫번째 인자로 들어간 함수가 바로 int(x)이고 x에 리스트가 들어가서 정수타입으로 나온다.


print("*"*20)

# 출력문
# print에는 변수나 값 여러 개를 ,(콤마)로 구분
print(1,2,3,4,5)   #1 2 3 4 5
print("파이썬","R","Oracle")
#값 사이에 공백이 아닌 다른 문자를 넣고 싶을 때
# print의 sep에 문자 또는 문자열을 지정, sep는 구분자라는 뜻의 separator
#  print(값1, 값2, sep='문자 또는 문자열')
print(1,2,3,4,5, sep="\n ")   #1 2 3 4 5  => 1,2,3,4,5

# print(값, end='문자 또는 문자열') 
print(1)
print(2)
print(3)

print(1, end=" ")
print(2, end=" ")
print(3)
print("*"*20)
print(1,2,3,4,5, sep='\n ') 
print(1,2,3,4,5, end='\n ') 


print(1,2,3,4,5, sep='') 

#짝수와 홀수 판별하기
a = int(input("숫자를 입력하세요 : "))
print("==짝수와 홀수 판별하기==")
if a %2 == 0:
    print("d는 짝수입니다")
else:
    print("d는 홀수입니다")

# if..elif.. elif
# score = 점수를 입력하세요?
# 90이상 A, 80이상 B, 70점 이상 C, 60점 이상 D, 그렇지 않으면 F
# print("==if..elif..else==")
