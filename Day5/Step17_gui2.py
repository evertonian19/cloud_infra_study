# BinaryTest gui02.py
'''
source = "11110000"

print(int(source, 2))

source2 = "11110003"

#source 문자열 하나하나를 set로 만들어서 0 과 1 로만 이루어져 있는지 여부 알아내기

result1 = set(source).issubset({"0", "1"})
result2 = set(source2).issubset({"0", "1"})

print(f" {source} 가 0과 1로만 되어있는지 여부: {result1}")
print(f" {source2} 가 0과 1로만 되어있는지 여부: {result2}")
print(f" {source} 가 8 자리 초과인지 여부: {len(source) > 8}")


print("clear")
'''
import tkinter as tk

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

    
def clicked(event=None):
    input_str = input_value.get().strip()
    
    # [가드 1] 입력값이 없으면 에러
    if not input_str:
        result_label2.config(text="⚠️ Please enter a value", fg="darkorange")
        return # 여기서 함수 끝!

    # [가드 2] 2진수가 아니면 에러
    input_set = set(input_str)
    if not input_set.issubset({'0', '1'}):
        result_label2.config(text="⚠️ Invalid Binary!", fg="red")
        input_value.delete(0, tk.END)
        return

    # --- 여기까지 왔다면 '값도 있고 2진수도 맞음'이 보장됨! ---
    num_10 = int(input_str, 2)
    
    if 0 <= num_10 <= 255:
        result_label2.config(text=f"Result: {num_10}", fg="blue")
    else:
        result_label2.config(text="⚠️ Range Error", fg="red")

    input_value.delete(0, tk.END)





#버튼
btn = tk.Button(root, text="Convert", command=clicked, width=10, bg="lightblue")
btn.pack(pady=15)

result_label2 = tk.Label(root, text="Result")
result_label2.pack(pady=15)


#창이 닫힐 때 까지 무한대기
input_value.bind("<Return>", clicked)
root.mainloop()
 


