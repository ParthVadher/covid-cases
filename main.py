import pandas as pd
import plotly.express as px


df = pd.read_csv("C:\\Users\\Dell\\Desktop\\dropBox\\Covid_data.csv")
sc = px.scatter(df,x = "date", y = "cases" , color = "country" , title = "Covid Cases Analysis")
sc.show()