import pandas as pd
import matplotlib.pyplot as plt

# Create data
data = {
    'Region': ['East','West','South','East','West','South','East','West'],
    'Sales': [200,500,300,450,150,600,250,350]
}

# Convert to DataFrame
df = pd.DataFrame(data)

print(df)

# Group data
region_sales = df.groupby('Region')['Sales'].sum()

print(region_sales)

# Plot
region_sales.plot(kind='bar')
plt.title("Sales by Region")
plt.show()