import streamlit as st
import pandas as pd
import plotly.express as px
import joblib
import matplotlib.pyplot as plt

# ---------------------------
# Load dataset & models
# ---------------------------
df = pd.read_csv("data/world_happiness.csv")

lr_model = joblib.load("linear_model.pkl")
rf_model = joblib.load("rf_model.pkl")

features = ['Economy (GDP per Capita)','Health (Life Expectancy)',
            'Freedom','Trust (Government Corruption)',
            'Generosity','Family','Dystopia Residual']

# ---------------------------
# Sidebar Navigation
# ---------------------------
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["Dashboard", "Top 10 Happiest Countries",
                                   "Feature Importance", "Prediction"])

# ---------------------------
# Title
# ---------------------------
st.title("🌍 World Happiness Analysis & Prediction")
st.write("Interactive dashboard for analyzing global happiness data and predicting happiness scores.")

# ---------------------------
# Dashboard: Dataset Preview + Map
# ---------------------------
if menu == "Dashboard":
    st.subheader("📂 Dataset Preview")
    if st.checkbox("Show dataset"):
        st.dataframe(df)

    st.subheader("🌍 Global Happiness Map")
    fig_map = px.choropleth(
        df,
        locations="Country",
        locationmode="country names",
        color="Happiness Score",
        hover_name="Country",
        title="World Happiness Score"
    )
    st.plotly_chart(fig_map)

# ---------------------------
# Top 10 Happiest Countries
# ---------------------------
elif menu == "Top 10 Happiest Countries":
    st.subheader("🏆 Top 10 Happiest Countries")
    top10 = df.sort_values("Happiness Score", ascending=False).head(10)
    fig_top = px.bar(
        top10,
        x="Happiness Score",
        y="Country",
        orientation="h",
        color="Happiness Score",
        title="Top 10 Happiest Countries"
    )
    st.plotly_chart(fig_top)

# ---------------------------
# Feature Importance
# ---------------------------
elif menu == "Feature Importance":
    st.subheader("📊 Feature Importance")
    importance = rf_model.feature_importances_

    fig, ax = plt.subplots()
    pd.Series(importance, index=features).sort_values().plot(kind="barh", ax=ax)
    ax.set_title("Feature Importance (Random Forest)")
    st.pyplot(fig)

# ---------------------------
# Prediction Section
# ---------------------------
elif menu == "Prediction":
    st.subheader("🤖 Predict Happiness Score")

    economy = st.slider("Economy (GDP per Capita)", 0.0, 2.0, 1.0)
    health = st.slider("Health (Life Expectancy)", 0.0, 1.5, 0.8)
    freedom = st.slider("Freedom", 0.0, 1.0, 0.5)
    trust = st.slider("Trust (Government Corruption)", 0.0, 1.0, 0.1)
    generosity = st.slider("Generosity", 0.0, 1.0, 0.2)
    family = st.slider("Family", 0.0, 2.0, 1.0)
    dystopia = st.slider("Dystopia Residual", 0.0, 3.0, 1.5)

    if st.button("Predict Happiness Score", key="predict_happiness"):
        input_data = pd.DataFrame({
            'Economy (GDP per Capita)': [economy],
            'Health (Life Expectancy)': [health],
            'Freedom': [freedom],
            'Trust (Government Corruption)': [trust],
            'Generosity': [generosity],
            'Family': [family],
            'Dystopia Residual': [dystopia]
        })
        prediction = lr_model.predict(input_data)[0]
        st.success(f"Predicted Happiness Score: {prediction:.2f}")