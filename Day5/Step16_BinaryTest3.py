# BinaryText/test03.py

# 비트연산 or, xor, not
a = 0b1100
b = 0b1010

# bit or 연산 |
print(bin(a|b))

# bit xor 연산
print(bin(a^b))

# bit not 연산
print(bin(~a))

#~x = -(x + 1)
# 조금 더 깔끔하게 보는 방법
print(bin(~a & 0xF))