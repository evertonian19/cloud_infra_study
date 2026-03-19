#Step04_Str2.py 


#json , info는 str type이긴 한데 문자열이 특별한 형식을 띄고있다.
import json

info = '''{
  "name": "Cahill",
  "adr": "서울",
  "foods": ["치킨", "피자"]
}'''

result = json.loads(info)

print(result["name"])
print(result["adr"])
print(result["foods"])
print(result["foods"][0])
print(result["foods"][1])


result2 = json.dumps(result)

print("clear")

#jsonloads() = json변환 -> python dict / json.dumps() = python dict -> json변환
#XML

info = '''
<member>
  <name>Cahill</name>
  <adr>서울</adr>
  <food>치킨</food>
  <food>피자</food>
</member>
'''

#Yaml
info = '''
name: Cahill
adr: 서울
foods:
  - 치킨
  - 피자
'''
