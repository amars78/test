import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# 📅 기간 설정
end_date = datetime.today()
start_date = end_date - timedelta(days=365)

# 🔝 Top 5 기업 티커
top5_tickers = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Nvidia": "NVDA",
    "Amazon": "AMZN",
    "Alphabet (Google)": "GOOGL"
}

# 📥 데이터 수집 함수
@st.cache_data
def fetch_top5_stock_data():
    stock_data = {}
    for name, ticker in top5_tickers.items():
        df = yf.download(ticker, start=start_date, end=end_date)
        if not df.empty:
            stock_data[name] = df["Close"]
    combined_df = pd.DataFrame(stock_data)
    combined_df.dropna(inplace=True)
    return combined_df

# 📈 선형 그래프 함수
def plot_stock_prices(df):
    fig, ax = plt.subplots(figsize=(12, 6))
    for company in df.columns:
        ax.plot(df.index, df[company], label=company)

    ax.set_title("📈 글로벌 Top 5 기업 최근 1년 주가 변화", fontsize=16)
    ax.set_xlabel("날짜")
    ax.set_ylabel("주가 (USD)")
    ax.legend()
    ax.grid(True)
    return fig

# ✅ Streamlit 앱 시작
st.set_page_config(page_title="Top 5 선형 주가 그래프", layout="wide")
st.title("🌍 글로벌 시가총액 Top 5 기업의 선형 주가 그래프")

# 📦 데이터 로딩
df = fetch_top5_stock_data()

if df.empty:
    st.error("❌ 주가 데이터를 불러오지 못했습니다.")
else:
    st.write("✅ 최근 1년 간 주가 데이터 (종가 기준)")
    st.dataframe(df.tail())

    # 📊 선형 그래프 출력
    fig = plot_stock_prices(df)
    st.pyplot(fig)
