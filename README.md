# 📊 Market Clustering AI

This project builds an AI agent that analyzes publicly traded companies based on financial indicators and automatically groups them into clusters using unsupervised learning (K-Means). It aims to help investors identify similar companies and understand market structures through data-driven insights.

---

## 🧠 Objective

To analyze companies and group them based on financial similarity and risk, using the following technologies:

- **Language**: Python
- **Libraries**: `yfinance`, `pandas`, `scikit-learn`, `matplotlib`, `seaborn`
- **Machine Learning**: K-Means (Unsupervised Learning)
- **Visualization**: PCA (Principal Component Analysis)

---

## 📥 Data Source

Company data is collected in real-time using the **Yahoo Finance API** (`yfinance`). Each company is represented by the following key financial indicators:

- `MarketCap` – Market Capitalization
- `Revenue` – Total Revenue
- `Profit` – Gross Profit
- `Debt` – Total Debt

---

## 📈 Clustering Approach

The model uses **K-Means Clustering** to group companies into 3 clusters based on the 4 financial indicators.  
Data is preprocessed using `StandardScaler`, and visualized using `PCA` for 2D representation.

Example output:  
<img src="pca-plot.png" width="600" alt="Cluster PCA Visualization">

---

## 📁 Project Structure

