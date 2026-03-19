#공백 제거 Str

text = "           Cloud Infra            "
result1 = text.strip()


#.으로 븐리하기
myIp = "192.168.0.2"
result2 = myIp.split(".")

#join 다시 합치기
result3 = ".".join(result2)

#특정 문자열 찾아서 대체하기
result4 = "hello mimi!".replace("mi","ma", 1)

result5 = "python".upper()
result6 = "PYTHON".lower()

print("Clear")
