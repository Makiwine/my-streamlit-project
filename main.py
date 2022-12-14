import streamlit as st
import plotly_express as px
import pandas as pd
import altair as alt

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

st.title('COVID-19 DATASET DISPLAY :')
st.image('covid19.jpg')
st.markdown('Dataset :')
df = pd.read_csv('day_wise.csv')
df.drop(['Date'], axis=1, inplace=True)
st.write(df.head(20))


global numeric_columns
global non_numeric_columns
try:
    numeric_columns = list(df.select_dtypes(['float', 'int']).columns)
    non_numeric_columns = list(df.select_dtypes(['object']).columns)
    non_numeric_columns.append(None)
    print(non_numeric_columns)
except Exception as e:
    print(e)

st.title('Scatterplot')
x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
plot=alt.Chart(df).mark_circle().encode(x=x_values, y=y_values).interactive()
# display the char
st.altair_chart(plot,use_container_width=True)   


st.sidebar.subheader("Histogram Settings")
st.title('Histogram')
x = st.sidebar.selectbox('Select target column:', options=numeric_columns)
bin_size = st.sidebar.slider("Number of Bins", min_value=10,
                             max_value=100, value=40)
plot = px.histogram(x=x, data_frame=df)
st.plotly_chart(plot)


app_mode = st.sidebar.selectbox('Select Page',['Home']) #two pages

if app_mode=='Home':
    choises=st.selectbox('Which graphes you want to plot', ['','bar_chart', 'line_chart','area_chart','Boxplot'])
    if choises=='bar_chart':
        st.markdown('Covid desease dataset by country/region ')
        st.title('Bar chart of confirmed cases and Active cases')
        st.bar_chart(df[['Confirmed','Active']].head(20))
        st.title('Bar chart of confirmed cases and Deaths cases')
        st.bar_chart(df[['Confirmed','Deaths']].head(20))
        st.title('Bar chart of Deaths cases and Recovered one')
        st.bar_chart(df[['Deaths','Recovered']].head(20))
    elif choises=='line_chart':
        st.markdown('Covid desease dataset by country/region ')
        st.markdown('Lineplots')
        st.line_chart(df,width=1100, height=400)

    elif choises=='area_chart':
        
        st.markdown('Covid desease dataset by country/region ')
        st.write('This is a area_chart.')
        st.area_chart(df)
    elif choises=='Boxplot':
        st.markdown('Covid desease dataset by country/region ')
        st.markdown('Boxplot')
        plot = px.box(df)
        st.plotly_chart(plot)
