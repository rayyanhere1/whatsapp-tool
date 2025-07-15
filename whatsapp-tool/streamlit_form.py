import streamlit as st
import requests

st.markdown("""
    <div style='background: linear-gradient(90deg, #f9e7fe 0%, #e0c3fc 100%); padding: 2.2rem 1.5rem 1.5rem 1.5rem; border-radius: 18px; box-shadow: 0 4px 24px 0 rgba(108,71,255,0.10); max-width: 520px; margin: 2.5rem auto 2rem auto;'>
        <h2 style='text-align: center; color: #a259c6; font-size: 2.5rem; font-weight: 800; letter-spacing: 1.5px; margin-bottom: 0.5rem; font-family: Segoe UI, sans-serif;'>
            💍 Rishta Finder Form
        </h2>
        <p style='text-align: center; color: #5a5a5a; font-size: 1.18rem; margin-bottom: 0; font-family: Segoe UI, sans-serif;'>
            Helping souls meet, one WhatsApp message at a time 😅
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    div.stButton > button {
        background: linear-gradient(90deg, #f472b6, #facc15);
        color: white;
        border: none;
        font-weight: bold;
        padding: 0.8rem 2.2rem;
        border-radius: 10px;
        font-size: 1.1rem;
        box-shadow: 0 2px 8px 0 rgba(244,114,182,0.10);
        transition: 0.3s;
        margin-top: 1rem;
    }
    div.stButton > button:hover {
        background: linear-gradient(90deg, #facc15, #f472b6);
        color: #fff;
        transform: scale(1.07);
        box-shadow: 0 4px 16px 0 rgba(244,114,182,0.18);
    }
    </style>
""", unsafe_allow_html=True)

name = st.text_input("👤 Name", placeholder="Enter your name")
age = st.text_input("🧓 Age", placeholder="Enter your age")
phone = st.text_input("📱 WhatsApp Number", placeholder="e.g. 3061234567")
gender = st.selectbox("🧑‍🤝‍🧑 Gender", ["Male", "Female"])
message = st.text_area("💬 Personal Message (optional)", placeholder="Any preferences or notes?", value="")

if st.button("✨ Send Rishta Message"):
    formatted_phone = "+92" + phone.lstrip("0") if not phone.startswith("+") else phone

    msg = (
        "Assalam u Alaikum! \n"
        "Dear user, I have found a suitable rishta for you. Here are the details:\n\n"
        "Name: Muhammad Rayyan\n"
        "Age: 16\n"
        "Education: matric in computer science (ongoing-still studying)\n"
        "Profession: Full stack developer\n"
        "Location: Karachi\n"
        "Hobbies: ['Coding', 'Cricket', 'Travelling']\n"
        "Marital Status: Single\n\n"
        "If you're interested, reply back and we will discuss further. ❤️"
    )

    INSTANCE_ID = st.secrets["INSTANCE_ID"]
    API_KEY = st.secrets["API_KEY"]

    url = f"https://api.ultramsg.com/{INSTANCE_ID}/messages/chat"
    payload = {
        "token": API_KEY,
        "to": formatted_phone,
        "body": msg
    }

    try:
        res = requests.post(url, data=payload)
        data = res.json()
        if data.get("sent") == "true" or data.get("message") == "ok":
            st.success("🎉 Rishta message sent on WhatsApp!")
        else:
            st.error(f"❌ Something went wrong: {data}")
    except Exception as e:
        st.error(f"⚠️ Error: {e}") 