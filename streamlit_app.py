import streamlit as st
from google import genai
from google.genai import types

### Load your API Key
try:
    gemini_api_key = st.secrets['MyGeminiKey']
except (KeyError, FileNotFoundError):
    st.error(
        "No Gemini key found. Add `MyGeminiKey` under "
        "**Manage app → ⋮ → Settings → Secrets**, then refresh this page."
    )
    st.stop()

client = genai.Client(api_key=gemini_api_key)

MODEL = "gemini-3.1-flash-lite"

st.write("Choose a color, then press the button to generate a poem.")

# Radio selection
color = st.radio(
    "Choose a color:",
    ["Red", "Blue", "Yellow"]
)

# Button
if st.button("Press me!"):
    prompt = f"""
    Write a short poem about the color {color}.
    The poem must be exactly 4 lines.
    Make it simple and creative.
    """

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    st.write(response.text)
