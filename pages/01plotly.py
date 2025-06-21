import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta

# 페이지 레이아웃 설정
st.set_page_config(layout="wide", page_title="글로벌 시가총액 Top 10 주식 변화")

st.title("글로벌 시가총액 Top 10 기업 주식 변화 (최근 1년)")

# 2025년 6월 21일 기준, 일반적으로 알려진 시가총액 Top 10 (변동 가능성 있음)
# Yahoo Finance의 실시간 시가총액 순위는 직접 제공되지 않으므로, 이 리스트는 수동으로 관리됩니다.
top_10_tickers = {
    "Apple (AAPL)": "AAPL",
    "Microsoft (MSFT)": "MSFT",
    "NVIDIA (NVDA)": "NVDA",
    "Alphabet (GOOGL)": "GOOGL", # 또는 GOOG
    "Amazon (AMZN)": "AMZN",
    "Meta Platforms (META)": "META",
    "Saudi Aramco (2222.SR)": "2222.SR", # 사우디 증권 거래소
    "Berkshire Hathaway (BRK-A)": "BRK-A", # Class A, 또는 BRK-B (Class B)
    "Eli Lilly and Company (LLY)": "LLY",
    "TSMC (TSM)": "TSM"
}

# 날짜 설정 (최근 1년)
end_date = datetime.now()
start_date = end_date - timedelta(days=365)

# 사이드바에서 기업 선택
st.sidebar.header("기업 선택")
selected_companies_display = st.sidebar.multiselect(
    "시각화할 기업을 선택하세요:",
    options=list(top_10_tickers.keys()),
    default=list(top_10_tickers.keys()) # 기본적으로 모든 기업 선택
)

if not selected_companies_display:
    st.warning("📊 하나 이상의 기업을 선택해주세요!")
else:
    st.write(f"📈 선택된 기업들의 **{start_date.strftime('%Y-%m-%d')}** 부터 **{end_date.strftime('%Y-%m-%d')}** 까지의 주식 변화입니다.")

    for company_display_name in selected_companies_display:
        ticker = top_10_tickers[company_display_name]
        company_name = company_display_name.split(' ')[0] # 괄호 안 티커 제거

        st.subheader(f"🌐 {company_name} ({ticker})")

        try:
            # 주식 데이터 다운로드
            with st.spinner(f"✨ {company_name} ({ticker}) 데이터를 불러오는 중..."):
                data = yf.download(ticker, start=start_date, end=end_date, progress=False) # progress=False로 콘솔 출력 줄임

            if data.empty:
                st.error(f"⚠️ **{company_name} ({ticker})** 의 데이터를 가져오지 못했습니다. 티커를 확인하거나 잠시 후 다시 시도해주세요.")
                continue

            # Plotly 그래프 생성
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='종가'))

            fig.update_layout(
                title=f'**{company_name} ({ticker})** 주식 종가 변화',
                xaxis_title='날짜',
                yaxis_title='종가 (USD)',
                hovermode="x unified", # 마우스를 올렸을 때 x축 기준으로 모든 라인 값 표시
                template="plotly_white", # 깔끔한 흰색 배경 템플릿
                height=400 # 차트 높이 조정
            )
            st.plotly_chart(fig, use_container_width=True) # 컨테이너 너비에 맞춰 차트 크기 조정

        except Exception as e:
            st.error(f"❌ **{company_name} ({ticker})** 의 데이터를 가져오거나 시각화하는 중 오류가 발생했습니다: {e}")
