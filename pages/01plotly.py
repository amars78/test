import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta

st.set_page_config(layout="wide")

st.title("글로벌 시가총액 Top 10 기업 주식 변화 (최근 1년)")

# 2025년 6월 21일 기준, 시가총액 Top 10 (변동 가능성 있음)
# 실제 Yahoo Finance에서 시가총액 순위를 실시간으로 가져오는 API는 유료이거나 제한적입니다.
# 따라서, 일반적으로 알려진 Top 10 기업 티커를 수동으로 입력합니다.
# 이 리스트는 업데이트될 수 있으므로, 필요에 따라 수정해주세요.
top_10_tickers = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "NVIDIA": "NVDA",
    "Alphabet (Google)": "GOOGL", # 또는 GOOG
    "Amazon": "AMZN",
    "Meta Platforms": "META",
    "Saudi Aramco": "2222.SR", # 사우디아람코 (사우디 증권 거래소)
    "Berkshire Hathaway": "BRK-A", # 또는 BRK-B (Class B)
    "Eli Lilly and Company": "LLY",
    "TSMC": "TSM"
}

# 날짜 설정 (최근 1년)
end_date = datetime.now()
start_date = end_date - timedelta(days=365)

selected_companies = st.multiselect(
    "시각화할 기업을 선택하세요:",
    options=list(top_10_tickers.keys()),
    default=list(top_10_tickers.keys()) # 기본적으로 모든 기업 선택
)

if not selected_companies:
    st.warning("하나 이상의 기업을 선택해주세요.")
else:
    st.write(f"선택된 기업들의 {start_date.strftime('%Y-%m-%d')} 부터 {end_date.strftime('%Y-%m-%d')} 까지의 주식 변화입니다.")

    for company_name in selected_companies:
        ticker = top_10_tickers[company_name]
        try:
            # 주식 데이터 다운로드
            data = yf.download(ticker, start=start_date, end=end_date)

            if data.empty:
                st.write(f"### {company_name} ({ticker})")
                st.warning(f"{company_name}의 데이터를 가져오지 못했습니다. 티커를 확인해주세요.")
                continue

            fig = go.Figure()
            fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='종가'))

            fig.update_layout(
                title=f'{company_name} ({ticker}) 주식 종가 변화',
                xaxis_title='날짜',
                yaxis_title='종가 (USD)',
                hovermode="x unified",
                template="plotly_white"
            )
            st.plotly_chart(fig, use_container_width=True)

        except Exception as e:
            st.error(f"{company_name} ({ticker})의 데이터를 가져오는 중 오류가 발생했습니다: {e}")

st.markdown("""
---
**참고:**
* 위 시가총액 Top 10 리스트는 변동될 수 있습니다. (2025년 6월 21일 기준 추정)
* 사우디 아람코(2222.SR)와 같은 일부 해외 기업은 데이터 로딩이 느리거나, Yahoo Finance에서 제공하는 데이터가 제한적일 수 있습니다.
* `yfinance` 라이브러리는 Yahoo Finance의 데이터를 기반으로 하므로, Yahoo Finance의 데이터 제공 정책에 따라 데이터에 접근이 제한될 수 있습니다.
""")
