 # Step08_Input.py

 # 콘솔창으로 부터 문자열 입력 받기

input_msg = input("메세지 입력:")

print(f"입력한 메세지: {input_msg}")

input_name: str = input("이름 입력:")
input_addr: str = input("주소 입력:")

print(f"이름:{input_name} 주소:{input_addr}")

 # 문자열로 입력 받은 후
input_pay: str = input("연봉 입력:")
 # 숫자로 변경해서 +20% 값을 얻어내기
pay : int = int(input_pay) * 1.2

print(f"Next year Pay ${pay:.0f}")