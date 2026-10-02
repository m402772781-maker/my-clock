import streamlit as st
from datetime import datetime
import pytz  # این کتابخانه برای مدیریت مناطق زمانی است
import time

# تنظیم استایل صفحه برای اینکه وسط‌چین و زیباتر باشد
st.set_page_config(page_title="ساعت دیجیتال من", page_icon="⏰")

# ایجاد یک محل برای نمایش ساعت (Placeholder)
placeholder = st.empty()

# تعیین منطقه زمانی ایران
iran_tz = pytz.timezone('Asia/Tehran')

# حلقه بی‌نهایت برای به‌روزرسانی ثانیه‌به‌ثانیه
while True:
    # گرفتن زمان دقیق ایران
    now = datetime.now(iran_tz)
    
    # تبدیل زمان به فرمت خوانا (ساعت:دقیقه:ثانیه)
    current_time = now.strftime("%H:%M:%S")
    # اضافه کردن تاریخ (اختیاری)
    current_date = now.strftime("%Y/%m/%d")

    # نمایش در صفحه
    with placeholder.container():
        st.title("⏰ ساعت دیجیتال")
        st.subheader(f"تاریخ: {current_date}")
        st.markdown(f"<h1 style='text-align: center; font-size: 100px; color: #FF4B4B;'>{current_time}</h1>", unsafe_allow_html=True)
    
    # صبر کردن برای ۱ ثانیه و بعد تکرار حلقه
    time.sleep(1)
