# Step16_RegExp3.py
import re
from turtle import radians


logs = [
    "[INFO] Server started successfully.",
    "[WARN] Memory usage is high.",
    "[ERROR] Database connection failed.",
    "[DEBUG] x = 10"
]

# 정규표현식 패턴: ERROR 또는( | ) WARN이 포함된 문자열 찾기
# [ ] 대괄호 안에 있는 글자들을 찾기 위해 \[ \] 처럼 이스케이프 처리를 해줍니다.
pattern = r"\[(^ERROR|^WARN)\]"

print("--- 필터링된 중요 로그 출력 ---")
for log in logs:
    if re.search(pattern, log):
        print(log)
#첫 글자가 W or R or N ㅇㄴ지를 검증할 수 있는 정규표현식
pattern1 = r"^[WARN]"
# [WARN] 으로 시작하는지 검증할 수 있는 정규표현식
pattern2 = r"^\[WARN\]"
# [ERROR]으로 시작하는지 검증할 수 있는 정규표현식
pattern3 = r"^\[ERROR]\]"
# WARN or ERROR 로 시작하는지 검직할 수 있는 정규표현식
pattern4 = r"^(WARN|ERROR)"
# [WARN] or [ERROR] 로 시작하는지 검직할 수 있는 정규표현식
pattern5 = r"^\[(WARM|ERROR)\]"

for tmp in logs:
    if re.search(pattern1, tmp):
     print(tmp)
