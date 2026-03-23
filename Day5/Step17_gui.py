# gui01.py


# ui Toolkit 을 사용할 수 있는 interface객체 import 하기
import tkinter as tk
from tkinter import messagebox

# root 창 생성
root = tk.Tk()
# 제목 설정
root.title("Fotmob")

#창의 크기
root.geometry("400x400")

# 레이블
label = tk.Label(root, text="Converting Decimal to Binary")
label.pack(pady=30)

#입력창
input_value = tk.Entry(root, font=("Arial", 18))
input_value.pack(pady=5)
input_value.focus() # 포커스 추가


'''
def clicked():
    print("Check!")
    #Entry(입력창)에 입력한 문자열 읽어오기
    name=name_entry.get()
    # label text 수정하기
    label2.config(text=f"Name : {name}")
'''


#step1 - 10진수 숫자를 입력하고 전송 버튼을 누르면 입력한 숫자가 아래의 Label에 출력되도록 만들기
'''
def clicked():
    # 1. Entry(입력창)에 입력한 문자열 읽어오기
    input_value = name_entry.get()
    
    # 2. 읽어온 값이 비어있지 않은지 확인 (에러 방지용)
    if input_value:
        # 3. label2의 text를 입력한 숫자로 수정하기
        label2.config(text=f"입력한 숫자: {input_value}",fg="black")
        # 입력 후 다음 입력을 위해 입력창 비워주기 (선택사항)
        name_entry.delete(0, tk.END) 
    else:
        label2.config(text="숫자를 입력해주세요!", fg="red")
'''



#step2 - 10진수 숫자를 입력하고 전송 버튼을 누르면 입력한 숫자를 2진수로 변경해서 아래의 Label에 출력되도록 만들기
'''
def clicked():
    print("Check!")
    # 1. 입력창(Entry)에서 문자열 가져오기
    input_str = name_entry.get().strip()
    
    # 2. 입력값이 있는지 확인 (안전장치)
    if input_str:
        try:
            # 3. 문자열을 정수(10진수)로 변환
            number_10 = int(input_str)
            
            # 4. 10진수를 2진수로 변환 (bin 함수 사용)
            number_2 = bin(number_10)
            
            # 5. 결과 레이블(label2)에 출력
            # f-string을 써서 10진수와 2진수를 동시에 보여주기
            label2.config(text=f"10진수: {number_10} -> 2진수: {number_2[2:]}", fg="blue")
            
        except ValueError:
            # 숫자가 아닌 글자를 입력했을 때의 에러 처리
            label2.config(text="⚠️  Not found data", fg="red")
    else:
        label2.config(text="⚠️ None", fg="darkorange")

    # 입력창 비우기
    name_entry.delete(0, tk.END)
'''



#step3 - 10진수 숫자를 입력하고 전송 버튼을 누르면 입력한 숫자를 2진수로 변경해서 아래의 Label에 출력되도록 만들기
#(2진수 8자리로 변경해서 , 전제조건 : 0~255 사이의 숫자가 아니면 경고알림 띄우기)
'''
def clicked(event=None):

    input_str = input_value.get().strip()
    
    if input_str:
        try:
            # 1. 숫자로 바꾸기
            num = int(input_str)
            
            # 2. 0~255 사이인지 확인하는 '게이트웨이'
            if 0 <= num <= 255:

                # 3. 범위 안일 때만 2진수로 변환해서 출력
                bin_num = f"{num:08b}"
                result_label2.config(text=f"10진수: {num} -> 2진수: {bin_num}", fg="blue")

            else:
                #messagebox.showerror("⚠️ Out of Range (0-255)")
                # 4. 범위를 벗어났을 때의 경고
                result_label2.config(text="⚠️ Out of Range (0-255)", fg="red")
                
        except Exception as e:
            result_label2.config(text="⚠️ Not found data", fg="red")
    else:
        result_label2.config(text="⚠️ Please enter a value", fg="darkorange")

    input_value.delete(0, tk.END)
'''
def clicked(event=None):
    print("Check!")
    # 1. 바뀐 이름인 input_value에서 값을 가져옵니다.
    input_str = input_value.get().strip()
    
    if input_str:
        try:
            # 2. 2진수 문자열을 10진수 정수로 변환 (기수 2 설정)
            num_10 = int(input_str, 2)
            
            # 3. 0~255 범위 체크 (8비트 옥텟 범위)
            if 0 <= num_10 <= 255:
                # 4. 바뀐 이름인 result_label2에 결과를 출력합니다.
                result_label2.config(text=f"Binary: {input_str} -> Decimal: {num_10}", fg="blue")
            else:
                result_label2.config(text="⚠️ Out of Range (0-255)", fg="red")
                
        except ValueError:
            # 0과 1이 아닌 숫자가 들어왔을 때의 예외 처리
            result_label2.config(text="⚠️ Invalid Binary! Use only 0 or 1", fg="red")
    else:
        result_label2.config(text="⚠️ Please enter a value", fg="darkorange")

    # 입력창 비우기
    input_value.delete(0, tk.END)





#버튼
btn = tk.Button(root, text="Convert", command=clicked, width=10, bg="lightblue")
btn.pack(pady=15)

result_label2 = tk.Label(root, text="Result")
result_label2.pack(pady=15)


#창이 닫힐 때 까지 무한대기
input_value.bind("<Return>", clicked)
root.mainloop()
 