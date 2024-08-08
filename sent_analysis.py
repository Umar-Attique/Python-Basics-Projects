import openai
import streamlit as st
from pathlib import Path
import configparser
openai.api_key='Enter the api key'
def sentiment_analysis(text):
    message = [
        {"role" : "system", "content" : """You are trained to analyze and detect the sentiment of given text.
                                            If you are unsure of answer you can say 'Sorry not sure' and recommend user to review manualy"""},
        {"role" : "user", "content" : """Analyze the following text and determine if the sentiment is : positive or negative.
                                        Return answer in a single word as either positive or negative:{text}"""}                                    
    ]
    response = openai.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages = message,
        max_tokens=1,
        n=1,
        stop=None,
        temperature=0.1
    )
    sentiment = response.choices[0].delta.content.lower()
    response=f"Oh,  {sentiment.lower()}."

    if sentiment == 'positive':
        # Generate improvement suggestions
        improvement_prompt=f"That's Great! sentiment is positive. Here are some suggestions for improvement."
        improvement_response=generate_suggestions(improvement_prompt)
        response += f"That's Great! sentiment is positive. {improvement_response}"
    else:
        # Generate avoidance suggestions
        avoidance_prompt=f"The sentiment is negative.How can this be avoided?"
        avoidance_response=generate_suggestions(improvement_prompt)
        response += f"That's Terrible! sentiment is negative. {avoidance_response}"
    return response
def generate_suggestions(prompt):
    # Create a new message for suggestion generation
    suggestion_message = [
        {"role" : "system", "content": prompt}
    ]
    openai.api_key='Enter your api key'
    suggestion_response = openai.chat.completions.create(
        model='gpt-3.5-terbo',
        messages=suggestion_message,
        max_tokens=100,
        n=100,
        stop=None,
        temperature=0.1
    )
    suggestion=suggestion_response.choices[0].delta.contetn.lower.strip()[:100]
    return f"Here's asuggestion: {suggestion}" 

string="I am a very happy person."
sentiment_analysis(string)
    

st.title('Sentimental Analyzer')
model ='gpt-3.5-turbo'
text = st.text_input("Enter the prompt here : ", "I love to read AI books.")
if st.button('Submit'):
    with st.spinner('Your prompt is under progressing'):
        sentiment = sentiment_analysis(text)
        st.success('OpenAI processing completed')

    st.write(f"Sentiment: {sentiment}")
        # Display the senti,ent to user