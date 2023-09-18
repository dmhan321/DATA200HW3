import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


# Streamlit App
st.title("My first graph")

data = pd.read_csv(r"toy_dataset.csv")
df = pd.DataFrame(data)

# group the dataframe by column 'City'
df_city = df.groupby('City')
print(df_city)
# calculate average income by city
average_income = df_city['Income'].mean()

# Graph: Bar Chart
average_income.plot(kind='bar', figsize=(8,6))

# add labels and title
plt.xlabel("City")
plt.ylabel("Average Income")
plt.title("Average Income per City")

plt.show()


# Visualize dataframe:
st.subheader("Detailed Data View")
st.dataframe(df)