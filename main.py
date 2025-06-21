import streamlit as st

# 🌟 Page Configuration
st.set_page_config(page_title="MBTI 직업 추천", page_icon="🧠", layout="centered")

# 🌈 Custom CSS for colorful and bold text
st.markdown("""
    <style>
        .title {
            font-size: 40px;
            text-align: center;
            font-weight: bold;
            color: #ff4b4b;
        }
        .subtitle {
            font-size: 24px;
            text-align: center;
            color: #5f9ea0;
        }
        .result-box {
            background-color: #ffe4e1;
            border-radius: 15px;
            padding: 20px;
            margin-top: 20px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
    </style>
""", unsafe_allow_html=True)

# 🎉 Title and Intro
st.markdown('<div class="title">💡 MBTI로 알아보는 직업 추천 💼</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">당신의 MBTI 유형을 선택하면<br>어울리는 직업을 추천해드려요! 🌟</div>', unsafe_allow_html=True)
st.markdown("---")

# 🔮 MBTI 직업 데이터
mbti_jobs = {
    "INTJ": ("전략가", ["데이터 사이언티스트 🤖", "시스템 엔지니어 🛠️", "정책 분석가 🧾"]),
    "INFP": ("중재자", ["작가 ✍️", "상담가 🗣️", "예술가 🎨"]),
    "ENTP": ("토론가", ["기획자 📊", "창업가 🚀", "마케팅 전문가 📣"]),
    "ESFP": ("연예인", ["배우 🎭", "이벤트 플래너 🎉", "판매 전문가 🛍️"]),
    "ISTJ": ("현실주의자", ["공무원 🧑‍💼", "회계사 📒", "법률 보조원 ⚖️"]),
    "ENFP": ("활동가", ["광고 기획자 📺", "기자 📰", "디자이너 🎨"]),
    "ISFJ": ("수호자", ["간호사 🩺", "사회복지사 🫂", "교사 👩‍🏫"]),
    "ESTP": ("사업가", ["영업 전문가 📈", "기업가 🧑‍💼", "파일럿 ✈️"]),
    # 필요 시 모든 MBTI 유형 추가 가능
}

# 🧠 사용자 입력
selected_mbti = st.selectbox("당신의 MBTI 유형은 무엇인가요? 🔍", list(mbti_jobs.keys()))

# 🎯 결과 출력
if selected_mbti:
    nickname, jobs = mbti_jobs[selected_mbti]
    st.markdown(f"""
        <div class="result-box">
            <h2>✨ {selected_mbti} ({nickname}) 유형에게 어울리는 직업은?</h2>
            <ul>
                {"".join([f"<li style='font-size:20px;'>✅ {job}</li>" for job in jobs])}
            </ul>
            <p style='font-size:18px;'>🌟 꿈을 향해 도전해보세요!</p>
        </div>
    """, unsafe_allow_html=True)

# 🎁 Footer
st.markdown("---")
st.markdown("📚 진로교육 플랫폼 | 만든이: **ChatGPT + 너의 아이디어!** 🚀", unsafe_allow_html=True)
