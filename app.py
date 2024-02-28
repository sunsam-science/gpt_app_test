import streamlit as st
from openai import OpenAI

client = OpenAI(
    api_key = st.secrets["API_KEY"]
)

st.title("그려달라는거 대충말하면 대충 그려주는 사이트 ver1.1.")

with st.form("form"):
    user_input = st.text_input("당신이 생성하고 싶은 이미지를 대충 적어ㅗㅅㅔ요")
    submit = st.form_submit_button("옛다!")

if submit and user_input:
    # st.write(user_input)
    gpt_prompt = [{
        "role" : "system",
        "content" : "If Korean, translate to English; if English, proceed. Briefly imagine detailed appearance. Respond concisely in around 20 words."
    }]

    gpt_prompt.append({
        "role" : "user",
        "content" : user_input
    })

    with st.spinner("기깔나게 작성중.."):
        gpt_response = client.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages  = gpt_prompt
        )

    prompt = gpt_response.choices[0].message.content.strip()
    st.header('당신이 원한게 이런 것입니까 Human? :sunglasses:', divider='rainbow')
    st.write(prompt)

    with st.spinner("일단 그리라니까 그려보는중.."):
        dalle_response = client.images.generate(
            prompt = prompt,
            size="256x256"
        )

    st.image(dalle_response.data[0].url)
