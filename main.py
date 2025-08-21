import streamlit as st

# --- 1. 앱 설정 및 제목 ---
st.set_page_config(
    page_title="MBTI 기반 진로 탐색 도우미",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 MBTI와 함께하는 나의 진로 탐색")
st.write("나의 MBTI 유형을 통해 나에게 맞는 진로를 탐색하고, 잠재력을 발견해보세요!")
st.markdown("---")

# --- 2. MBTI 정보 데이터 ---
# 여기에 더 많은 MBTI 유형과 정보를 추가할 수 있습니다.
mbti_data = {
    "선택해주세요": {
        "description": "위 드롭다운 메뉴에서 당신의 MBTI 유형을 선택해주세요.",
        "careers": []
    },
    "ISTJ": {
        "description": "현실적이고 책임감이 강하며 체계적인 사람입니다. 사실에 기반한 논리적인 판단을 선호하며, 약속을 중요하게 여깁니다.",
        "careers": ["회계사", "경찰관", "행정직 공무원", "IT 관리자", "엔지니어"]
    },
    "ENFJ": {
        "description": "타인에게 깊은 관심을 가지고 협력과 조화를 추구하는 따뜻하고 통찰력 있는 사람입니다. 타인의 성장을 돕는 것을 좋아하며 리더십이 강합니다.",
        "careers": ["교사", "상담사", "인사 담당자", "사회복지사", "마케터", "코치"]
    },
    "INFP": {
        "description": "이상주의적이고 창의적이며 가치 중심적인 사람입니다. 내면의 가치를 중요하게 여기고 타인의 이해에 노력하며, 따뜻한 마음을 가지고 있습니다.",
        "careers": ["작가", "예술가", "심리학자", "상담사", "도서관 사서", "큐레이터", "번역가"]
    },
    "ESTP": {
        "description": "활동적이고 현실적이며 새로운 경험을 즐기는 사람입니다. 문제 해결 능력이 뛰어나고 즉흥적인 상황 대처에 능합니다.",
        "careers": ["경영자", "영업직", "스포츠 선수/코치", "경찰관/소방관", "엔터테이너"]
    },
    "INTJ": {
        "description": "독립적이고 전략적이며 논리적인 사람입니다. 복잡한 문제를 해결하는 데 능하며, 장기적인 비전을 가지고 계획을 세웁니다.",
        "careers": ["과학자", "연구원", "소프트웨어 개발자", "변호사", "컨설턴트", "투자 분석가"]
    },
    "ESFP": {
        "description": "사교적이고 활동적이며 사람들과 어울리는 것을 좋아하는 사람입니다. 현실에 충실하며 유머 감각이 뛰어나 분위기 메이커 역할을 합니다.",
        "careers": ["연예인", "이벤트 플래너", "유치원 교사", "서비스업 종사자", "미용사", "영업사원"]
    },
}

# --- 3. MBTI 유형 선택 UI ---
st.subheader("나의 MBTI 유형은?")
selected_mbti = st.selectbox(
    "아래 드롭다운에서 당신의 MBTI 유형을 선택해주세요:",
    list(mbti_data.keys()),
    index=0 # '선택해주세요'가 기본값으로 보이도록 설정
)

# --- 4. 결과 표시 ---
if selected_mbti != "선택해주세요":
    st.markdown("---")
    st.subheader(f"✨ 당신은 **{selected_mbti}** 유형이시군요!")

    # MBTI 유형 설명
    st.write("### 🔍 유형 설명")
    st.info(mbti_data[selected_mbti]["description"])

    # 추천 진로
    st.write("### 🚀 추천 진로 분야")
    if mbti_data[selected_mbti]["careers"]:
        for career in mbti_data[selected_mbti]["careers"]:
            st.markdown(f"- {career}")
    else:
        st.write("이 유형에 대한 추천 진로 정보가 아직 없습니다. (추가 예정!)")

    st.markdown("---")
    st.write("💡 이 정보는 MBTI를 통한 진로 탐색에 도움이 될 수 있으나, 개인의 진정한 흥미와 적성은 스스로의 탐색을 통해 발견하는 것이 가장 중요합니다.")

else:
    st.info("MBTI 유형을 선택하시면 해당 유형에 대한 설명과 추천 진로를 확인하실 수 있습니다.")

# --- 앱 실행 방법 안내 ---
st.sidebar.header("앱 실행 방법")
st.sidebar.write("1. 이 코드를 `mbti_career.py`와 같은 이름으로 저장하세요.")
st.sidebar.write("2. 터미널(명령 프롬프트)을 열고, 파일이 저장된 폴더로 이동합니다.")
st.sidebar.write("3. 다음 명령어를 입력하여 앱을 실행합니다:")
st.sidebar.code("streamlit run mbti_career.py")
st.sidebar.write("4. 웹 브라우저에서 앱이 실행된 것을 확인합니다.")
