import streamlit as st
from detoxify import Detoxify
import re


# Load a toxicity detection model
def analyze_toxicity(text):
    """ Analyze the toxicity of each sentence in a given text. """
    results = []
    sentences = re.split(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", text)
    for i, sentence in enumerate(sentences):
        print(f'{i=}')
        if sentence.strip():
            result = Detoxify('original').predict(sentence)
            score = result['toxicity']
            results.append((sentence, score))

    return results

def highlight_text(text, score):
    """ Return HTML span with color based on toxicity score. """
    if score > 0.75:
        color = "red"
    elif score > 0.5:
        color = "orange"
    else:
        color = "black"
    return f"<span style='color: {color};'>{text}</span>"

st.title("Meeting Transcript Toxicity Analyzer")
transcript = st.text_area("Paste your meeting transcript here:", height=300)

if st.button("Analyze Toxicity"):
    if transcript:
        with st.spinner("Analyzing..."):
            analyzed_results = analyze_toxicity(transcript)
            highlighted_text = ''.join([highlight_text(sentence, score) for sentence, score in analyzed_results])
            st.markdown(highlighted_text, unsafe_allow_html=True)
    else:
        st.error("Please paste a transcript to analyze.")
