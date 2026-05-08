import pandas as pd

data = {
    "Name": ["Amit", "Riya", "Sam"],
    "Age": [21, 19, 23],
    "Score": [85, 92, 78],
}

df = pd.DataFrame(data)

print(df)

high_scores = df[df["Score"] > 80]
print(high_scores)
