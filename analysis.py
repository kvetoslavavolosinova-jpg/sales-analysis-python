print("SCRIPT STARTS HERE")
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

print(df.head())

df["revenue"] = df["price"] * df["quantity"]

print("\nTOP PRODUCTS:")
print(df.groupby("product")["revenue"].sum().sort_values(ascending=False))

print("\nTOP COUNTRIES:")
print(df.groupby("country")["revenue"].sum().sort_values(ascending=False))

top_products = df.groupby("product")["revenue"].sum()

top_products.plot(kind="bar")
plt.title("Top Products by Revenue")
plt.show()
import matplotlib.pyplot as plt

df["revenue"] = df["price"] * df["quantity"]

top_products = df.groupby("product")["revenue"].sum()

top_products.plot(kind="bar")
plt.title("Top Products by Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()
print("\n======================")
print("DATA ANALYSIS REPORT")
print("======================")
