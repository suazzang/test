#파이썬 자료구조 - 튜플
# 튜플의 생성
# –튜플은 소괄호 ( )로 생성(소괄호 생략 가능), 리스트는 대괄호 [ ]로 생성
# –튜플은 값을 수정할 수 없으며, 읽기만 가능해 읽기 전용 자료를 저장할 때 사용

tt1 = (10,20,30)
print(tt1)
print(type(tt1)) # <class 'tuple'>

tt2 = 10, 20, 30
print(tt2)   # (10, 20, 30)
print(type(tt2))   # <class 'tuple'>

# 항목이 하나인 튜플은 tt5와 tt6처럼 뒤에 쉼표(,) 붙임 : 튜플 = (값, ) or  튜플 = 값,
tt3 = (10,)
print(tt3)    #(10,)
print(type(tt3))  # <class 'tuple'>

#튜플 생성하기
# 빈 튜플 생성
# a = () 또는 a = tuple()
a = ()
print(a)     # ()
print(type(a))   # <class 'tuple'>

#zip()함수 : 묶는다
a = ['apple', 'banana', 'cherry']
b = [3500, 2000, 5000]
c = [10, 20, 50]
#각각의 리스트를 zip으로 묶는다
for a,b in zip(a, b) :
    print((a,b))
# ('apple', 3500)
# ('banana', 2000)
# ('cherry', 5000)



# apple : 3500
# banana : 2000
# cherry : 5000
# a = ['apple', 'banana', 'cherry']
# b = [3500, 2000, 5000]
# for a, b in zip(a, b) :
#     print(a, ":", b)
