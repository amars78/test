import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime, timedelta

# 🎯 시가총액 Top 10 기업 (2025년 기준, 티커 참고)
top10_tickers = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Saudi Aramco": "2222.SR",
    "Alphabet (Google)": "GOOGL",
    "Amazon": "AMZN",
    "Nvidia": "NVDA",
    "Berkshire Hathaway": "BRK-B",
    "Meta (Facebook)": "META",
    "TSMC": "TSM",
    "Eli Lilly": "LLY"
}

# 🌍 페이지 설정
st.set_page_config(page_title="🌐 글로벌 Top 10 시가총액 기업 주가 변화", layout="wide")
st.title("📈 글로벌 시가총액 Top 10 기업의 최근 1년간 주가 변화")

st.markdown("""
이 대시보드는 **Yahoo Finance** 데이터를 기반으로 최근 1년간의 주가 변화를 보여줍니다.  
Plotly 그래프는 마우스 오버, 확대/축소 등 상호작용이 가능합니다! 🧠
""")

# 📆 기간 설정
end_date = datetime.today()
start_date = end_date - timedelta(days=365)

# 🛠️ 데이터 수집
@st.cache_data
def fetch_data(tickers):
    data = {}
    for name, ticker in tickers.items():
        df = yf.download(ticker, start=start_date, end=end_date)
        if not df.empty:
            data[name] = df['Close']
    return data

stock_data = fetch_data(top10_tickers)

# 📊 Plotly 그래프
fig = go.Figure()

for company, prices in stock_data.items():
    fig.add_trace(go.Scatter(
        x=prices.index,
        y=prices,
        mode='lines',
        name=company,
        line=dict(width=2)
    ))

fig.update_layout(
    title="📉 최근 1년간 글로벌 Top 10 기업 주가 변화",
    xaxis_title="날짜",
    yaxis_title="주가 (USD)",
    hovermode="x unified",
    template="plotly_dark",
    legend=dict(orientation="h", y=-0.2),
    height=600
)

st.plotly_chart(fig, use_container_width=True)
