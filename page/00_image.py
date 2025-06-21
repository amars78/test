import streamlit as st

# 페이지 설정 (선택 사항 - Home.py에서 전역 설정됨)
# st.set_page_config(
#     page_title="MBTI 그림 갤러리 🖼️",
#     page_icon="🎨",
#     layout="centered"
# )

st.title("🎨 MBTI 그림 갤러리: 유형별 이미지로 특징을 느껴보세요! ✨")
st.markdown("각 MBTI 유형의 특징을 잘 나타내는 아름다운 그림들을 감상해 보세요. 😊")
st.write("---")

# MBTI 유형별 이미지 정보 (실제 이미지 경로로 변경해야 합니다!)
# 예시: "ISTJ": "images/istj.png"
# 주의: 이 이미지는 예시입니다. 실제 이미지를 your_app_directory/images/ 폴더에 넣고 경로를 지정해야 합니다.
# 이미지를 앱과 같은 디렉토리에 'images' 폴더를 만들고 그 안에 넣어주세요.
mbti_images = {
    "ISTJ": "https://via.placeholder.com/300x200.png?text=ISTJ+%EB%A1%9C%EA%B3%A0", # 예시 이미지 URL
    "ISFJ": "https://via.placeholder.com/300x200.png?text=ISFJ+%EB%A1%9C%EA%B3%A0",
    "ISTP": "https://via.placeholder.com/300x200.png?text=ISTP+%EB%A1%9C%EA%B3%A0",
    "ISFP": "https://via.placeholder.com/300x200.png?text=ISFP+%EB%A1%9C%EA%B3%A0",
    "INTJ": "https://via.placeholder.com/300x200.png?text=INTJ+%EB%A1%9C%EA%B3%A0",
    "INFJ": "https://via.placeholder.com/300x200.png?text=INFJ+%EB%A1%9C%EA%B3%A0",
    "INTP": "https://via.placeholder.com/300x200.png?text=INTP+%EB%A1%9C%EA%B3%A0",
    "INFP": "https://via.placeholder.com/300x200.png?text=INFP+%EB%A1%9C%EA%B3%A0",
    "ESTJ": "https://via.placeholder.com/300x200.png?text=ESTJ+%EB%A1%9C%EA%B3%A0",
    "ESFJ": "https://via.placeholder.com/300x200.png?text=ESFJ+%EB%A1%9C%EA%B3%A0",
    "ESTP": "https://via.placeholder.com/300x200.png?text=ESTP+%EB%A1%9C%EA%B3%A0",
    "ESFP": "https://via.placeholder.com/300x200.png?text=ESFP+%EB%A1%9C%EA%B3%A0",
    "ENTJ": "https://via.placeholder.com/300x200.png?text=ENTJ+%EB%A1%9C%EA%B3%A0",
    "ENFJ": "https://via.placeholder.com/300x200.png?text=ENFJ+%EB%A1%9C%EA%B3%A0",
    "ENTP": "https://via.placeholder.com/300x200.png?text=ENTP+%EB%A1%9C%EA%B3%A0",
    "ENFP": "https://via.placeholder.com/300x200.png?text=ENFP+%EB%A1%9C%EA%B3%A0",
}

# 갤러리 레이아웃 (3열로 배치)
cols = st.columns(3) # 3열로 이미지를 배치합니다.

mbti_types_list = list(mbti_images.keys())

for i, mbti_type in enumerate(mbti_types_list):
    with cols[i % 3]: # 각 열에 순서대로 이미지를 배치
        st.subheader(f"✨ {mbti_type}")
        image_path = mbti_images.get(mbti_type)
        if image_path:
            # st.image 함수는 로컬 파일 경로 또는 URL을 지원합니다.
            st.image(image_path, caption=f"{mbti_type}의 특징을 담은 이미지", use_column_width=True)
        else:
            st.warning(f"{mbti_type} 이미지를 찾을 수 없습니다. 😥")
        st.write("---") # 각 이미지 블록 아래 구분선

st.markdown("💡 **팁:** 각 유형의 이미지를 클릭하여 더 자세한 설명을 보거나, 이미지에 대한 당신의 생각을 적어보세요! (이 기능은 아직 구현되지 않았습니다. 😊)")
st.write("---")

# --- Footer ---
st.markdown("✨ **제작:** AI 진로 탐색 도우미 🤖 | **버전:** 1.0 🚀")
st.markdown("Made with ❤️ for your bright future! 🌟")
