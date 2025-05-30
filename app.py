# app.py

import streamlit as st
from main import run_agentic_gift_recommender

st.set_page_config(page_title="Agentic Gift Recommender")

st.title("🎁 Agentic Gift Recommender")
st.markdown("Describe a person, and we'll suggest a personalized gift idea with a link to buy it!")

# User input
person_info = st.text_area("🧍 Describe the person (e.g. age, interests, occasion):", height=150)

# Button
if st.button("✨ Generate Gift Idea"):
    if person_info.strip():
        with st.spinner("Thinking..."):
            result = run_agentic_gift_recommender(person_info)
        st.success("Gift idea ready!")

        st.markdown("### 🎁 Gift Idea & Pitch")
        st.write(result["gift_idea_and_pitch"])

        st.markdown("### 🔗 Product Link")
        st.markdown(f"[Buy it here]({result['product_link']})")
    else:
        st.warning("Please describe the person to get started.")
