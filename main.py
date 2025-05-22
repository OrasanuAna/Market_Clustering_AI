import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

tickers = [
    'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'TSLA', 'NVDA', 'NFLX', 'INTC', 'AMD', 'IBM', 'ORCL'
]

financial_data = []

for ticker in tickers:
    stock = yf.Ticker(ticker)
    info = stock.info

    financial_data.append({
        "Company": ticker,
        "MarketCap": info.get("marketCap"),
        "Revenue": info.get("totalRevenue"),
        "Profit": info.get("grossProfits"),
        "Debt": info.get("totalDebt"),
    })

df = pd.DataFrame(financial_data)

df_clean = df.dropna()


features = ["MarketCap", "Revenue", "Profit", "Debt"]
X = df_clean[features]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


kmeans = KMeans(n_clusters=3, random_state=0)
df_clean["Cluster"] = kmeans.fit_predict(X_scaled)


df_clean.to_csv("data/clustered_companies.csv", index=False)


pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
df_pca = pd.DataFrame(X_pca, columns=["PCA1", "PCA2"])
df_pca["Cluster"] = df_clean["Cluster"].values
df_pca["Company"] = df_clean["Company"].values

plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=df_pca,
    x="PCA1",
    y="PCA2",
    hue="Cluster",
    style="Company",
    palette="viridis",
    s=100
)
plt.title("Clusterele companiilor în spațiu PCA")
plt.xlabel("PCA 1")
plt.ylabel("PCA 2")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()


print(df_clean[["Company", "Cluster"]])
