import streamlit as st
import pandas as pd
import marvin
from openai import OpenAI
import re

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

#Sidebar
with st.sidebar:
    st.logo("logos/logo-no-background.png")
    st.title("Built to classify 311 data")
    choice = st.radio("Agency", ["All","Streets Department","Philly311 Contact Center",])
    st.info("""This application was designed with the citizen and call center responder in mind. It allows while suggesting: 1. Agency Assignment and 2. Importance/Urgency""")


#Body of Webpage
#Data
data = pd.read_csv('311_limit_30_7-7-24.csv')


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
data = data.applymap(remove_emails)

st.write(choice)

'''st.write(
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

predicted_sentiments = []
for i in data['description']:
    predicted_sentiments.append(marvin.classify([i], labels=["very urgent and very important", "less urgent and very important", "less important and very urgent", "less urgent and less important"]))  

data['Classification'] = predicted_sentiments

#data['Classification_Number'] = classification_mapping[1]


#Timestamp
ts = pd.Timestamp(year = 2024,  month = 7, day = 15, 
                  hour = 10, second = 49, tz = 'US/Eastern')

st.info(ts)
st.write(data)

Streets_Department_Filter = ['Illegal Dumping (private)']

#Abandoned Automobile (private)


if choice == "All":
    pass

if choice == "Streets Department":
    #rslt_df = data['title'].isin(Streets_Department_Filter)
    #st.write(rslt_df)
    pass
    '''