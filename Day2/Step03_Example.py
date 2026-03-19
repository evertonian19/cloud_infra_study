# Step03_Example.py

"""
회원 한명의 정보는 tel, name, adr 로 이루어져있다
그리고 그러한 회원이 여러명이다
여러명의 회원 정보를

"""


#dict 3개를 list에다가 담기

# 딕셔너리 5개를 담은 리스트 'members'

mem1 = {"num":1, "name":"김구라", "addr":"노량진"}
mem2 = {"num":2, "name":"해골", "addr":"노량진"}
mem3 = {"num":3, "name":"원숭이", "addr":"동물원"}
# dict 3 개를 list 에 담기
members = [mem1, mem2, mem3]

a = members #dict
b = members[0] #list
c = members[0]["num"] #dict의 num값
d = members[2]["name"]

print("clear")
