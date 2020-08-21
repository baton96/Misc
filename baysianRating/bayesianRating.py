# baysianRating = ( (avg_num_votes * avg_rating) + (this_num_votes * this_rating) ) / (avg_num_votes + this_num_votes)

# avg_num_votes: The average number of votes of all items that have num_votes>0
# avg_rating: The average rating of each item (again, of those that have num_votes>0)
# this_num_votes: number of votes for this item
# this_rating: the rating of this item

# avg_num_votes is used as the “magic” weight in this formula. The higher this
# value, the more votes it takes to influence the bayesian rating value

import pandas as pd

# df = pd.read_csv('imdb1000.csv')
# df = pd.read_csv('imdb100.csv')
df = pd.read_csv('imdb50.csv')
avg_num_votes = df.Votes.mean()

avg_rating = df.Rating.mean()
base_rating = avg_rating * avg_num_votes
df['BaysianRating'] = (base_rating + (df.Votes * df.Rating)) / (avg_num_votes + df.Votes)

print(df[['Title', 'Votes', 'Rating', 'BaysianRating']].head())


