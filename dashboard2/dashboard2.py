import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Header for the app
st.header('Indian Stock Dashboard')

# Sidebar inputs for ticker and exchange
ticker = st.sidebar.text_input('Symbol Code', 'INFY')
exchange = st.sidebar.text_input('Exchange', 'NSE')

# Constructing the URL
url = f'https://www.google.com/finance/quote/{ticker}:{exchange}'

# Fetching the webpage
response = requests.get(url)

# Parsing the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Extracting data
try:
    # Attempt to find the price using the class
    price = float(soup.find(class_="rPF6Lc").text.strip()[1:].replace(",", ""))
   
    # Creating a dictionary for the data
    dict1 = {
        'Price': price,
    }
    
    # Creating a DataFrame
    df = pd.DataFrame(dict1, index=['Extract Data'])
    
    # Displaying the DataFrame in Streamlit
    st.write(df)

except AttributeError:
    st.error("Unable to fetch data. Please check the symbol code and exchange.")
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")