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
    achievement_data["특징"].append("전략적 분석가")
    # 여기가 문제의 원인일 수 있는 부분으로 보입니다.
    # 긴 문자열은 삼중 따옴표 """ 로 감싸는 것이 안전합니다.
    achievement_data["설명"].append("논리적이고 분석적인 사고가 뛰어나 비문학 독해나 논리적 글쓰기에 탁월합니다. 문제를 해결하듯이 국어 시험에 접근하여 효율적인 학습 전략을 세우고 고득점을 달성합니다. 📈")
elif selected_mbti == "ISTP":
    achievement_data["MBTI 유형"].append("ISTP")
    achievement_data["평균 점수"].append(78)
    achievement_data["성취 등급"].append("B")
    achievement_data["특징"].append("실용적이고 문제 해결 지향")
    achievement_data["설명"].append("이론보다는 실제 적용에 흥미를 느끼는 경향이 있어, 문법 규칙이나 어휘를 실생활에 연결할 때 더 잘 이해합니다. 단답형 문제나 요약 등 실용적인 부분에 강할 수 있습니다. 🔨")
elif selected_mbti == "ISFP":
    achievement_data["MBTI 유형"].append("ISFP")
    achievement_data["평균 점수"].append(75)
    achievement_data["성취 등급"].append("B")
    achievement_data["특징"].append("예술적 감각, 자유로운 학습")
    achievement_data["설명"].append("예술적 감각과 감수성이 풍부하여 시나 소설 같은 문학 작품을 감성적으로 잘 받아들입니다. 다만, 틀에 박힌 학습이나 지루한 암기는 어려워할 수 있어 흥미를 유발하는 학습법이 필요합니다. 🎨")
elif selected_mbti == "INFP":
    achievement_data["MBTI 유형"].append("INFP")
    achievement_data["평균 점수"].append(88)
    achievement_data["성취 등급"].append("A")
    achievement_data["특징"].append("이상주의적, 감수성 풍부")
    achievement_data["설명"].append("따뜻한 마음과 상상력이 풍부하여 문학 작품의 메시지나 인물의 감정에 깊이 몰입합니다. 독서와 글쓰기를 통해 자신의 생각과 감정을 표현하는 데 재능이 있어 국어 실력 향상에 유리합니다. 💭")
elif selected_mbti == "INTP":
    achievement_data["MBTI 유형"].append("INTP")
    achievement_data["평균 점수"].append(89)
    achievement_data["성취 등급"].append("A")
    achievement_data["특징"].append("논리적 탐구자")
    achievement_data["설명"].append("지적 호기심이 많고 논리적 사고가 뛰어나 비문학 지문이나 복잡한 문장 구조를 분석하는 데 능합니다. 깊이 있는 이해를 추구하며, 모호한 개념을 명확히 하려는 경향이 있습니다. 🧠")
elif selected_mbti == "ESTP":
    achievement_data["MBTI 유형"].append("ESTP")
    achievement_data["평균 점수"].append(70)
    achievement_data["성취 등급"].append("C+")
    achievement_data["특징"].append("활동적이고 실용적")
    achievement_data["설명"].append("에너지가 넘치고 활동적이라 직접 경험하는 학습을 선호합니다. 토론이나 발표처럼 역동적인 활동에서 국어 실력을 발휘할 수 있습니다. 이론적인 암기보다는 실전에 강한 면모를 보입니다. 🏃‍♂️")
elif selected_mbti == "ESFP":
    achievement_data["MBTI 유형"].append("ESFP")
    achievement_data["평균 점수"].append(68)
    achievement_data["성취 등급"].append("C")
    achievement_data["특징"].append("사교적이고 즐거움 추구")
    achievement_data["설명"].append("사람들과 어울리며 배우는 것을 즐거워하고, 재미있는 활동을 통해 국어에 접근하는 것을 선호합니다. 지루한 암기는 어려워할 수 있지만, 흥미를 느끼는 분야의 독서나 글쓰기에는 몰입합니다. 🎉")
