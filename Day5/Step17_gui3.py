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

result_label2 = tk.Label(root, text="IP를 입력하고 Enter!", font=("Arial", 12))
result_label2.pack(pady=20)


def convert_ip(event=None):
    """
    입력창(Entry)에 입력된 IPv4 주소를
    8비트 2진수 형태로 변환하여 결과 라벨에 표시하는 함수
    """
    ip_str = input_value.get().strip()
    
    if not ip_str:
        result_label2.config(text="IP를 입력하세요", fg="gray")
        return

    try:
        parts = ip_str.split('.')
        
        # IPv4 옥텟 개수 검증
        if len(parts) != 4:
            raise ValueError
            
        binary_list = []

        for p in parts:
            val = int(p)

            # 0 ~ 255 범위 검증
            if 0 <= val <= 255:
                binary_list.append(f"{val:08b}")
            else:
                raise ValueError
        
        # 결과 결합 및 출력
        final_result= " . ".join(binary_list)
        result_label2.config(text= final_result ,fg="blue" )
        input_value.delete(0, tk.END)
    except ValueError:
        result_label2.config(text="올바른 IPv4 형식이 아닙니다 (0~255)", fg="red")
        

#창이 닫힐 때 까지 무한대기
input_value.bind("<Return>", convert_ip)
root.mainloop()