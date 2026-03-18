# list type에 대해서 알아보기

nums = [10,20,30,40,50]
names = ["KDB","Son","CR7","Lionel","James","Jordan"]

#list 안에 들어있는 데이터를 앞에서부터 순서대로 참조하면서 어떤 동작을 할 일들이 많이 발생한다.
print("Final MOM who is this!!!")

for MOM in names :
    print(MOM)

for i in range(3):
    print("펩시 제로 너무 맛있다!")

r1 = range(5)
r2 = range(10)

print(r1)
print(r2)

for item in range(5):
    print(item)

result2 = range(len(names))

for i in range(len(names)):
  
       print ("list의 index와 함께 출력합니다.")
       print (i, names[i])

print("CLEAR!!")