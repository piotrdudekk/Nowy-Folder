import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

pd.set_option('display.max_columns', None)

print(*[x.split(".")[0] for x in os.listdir("opinions")], sep = "\n")

product_id = input("Enter product ID: ")

opinions = pd.read_json(f"./opinions/{product_id}.json")

opinions_count = opinions.shape[0]
pros_count = opinions.pros.map(bool).sum()
cons_count = opinions.cons.map(bool).sum()
average_score = opinions.stars.mean()

print(f"""Ther are {opinions_count} opinions in data set. 
For {pros_count} opinions list of advantages is available. 
For {cons_count} opinions list of disadvantages is available. 
Average score based on onionions stars is equal to {average_score:.1f}""")

recommendations = opinions.recommendation.value_counts(dropna = False).sort_index()
plt.figure(figsize = (7, 4))
recommendations.plot.pie(
    label = "",
    labels = ['Don\'t recommend', 'Recommend', 'No opinion'],
    colors = ['crimson', 'forestgreen', 'lightskyblue'],
    autopct = "%1.1f%%",
    pctdistance = 1.2,
    labeldistance = 1.4
)
plt.title("Share of recommendations in opinions")
plt.legend(bbox_to_anchor = (1.0, 1.0))
plt.tight_layout()
plt.savefig(f"./figures/{product_id}_pie.png")
plt.close()

stars = opinions.stars.value_counts().reindex(np.arange(0, 5.5, 0.5), fill_value = 0)
stars.plot.bar(color = "lightskyblue")
for index, value in enumerate(stars):
    plt.text(index, value+1.5, str(value), ha = 'center')
plt.xlabel("Rating")
plt.ylabel("Number of opinions")
plt.title("Frequency of ratings")
plt.savefig(f"./figures/{product_id}_bar.png")
plt.close()

stars_recommendations = pd.crosstab(opinions.stars, opinions.recommendation)
print(stars_recommendations)