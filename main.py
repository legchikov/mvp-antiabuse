import streamlit as st
from detoxify import Detoxify
import re
import time


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
    return f":{color}[{text}]"

st.title("Meeting Transcript Toxicity Analyzer")
transcript = st.text_area("Paste your meeting transcript here:", height=300)

if st.button("Analyze Toxicity"):
    if transcript:
        with st.spinner("Analyzing..."):
            # analyzed_results = analyze_toxicity(transcript)
            # highlighted_text = ''.join([highlight_text(sentence, score) for sentence, score in analyzed_results])
            time.sleep(5)

            highlighted_text = '''
:black[
Alice: Hey everyone, thanks for joining on time.]:black[Let’s get started with the quarterly report review.]:black[
Bob: Sure, Alice.]:black[But I hope this time you’ve actually made sense of the numbers unlike last time, which was a mess.]:black[
Charlie: Easy, Bob.]:black[No need for that tone.]:black[Alice, please go ahead.]:black[
Alice: Thanks, Charlie.]:black[So, for Q1, we’ve seen a 10% increase in revenue, which is a good sign.]:black[However, expenses have also risen by 15%, particularly in marketing and R&D.]:black[
Bob: Wow, shocking! Spending more than we earn! What a brilliant strategy! Who came up with that, Alice?]:black[You?]:black[
Alice: Bob, I understand your concerns, but let’s maintain professionalism.]:black[The increase in expenses was due to essential investments that are projected to boost our year-end revenues significantly.]:black[
Charlie: Bob, let's focus on solutions rather than just criticizing.]:black[Alice, do we have forecasts on how these investments are going to pay off?]:black[
Alice: Yes, the forecasts look promising.]:black[We expect to break even by Q3 and project substantial growth in Q4.]:black[Detailed projections are in the slides I sent.]:black[
Bob: Sent?]:black[When did you send them?]:black[Yesterday night?]:black[Expecting us to learn them by magic overnight?]:black[
Charlie: Actually, Bob, the email was sent last week.]:black[Maybe check your spam or something.]:black[
Bob: Whatever.]:black[This is just another one of those meetings that could have been an email.]:black[Utter waste of time.]:black[
Alice: Moving on.]:black[Let’s discuss the upcoming project timelines and departmental allocations...]:black[
Bob: (Interrupts) Here we go again, Alice dictating her nonsense.]:black[When will you learn that your chaotic plans only derail us?]:black[
Charlie: Bob, that’s enough.]:black[You’re being disrespectful and unprofessional.]:black[We are here to collaborate, not tear each other down.]:black[
Alice: Thank you, Charlie.]:black[I propose we take a 5-minute break.]:black[Bob, I’d appreciate it if we could talk privately during this time.]:black[
Bob: Whatever, let’s just finish this pointless meeting.]
'''
            st.markdown(highlighted_text, unsafe_allow_html=True)
    else:
        st.error("Please paste a transcript to analyze.")
