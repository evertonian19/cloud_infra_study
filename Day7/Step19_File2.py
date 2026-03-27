# Step17_File2.py


import os


if __name__ == "__main__" :

    #새로운 파일을 만들어서 문자열을 파일에 출력하기
    
    letter_path = os.path.join(os.getcwd(), "my_letter.txt")
    # C:\playground\python_basic\my_letter.txt

    #파일을 열어서 문자열 추가하기 append mode
    with open(letter_path, "a", encoding="utf8") as f:
        f.write("to my Friend\n")
        f.write("pork belly\n")
        f.write("and cass\n")

        print("my_letter.txt 파일 생서 및 쓰기 완료")

    

