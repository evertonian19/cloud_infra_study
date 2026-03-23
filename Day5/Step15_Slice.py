# Step15_Slice.py

'''
   slice 의 기본 문법
[시작 : 끝 : 증감]

  - 시작은 해당 인덱스 포함
  - 끝은 해당 인덱스 제외


'''

nums = [10, 20, 30, 40, 50]

print(nums[1:])
print(nums[2:])
print(nums[3:])


print("------------")


print(nums[:3])
print(nums[:2])
print(nums[:1])


print("------------")

# 20,30,40 이 들어있는 list를 얻어내려면?
print(nums[1:4])

print("------------")

print(nums[::1])
print(nums[::2])
print(nums[::3])