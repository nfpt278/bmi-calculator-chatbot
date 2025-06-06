import tkinter as tk
from tkinter import messagebox

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight 😟", "Bạn hơi gầy đó, nhớ ăn uống đủ chất nha!"
    elif bmi < 24.9:
        return "Normal weight 😎", "Thân hình cân đối tuyệt vời! Duy trì nhé 💪"
    elif bmi < 29.9:
        return "Overweight 😬", "Hơi dư cân nhẹ, thử đi bộ hoặc giảm tinh bột xem sao!"
    else:
        return "Obesity 😢", "Cảnh báo! Cân nặng ở mức nguy cơ. Nên gặp chuyên gia dinh dưỡng nha."

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        three_sizes = entry_three.get()

        bmi = weight / (height ** 2)
        category, comment = get_bmi_category(bmi)

        result = f"BMI của bạn là: {bmi:.2f}\nPhân loại: {category}\nNhận xét: {comment}"
        if three_sizes:
            result += f"\nSố đo 3 vòng: {three_sizes} 😘"

        messagebox.showinfo("Kết quả BMI", result)
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ!")

# Giao diện
root = tk.Tk()
root.title("BMI Chatbot GUI")
root.geometry("350x300")

tk.Label(root, text="Cân nặng (kg):").pack()
entry_weight = tk.Entry(root)
entry_weight.pack()

tk.Label(root, text="Chiều cao (m):").pack()
entry_height
