import numpy as np
import pandas as pd
import streamlit as st
import nltk
nltk.download('vader_lexicon')
import contractions
import Relative
from nltk.sentiment.vader import SentimentIntensityAnalyzer


st.write("## Brand Avoidance Likelihood Estimator") 

Gender = st.selectbox('Consumer\'s gender:', ["Female", "Male","Unknown", "Unspecified"])
Relation = st.selectbox('Whether the consumer was the primary victim:', ["Yes", "No"])

user_input = st.text_input("The failure incident description:")


def Resp(T, G, R): 
    if G == "Female":
        GenderCoeff = 0
    elif G == "Male":
        GenderCoeff = .02
    elif G == "Unknown":
        GenderCoeff = .21
    else:
        GenderCoeff = .18
            
    if R == "Yes":
        RelationCoeff =  -.05
    else:
        RelationCoeff = 0

    TenseAndSent = Relative(text)

    Relative = TenseAndSent['

    Cop = .02

    Answer = (-.19 * Relative) + GenderCoeff + RelationCoeff + (.01 * Comp) + (1.14 * Cop) - 2.02

    Odds = np.exp(Answer)
    
    Prob = Odds/(1+Odds) 

    if T == "":
        Response = 0
    else:
        st.write("The odds of this consumer avoiding your brand in the future are:", round(Odds, 2))
        Response = round(Prob, 2) * 100
    return Response

Response = Resp(user_input, Gender, Relation)

st.write("The likelihood that this consumer avoids your brand in the future is:", Response, "%")
