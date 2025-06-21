import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime, timedelta

# 🔧 페이지 설정
st.set_page_config(page_title="📊 글로벌 시가총액 TOP10 주가 변화", layout="wide")
st.title("🌍 글로벌 시가총액 TOP10 기업의 최근 1년간 주가 변화 📈")

# 🏢 시가총액 Top 10 기업 (미국 중심, 안정적인 티커 기준)
top10_stocks = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Alphabet": "GOOGL",
    "Amazon": "AMZN",
    "Nvidia": "NVDA",
    "Berkshire Hathaway": "BRK-B",
    "Meta": "META",
    "TSMC": "TSM",
    "Eli Lilly": "LLY",
    "Tesla": "TSLA"
}

# 📆 날짜 범위 설정
end_date = datetime.today()
start_date = end_date - timedelta(days=365)

# 📦 데이터 불러오기 (캐시로 속도 향상)
@st.cache_data
def load_data(tickers):
    stock_history = {}
    for name, ticker in tickers.items():
        try:
            df = yf.download(ticker, start=start_date, end=end_date)
            if not df.empty:
                stock_history[name] = df["Close"]
        except:
            st.warning(f"❌ {name}({ticker})의 데이터를 불러오지 못했습니다.")
    return stock_history

data = load_data(top10_stocks)

# 📊 Plotly 시각화
fig = go.Figure()
for name, prices in data.items():
    fig.add_trace(go.Scatter(
        x=prices.index,
        y=prices.values,
        mode='lines',
        name=name,
        line=dict(width=2)
    ))

fig.update_layout(
    title="📈 글로벌 Top 10 기업의 주가 변화 (최근 1년)",
    xaxis_title="날짜",
    yaxis_title="종가 (USD)",
    template="plotly_white",
    hovermode="x unified",
    height=600,
    legend=dict(orientation="h", yanchor="bottom", y=-0.3)
)

# 🔍 차트 출력
if data:
    st.plotly_chart(fig, use_container_width=True)
else:
    st.error("⚠️ 데이터를 불러오지 못했습니다. 인터넷 연결 또는 티커 오류를 확인하세요.")
