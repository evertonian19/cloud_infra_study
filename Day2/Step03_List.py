# list type 에 대해서 알아보자
 
names = ["김구라","해골","원숭이"]
nums=[10,20,30,40]

nums.append(100)

#len() builtin 함수를 이용해서 list의 길이를 얻어낼 수 있다.
nums_len = len(nums)

#인덱스에 의한 참조(창모)
name0 = names[1]

#인덱스를 이용해서 삭제
del names[1]

#값에 의한 삭제
names.remove("원숭이")

name0 = names[0]

# 맨 마지막 inex를 삭제하면서 값을 가져오기
nums.pop()

result = nums.pop()

print("종료합니다")
