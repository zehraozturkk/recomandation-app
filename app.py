import streamlit as st
import pandas as pd
from recomandation import (
    get_seasonal_recommendations,
    recommendation_asin,
    get_frequently_bought_together,
    get_popular_products_in_price_range,
    load_data, 
    preprocess_data
)  # Import all your recommendation functions

merged_df_clean = load_data()
x = preprocess_data(merged_df_clean)

# Load your data
df = pd.read_csv("merged_df_hendel.csv")

# Streamlit App Layout
st.title('Recommendation System Application')

# Creating Tabs
home_tab, category_tab, price_tab, season_tab, basket_tab, nothing_tab = st.tabs(["Homepage", "Category", "Price", "Season", "Basket", "Nothing"])

# For each tab, we'll implement the corresponding recommendation function
with home_tab:
    st.write("Welcome to the Recommendation System!")
    
with category_tab:
    asin_input = st.text_input('Enter ASIN for Category Recommendation:')
    if st.button('Show Category Recommendations'):
        if asin_input:
            recommendations = recommendation_asin(asin_input, x, merged_df_clean)
            if 'Error' in recommendations.columns:
                st.write(recommendations['Error'].iloc[0])
            else:
                st.write(recommendations)
        else:
            st.write("Please enter a valid ASIN.")

    # Kullanıcıdan ASIN girişi alma


with price_tab:
    price_range = st.selectbox('Select Price Range:', df['price_range'].unique())
    if st.button('Show Price Range Recommendations'):
        if price_range:
            recommendations = get_popular_products_in_price_range(price_range, df)
            st.write(recommendations)

with season_tab:
    season = st.selectbox('Select Season:', ['Winter', 'Spring', 'Summer', 'Fall'])
    if st.button('Show Seasonal Recommendations'):
        if season:
            recommendations = get_seasonal_recommendations(season, df)
            st.write(recommendations)

with basket_tab:
    order_id_input = st.text_input('Enter Order ID for Basket Recommendation:')
    if st.button('Show Basket Recommendations'):
        if order_id_input:
            related_products = get_related_products(order_id_input, df)
            st.write(f"Related Products: {related_products}")

# Add functionality to other tabs if needed

