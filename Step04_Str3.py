
# yaml 형식의 문자열 다루기

# yaml 문자열을 대룰때는 외부 모듈을 pip 로 설치를 해서 import 를 해야한다.

info = '''
name: kevin mirallas
addr: london
foods:
  - pizza
  - bacon
  - salad
  - sushi
  - rabbit
  - duck
isMan: true
body:
  - weight: 80
  - height: 229
team:
  - 2012-2013 man.u
  - 2013-2016 man city
  - 2016-2019 spurs
  - 2019~ everton
'''

# 과제 검색 혹은 ai 의 도움을 받아서 info 에 들어 있는 문자열을 dict type 으로 바꾸기
# 그런 다음 dict 에 들어 있는 내용을 확인 후 다시 dict 에 있는 내용을 이용해서 yaml 문자열 형식으로 변환하기.


import yaml
import json

# 1. 주어진 YAML 형식의 문자열 (info)
info = '''
name: kevin mirallas
addr: london
foods:
  - pizza
  - bacon
  - salad
  - sushi
  - rabbit
  - duck
isMan: true
body:
  - weight: 80
  - height: 229
team:
  - 2012-2013 man.u
  - 2013-2016 man city
  - 2016-2019 spurs
  - 2019~ everton
'''

# [과제 1] 문자열을 dict type으로 바꾸기 (Parsing)
# yaml.safe_load()를 사용하여 YAML 문자열을 파이썬 딕셔너리로 깔끔하게 변환하기
data_dict = yaml.safe_load(info)

print("--- [1] 변환된 Dictionary 내용 확인 ---")
print(f"타입: {type(data_dict)}")
print(data_dict)
print(f"이름 확인: {data_dict['name']}")
print(f"현재 팀 확인: {data_dict['team'][-1]}") # 2019~ EVERTON


# dict 내용을 다시 YAML 문자열 형식으로 변환하기 (Dumping)
# yaml.dump()를 사용하면 딕셔너리를 다시 예쁜 YAML 문자열로 만들기
# allow_unicode=True는 한글이 섞여있을 때 깨지지 않게 해주고, sort_keys=False는 순서를 유지
yaml_string = yaml.dump(data_dict, allow_unicode=True, sort_keys=False)

print("\n--- [2] 다시 YAML 문자열로 변환된 결과 ---")
print(yaml_string)