import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="청소년 상담복지센터 지도", layout="wide")
st.title("🧑‍🎓 전국 청소년 상담복지센터 위치 지도")

# 데이터 로드
@st.cache_data
def load_data():
    df = pd.read_csv("cs.csv", encoding='utf-8')
    df = df.dropna(subset=["위도", "경도"])  # 위도/경도 없는 행 제거
    return df

df = load_data()

# 지도 중심 좌표 (서울 시청 기준)
center_lat, center_lon = 37.5665, 126.9780
m = folium.Map(location=[center_lat, center_lon], zoom_start=7)

# 마커 추가
for _, row in df.iterrows():
    name = row.get("센터명", "이름 없음")
    phone = row.get("전화번호", "번호 없음")
    lat = row["위도"]
    lon = row["경도"]
    
    popup_html = f"<b>{name}</b><br>📞 {phone}"
    folium.Marker(
        location=[lat, lon],
        popup=popup_html,
        tooltip=name,
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)

# Streamlit에서 지도 렌더링
st.subheader("🗺 지도 보기")
st_folium(m, width=1000, height=600)
