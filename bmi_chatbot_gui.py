# BMI Calculator Chatbot with Tkinter GUI (Enhanced Design)
# Author: Grok (xAI), based on original code from https://github.com/nfpt278/bmi-calculator-chatbot
# Description: A GUI application to calculate BMI with a sea-themed, elegant interface.
# Requirements: Python 3.6+, tkinter, Pillow (for background image)
# How to run:
# 1. Install Pillow: pip install Pillow
# 2. Download a sea background image (e.g., sea.jpg) and place it in the same folder as this script
# 3. Save this file as bmi_chatbot_gui.py
# 4. Run: python bmi_chatbot_gui.py

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os

def calculate_bmi():
    """Calculate BMI and display result with chatbot-like feedback."""
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # Convert cm to meters
        if weight <= 0 or height <= 0:
            messagebox.showerror("Lỗi", "Cân nặng và chiều cao phải lớn hơn 0!", font=("Helvetica", 10))
            return
        bmi = weight / (height ** 2)
        if bmi < 18.5:
            category = "Gầy (Thiếu cân)"
            advice = ("Bạn hơi gầy đó! Hãy ăn uống đủ chất và tập thể dục nhẹ nhàng để tăng cân khỏe mạnh. "
                     "Thử ăn thêm các bữa phụ giàu protein nhé!")
        elif 18.5 <= bmi <= 24.9:
            category = "Bình thường"
            advice = ("Chúc mừng, BMI của bạn ở mức lý tưởng! Hãy duy trì lối sống lành mạnh với chế độ ăn "
                     "cân bằng và tập thể dục đều đặn.")
        elif 25 <= bmi <= 29.9:
            category = "Thừa cân"
            advice = ("Bạn đang hơi thừa cân. Hãy thử giảm tinh bột, ăn nhiều rau xanh và tập thể dục như đi bộ "
                     "hoặc yoga để kiểm soát cân nặng.")
        else:
            category = "Béo phì"
            advice = ("BMI của bạn ở mức cao, có nguy cơ ảnh hưởng sức khỏe. Hãy tham khảo ý kiến bác sĩ và xây "
                     "dựng kế hoạch giảm cân an toàn với chế độ ăn kiêng và tập luyện.")
        result_text = f"BMI của bạn: {bmi:.2f}\nPhân loại: {category}\nLời khuyên: {advice}"
        result_label.config(text=result_text)
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ cho cân nặng và chiều cao!", font=("Helvetica", 10))

def clear_inputs():
    """Clear input fields and result display."""
    weight_entry.delete(0, END)
    height_entry.delete(0, END)
    result_label.config(text="BMI của bạn sẽ hiển thị ở đây.")

def on_button_hover(event):
    """Change button color on hover."""
    event.widget.config(bg="#0288D1")

def on_button_leave(event):
    """Revert button color when not hovering."""
    event.widget.config(bg="#4FC3F7")

# Create main window
root = Tk()
root.title("Chatbot Tính BMI - Biển Xanh")
root.geometry("400x500")
root.resizable(False, False)
root.configure(bg="#E0F7FA")  # Light sea blue background

# Load background image (sea)
try:
    # Replace 'sea.jpg' with your image file name
    image_path = os.path.join(os.path.dirname(__file__), "sea.jpg")
    bg_image = Image.open(image_path)
    bg_image = bg_image.resize((400, 500), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
except Exception as e:
    print(f"Không thể tải hình nền: {e}. Sử dụng nền màu thay thế.")

# Create main frame for widgets
main_frame = Frame(root, bg="#FFFFFF", relief="raised", borderwidth=5)
main_frame.place(relx=0.5, rely=0.5, anchor="center", width=350, height=450)

# Title
Label(main_frame, text="Chatbot Tính BMI", font=("Helvetica", 18, "bold"), bg="#FFFFFF", fg="#01579B").pack(pady=15)

# Weight input
Label(main_frame, text="Cân nặng (kg):", font=("Helvetica", 12), bg="#FFFFFF", fg="#01579B").pack()
weight_entry = Entry(main_frame, font=("Helvetica", 12), width=20, bg="#E0F7FA", fg="#01579B", relief="flat", borderwidth=2)
weight_entry.pack(pady=5)

# Height input
Label(main_frame, text="Chiều cao (cm):", font=("Helvetica", 12), bg="#FFFFFF", fg="#01579B").pack()
height_entry = Entry(main_frame, font=("Helvetica", 12), width=20, bg="#E0F7FA", fg="#01579B", relief="flat", borderwidth=2)
height_entry.pack(pady=5)

# Buttons
calc_button = Button(main_frame, text="Tính BMI", font=("Helvetica", 12), bg="#4FC3F7", fg="#FFFFFF", relief="flat", borderwidth=2, command=calculate_bmi)
calc_button.pack(pady=10)
calc_button.bind("<Enter>", on_button_hover)
calc_button.bind("<Leave>", on_button_leave)

clear_button = Button(main_frame, text="Xóa", font=("Helvetica", 12), bg="#4FC3F7", fg="#FFFFFF", relief="flat", borderwidth=2, command=clear_inputs)
clear_button.pack(pady=5)
clear_button.bind("<Enter>", on_button_hover)
clear_button.bind("<Leave>", on_button_leave)

# Result display
result_label = Label(main_frame, text="BMI của bạn sẽ hiển thị ở đây.", font=("Helvetica", 12), bg="#FFFFFF", fg="#01579B", wraplength=320, justify="left")
result_label.pack(pady=20)

# Start the main loop
root.mainloop()
