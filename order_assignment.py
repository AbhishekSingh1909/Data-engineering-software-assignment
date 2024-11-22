import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# read csv file to panda to get tables
df_orders = pd.read_csv("./orders.csv")

# df_orders['order_date'] = pd.to_datetime(df_orders['order_date'])

df_order_items = pd.read_csv("./order_items.csv")

# create company database
conn = sqlite3.connect("company_database.db")

df_orders.to_sql('orders', conn, if_exists='replace', index=False)
df_order_items.to_sql('order_items', conn, if_exists='replace', index=False)

# query to get records from order table

query = '''
select
    order_date as order_date,
    round(sum(amount), 2) AS daily_total_sales
from
    orders
group by
    order_date
order by
    order_date
    limit 100
'''

query_results = pd.read_sql_query(query, conn)

dates = query_results['order_date']
total_sale = query_results['daily_total_sales']


# Create the line plot
plt.figure(figsize=(12, 6))
# plt.plot(dates, total_sale, marker='o', linestyle='-',
#          color='b', label='Daily Sales')

plt.plot(dates, total_sale, marker='o', linestyle='-',
         color='b', label='Daily Sales')

plt.gca().xaxis.set_major_locator(
    plt.MaxNLocator(50))  # Show only 10 ticks on x-axis
# Customize the plot
plt.title('Daily Sales', fontsize=16)
plt.xlabel('Order Date', fontsize=12)
plt.ylabel('Sales Amount ($)', fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.yticks(fontsize=10)
plt.grid(visible=True, linestyle='--', alpha=0.7)
plt.legend(fontsize=10)
plt.tight_layout()

# Display the plot
plt.show()


# Close the database connection
conn.close()
