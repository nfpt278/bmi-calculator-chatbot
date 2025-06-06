# BMI Calculator Chatbot with Tkinter GUI
# Author: Grok (xAI), based on original code from https://github.com/nfpt278/bmi-calculator-chatbot
# Description: A GUI application to calculate BMI and provide health advice via a chatbot-like interface.
# Requirements: Python 3.6+, tkinter (usually included with Python)
# How to run:
# 1. Save this file as bmi_chatbot_gui.py
# 2. Ensure Python is installed: python --version
# 3. On Linux, install tkinter if needed: sudo apt-get install python3-tk
# 4. Run: python bmi_chatbot_gui.py

from tkinter import *
from tkinter import messagebox

def calculate_bmi():
    """Calculate BMI and display result with chatbot-like feedback."""
    try:
        # Get input values
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # Convert cm to meters
        
        # Validate inputs
        if weight <= 0 or height <= 0:
            messagebox.showerror("Lỗi", "Cân nặng và chiều cao phải lớn hơn 0!")
            return
        
        # Calculate BMI
        bmi = weight / (height ** 2)
        
        # Determine BMI category and chatbot response
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
        
        # Update result display
        result_text = f"BMI của bạn: {bmi:.2f}\nPhân loại: {category}\nLời khuyên: {advice}"
        result_label.config(text=result_text)
        
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ cho cân nặng và chiều cao!")

def clear_inputs():
    """Clear input fields and result display."""
    weight_entry.delete(0, END)
    height_entry.delete(0, END)
    result_label.config(text="BMI của bạn sẽ hiển thị ở đây.")

# Create main window
root = Tk()
root.title("Chatbot Tính BMI")
root.geometry("400x500")
root.resizable(False, False)

# Create and pack widgets
Label(root, text="Chatbot Tính BMI", font=("Arial", 16, "bold")).pack(pady=10)

# Weight input
Label(root, text="Cân nặng (kg):", font=("Arial", 12)).pack()
weight_entry = Entry(root, font=("Arial", 12), width=20)
weight_entry.pack(pady=5)

# Height input
Label(root, text="Chiều cao (cm):", font=("Arial", 12)).pack()
height_entry = Entry(root, font=("Arial", 12), width=20)
height_entry.pack(pady=5)

# Buttons
Button(root, text="Tính BMI", font=("Arial", 12), command=calculate_bmi).pack(pady=10)
Button(root, text="Xóa", font=("Arial", 12), command=clear_inputs).pack(pady=5)

# Result display
result_label = Label(root, text="BMI của bạn sẽ hiển thị ở đây.", font=("Arial", 12), wraplength=350, justify="left")
result_label.pack(pady=20)

# Start the main loop
root.mainloop()
