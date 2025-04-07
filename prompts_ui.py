from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()  # Load environment variables from .env
model = ChatOpenAI()


st.header('Research Tool')


paper_input = st.selectbox('Select Reasearch Paper Name',["Generative AI for Visualization: State of the Art and Future Directions",
    "Investigating Explainability of Generative AI for Code through Scenario-based Design",
    "Fine-Grained Human Feedback Gives Better Rewards for Language Model Training",
    "Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding",
    "Generative AI At Work",
    "Improving Language Understanding by Generative Pre-Training",
    "Reinforcement Learning with Human Feedback: Learning Dynamic Choices via Pessimism",
    "A Neural Probabilistic Language Model",
    "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",
    "Training Language Models to Follow Instructions with Human Feedback"])

style_input = st.selectbox('Select Explanation Style', ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"])

length_input = st.selectbox('Select Length',['Short','Medium','Long'])

template = load_prompt(r'C:\Users\DELL\Desktop\LangChain\venv\template.json')


if st.button('summarize'):
    chain = template | model
    result = chain.invoke({
        'paper_input' : paper_input,
        'style_input' : style_input,
        'length_input' : length_input
    })

    st.write(result.content)



