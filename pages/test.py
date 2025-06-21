import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from geopy.distance import geodesic
from streamlit_javascript import st_javascript

# 센터 데이터 불러오기 (예: DataFrame로 직접 로딩)
columns = ["센터명", "시도명", "시군구명", "주소", "위도", "경도"]
data = [
    # 예시 일부 데이터 (전체 추가 필요 시 알려주세요)
    ["서울시청소년상담복지센터", "서울특별시", "중구", "서울특별시 중구 을지로 11길 23 7층", 37.566375, 126.990471],
    ["종로구청소년상담복지센터", "서울특별시", "종로구", "서울특별시 종로구 명륜길 90", 37.585501, 126.997992],
    ["관악구청소년상담복지센터", "서울특별시", "관악구", "서울특별시 관악구 남부순환로 234길 73", 37.484294, 126.931754],
    ["강동구청소년상담복지센터", "서울특별시", "강동구", "서울특별시 강동구 아리수로93길 47", 37.553258, 127.170669],
    # 전체 센터 목록 필요 시 이어서 붙여주세요
]
df = pd.DataFrame(data, columns=columns)

st.title("📍 내 위치에서 가장 가까운 청소년 상담센터")

# 사용자 위치 가져오기
coords = st_javascript(
    """
    navigator.geolocation.getCurrentPosition(
        (pos) => {
            const coords = {latitude: pos.coords.latitude, longitude: pos.coords.longitude};
            window.parent.postMessage(coords, "*");
        },
        (err) => {
            window.parent.postMessage({error: err.message}, "*");
        }
    );
    """,
    key="get_user_location"
)

# 기본 좌표 (서울시청)
default_lat, default_lon = 37.5665, 126.9780

# 좌표 유효성 확인
if coords and "latitude" in coords and "longitude" in coords:
    user_lat = coords["latitude"]
    user_lon = coords["longitude"]
    st.success(f"📌 현재 위치: {user_lat:.4f}, {user_lon:.4f}")
else:
    user_lat, user_lon = default_lat, default_lon
    st.warning("현재 위치를 가져올 수 없습니다. 기본 위치(서울시청)로 설정합니다.")

# 거리 계산 및 가장 가까운 센터 찾기
df["거리"] = df.apply(lambda row: geodesic((user_lat, user_lon), (row["위도"], row["경도"])).km, axis=1)
nearest = df.sort_values("거리").iloc[0]

st.subheader("🔍 가장 가까운 상담센터")
st.markdown(f"""
**🏢 센터명:** {nearest['센터명']}  
📍 **주소:** {nearest['주소']}  
🛣️ **거리:** {nearest['거리']:.2f} km
""")

# 지도 그리기
m = folium.Map(location=[user_lat, user_lon], zoom_start=12)
folium.Marker([user_lat, user_lon], tooltip="내 위치", icon=folium.Icon(color="blue")).add_to(m)

# 전체 센터 마커
for _, row in df.iterrows():
    folium.Marker([row["위도"], row["경도"]], tooltip=row["센터명"], icon=folium.Icon(color="green")).add_to(m)

# 가장 가까운 센터 강조
folium.Marker([nearest["위도"], nearest["경도"]], tooltip=f"가장 가까운 센터: {nearest['센터명']}", icon=folium.Icon(color="red")).add_to(m)

st_folium(m, width=800, height=500)
