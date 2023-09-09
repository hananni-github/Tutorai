# Bring in deps
import os
from gtts import gTTS
from tabnanny import verbose 
from apikey import apikey 
import streamlit as st 
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate 
from langchain.chains import LLMChain



os.environ['OPENAI_API_KEY'] = apikey

# App Freamwork 
st.title('🦜🔗 TutorAi')
Subject = st.sidebar.selectbox("Pick a subject of your Staduy", ("Physics", "Mathematics", "Biology", "Geography"))
prompt = st.text_input(" What you whant to learn")

# Prompt templates
title_template = PromptTemplate(
    input_variables = ['Subject'], 
    template='You are a professional tutor in {Subject} in arabic'
)

##LLM
llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True)

# Show stuff to the screen
if prompt:
    response = title_chain.run(Subject=prompt)
    st.write(response)
    
   
if prompt:
    # Create a gTTS object
    tts = gTTS(text=response, lang='ar')
   
    # Save the audio to a file
    tts.save("output_audio.mp3")

    # Play the audio (on systems with a compatible player)
    st.audio("output_audio.mp3", format="audio/mp3")
else:
    # Display a message if 'response' is empty
    st.write("No text to convert to audio.")
