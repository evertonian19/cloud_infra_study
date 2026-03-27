# Step16_File.py

import os

if __name__ == "__main__" :
    #현재 작업 폴더의 경로 os.getcwd()
    print(os.getcwd())
    # 파일 구분자 os.sep (window 는 역슬레시, linux는 슬레시를 얻어낸다)
    print(os.sep)
    r'''
    현재 memo.txt 파일은 C:\playground\python_basic\memo.txt 의 경로에 존재한다.
    해당 경로를 문자열로 만들어 보기
    '''

    path:str = os.path.join(os.getcwd(),"memo.txt")

    print(path)

    # with 구문을 이용해서 path 경로에 있는 text 파일을 읽기 전용으로 열어서 f 라는 별칭으로 사용
    with open(path, "r", encoding="utf-8") as f:
        #파일에서 문자열 열기
        result = f.read()
        print("---memo.txt 파일의 내용---")
        print(result)