import streamlit as st
from detoxify import Detoxify
import re
import time


meeting_script = '''
Alice: Hey idiots, thanks for joining on time. Let’s get started with the quarterly report review.

Bob: Sure, Alice. But I hope this time you’ve actually made sense of the numbers unlike last time, which was a mess.

Charlie: Easy, Bob. No need for that tone. Alice, please go ahead.

Alice: Thanks, Charlie. So, for Q1, we’ve seen a 10% increase in revenue, which is a good sign. However, expenses have also risen by 15%, particularly in marketing and R&D.

Bob: Wow, shocking! Spending more than we earn! What a brilliant strategy! Who came up with that, Alice? You?

Alice: Bob, I understand your concerns, but let’s maintain professionalism. The increase in expenses was due to essential investments that are projected to boost our year-end revenues significantly.

Charlie: Fuck Bob, let's focus on solutions rather than just criticizing. Alice, do we have forecasts on how these investments are going to pay off?

Alice: Yes, the forecasts look promising. We expect to break even by Q3 and project substantial growth in Q4. Detailed projections are in the slides I sent.

Bob: Sent? When did you send them? Yesterday night? Expecting us to learn them by magic overnight?

Charlie: Actually, Bob, you are idiot! the email was sent last week. Maybe check your spam or something.

Bob: Whatever. This is just another one of those meetings that could have been an email. Utter waste of time.

Alice: Moving on. Let’s discuss the upcoming project timelines and departmental allocations...

Bob: (Interrupts) Here we go again, Alice dictating her nonsense. When will you learn that your chaotic plans only derail us?

Charlie: Bob, that’s enough. You’re being disrespectful and unprofessional. We are here to collaborate, not tear each other down.

Alice: Thank you, Charlie. I propose we take a 5-minute break. Bob, I’d appreciate it if we could talk privately during this time.

Bob: Whatever, let’s just finish this pointless meeting.
'''


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
transcript = st.text_area("Paste your meeting transcript here:", height=300, value=meeting_script)

if st.button("Analyze Toxicity"):
    if transcript:
        with st.spinner("Analyzing..."):
            # analyzed_results = analyze_toxicity(transcript)
            # highlighted_text = ''.join([highlight_text(sentence, score) for sentence, score in analyzed_results])
            time.sleep(5)

            highlighted_text = '''
:black[Alice: Hey everyone, thanks for joining on time.]  :{grey}[0.00]
:black[Let’s get started with the quarterly report review.]  :{grey}[0.00]
:black[Bob: Sure, Alice.]  :{grey}[0.00]
:black[But I hope this time you’ve actually made sense of the numbers unlike last time, which was a mess.]  :{grey}[0.00]
:black[Charlie: Easy, Bob.]  :{grey}[0.00]
:black[No need for that tone.]  :{grey}[0.00]
:black[Alice, please go ahead.]  :{grey}[0.00]
:black[Alice: Thanks, Charlie.]  :{grey}[0.00]
:black[So, for Q1, we’ve seen a 10% increase in revenue, which is a good sign.]  :{grey}[0.00]
:black[However, expenses have also risen by 15%, particularly in marketing and R&D.]  :{grey}[0.00]
:black[Bob: Wow, shocking! Spending more than we earn! What a brilliant strategy! Who came up with that, Alice?]  :{grey}[0.00]
:black[You?]  :{grey}[0.01]
:black[Alice: Bob, I understand your concerns, but let’s maintain professionalism.]  :{grey}[0.00]
:black[The increase in expenses was due to essential investments that are projected to boost our year-end revenues significantly.]  :{grey}[0.00]
**:red[Charlie: Fuck Bob, let's focus on solutions rather than just criticizing.]**  :{grey}0.99]
:black[Alice, do we have forecasts on how these investments are going to pay off?]  :{grey}[0.00]
:black[Alice: Yes, the forecasts look promising.]  :{grey}[0.00]
:black[We expect to break even by Q3 and project substantial growth in Q4.]  :{grey}[0.00]
:black[Detailed projections are in the slides I sent.]  :{grey}[0.00]
:black[Bob: Sent?]  :{grey}[0.00]
:black[When did you send them?]  :{grey}[0.00]
:black[Yesterday night?]  :{grey}[0.00]
:black[Expecting us to learn them by magic overnight?]  :{grey}[0.00]
**:red[Charlie: Actually, Bob, you are idiot! the email was sent last week.]**  :{grey}0.97]
:black[Maybe check your spam or something.]  :{grey}[0.00]
:black[Bob: Whatever.]  :{grey}[0.00]
:black[This is just another one of those meetings that could have been an email.]  :{grey}[0.00]
:black[Utter waste of time.]  :{grey}[0.15]
:black[Alice: Moving on.]  :{grey}[0.00]
:black[Let’s discuss the upcoming project timelines and departmental allocations...]  :{grey}[0.00]
:black[Bob: (Interrupts) Here we go again, Alice dictating her nonsense.]  :{grey}[0.11]
:black[When will you learn that your chaotic plans only derail us?]  :{grey}[0.00]
:black[Charlie: Bob, that’s enough.]  :{grey}[0.01]
:black[You’re being disrespectful and unprofessional.]  :{grey}[0.01]
:black[We are here to collaborate, not tear each other down.]  :{grey}[0.00]
:black[Alice: Thank you, Charlie.]  :{grey}[0.00]
:black[I propose we take a 5-minute break.]  :{grey}[0.00]
:black[Bob, I’d appreciate it if we could talk privately during this time.]  :{grey}[0.00]
:black[Bob: Whatever, let’s just finish this pointless meeting.]  :{grey}[0.04]
            
'''

            st.write(highlighted_text)
    else:
        st.error("Please paste a transcript to analyze.")
