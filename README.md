# 🌍 World’s Happiness Prediction Project

This project analyzes and predicts global happiness scores using data from the World Happiness Report. It applies data analysis, visualization, and machine learning models to understand the factors influencing happiness across countries.

---

## 📌 Project Overview

The goal of this project is to explore the factors that contribute to happiness levels around the world and build machine learning models to predict happiness scores based on those factors.

The project includes:
- Data preprocessing and cleaning
- Exploratory Data Analysis (EDA)
- Data visualization
- Machine learning model training
- Model evaluation
- A simple Streamlit UI for predictions

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

The dataset is based on the **World Happiness Report**, which ranks countries based on happiness levels.

Typical features used in the dataset include:

- GDP per capita
- Social support
- Healthy life expectancy
- Freedom to make life choices
- Generosity
- Perceptions of corruption

These features are used to predict the **Happiness Score**.

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

##  Working link:
**https://world-s-happiness-kzbfbqosd5ec7fwukk2g9d.streamlit.app/**

## 👩‍💻 Author

**Bhargavi Nakathe**

GitHub:  
https://github.com/bhargavi-nakathe

---

⭐ If you like this project, consider giving it a star on GitHub!
