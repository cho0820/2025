import streamlit as st

# 페이지 설정 (기본값)
st.set_page_config(
    page_title="나만의 감정 다이어리", # ❤️ '나만의' 감정 다이어리!
    page_icon="💖",
    layout="centered"
)

# ⭐️ 제목과 인사말
st.title("💖 나만의 감정 다이어리 💖")
st.write("안녕! 😊 지금 어떤 감정을 느끼고 있는지 알려줄래?")

# ✍️ 사용자 감정 체크박스 선택받기
st.markdown("---") # 구분선 추가
st.subheader("지금 어떤 감정들을 느끼고 있니? 여러 개 선택해도 괜찮아! 🧐")

# 감정 리스트 정의 (체크박스로 보여줄 것들)
emotion_flags = {
    "슬픔/우울": False,
    "화남/짜증": False,
    "불안/걱정": False,
    "지루함/심심": False,
    "무기력함/늘어짐": False, # 새로 추가된 감정
    "설렘/기대": False,     # 새로 추가된 감정
    "피곤함/지침": False,   # 새로 추가된 감정
    "열등감/비교": False    # 새로 추가된 감정
}

# 체크박스 생성 및 선택 상태 저장
# `key`를 이용해서 Streamlit이 각 체크박스를 구분하게 해줘!
for emotion_text in emotion_flags.keys():
    emotion_flags[emotion_text] = st.checkbox(emotion_text, key=f"checkbox_{emotion_text.replace('/', '_')}")

# 선택된 감정이 있는지 확인하는 플래그
any_emotion_selected = False

st.markdown("---") # 구분선 추가

# 💡 감정 해소법 제안 로직
# 체크박스를 통해서 선택된 감정들을 하나씩 확인하고 해소법을 보여줄 거야!
if emotion_flags["슬픔/우울"]:
    any_emotion_selected = True
    st.subheader("💧 슬프거나 우울할 때 해소법이야! 🤗")
    st.info("따뜻한 위로와 격려가 필요해. 🫂")
    st.write("- **좋아하는 노래 들으며 마음껏 울기:** 감정을 표출하는 건 정말 중요해!")
    st.write("- **친한 사람에게 털어놓기:** 이야기하는 것만으로도 마음이 가벼워질 때가 많아.")
    st.write("- **따뜻한 차 마시며 쉬기:** 나만이 좋아하는 영화나 책을 보면서 잠시 현실에서 벗어나 봐.")
    st.write("- **일기 쓰기:** 감정을 글로 정리하면 생각도 정리되고 후련할 수 있어.")
    st.image("https://media.istockphoto.com/id/1417947367/ko/%EB%B2%A1%ED%84%B0/3d-%EC%98%90%EB%A1%9C%EC%9A%B0-%EC%8A%AC%ED%94%88-%EC%9A%B8%EC%9D%8C-%EC%9D%B4%EB%AA%A8%ED%8B%B0%EC%BD%98-%EC%A0%88%EC%97%B0.jpg?s=612x612&w=0&k=20&c=1VdCrOhGpoP6h_Q7ndEozZNNUY69u_lJO6iIbGDFxx4=", width=400)
    st.markdown("---") # 감정별 해소법 뒤에 구분선 추가

if emotion_flags["화남/짜증"]:
    any_emotion_selected = True
    st.subheader("😡 화나거나 짜증 날 때 해소법이야! 💥")
    st.info("에너지를 건강하게 풀어주는 게 중요해! 💥")
    st.write("- **신나는 음악 틀고 몸 움직이기:** 춤을 추거나 산책을 하면서 에너지를 발산해봐!")
    st.write("- **심호흡 크게 여러 번 하기:** 숨을 깊게 들이쉬고 천천히 내쉬면서 마음을 가라앉혀봐.")
    st.write("- **베개나 이불 때리기:** 안전하게 화를 푸는 방법도 있어!")
    st.write("- **잠시 상황에서 벗어나기:** 잠깐 다른 일에 집중하거나 자리를 피하는 것도 방법이야.")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRi1GssYS-_EIIigcUZVf7nYFTWTiPxJfijTA&s", width=400)
    st.markdown("---")

