import streamlit as st
import pandas as pd
from recomandation import get_seasonal_recommendations  # Fonksiyonlarınızı buradan içe aktarın

st.title('Öneri Sistemi Uygulaması')

user_input = st.text_input('Bir ürün girin:')

user_input = st.button('Önerileri Göster')

if user_input:
    # Fonksiyonu çağırarak önerileri alın
    df = pd.read_csv("orders_clean.csv")
    recommendations = get_seasonal_recommendations('Summer', df)
    st.write('Önerilen ürünler:')
    
    # Önerileri DataFrame olarak gösterin
    st.write(recommendations)
