import streamlit as st
import pandas as pd

st.set_page_config(layout="centered")

st.title("MBTI별 국어 과목 성취도 분석 📚")
st.write("당신의 MBTI 유형을 선택하고 국어 과목 성취도(가상)와 그 이유를 확인해보세요!")

# MBTI 유형 리스트
mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# 스크롤바(select_slider)로 MBTI 유형 선택
selected_mbti = st.select_slider(
    "MBTI 유형을 선택하세요 👇",
    options=mbti_types
)

st.write(f"---")
st.header(f"선택하신 MBTI 유형은 **{selected_mbti}** 입니다. ✨")

# 가상 국어 성취도 데이터 및 설명 생성
# 이 데이터와 설명은 실제 MBTI 연구 결과가 아닌 예시를 위한 임의의 값입니다.
achievement_data = {
    "MBTI 유형": [],
    "평균 점수": [],
    "성취 등급": [],
    "특징": [],
    "설명": [] # 설명 칼럼 추가
}

# 각 MBTI 유형별 가상 데이터 및 설명 할당
# 이 부분은 실제 데이터나 통계에 기반하지 않으며, 예시를 위한 임의의 값입니다.
# 필요에 따라 이 데이터를 수정하여 다양한 시나리오를 나타낼 수 있습니다.
if selected_mbti == "ISTJ":
    achievement_data["MBTI 유형"].append("ISTJ")
    achievement_data["평균 점수"].append(85)
    achievement_data["성취 등급"].append("A")
    achievement_data["특징"].append("성실하고 꾸준함")
    achievement_data["설명"].append("체계적이고 책임감이 강해 국어 교과서 내용과 규칙을 꼼꼼하게 습득합니다. 지루해 보이는 문법이나 어휘도 꾸준히 학습하여 높은 기본기를 바탕으로 안정적인 성취도를 보입니다. 📝")
elif selected_mbti == "ISFJ":
    achievement_data["MBTI 유형"].append("ISFJ")
    achievement_data["평균 점수"].append(82)
    achievement_data["성취 등급"].append("B+")
    achievement_data["특징"].append("세심하고 노력파")
    achievement_data["설명"].append("타인의 감정이나 스토리에 공감하는 능력이 뛰어나 문학 작품을 깊이 이해하는 데 강점을 가집니다. 성실하게 복습하고 정리하는 습관으로 꾸준히 좋은 성적을 유지합니다. 💖")
elif selected_mbti == "INFJ":
    achievement_data["MBTI 유형"].append("INFJ")
    achievement_data["평균 점수"].append(90)
    achievement_data["성취 등급"].append("A+")
    achievement_data["특징"].append("깊이 있는 통찰력")
    achievement_data["설명"].append("이상주의적이고 통찰력이 뛰어나 문학 작품의 숨겨진 의미나 작가의 의도를 잘 파악합니다. 추상적인 개념이나 비유적 표현에 대한 이해가 높아 국어 심화 학습에 강합니다. 💡")
elif selected_mbti == "INTJ":
    achievement_data["MBTI 유형"].append("INTJ")
    achievement_data["평균 점수"].append(92)
    achievement_data["성취 등급"].append("A+")
    achievement_data["특징"].append("전략적
