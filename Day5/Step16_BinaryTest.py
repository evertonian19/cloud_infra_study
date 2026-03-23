# BinaryText/test01.py

# python 에서 2진수 다루기

# 2진수는 숫자를 만들때 prefix로 0b
num1 = 0b1010 # 10 진수로 환산했을 때 10이 된다

result = num1+5
print(result)


# 10진수를 2진수로 변환

num2 = 150
result2 = bin(num2) # bin() 함수를 호출하면서 10진수를 넣러주면 2진수 값이 나온다. 
print(result2[2::])

print("--------------")


line = "abcde12345"
print(line[5:10]) # 5번 인덱스 이상, 10번 인덱스 미만의 문자열 얻어내기

# 위의 result 문자열에서 (0bxxxx)에서 0b를 제거한 순수 2진수 형태의 문자열만 럳어내려면?
print(result2[2:])