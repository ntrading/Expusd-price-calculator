import streamlit as st

# 스마트폰 화면에 맞춘 설정
st.set_page_config(page_title="수출 단가 계산기", layout="centered")

st.title("수출 단가 계산기 📊")
st.markdown("---")

# 입력 폼 (환율 입력창 삭제됨)
krw_cost = st.number_input("원가 입력 (원)", min_value=0, step=1000, format="%d")

st.markdown("---")

# 계산 버튼
if st.button("달러 단가 계산하기", use_container_width=True):
    if krw_cost > 0:
        # 1. 원가에 35% 마진 더하기 (원가 * 1.35)
        target_krw = krw_cost * 1.35
        
        # 2. 두 가지 경우의 달러 단가 계산
        price_under_1200 = target_krw / 1000
        price_over_1200 = target_krw / 1200
        
        # 3. 결과 출력 (모바일에서 보기 좋게 위아래 박스로 배치)
        st.info(f"🔽 **환율 1200원 미만일 때**\n### ${price_under_1200:.2f}")
        st.warning(f"🔼 **환율 1200원 이상일 때**\n### ${price_over_1200:.2f}")
        
    else:
        st.error("정확한 원가를 1원 이상 입력해주세요.")