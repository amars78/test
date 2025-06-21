import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime, timedelta

# ✅ Streamlit 페이지 설정
st.set_page_config(page_title="Top 5 주가 시각화", layout="wide")
st.title("📈 글로벌 시가총액 Top 5 기업의 최근 1년 주가 변화")

# 🔝 시가총액 기준 Top 5 기업 (미국)
top5_tickers = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Nvidia": "NVDA",
    "Amazon": "AMZN",
    "Alphabet (Google)": "GOOGL"
}

# 📅 최근 1년 범위
end_date = datetime.today()
start_date = end_date - timedelta(days=365)

# 📦 주가 데이터 불러오기
@st.cache_data
def fetch_stock_data():
    data = {}
    for name, ticker in top5_tickers.items():
        df = yf.download(ticker, start=start_date, end=end_date)
        if not df.empty:
            data[name] = df["Close"]
    return data

# 데이터 수집
stock_data = fetch_stock_data()

# ✅ Plotly 선형 그래프
if not stock_data:
    st.error("❌ 주가 데이터를 불러오지 못했습니다.")
else:
    fig = go.Figure()

    for name, prices in stock_data.items():
        fig.add_trace(go.Scatter(
            x=prices.index,
            y=prices.values,
            mode='lines',
            name=name
        ))

    fig.update_layout(
        title="📊 글로벌 Top 5 기업 주가 변화 (최근 1년)",
        xaxis_title="날짜",
        yaxis_title="종가 (USD)",
        template="plotly_white",
        hovermode="x unified",
        height=600,
        legend=dict(orientation="h", yanchor="bottom", y=-0.3)
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("💡 데이터를 확대하거나 마우스를 올려서 세부 정보를 확인해보세요.")
