# Step05_Function.py 

"""

Function type

- 특정 시점에 여러줄의 명령어 실행
- 함수도 data이다 (변수에 담을 수 있다)
- 함수안에 저장된 code를 일괄실행 하는 것을 함수를 call 한다고 이야기한다.
- 함수는 저장된 code를 다 실행하고 나면 원래 call했던 위치로 실행의 흐름이 넘어온다.
- call 했던 위치로 돌아오면서 어떤 data 를 반드시 가져온다.

"""

def test1():
    print("test1() 호출됨")

test1()
rseult1 = test1()

# 매개변수가 선언되어 있는 함수
# 매개변수에 대입할 값을 전달해야지

def test2(arg):
    print("전달 받은 내용:", arg)
    print(f"전달 받은 내용: {arg}")

test2("GOAL")
test2(10)
test2("kim")

# 값(숫자)을 2개 전달 받아서 전달 받은 두 수의 합을 출력하는 함수

def print_sum(num1: int, num2: int):
    sum = num1*num2
    print(f"{num1} * {num2} = {sum}")

print_sum(30, 30)



def print_info(name: str, addr: str):
    print(f" name is {name} and addr is {addr}")

print_info("Jack","Manchester")
# kewyword 를 이용해서 인자(argument)를 전달하기
print_info(addr="london", name="Bruno")

def get_sum(num1:int, num2:int):
    sum=num1-num2
    return sum


reseult2 = get_sum(100, 500)
print(reseult2)

print("Clear.")
