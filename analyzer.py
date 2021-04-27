import os
import pandas as pd

pd.set_option('display.max_columns', None)

print(*[x.split(".")[0] for x in os.listdir("opinions")], sep="\n")

product_id = input("Enter product ID: ")

opinions = pd.read_json(f"./opinions/{product_id}.json")

opinions_count = opinions.shape[0]
pros_count = opinions.pros.map(bool).sum()
cons_count = opinions.cons.map(bool).sum()
average_score = opinions.stars.mean()

print(f"""There are {opinions_count} opinions in data set. 
For {pros_count} opinions list of advantages is available. 
For {cons_count} opinions list of disadvantages is available. 
Average score based on opinions stars is equal to {average_score:.1f}""")

recommendations = opinions.recommendation.value_counts(dropna=False)

print(type(recommendations))