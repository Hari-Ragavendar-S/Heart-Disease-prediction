import pandas as pd

df = pd.read_excel("heart.xlsx")


df.to_csv("heart.csv", index=False)

print("Converted Excel to CSV successfully ")
