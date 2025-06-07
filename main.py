import streamlit as st
import pandas as pd

st.set_page_config(layout="centered") # 페이지 레이아웃 설정 (wide 또는 centered)

st.title("MBTI별 국어 과목 성취도 분석 📚")
st.write("당신의 MBTI 유형을 선택하고 국어 과목 성취도(가상)를 확인해보세요!")

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

# 가상 국어 성취도 데이터 생성 (예시)
# 실제 데이터가 아니므로, 각 MBTI별로 임의의 값을 할당합니다.
# '성취도 점수'는 100점 만점으로 가정합니다.
achievement_data = {
    "MBTI 유형": [],
    "평균 점수": [],
    "성취 등급": [],
    "특징": []
}

# 각 MBTI 유형별 가상 데이터 할당
# 이 부분은 실제 데이터나 통계에 기반하지 않으며, 예시를 위한 임의의 값입니다.
# 필요에 따라 이 데이터를 수정하여 다양한 시나리오를 나타낼 수 있습니다.
if selected_mbti == "ISTJ":
    achievement_data["MBTI 유형"].append("ISTJ")
    achievement_data["평균 점수"].append(85)
    achievement_data["성취 등급"].append("A")
    achievement_data["특징"].append("성실하고 꾸준한 학습으로 높은 성취도를 보입니다.")
elif selected_mbti == "ISFJ":
    achievement_data["MBTI 유형"].append("ISFJ")
    achievement_data["평균 점수"].append(82)
    achievement_data["성취 등급"].append("B+")
    achievement_data["특징"].append("세심한 학습 계획과 노력이 성과로 나타납니다.")
elif selected_mbti == "INFJ":
    achievement_data["MBTI 유형"].append("INFJ")
    achievement_data["평균 점수"].append(90)
    achievement_data["성취 등급"].append("A+")
    achievement_data["특징"].append("깊이 있는 이해와 통찰력으로 뛰어난 성취를 이룹니다.")
elif selected_mbti == "INTJ":
    achievement_data["MBTI 유형"].append("INTJ")
    achievement_data["평균 점수"].append(92)
    achievement_data["성취 등급"].append("A+")
    achievement_data["특징"].append("전략적인 사고와 분석력으로 국어 과목을 정복합니다.")
elif selected_mbti == "ISTP":
    achievement_data["MBTI 유형"].append("ISTP")
    achievement_data["평균 점수"].append(78)
    achievement_data["성취 등급"].append("B")
    achievement_data["특징"].append("실용적인 학습을 선호하며, 문제 해결 능력에 강합니다.")
elif selected_mbti == "ISFP":
    achievement_data["MBTI 유형"].append("ISFP")
    achievement_data["평균 점수"].append(75)
    achievement_data["성취 등급"].append("B")
    achievement_data["특징"].append("자유로운 분위기에서 창의적인 학습을 할 때 몰입도가 높습니다.")
elif selected_mbti == "INFP":
    achievement_data["MBTI 유형"].append("INFP")
    achievement_data["평균 점수"].append(88)
    achievement_data["성취 등급"].append("A")
    achievement_data["특징"].append("상상력과 감수성을 바탕으로 문학 작품 이해에 탁월합니다.")
elif selected_mbti == "INTP":
    achievement_data["MBTI 유형"].append("INTP")
    achievement_data["평균 점수"].append(89)
    achievement_data["성취 등급"].append("A")
    achievement_data["특징"].append("논리적 사고와 탐구심으로 국어 지식을 깊이 파고듭니다.")
elif selected_mbti == "ESTP":
    achievement_data["MBTI 유형"].append("ESTP")
    achievement_data["평균 점수"].append(70)
    achievement_data["성취 등급"].append("C+")
    achievement_data["특징"].append("활동적이고 즉흥적인 학습을 선호하며, 실전에 강합니다.")
elif selected_mbti == "ESFP":
    achievement_data["MBTI 유형"].append("ESFP")
    achievement_data["평균 점수"].append(68)
    achievement_data["성취 등급"].append("C")
    achievement_data["특징"].append("흥미 위주의 학습을 선호하며, 발표나 토론에 능합니다.")
elif selected_mbti == "ENFP":
    achievement_data["MBTI 유형"].append("ENFP")
    achievement_data["평균 점수"].append(87)
    achievement_data["성취 등급"].append("A")
    achievement_data["특징"].append("다양한 아이디어와 열정으로 국어 학습에 즐겁게 참여합니다.")
elif selected_mbti == "ENTP":
    achievement_data["MBTI 유형"].append("ENTP")
    achievement_data["평균 점수"].append(91)
    achievement_data["성취 등급"].append("A+")
    achievement_data["특징"].append("비판적 사고와 뛰어난 언변으로 국어 토론에서 빛을 발합니다.")
elif selected_mbti == "ESTJ":
    achievement_data["MBTI 유형"].append("ESTJ")
    achievement_data["평균 점수"].append(80)
    achievement_data["성취 등급"].append("B+")
    achievement_data["특징"].append("체계적인 학습과 계획으로 목표 달성에 뛰어납니다.")
elif selected_mbti == "ESFJ":
    achievement_data["MBTI 유형"].append("ESFJ")
    achievement_data["평균 점수"].append(79)
    achievement_data["성취 등급"].append("B")
    achievement_data["특징"].append("협력 학습과 소통을 통해 국어 실력을 향상시킵니다.")
elif selected_mbti == "ENFJ":
    achievement_data["MBTI 유형"].append("ENFJ")
    achievement_data["평균 점수"].append(93)
    achievement_data["성취 등급"].append("A+")
    achievement_data["특징"].append("타인과의 공감 능력과 리더십으로 국어 학습을 이끌어갑니다.")
elif selected_mbti == "ENTJ":
    achievement_data["MBTI 유형"].append("ENTJ")
    achievement_data["평균 점수"].append(95)
    achievement_data["성취 등급"].append("A+")
    achievement_data["특징"].append("목표 지향적이고 추진력이 강해 국어 과목에서 최고의 성과를 냅니다.")

# 데이터프레임으로 변환
df = pd.DataFrame(achievement_data)

# 결과 표로 보여주기
st.table(df)

st.write("---")
st.info("ℹ️ 이 데이터는 실제 MBTI별 국어 성취도와는 무관한 **가상의 예시**입니다.")
st.write("더 궁금한 점이 있으시면 언제든지 질문해주세요! 😊")
