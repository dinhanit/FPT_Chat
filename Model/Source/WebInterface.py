import streamlit as st
from SetModel import Model
from VniAcronym import Acronym
import streamlit as st
import pandas as pd
import altair as alt

@st.cache_data()
def get_acronym_instance():
    return Acronym()

@st.cache_data()
def get_model_instance():
    return Model('fine_tuned_model')

# Get the instances of Acronym and Model
A = get_acronym_instance()
M = get_model_instance()

st.title("FeedBack")
input_text = st.text_input("Enter your question", key="user_input")
input_text = A.Solve_Acr(input_text)
label, cof = M.Predict(input_text)
with open("HisFeedBack/"+label+'.txt','a',encoding = 'utf8') as f:
    f.write(input_text+'\n')
st.write("Your FeedBack: ",input_text)
st.write("Category: ",label)


with open("HisFeedBack/Positive.txt",'r',encoding = 'utf8') as f:
    num_pos = len(f.readlines())
with open("HisFeedBack/Negative.txt",'r',encoding = 'utf8') as f:
    num_neg = len(f.readlines())
# Sample data
data = {
    'Category': ['Positive', 'Negative'],
    'Values': [num_pos, num_neg]
}

df = pd.DataFrame(data)

# Create the bar chart using Altair
chart = alt.Chart(df).mark_bar().encode(
    x=alt.X('Category', axis=alt.Axis(title='')),
    y=alt.Y('Values', axis=alt.Axis(title=''))
).properties(
    width=100,
    height=400
)

st.altair_chart(chart, use_container_width=True)


