import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


# Streamlit App
st.title("My first graph")

data = pd.read_csv(r"toy_dataset.csv")
df = pd.DataFrame(data)

# group the dataframe by column 'City'
df_city = df.groupby('City')
# calculate average income by city
average_income = df_city['Income'].mean().reset_index(name='mean')

# Graph: Bar Chart
average_income.plot(kind='bar', figsize=(8,6))
fig, ax = plt.subplots()
ax.bar(average_income['City'], average_income['mean'] )

# add labels and title
plt.xlabel("City", rotation='vertical')
plt.ylabel("Average Income")
plt.title("Average Income per City")

st.pyplot(fig)

st.write("'Mountain View has the highest average income for toys")

# Visualize dataframe:
st.subheader("Detailed Data View")
st.dataframe(df)