if emotion_flags["불안/걱정"]:
    any_emotion_selected = True
    st.subheader("😬 불안하거나 걱정될 때 해소법이야! 🧘‍♀️")
    st.info("마음을 차분하게 다스리는 연습을 해보는 게 좋아. 🧘‍♀️")
    st.write("- **명상이나 스트레칭 하기:** 마음을 편안하게 해주는 데 도움이 될 거야.")
    st.write("- **걱정 목록 작성하기:** 무엇이 불안한지 적어보고, 해결 가능한 것과 불가능한 것을 구분해봐.")
    st.write("- **긍정적인 상상하기:** 잘 될 거야! 하고 스스로에게 힘을 주는 상상을 해보는 건 어때?")
    st.write("- **따뜻한 물로 샤워하기:** 몸이 이완되면서 마음도 편안해질 수 있어.")
    st.image("https://www.k-health.com/news/photo/202209/61110_65169_118.jpg", width=400)
    st.markdown("---")

if emotion_flags["지루함/심심"]:
    any_emotion_selected = True
    st.subheader("😴 지루하거나 심심할 때 해소법이야! 🧐")
    st.info("새로운 자극을 주는 게 좋아! 🧐")
    st.write("- **새로운 취미 찾기:** 평소 관심 있었던 것을 찾아보고 시도해봐.")
    st.write("- **가볍게 산책하기:** 밖으로 나가 신선한 공기를 마시면 기분이 전환될 거야.")
    st.write("- **친구랑 수다 떨기:** 재밌는 이야기를 나누면서 활력을 얻어봐.")
    st.write("- **영상 만들기:** 쇼츠나 릴스 같은 나만의 영상을 만들어 보는 건 어때? 생각보다 재미있어!")
    st.image("https://blog.speak.com/wp-content/uploads/2022/08/%E1%84%8C%E1%85%B5%E1%84%85%E1%85%AE%E1%84%92%E1%85%A2-%E1%84%8B%E1%85%A7%E1%86%BC%E1%84%8B%E1%85%A5%E1%84%85%E1%85%A9-boring-bored.jpg", width=400)
    st.markdown("---")

if emotion_flags["무기력함/늘어짐"]:
    any_emotion_selected = True
    st.subheader("💤 무기력하거나 늘어질 때 해소법이야! 😴")
    st.info("아주 작은 것부터 시작해 보는 게 좋아! 😴")
    st.write("- **작은 성공 경험 만들기:** '양치하기', '물 한 잔 마시기' 등 아주 사소한 목표라도 달성해 봐.")
    st.write("- **환경 변화 주기:** 하던 자리에서 잠시 일어나 다른 공간으로 이동해 보거나, 창문을 열어 환기해 봐.")
    st.write("- **아무 생각 없이 멍 때리기:** '내가 왜 이렇지?' 하고 자책하기보다, 그냥 잠시 아무것도 안 해봐.")
    st.write("- **가볍게 몸 움직이기:** 좋아하는 노래를 틀어놓고 제자리 걷기 5분이라도 시도해 봐!")
    st.image("https://d2m9duoqjhyhsq.cloudfront.net/marketingContents/article/article485-03.jpg", width=400)
    st.markdown("---")

if emotion_flags["설렘/기대"]:
    any_emotion_selected = True
    st.subheader("💖 설레거나 기대될 때 즐기는 방법이야! 🤩")
    st.info("그 행복한 감정을 마음껏 즐기고 에너지를 발산해봐! 🤩")
    st.write("- **그 감정 마음껏 즐기기:** 이 순간을 사진이나 영상으로 기록하고, 친구들에게 공유해 봐.")
    st.write("- **구체적인 계획 세우기:** 설레는 이벤트가 있다면 세부 계획을 세워 더 깊이 몰입해 봐.")
    st.write("- **긍정적인 에너지 활용하기:** 이 좋은 기운으로 평소 미뤄왔던 일을 해보는 건 어때?")
    st.write("- **나만의 방식으로 표현하기:** 그림을 그리거나, 시를 쓰는 등 설렘을 표현하는 활동을 해 봐.")
    st.image("https://i.pinimg.com/736x/26/c7/81/26c7810ae93a44ebd5152640fa088f80.jpg", width=400) 
    st.markdown("---")

