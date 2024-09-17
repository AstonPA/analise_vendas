import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('sales_data.csv')


print(df.head())


df['Date'] = pd.to_datetime(df['Date'])


df['YearMonth'] = df['Date'].dt.to_period('M')


monthly_sales = df.groupby('YearMonth')['Sales'].mean()


print(monthly_sales)


sns.set(style="whitegrid")


plt.figure(figsize=(12, 6))
sns.lineplot(x=monthly_sales.index.astype(str), y=monthly_sales.values)
plt.xticks(rotation=45)
plt.title('Venda Média por Mês')
plt.xlabel('Mês')
plt.ylabel('Venda Média')
plt.tight_layout()
plt.show()
