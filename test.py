import streamlit as st

# 페이지 설정 (기본값)
st.set_page_config(
    page_title="나만의 감정 다이어리", # ❤️ '나만의' 감정 다이어리!
    page_icon="💖",
    layout="centered"
)

# ⭐️ 제목과 인사말
st.title("💖 나만의 감정 다이어리 💖")
st.write("안녕! 😊 지금 어떤 감정을 느끼고 있는지 알려줄래?") # ✨ 영철이 이름 대신 안녕!
st.write("내가 네 마음을 다독여 줄 수 있는 방법을 찾아볼게!✨") # 🌟 '네 마음'으로 변경

# ✍️ 사용자 감정 입력받기
user_emotion = st.text_input("지금 어떤 감정을 느끼고 있니?", placeholder="예: 슬픔, 화남, 불안, 짜증, 지루함 등")

# 💡 감정 해소법 제안 로직
if user_emotion: # 사용자가 뭔가 입력했을 때만 작동!
    st.markdown(f"---") # 구분선 추가

    st.subheader(f"나만이 느끼는 '{user_emotion}'에 대한 해소법이야! 🤗") # ✨ '나만이' 느끼는!

    # 다양한 감정에 따른 맞춤 해소법
    if "슬픔" in user_emotion or "우울" in user_emotion:
        st.info("슬프거나 우울할 땐 따뜻한 위로와 격려가 필요해. 🫂")
        st.write("- **좋아하는 노래 들으며 마음껏 울기:** 감정을 표출하는 건 정말 중요해!")
        st.write("- **친한 사람에게 털어놓기:** 이야기하는 것만으로도 마음이 가벼워질 때가 많아.")
        st.write("- **따뜻한 차 마시며 쉬기:** 나만이 좋아하는 영화나 책을 보면서 잠시 현실에서 벗어나 봐.") # 🌟 '나만이' 좋아하는
        st.write("- **일기 쓰기:** 감정을 글로 정리하면 생각도 정리되고 후련할 수 있어.")
        st.image("https://media.giphy.com/media/efg1o9YpI551XgK5N6/giphy.gif", caption="토닥토닥 괜찮아 💖", width=200) # 귀여운 GIF 추가!
    elif "화남" in user_emotion or "짜증" in user_emotion:
        st.info("화가 나거나 짜증 날 땐 에너지를 건강하게 풀어주는 게 중요해! 💥")
        st.write("- **신나는 음악 틀고 몸 움직이기:** 춤을 추거나 산책을 하면서 에너지를 발산해봐!")
        st.write("- **심호흡 크게 여러 번 하기:** 숨을 깊게 들이쉬고 천천히 내쉬면서 마음을 가라앉혀봐.")
        st.write("- **베개나 이불 때리기:** 안전하게 화를 푸는 방법도 있어!")
        st.write("- **잠시 상황에서 벗어나기:** 잠깐 다른 일에 집중하거나 자리를 피하는 것도 방법이야.")
        st.image("https://media.giphy.com/media/zP780Q6tY7tN0u4B6d/giphy.gif", caption="후~ 크게 숨 쉬자! 😤", width=200)
    elif "불안" in user_emotion or "걱정" in user_emotion:
        st.info("불안하고 걱정될 때는 마음을 차분하게 다스리는 연습을 해보는 게 좋아. 🧘‍♀️")
        st.write("- **명상이나 스트레칭 하기:** 마음을 편안하게 해주는 데 도움이 될 거야.")
        st.write("- **걱정 목록 작성하기:** 무엇이 불안한지 적어보고, 해결 가능한 것과 불가능한 것을 구분해봐.")
        st.write("- **긍정적인 상상하기:** 잘 될 거야! 하고 스스로에게 힘을 주는 상상을 해보는 건 어때?")
        st.write("- **따뜻한 물로 샤워하기:** 몸이 이완되면서 마음도 편안해질 수 있어.")
        st.image("https://media.giphy.com/media/zNn9q8uI6B8v2uI6d/giphy.gif", caption="차분하게 숨쉬기 😌", width=200) # 이미지 링크 수정!
    elif "지루함" in user_emotion or "심심" in user_emotion:
        st.info("지루하거나 심심할 때는 새로운 자극을 주는 게 좋아! 🧐")
        st.write("- **새로운 취미 찾기:** 평소 관심 있었던 것을 찾아보고 시도해봐.")
        st.write("- **가볍게 산책하기:** 밖으로 나가 신선한 공기를 마시면 기분이 전환될 거야.")
        st.write("- **친구랑 수다 떨기:** 재밌는 이야기를 나누면서 활력을 얻어봐.")
        st.write("- **영상 만들기:** 쇼츠나 릴스 같은 나만의 영상을 만들어 보는 건 어때? 생각보다 재미있어!") # 🌟 '나만의' 영상
        st.image("https://media.giphy.com/media/vK8vJ8p6jP1QdYtY7P/giphy.gif", caption="새로운 것 찾기! 🥳", width=200)
    else:
        st.warning("음... 어떤 감정인지 정확히는 모르겠지만... 😅")
        st.write("어떤 감정이든 소중한 나만의 마음이야! 이럴 땐 다음 방법들을 시도해 보는 건 어때? ✨") # ✨ '나만의' 마음!
        st.write("- **맛있는 거 먹기:** 나만이 좋아하는 음식 먹으면서 기분 전환하기!") # 🌟 '나만이' 좋아하는
        st.write("- **낮잠 자기:** 충분한 휴식은 마음을 편안하게 해줘.")
        st.write("- **셀프 칭찬하기:** '오늘도 수고했어!' 하면서 스스로를 안아줘! 넌 최고! 👍") # 🌟 '넌 최고!'로 변경
        st.write("- **좋아하는 드라마나 유튜브 보기:** 가볍게 즐길 수 있는 콘텐츠로 스트레스 풀기!")
        st.image("https://media.giphy.com/media/v1.giphy.com/media/M9wQYjMv13G8Lw3LzP/giphy.gif", caption="넌 최고! 👍", width=200) # 캡션도 변경!

  
    st.markdown("##### 혹시 다른 감정에도 추가하고 싶은 해소법이 있다면 언제든지 말해줘! 같이 발전시켜나가자! 💪")
