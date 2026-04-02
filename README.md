# 🌍 World’s Happiness Prediction Project

This project analyzes the World Happiness dataset and builds machine learning models to predict the happiness score of countries based on socio-economic indicators.

The project also includes an interactive Streamlit dashboard for exploring global happiness data, comparing countries, and predicting happiness scores.
---
##  Working link:
**https://world-s-happiness-kzbfbqosd5ec7fwukk2g9d.streamlit.app/**

## 📸 App Screenshots

### Dashboard
![Dashboard](images/dashboard.png)

### Feature Importance
![Map](images/feature_imp.png)

### Country Comparison
![Comparison](images/comparison.png)

---

📊 Interactive Dashboard

• Global Happiness Map  
• Top 10 Happiest Countries Visualization  
• Feature Importance Analysis  

🤖 Machine Learning Prediction

• Predict happiness score using Linear Regression model  
• User-controlled sliders for socio-economic indicators  

🌍 Country Comparison

• Compare happiness scores of two countries  
• Interactive visual comparison  


---

## 📁 Project Structure

```
World-s-Happiness/
│
├── data/
│   └── (dataset files)
│
├── World_Happinesss.ipynb      # Jupyter notebook for analysis and model training
├── app.py                      # Streamlit
├── model.py                    # Model training and prediction code
├── linear_model.pkl            # Saved Linear Regression model
├── rf_model.pkl                # Saved Random Forest model
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```

---

## 📊 Dataset

Dataset: World Happiness Report from kaggle

Features used:
• Economy (GDP per Capita)
• Health (Life Expectancy)
• Freedom
• Trust (Government Corruption)
• Generosity
• Family
• Dystopia Residual

---
## ⚙️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib / Seaborn
- Streamlit
- Jupyter Notebook

---

## 🧠 Machine Learning Models

The following models are implemented:

1. **Linear Regression**
2. **Random Forest Regression**

Models are trained on the dataset and saved using **Pickle** for later predictions.

---

## 📈 Model Accuracy

You can update this section with your actual model results.

| Model | Accuracy / R² Score |
|------|----------------------|
| Linear Regression | **0.99** |
| Random Forest | **0.94** |

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/bhargavi-nakathe/World-s-Happiness.git
cd World-s-Happiness
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run the Streamlit

```bash
streamlit run app.py
```

## 📊 Exploratory Data Analysis

The notebook includes visualizations such as:

- Correlation heatmaps
- Feature importance plots
- Country happiness comparisons
- Distribution of happiness scores

---

## 🎯 Project Goals

- Understand global happiness trends
- Identify important factors affecting happiness
- Build predictive models
- Deploy a simple prediction interface

---

## 🤝 Contributing

Contributions are welcome.

If you'd like to improve the project:

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Open a pull request

---

## 👩‍💻 Author

**Bhargavi Nakathe**

GitHub:  
https://github.com/bhargavi-nakathe

---

⭐ If you like this project, consider giving it a star on GitHub!
