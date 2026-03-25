# Step16_RegExp3.py
import re


logs = [
    "[INFO] Server started successfully.",
    "[WARN] Memory usage is high.",
    "[ERROR] Database connection failed.",
    "[DEBUG] x = 10"
]

# 정규표현식 패턴: ERROR 또는( | ) WARN이 포함된 문자열 찾기
# [ ] 대괄호 안에 있는 글자들을 찾기 위해 \[ \] 처럼 이스케이프 처리를 해줍니다.
pattern = r"\[(ERROR|WARN)\]"

print("--- 필터링된 중요 로그 출력 ---")
for log in logs:
    if re.search(pattern, log):
        print(log)