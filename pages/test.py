import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from geopy.distance import geodesic

# 데이터 로드
@st.cache_data
def load_data():
    return pd.read_csv("cs.csv")

df = load_data()

st.title("📍 청소년 상담센터 위치 안내")

# 사용자 현재 위치 입력
st.subheader("🧭 현재 위치 입력")
col1, col2 = st.columns(2)
with col1:
    user_lat = st.number_input("위도 입력", value=37.5665, format="%.6f")
with col2:
    user_lon = st.number_input("경도 입력", value=126.9780, format="%.6f")

# 거리 계산
def find_nearest(lat, lon, df):
    df["거리(km)"] = df.apply(lambda row: geodesic((lat, lon), (row["위도"], row["경도"])).km, axis=1)
    return df.sort_values("거리(km)").reset_index(drop=True)

# 가장 가까운 센터 찾기
nearest_df = find_nearest(user_lat, user_lon, df)
nearest = nearest_df.iloc[0]

st.success(f"📌 가장 가까운 상담센터는:\n\n**{nearest['주소']}**\n\n→ 거리: `{nearest['거리(km)']:.2f}km`")

# 지도 표시
st.subheader("🗺️ 지도에서 위치 보기")
m = folium.Map(location=[user_lat, user_lon], zoom_start=12)

# 현재 위치 마커
folium.Marker(
    [user_lat, user_lon],
    tooltip="내 위치",
    icon=folium.Icon(color="blue", icon="user")
).add_to(m)

# 상담센터 마커
for _, row in df.iterrows():
    folium.Marker(
        [row["위도"], row["경도"]],
        tooltip=row["주소"],
        icon=folium.Icon(color="green", icon="info-sign")
    ).add_to(m)

# 가장 가까운 상담센터 강조
folium.Marker(
    [nearest["위도"], nearest["경도"]],
    tooltip="가장 가까운 상담센터",
    icon=folium.Icon(color="red", icon="star")
).add_to(m)

# 지도 렌더링
st_data = st_folium(m, width=800, height=500)
