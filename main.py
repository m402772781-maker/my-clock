import streamlit as st
import time
from datetime import datetime

# تنظیم عنوان صفحه
st.set_page_config(page_title="ساعت آنلاین", page_icon="⏰")

st.title("ساعت دیجیتال من")
st.write("این ساعت روی وب اجرا می‌شود و در موبایل و لپ‌تاپ قابل مشاهده است.")

# ایجاد یک جای خالی در صفحه برای آپدیت کردن زمان
placeholder = st.empty()

# حلقه برای آپدیت لحظه‌ای ساعت
while True:
    current_time = datetime.now().strftime("%H:%M:%S")
    # نمایش زمان در یک کادر زیبا (metric)
    placeholder.metric("زمان دقیق:", current_time)
    
    time.sleep(1) # توقف برای یک ثانیه

