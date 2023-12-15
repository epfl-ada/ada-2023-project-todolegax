import pandas as pd
import os

# Define the data folder paths for BeerAdvocate
DATA_FOLDER_BA = 'data/BeerAdvocate/'

# Define the file paths for the datasets
Beers_DATASET = DATA_FOLDER_BA+"beers.csv"
Users_DATASET = DATA_FOLDER_BA+"users.csv"
Reviews_DATASET = DATA_FOLDER_BA+"reviews_BA.csv"
Breweries_DATASET = DATA_FOLDER_BA+"breweries.csv"

row_count = 0

# Open the file and count the lines
with open(Reviews_DATASET, 'r', encoding='utf-8') as file:
    for line in file:
        row_count += 1

print(f'Number of rows in the file: {row_count}')


lines_per_file = 2316998
smallfile = None
with open(Reviews_DATASET, 'r', encoding='utf-8') as bigfile:
    for lineno, line in enumerate(bigfile):
        if lineno % lines_per_file == 0:
            if smallfile:
                smallfile.close()
            small_filename = '../DATA/BeerAdvocate/reviews/small_file_{}.txt'.format(lineno + lines_per_file)
            smallfile = open(small_filename, "w", encoding='utf-8')
        smallfile.write(line)
    if smallfile:
        smallfile.close()


directory = DATA_FOLDER_BA + 'reviews/'
reviews = pd.DataFrame()
for filename in os.listdir(directory):
    # Initialize empty lists to store the extracted data
    beer_data = []
    current_review = {}  # Initialize an empty dictionary to store the current review
    # Open the text file and read it line by line
    with open(directory + filename, 'r', encoding='utf-8') as file:

        for line in file:
            line = line.strip()  # Remove leading/trailing whitespace
            if line:  # If the line is not empty
                key, value = line.split(":",1)
                current_review[key] = value
            else:  # Blank line indicates the end of a review
                if current_review:
                    beer_data.append(current_review)
                current_review = {}  # Reset the dictionary for the next review

    # If there's any remaining review, add it to the list
    if current_review:
        beer_data.append(current_review)

    # Convert the list of dictionaries into a Pandas DataFrame
    reviews_tmp = pd.DataFrame(beer_data)
    reviews = pd.concat([reviews,reviews_tmp])


lines_per_file = 2316998
smallfile = None
with open(Reviews_DATASET, 'r', encoding='utf-8') as bigfile:
    for lineno, line in enumerate(bigfile):
        if lineno % lines_per_file == 0:
            if smallfile:
                smallfile.close()
            small_filename = '../DATA/BeerAdvocate/reviews/small_file_{}.txt'.format(lineno + lines_per_file)
            smallfile = open(small_filename, "w", encoding='utf-8')
        smallfile.write(line)
    if smallfile:
        smallfile.close()

filename_review = DATA_FOLDER_BA + 'reviews_BA.csv'
reviews.to_csv(filename_review, encoding='utf-8', index=False)