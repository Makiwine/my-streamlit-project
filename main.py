import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import altair as alt
import pickle  #to load a saved model
import base64  #to open .gif files in streamlit app
@st.cache(suppress_st_warning=True)
def get_fvalue(val):
    feature_dict = {"No":1,"Yes":2}
    for key,value in feature_dict.items():
        if val == key:
            return value

def get_value(val,my_dict):
    for key,value in my_dict.items():
        if val == key:
            return value
        
global numeric_columns
global non_numeric_columns
try:
    st.write(df)
    numeric_columns = list(df.select_dtypes(['float', 'int']).columns)
    non_numeric_columns = list(df.select_dtypes(['object']).columns)
    non_numeric_columns.append(None)
    print(non_numeric_columns)
except Exception as e:
    print(e)

def load_data():
    df=pd.read_csv("day_wise.csv")
    
    return df

app_mode = st.sidebar.selectbox('Select Page',['Home']) #two pages
st.sidebar.subheader("Histogram Settings")
st.markdown('Histogram')
x = st.sidebar.selectbox('Select target column:', options=numeric_columns)
bin_size = st.sidebar.slider("Number of Bins", min_value=10,max_value=100, value=40)
plot = px.histogram(x=x, data_frame=data)
st.plotly_chart(plot)
    
st.markdown('Scatterplot')
x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
plot=alt.Chart(data).mark_circle().encode(x=x_values, y=y_values).interactive()
# display the char
st.altair_chart(plot,use_container_width=True)
if app_mode=='Home':
    choises=st.selectbox('Which graphes you want to plot', ['line_chart','area_chart','Boxplot'])
    st.title('COVID-19 DATASET DISPLAY :')
    st.image('covid19.jpg')
    
    data = load_data()
    # st.write(data)
    df= data.drop(["Date"], axis=1,inplace =True)
    st.markdown("dataset:")
    st.write(data)
    if choises=='line_chart':
       st.markdown('Lineplots')
       st.line_chart(df,width=1100, height=400)

    elif choises=='area_chart':
        st.write('This is a area_chart.')
        st.area_chart(df)
    elif choises=='Boxplot':
        st.markdown('Boxplot')
        plot = px.box(df)
        st.plotly_chart(plot)
        
 
