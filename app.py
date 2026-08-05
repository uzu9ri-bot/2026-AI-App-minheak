import streamlit as st
import google.generativeai as genai
from PIL import Image
import urllib.parse

# -----------------------------------
# 1. 기본 설정
# -----------------------------------

st.set_page_config(
    page_title="HealthyFood AI",
    page_icon="🥗",
    layout="centered"
)

st.title("🥗 HealthyFood AI")
st.write("음식 사진을 올리면 건강한 레시피를 추천합니다.")

# -----------------------------------
# 2. Gemini API 키
# -----------------------------------

GEMINI_API_KEY = "여기에_본인_API_KEY_입력"

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

# -----------------------------------
# 3. AI 분석 함수
# -----------------------------------

def analyze_food(image):

    prompt = """
당신은 영양사입니다.

다음 순서로 답해주세요.

1. 음식 이름

2. 건강에 좋지 않은 이유

3. 건강하게 바꾸는 방법

4. 추천 레시피

5. 간단한 조리법

답변은 한국어로 작성해주세요.
"""

    response = model.generate_content([prompt, image])

    return response.text


# -----------------------------------
# 4. 이미지 생성 함수
# -----------------------------------

def make_image(recipe):

    recipe = urllib.parse.quote(recipe)

    return f"https://image.pollinations.ai/prompt/{recipe}"


# -----------------------------------
# 5. 사진 업로드
# -----------------------------------

uploaded_file = st.file_uploader(

    "음식 사진을 선택하세요",

    type=["jpg", "jpeg", "png"]

)

# -----------------------------------
# 6. 분석 시작
# -----------------------------------

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(image, caption="업로드한 사진", width=300)

    if st.button("🍳 건강하게 바꾸기"):

        with st.spinner("AI가 분석중입니다..."):

            result = analyze_food(image)

        st.success("분석 완료!")

        st.subheader("📋 AI 분석 결과")

        st.write(result)

        # 이미지 생성용 이름
        recipe_name = "Healthy Food"

        image_url = make_image(recipe_name)

        st.subheader("🥗 건강한 음식 예시")

        st.image(image_url)

# -----------------------------------
# 7. 하단
# -----------------------------------

st.markdown("---")
st.caption("HealthyFood AI MVP")