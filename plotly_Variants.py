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


sk = df['variant'] == 'Delta'
fig = px.scatter(df[sk] , y='num_sequences', x='perc_sequences',color='location', size='num_sequences_total',labels={
                     "location": "COUNTRIES",
                     "perc_sequences": "Percentage of Sequences",
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