elif selected_mbti == "ENFP":
    achievement_data["MBTI 유형"].append("ENFP")
    achievement_data["평균 점수"].append(87)
    achievement_data["성취 등급"].append("A")
    achievement_data["특징"].append("열정적이고 창의적")
    achievement_data["설명"].append("새로운 아이디어를 탐색하고 다양한 가능성을 열어두는 것을 즐겨, 문학 작품의 다양한 해석이나 창의적 글쓰기에 강합니다. 토론이나 발표를 통해 자신의 생각을 자유롭게 표현합니다. ✨")
elif selected_mbti == "ENTP":
    achievement_data["MBTI 유형"].append("ENTP")
    achievement_data["평균 점수"].append(91)
    achievement_data["성취 등급"].append("A+")
    achievement_data["특징"].append("재치 있는 변론가")
    achievement_data["설명"].append("비판적 사고와 뛰어난 언변으로 국어 토론이나 논술에서 두각을 나타냅니다. 고정관념을 깨는 독특한 시각으로 작품을 분석하고, 복잡한 문제에 대한 논리적 해결책을 제시하는 데 능합니다. 🗣️")
elif selected_mbti == "ESTJ":
    achievement_data["MBTI 유형"].append("ESTJ")
    achievement_data["평균 점수"].append(80)
    achievement_data["성취 등급"].append("B+")
    achievement_data["특징"].append("실행력 강한 관리자")
    achievement_data["설명"].append("목표 지향적이고 체계적이며, 효율적인 학습 계획을 세워 국어 성적을 관리합니다. 명확하고 실용적인 정보를 선호하며, 규칙과 절차에 따라 문제 풀이에 접근하는 것을 잘합니다. 📊")
elif selected_mbti == "ESFJ":
    achievement_data["MBTI 유형"].append("ESFJ")
    achievement_data["평균 점수"].append(79)
    achievement_data["성취 등급"].append("B")
    achievement_data["특징"].append("친화적이고 협력적")
    achievement_data["설명"].append("사람들과의 소통을 중요하게 생각하며, 협력 학습이나 그룹 스터디를 통해 국어 실력을 향상시킵니다. 다른 사람들의 의견을 경청하고 공유하며 학습 동기를 얻는 경향이 있습니다. 🤝")
elif selected_mbti == "ENFJ":
    achievement_data["MBTI 유형"].append("ENFJ")
    achievement_data["평균 점수"].append(93)
    achievement_data["성취 등급"].append("A+")
    achievement_data["특징"].append("영감을 주는 리더")
    achievement_data["설명"].append("타인의 성장을 돕고 영감을 주는 것을 좋아하여, 국어 학습에서 친구들을 돕거나 그룹 활동을 주도하며 자신의 실력도 향상시킵니다. 공감 능력이 뛰어나 문학 작품을 깊이 이해하고 표현합니다. 🌟")
elif selected_mbti == "ENTJ":
    achievement_data["MBTI 유형"].append("ENTJ")
    achievement_data["평균 점수"].append(95)
    achievement_data["성취 등급"].append("A+")
    achievement_data["특징"].append("타고난 지휘관")
    achievement_data["설명"].append("목표를 설정하고 이를 달성하기 위해 강력한 추진력과 리더십을 발휘합니다. 국어 학습에서도 효율적인 전략을 세우고, 복잡한 문제를 해결하는 데 탁월한 능력을 보여줍니다. 👑")

# 데이터프레임으로 변환
df = pd.DataFrame(achievement_data)

# 결과 표로 보여주기
st.table(df)

st.write("---")
st.info("ℹ️ 위에 제시된 MBTI별 국어 성취도 점수, 등급 및 설명은 **가상의 예시**입니다. 실제 MBTI 유형과 국어 성취도 사이에 직접적인 인과관계가 있음을 나타내지 않습니다. 개인의 학습 능력과 성과는 다양한 요인에 의해 결정됩니다.")
st.write("더 궁금한 점이 있으시면 언제든지 질문해주세요! 😊")
