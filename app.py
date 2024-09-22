import streamlit as st
import pandas as pd
import marvin
from openai import OpenAI
import re

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

marvin.settings.openai.api_key = st.secrets["OPENAI_API_KEY"]

#Page Config
st.set_page_config(layout="wide")

#Body of Webpage
#Data
@st.cache_data()
def load_data():
    data = pd.read_csv('311_limit_30_7-7-24.csv')
    return data

data = load_data()
# Cleaning up dataframe
data = data.drop(columns=['web-scraper-order', 'web-scraper-start-url'])

# Define a function to remove emails
def remove_emails(text):
    if isinstance(text, str):
        # Regex pattern to identify email addresses
        email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
        return re.sub(email_pattern, '', text)
    return text

# Apply the function across all columns in the DataFrame
data = data.map(remove_emails)



#Sidebar
with st.sidebar:
    st.logo("logos/logo-no-background.png")
    st.title("Streamlining Neighbors' Voices")
    with st.expander("How to Use"):
            st.write("""1. Choose desired filters  
    2. Click Classification Column Header to sort by top issues""")  
    issue_title = st.selectbox(label='Select an Issue Type:', index=None, options=data['title'].unique())
    st.write("""This application was designed with the citizen and call center responder in mind. It has two key insights for action:  
             1. Agency Assignment    
            2. Importance/Urgency Matrix Ranking""")

agency_to_issue = {
    "Streets Department" : ["Illegal Dumping (private)"]
}


st.header(
    """
Explore how ML can help classify 311 complaints 
"""
)


# Define a mapping from classification text to integer
classification_mapping = {
    "Very Urgent and Very Important": 1,
    "Less Urgent and Very Important": 2,
    "Less Important and Very Urgent": 3,
    "Less Urgent and Less Important": 4
}


description_list = data['description']

#predicted_sentiments = []
#for i in data['description']:
#    predicted_sentiments.append(marvin.classify([i], labels=["very urgent and very important", "less urgent and very important", "less important and very urgent", "less urgent and less important"]))  

#data['Classification'] = predicted_sentiments

#data['Classification_Number'] = classification_mapping[1]


#Timestamp
ts = pd.Timestamp(year = 2024,  month = 7, day = 15, 
                  hour = 10, second = 49, tz = 'US/Eastern')

st.info(f'Last Updated: [{ts}]')


Streets_Department_Filter = ["Illegal Dumping (private)"]


#Issue filtering
if issue_title == "Illegal Dumping (private)":
            st.caption(f'Filtering by Issue Type: :green[{issue_title}]')
            data = data[data['title'] == issue_title]

if issue_title == "Abandoned Automobile (private)":
            st.caption(f'Filtering by Issue Type: :green[{issue_title}]')
            data = data[data['title'] == issue_title]

if issue_title == "Traffic Sign Complaint (private)":
            st.caption(f'Filtering by Issue Type: :green[{issue_title}]')
            data = data[data['title'] == issue_title]

if issue_title == "Construction Complaint (private)":
            st.caption(f'Filtering by Issue Type: :green[{issue_title}]')
            data = data[data['title'] == issue_title]


#st.dataframe(data)

st.write(f"Data Source: https://iframe.publicstuff.com/#?client_id=242")