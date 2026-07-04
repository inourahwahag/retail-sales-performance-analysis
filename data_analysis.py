import pandas as pd

# Load dataset
df = pd.read_csv("superstore.csv")

# Convert date columns
df["Order.Date"] = pd.to_datetime(df["Order.Date"])
df["Ship.Date"] = pd.to_datetime(df["Ship.Date"])

# Business KPIs
print("Total Sales:", df["Sales"].sum())
print("Total Profit:", round(df["Profit"].sum(), 2))
print("Total Orders:", df["Order.ID"].nunique())
print("Total Customers:", df["Customer.ID"].nunique())
print("Average Order Value:", round(df["Sales"].mean(), 2))

# Sales by Category
print("\nSales by Category")
print(df.groupby("Category")["Sales"].sum().sort_values(ascending=False))

# Profit by Category
print("\nProfit by Category")
print(df.groupby("Category")["Profit"].sum().sort_values(ascending=False))

# Top 10 Products by Sales
print("\nTop 10 Products by Sales")
print(
    df.groupby("Product.Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

# Sales by Region
print("\nSales by Region")
print(
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

# Profit by Region
print("\nProfit by Region")
print(
    df.groupby("Region")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

# Top 10 Customers by Sales
print("\nTop 10 Customers by Sales")
print(
    df.groupby("Customer.Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

# Top 10 Customers by Profit
print("\nTop 10 Customers by Profit")
print(
    df.groupby("Customer.Name")["Profit"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

# Create Shipping Days column
df["Shipping Days"] = (df["Ship.Date"] - df["Order.Date"]).dt.days

print("\nAverage Shipping Days:")
print(round(df["Shipping Days"].mean(), 2))

# Profit by Discount

print("\nAverage Profit by Discount")

print(
    df.groupby("Discount")["Profit"]
    .mean()
    .sort_values(ascending=False)
)

# Export cleaned dataset
df.to_csv("cleaned_superstore.csv", index=False)

print("\nCleaned dataset exported successfully.")