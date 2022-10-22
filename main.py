import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
from sklearn import preprocessing
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

app_mode = st.sidebar.selectbox('Select Page',['Home']) #two pages

if app_mode=='Home':
    choises=st.selectbox('Which graphes you want to plot', ['hist', 'bar_chart', 'line_chart','area_chart','altair_chart'])
    if choises=='hist':
        st.title('COVID-19 DATASET DISPLAY :')
        st.image('covid19.jpg')
        st.markdown('Dataset :')
        df = pd.read_csv('day_wise.csv')
        df.drop(['Date'], axis=1, inplace=True)
        scaler = preprocessing.StandardScaler()
        scaler.fit(df)
        df_scale = scaler.transform(df)
        df = pd.DataFrame(df_scale, columns=['Confirmed', 'Deaths', 'Recovered', 'Active','New cases','New deaths','New recovered','Deaths / 100 Cases','Recovered / 100 Cases','Deaths / 100 Recovered','No. of countries'])
        st.write(df.head(20))
        st.markdown('Covid desease dataset by country/region ')
        fig,ax = plt.subplots()
        ax.hist(df, bins=15)
        st.pyplot(fig)
    elif choises=='bar_chart':
        st.title('COVID-19 DATASET DISPLAY :')
        st.image('covid19.jpg')
        st.markdown('Dataset :')
        df = pd.read_csv('covid_19_clean_complete.csv')
        df.drop(['Date'], axis=1, inplace=True)
        scaler = preprocessing.StandardScaler()
        scaler.fit(df)
        df_scale = scaler.transform(df)
        df = pd.DataFrame(df_scale, columns=['Confirmed', 'Deaths', 'Recovered', 'Active','New cases','New deaths','New recovered','Deaths / 100 Cases','Recovered / 100 Cases','Deaths / 100 Recovered','No. of countries'])
        st.write(df.head(20))
        st.markdown('Covid desease dataset by country/region ')
        st.bar_chart(df)
    elif choises=='line_chart':
        st.title('COVID-19 DATASET DISPLAY :')
        st.image('covid19.jpg')
        st.markdown('Dataset :')
        df = pd.read_csv('covid_19_clean_complete.csv')
        df.drop(['Date'], axis=1, inplace=True)
        scaler = preprocessing.StandardScaler()
        scaler.fit(df)
        df_scale = scaler.transform(df)
        df = pd.DataFrame(df_scale, columns=['Confirmed', 'Deaths', 'Recovered', 'Active','New cases','New deaths','New recovered','Deaths / 100 Cases','Recovered / 100 Cases','Deaths / 100 Recovered','No. of countries'])
        st.write(df.head(20))
        st.markdown('Covid desease dataset by country/region ')
        st.line_chart(df)
    elif choises=='area_chart':
        st.title('COVID-19 DATASET DISPLAY :')
        st.image('covid19.jpg')
        st.markdown('Dataset :')
        df = pd.read_csv('covid_19_clean_complete.csv')
        df.drop(['Date'], axis=1, inplace=True)
        scaler = preprocessing.StandardScaler()
        scaler.fit(df)
        df_scale = scaler.transform(df)
        df = pd.DataFrame(df_scale, columns=['Confirmed', 'Deaths', 'Recovered', 'Active','New cases','New deaths','New recovered','Deaths / 100 Cases','Recovered / 100 Cases','Deaths / 100 Recovered','No. of countries'])
        st.write(df.head(20))
        st.markdown('Covid desease dataset by country/region ')
        st.area_chart(df)
    else:
        st.title('COVID-19 DATASET DISPLAY :')
        st.image('covid19.jpg')
        st.markdown('Dataset :')
        df = pd.read_csv('covid_19_clean_complete.csv')
        df.drop(['Date'], axis=1, inplace=True)
        scaler = preprocessing.StandardScaler()
        scaler.fit(df)
        df_scale = scaler.transform(df)
        df = pd.DataFrame(df_scale, columns=['Confirmed', 'Deaths', 'Recovered', 'Active','New cases','New deaths','New recovered','Deaths / 100 Cases','Recovered / 100 Cases','Deaths / 100 Recovered','No. of countries'])
        st.write(df.head(20))
        st.markdown('Covid desease dataset by country/region ')
        c=alt.Chart(df).mark_point().encode(df)
        st.altair_chart(c, use_container_width=True)