if emotion_flags["피곤함/지침"]:
    any_emotion_selected = True
    st.subheader("😩 피곤하거나 지쳐있을 때 해소법이야! 💤")
    st.info("충분한 휴식이 가장 중요해! 💤 **특히 학교에서 할 수 있는 방법들도 알려줄게!**")
    st.write("- **짧은 낮잠 자기:** 쉬는 시간이나 점심시간에 책상에 엎드려서 10~20분이라도 짧게 자 봐! 의외로 효과가 좋아.")
    st.write("- **복도 산책하기:** 점심시간에 밥 먹고 친구랑 복도 한 바퀴 돌거나, 매점 가는 길에 기지개 한번 켜보는 거야.")
    st.write("- **눈 운동하기:** 먼 곳과 가까운 곳을 번갈아 보거나, 눈 감고 손바닥으로 눈을 살짝 덮어 쉬게 해줘.")
    st.write("- **스트레칭 하기:** 의자에 앉아서 어깨를 뒤로 돌리거나, 목을 좌우로 쭉 늘려주는 간단한 스트레칭만 해도 피로가 좀 풀릴 거야.")
    st.write("- **시원한 물 마시기:** 졸음이 올 땐 시원한 물 한 잔이 도움이 돼!")
    st.image("https://image.dongascience.com/Photo/2019/01/ad5119d6bb549a9ed9e3a897f91eb527.jpg", width=400)
    st.markdown("---")

if emotion_flags["열등감/비교"]:
    any_emotion_selected = True
    st.subheader("😒 열등감이 느껴지거나 남과 비교될 때 해소법이야! ✨")
    st.info("남과의 비교보다는 나 자신에게 집중하는 게 중요해. ✨")
    st.write("- **나만의 장점 찾기:** 종이에 나의 좋은 점이나 잘하는 점을 5가지 이상 적어봐.")
    st.write("- **SNS 잠시 멀리하기:** 다른 사람의 완벽해 보이는 모습은 잠시 잊고, 나 자신을 돌보는 시간을 가져.")
    st.write("- **긍정적인 자기 암시:** 거울을 보며 '나는 소중한 존재야', '나는 충분히 잘하고 있어'라고 말해줘.")
    st.write("- **나만의 속도에 집중하기:** 남들과 비교하지 말고, 어제보다 더 나은 오늘을 만들려고 노력해 봐.")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSCQRakKTnq9A5O-PUjoYcgKYovQZFgH1XwsQ&s", width=400)
    st.markdown("---")

# 아무 감정도 선택되지 않았을 때 일반적인 조언 표시
if not any_emotion_selected:
    st.warning("아직 어떤 감정도 선택하지 않았어! 😅")
    st.write("혹시 지금 느끼는 감정이 위에 없거나, 어떤 감정을 선택해야 할지 모르겠다면...")
    st.write("어떤 감정이든 소중한 나만의 마음이야! 이럴 땐 다음 방법들을 시도해 보는 건 어때? ✨")
    st.write("- **맛있는 거 먹기:** 나만이 좋아하는 음식 먹으면서 기분 전환하기!")
    st.write("- **낮잠 자기:** 충분한 휴식은 마음을 편안하게 해줘.")
    st.write("- **셀프 칭찬하기:** '오늘도 수고했어!' 하면서 스스로를 안아줘! 넌 최고! 👍")
    st.write("- **좋아하는 드라마나 유튜브 보기:** 가볍게 즐길 수 있는 콘텐츠로 스트레스 풀기!")
    st.image("https://media.giphy.com/media/v1.giphy.com/media/M9wQYjMv13G8Lw3LzP/giphy.gif", caption="넌 최고! 👍", width=400)
    st.markdown("---")


st.markdown("##### 감정 해소법이 궁금할 때 언제든지 찾아와!")
