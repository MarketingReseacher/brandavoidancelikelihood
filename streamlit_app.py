import numpy as np
import pandas as pd
import streamlit as st
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

backgroundColor="#E1E1E1"
textColor="#1C1962"

st.header("Brand Avoidance Likelihood Estimator")

Gender = st.selectbox('Consumer\'s gender:', ["Female", "Male","Unknown", "Unspecified"])
Relation = st.selectbox('Whether the consumer was the primary victim:', ["Yes", "No"])

user_input = st.text_input("The failure incident description:")


def Resp(T, G, R): 
    if G == "Female":
        GenderCoeff = 0
    elif G == "Male":
        GenderCoeff = .01
    elif G == "Unknown":
        GenderCoeff = .20
    else:
        GenderCoeff = .16
            
    if R == "Yes":
        RelationCoeff =  -.06
    else:
        RelationCoeff = 0

    analyzer = SentimentIntensityAnalyzer()
    
    Neg = analyzer.polarity_scores(T).get('compound')

    Cop = .03

    Answer = (-5.6 * Neg) + GenderCoeff + RelationCoeff + (1.05 * Cop) - .08

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
