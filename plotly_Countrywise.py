import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px

path = "C:/Users/irfan/OneDrive/Desktop/MO TECH/covid-variants.csv"
df = pd.read_csv(path)
df.head(n=5)

print(df['variant'].value_counts(dropna=False))
print(df['location'].value_counts(dropna=False))

mk = df['location'] == 'India'
fig = px.scatter(df[mk], y='perc_sequences', x='num_sequences',size = 'num_sequences_total', color='variant' ,labels={
                     "variant": "VARIANTS",
                     "num_sequences": "Number Of Sequences Recorded",
                    },
                title="Countrywise Effect of COVID-19 Variants")
fig.update_layout(
    font=dict(
        family="Josefin Sans",
        size=15,
        color="RebeccaPurple"
    )
)

fig.show()
