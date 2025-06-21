import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime, timedelta

# 📅 기간 설정 (최근 1년)
end_date = datetime.today()
start_date = end_date - timedelta(days=365)

# ✅ 시가총액 상위 5개 미국 기업
tickers = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Nvidia": "NVDA",
    "Amazon": "AMZN",
    "Meta": "META"
}

# 🌐 페이지 설정
st.set_page_config(page_title="선형 주가 그래프", layout="wide")
st.title("📈 글로벌 시가총액 Top 5 기업의 선형 주가 변화 그래프")

# 📥 주가 데이터 로딩
@st.cache_data
def load_data():
    stock_data = {}
    for name, ticker in tickers.items():
        df = yf.download(ticker, start=start_date, end=end_date)
        if not df.empty:
            stock_data[name] = df["Close"]
    return stock_data

data = load_data()

# ✅ 그래프 출력
if not data:
    st.error("❌ 데이터를 불러올 수 없습니다. 인터넷 연결 또는 티커 확인 필요.")
else:
    fig = go.Figure()

    # 각 기업마다 선형 그래프 추가
    for company, close_prices in data.items():
        fig.add_trace(go.Scatter(
            x=close_prices.index,
            y=close_prices.values,
            mode='lines',
            name=company,
            line=dict(shape='linear')  # 👈 선형
        ))

    # 레이아웃 구성
    fig.update_layout(
        title="📊 최근 1년간 글로벌 Top 5 기업 주가 (선형 그래프)",
        xaxis_title="날짜",
        yaxis_title="종가 (USD)",
        hovermode="x unified",
        template="plotly_white",
        height=600,
        legend=dict(orientation="h", yanchor="bottom", y=-0.3)
    )

    # 📊 그래프 출력
    st.plotly_chart(fig, use_container_width=True)
