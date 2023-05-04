import pandas as pd, matplotlib.pyplot as plt
import plotly.express as px


data = pd.read_csv("data.csv")
student = pd.read_csv("student.csv", index_col=0)


#class_four1 = student[student["mark"] == 60]["name"]
#class_groups = student.groupby("class")["name"].count()

#tt = data.nlargest(5, "Pulse", keep="last")


st = student[~student['mark'].isnull()]
print(st)
