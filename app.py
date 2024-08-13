import streamlit as st
from recomandation import get_seasonal_recommendations  # Fonksiyonlarınızı buradan içe aktarın

st.title('Öneri Sistemi Uygulaması')

user_input = st.text_input('Bir ürün girin:')

if user_input:
    # Fonksiyonu çağırarak önerileri alın
    recommendations = get_seasonal_recommendations('Summer', df)
    st.write('Önerilen ürünler:')
    for rec in recommendations:
        st.write(rec)
