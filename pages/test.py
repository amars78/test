import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from geopy.distance import geodesic

# CSV 데이터 직접 DataFrame으로 정의 (간단화를 위해 일부 열 생략)
data = [
    ["서울시청소년상담복지센터", "서울특별시", "중구", "서울특별시 중구 을지로 11길 23 7층", 37.566375, 126.990471],
    ["종로구청소년상담복지센터", "서울특별시", "종로구", "서울특별시 종로구 명륜길 90", 37.585501, 126.997992],
    ["용산구청소년상담복지센터", "서울특별시", "용산구", "서울특별시 용산구 백범로 329", 37.534241, 126.963403],
    ["성동구청소년상담복지센터", "서울특별시", "성동구", "서울특별시 성동구 행당로6길 24-15", 37.561491, 127.026402],
    ["광진구청소년상담복지센터", "서울특별시", "광진구", "서울특별시 광진구 아차산로 24길 17", 37.534201, 127.067332],
    ["강동구청소년상담복지센터", "서울특별시", "강동구", "서울특별시 강동구 아리수로93길 47", 37.553258, 127.170669],
    # ... 필요 시 나머지 센터도 추가 가능
]

columns = ["센터명", "시도명", "시군구명", "주소", "위도", "경도"]
df = pd.DataFrame(data, columns=columns)

st.title("📍 내 위치에서 가까운 청소년 상담센터 찾기")

# 사용자 위치 입력
st.subheader("🧭 현재 위치 입력")
col1, col2 = st.columns(2)
with col1:
    user_lat = st.number_input("현재 위도 입력", value=37.5665, format="%.6f")
with col2:
    user_lon = st.number_input("현재 경도 입력", value=126.9780, format="%.6f")

# 거리 계산 함수
def get_nearest_center(user_lat, user_lon):
    df["거리"] = df.apply(lambda row: geodesic((user_lat, user_lon), (row["위도"], row["경도"])).km, axis=1)
    nearest = df.sort_values("거리").iloc[0]
    return nearest

nearest = get_nearest_center(user_lat, user_lon)

# 결과 표시
st.success(f"\n가장 가까운 상담센터는 **{nearest['센터명']}** 입니다!\n\n📍 주소: {nearest['주소']}\n\n🛣️ 거리: {nearest['거리']:.2f} km")

# 지도 생성
m = folium.Map(location=[user_lat, user_lon], zoom_start=12)
folium.Marker([user_lat, user_lon], tooltip="내 위치", icon=folium.Icon(color="blue")).add_to(m)

# 모든 센터 마커 표시
for _, row in df.iterrows():
    folium.Marker(
        [row["위도"], row["경도"]],
        tooltip=row["센터명"],
        icon=folium.Icon(color="green")
    ).add_to(m)

# 가장 가까운 센터 강조
folium.Marker(
    [nearest["위도"], nearest["경도"]],
    tooltip=f"가장 가까운 센터: {nearest['센터명']}",
    icon=folium.Icon(color="red", icon="star")
).add_to(m)

st.subheader("🗺️ 지도 보기")
st_folium(m, width=800, height=500)
