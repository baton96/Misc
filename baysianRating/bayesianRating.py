# baysianRating = ( (avg_num_votes * avg_rating) + (this_num_votes * this_rating) ) / (avg_num_votes + this_num_votes)

# avg_num_votes: The average number of votes of all items that have num_votes>0
# avg_rating: The average rating of each item (again, of those that have num_votes>0)
# this_num_votes: number of votes for this item
# this_rating: the rating of this item

# avg_num_votes is used as the “magic” weight in this formula. The higher this
# value, the more votes it takes to influence the bayesian rating value

import pandas as pd

df = pd.read_csv('imdb50.csv').sort_values('Rating').reset_index(drop=True)
avg_num_votes = df.Votes.mean()
base_rating = df.Rating.mean() * avg_num_votes
df['BaysianRating'] = (base_rating + (df.Votes * df.Rating)) / (avg_num_votes + df.Votes)

# print(df[['Votes', 'Rating', 'BaysianRating']])
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(df.Rating, marker='.', linestyle='')
ax.plot(df.BaysianRating, marker='.', linestyle='')
plt.show()
