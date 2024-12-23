import streamlit as st
import time
import matplotlib.pyplot as plt

st.title("🎉 สุขสันต์วันเกิดนะคะ! 🎉")

st.subheader("ขอให้วันเกิดปีนี้ของเธอเต็มไปด้วยความสุข ความรัก และเป็นการเติบโตที่ดีค่ะ 💖")

st.write("""
    🎂 ขอให้เธอมีวันที่ดีมากๆ และขอให้ปีนี้เป็นปีที่ดีที่สุดสำหรับเธอนะคะ!
    🍰 เราจะอยู่ข้างๆเธอตรงนี้เสมอ ไม่ว่าเธอจะเจอเรื่องอะไรจะมีเราไปด้วยเสมอ
    🎁 รักเธอที่สู้ดดดดด...ขอบคุณที่เกิดมาให้เรารักนะคะ
""")

image_url = "https://live.staticflickr.com/65535/54221439737_18c1b97e95_m.jpg"
st.image(image_url, caption="น่ารักกกก", use_container_width=True)

st.subheader("ความน่ารักของแฟนผม ❤️")
categories = ['Eyes', 'Smile', 'Confidence', 'Kindness', 'Sense of Humor']
scores = [10, 10, 10, 10, 9.8] 

fig, ax = plt.subplots()
ax.bar(categories, scores, color='pink')
ax.set_xlabel('\nAttributes of Her')
ax.set_ylabel('Score (1-10)')
ax.set_title('\nHer Charm Scoring')
st.pyplot(fig)

st.title("หนึ่งวันของแฟนผม❤️")

st.write("""
    Chart แสดงภาระงานของแฟนผมในแต่ละวัน😊
""")

labels = ['Sleep', 'Eat', 'Live Life']
sizes = [45, 45, 10] 
colors = ['#FFB6C1', '#FF69B4', '#FFC0CB']
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  
st.pyplot(fig)

st.markdown("""
    <iframe width="560" height="315" 
            src="https://www.youtube.com/embed/zLSuNuFjgYI?autoplay=1" 
            frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture">
    </iframe>
""", unsafe_allow_html=True)

with st.spinner('เอ๋ง...'):
    time.sleep(3)

st.success("ขอบคุณที่เติบโตมาอย่างดีเพื่อให้เราตกหลุมรักนะคะ! 🎈")
