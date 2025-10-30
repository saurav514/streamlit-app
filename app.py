import streamlit as st

st.set_page_config(page_title="Which Saurabh Are You?")

st.title("🧠 Which Saurabh Are You?")
st.write("Answer the questions below to find out!")

questions = [
    {
        "q": "How do you spend your weekends?",
        "options": ["Chill at home", "Focus on goals", "Hang with friends", "Do creative projects"]
    },
    {
        "q": "What’s your go-to drink?",
        "options": ["Coffee", "Energy drink", "Juice", "Tea"]
    },
]

answers = []

for i, q in enumerate(questions):
    st.subheader(q["q"])
    answer = st.radio("Select one:", q["options"], key=i)
    answers.append(answer)

if st.button("Show My Result"):
    st.success("You’re the Creative Saurabh! 🎨 (or whatever logic you choose)")

