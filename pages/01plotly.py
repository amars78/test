import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime, timedelta

# 📅 날짜 설정
end = datetime.today()
start = end - timedelta(days=365)

# ✅ 안정적으로 작동하는 미국 상장사 Top 5 (검증용)
tickers = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Nvidia": "NVDA",
    "Amazon": "AMZN",
    "Meta": "META"
}

# Streamlit 앱 설정
st.set_page_config(page_title="Top5 주가 변화", layout="wide")
st.title("📈 글로벌 시가총액 Top5 기업 주가 변화 (1년)")
st.markdown("💡 데이터 출처: Yahoo Finance (yfinance)")

# 📥 데이터 수집
@st.cache_data
def fetch_prices():
    all_data = {}
    for name, ticker in tickers.items():
        df = yf.download(ticker, start=start, end=end)
        if not df.empty:
            all_data[name] = df['Close']
    return all_data

prices = fetch_prices()

# ✅ 데이터 확인
if not prices:
    st.error("❌ 데이터를 불러올 수 없습니다. 인터넷 연결 또는 Yahoo Finance 서버를 확인하세요.")
else:
    # 📊 Plotly 그래프 그리기
    fig = go.Figure()

    for name, series in prices.items():
        fig.add_trace(go.Scatter(
            x=series.index,
            y=series.values,
            mode='lines',
            name=name
        ))

    fig.update_layout(
        title="📊 최근 1년간 주가 변화 (Top 5 기업)",
        xaxis_title="날짜",
        yaxis_title="종가 (USD)",
        template="plotly_white",
        hovermode="x unified",
        height=600,
        legend=dict(orientation="h", yanchor="bottom", y=-0.3)
    )

    st.plotly_chart(fig, use_container_width=True)
