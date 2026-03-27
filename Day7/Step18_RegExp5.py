# Step16_RegExp5.py
import re



if __name__ == "__main__":
     input_id = input("아이디 입력(영문자로 시작하고, 5~10글자 이내, 특수문자 허용안함)")

     # 조건에 맞으면 "가입되었습니다" , 맞지 않으면 "사용할 수 없는 아이디입니다" 라고 출력하기

pattern = r"^[a-zA-Z][a-zA-Z0-9]{4,9}$"

214
if re.fullmatch(pattern, input_id) :
     print("✅ 가입되었습니다.")
else:
        # 실패 시 구체적인 이유를 안내해주는 게 '친절한 에이스'의 센스죠!
        print("❌ 사용할 수 없는 아이디입니다.")
        print("   - 영문으로 시작하는 아이디")
        print("   - 길이는 5자 이상 10자 이하")
  