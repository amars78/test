import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime, timedelta

# 페이지 설정
st.set_page_config(page_title="Top10 시가총액 주가 변화", layout="wide")

st.title("📈 글로벌 시가총액 Top10 기업 - 최근 1년 주가 변화")

# ✅ 검증된 티커 목록 (미국 기업)
tickers = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Amazon": "AMZN",
    "Nvidia": "NVDA",
    "Alphabet (Google)": "GOOGL",
    "Meta (Facebook)": "META",
    "Tesla": "TSLA",
    "Berkshire Hathaway": "BRK-B",
    "Eli Lilly": "LLY",
    "Visa": "V"
}

# 기간 설정 (최근 1년)
end_date = datetime.today()
start_date = end_date - timedelta(days=365)

# 📦 데이터 수집
@st.cache_data
def get_data():
    price_data = {}
    for name, ticker in tickers.items():
        df = yf.download(ticker, start=start_date, end=end_date)
        if not df.empty:
            price_data[name] = df["Close"]
    return price_data

data = get_data()

# ⚠️ 데이터가 없으면 메시지 표시
if not data:
    st.error("❌ 주가 데이터를 불러오지 못했습니다. 나중에 다시 시도해주세요.")
else:
    # 📊 Plotly 그래프 생성
    fig = go.Figure()
    for name, prices in data.items():
        fig.add_trace(go.Scatter(
            x=prices.index,
            y=prices.values,
            mode='lines',
            name=name
        ))

    fig.update_layout(
        title="📊 글로벌 Top10 기업의 주가 추이 (1년)",
        xaxis_title="날짜",
        yaxis_title="종가 (USD)",
        hovermode="x unified",
        template="plotly_white",
        height=600,
        legend=dict(orientation="h", yanchor="bottom", y=-0.3)
    )

    # 차트 출력
    st.plotly_chart(fig, use_container_width=True)
