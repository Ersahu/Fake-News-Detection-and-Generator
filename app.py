import streamlit as st
import joblib
import random

# Load model and vectorizer
vectorizer = joblib.load("vectorizer.jb")
model = joblib.load("lr_model.jb")

# Predefined fake news sentence patterns
fake_news_templates = [
    "BREAKING: {} has officially announced a shocking decision affecting millions!",
    "Shocking news! {} may soon become illegal according to leaked documents!",
    "A new report claims {} is causing serious long-term health issues.",
    "Experts warn that {} is being manipulated by the government!",
    "Social media is exploding after rumors that {} will be banned nationwide!"
]

topics = [
    "chocolate milk",
    "Instagram reels",
    "Tesla cars",
    "mobile phones",
    "street food",
    "AI robots",
    "college exams",
    "cricket teams",
    "celebrities",
    "pet dogs"
]


# UI
st.title("📰 Fake News System")
menu = st.radio("Choose an Option:", ("Generate Fake News" , "Detect Fake News"))

# ----------- Fake News Detection Feature -----------
if menu == "Detect Fake News":
    st.subheader("🔍 Fake News Detector")
    st.write("Enter a News Article below:")

    input_text = st.text_area("News Article:")

    if st.button("Check News"):
        if input_text.strip():
            transform_input = vectorizer.transform([input_text])
            prediction = model.predict(transform_input)

            if prediction[0] == 1:
                st.success("✔ The News is Real!")
            else:
                st.error("❌ The News is Fake!")
        else:
            st.warning("⚠ Please enter some text to analyze.")

# ----------- Fake News Generator Feature  -----------
elif menu == "Generate Fake News":
    import os
    os.environ["TRANSFORMERS_NO_TF"] = "1"
    from transformers import pipeline

    st.subheader("🤖 Fake News Generator")
    st.write("Click below to generate a realistic fake news paragraph.")

    @st.cache_resource
    def load_model():
        return pipeline(
            "text-generation",
            model="gpt2",
            device=-1  # CPU
        )

    generator = load_model()

    if st.button("Generate Fake News"):
        prompt = (
            "Breaking News: Today reports are coming in that "
            "a major unexpected event has occurred. According to early "
            "sources, "
        )

        result = generator(
            prompt,
            max_length=120,
            temperature=0.7,
            top_k=50,
            top_p=0.95,
            do_sample=True,
            repetition_penalty=1.2
        )

        generated_text = result[0]['generated_text']

        # Clean weird symbols or non-printable characters
        cleaned_text = "".join(ch for ch in generated_text if ch.isprintable())

        st.text_area("Generated Fake News:", cleaned_text, height=250)
