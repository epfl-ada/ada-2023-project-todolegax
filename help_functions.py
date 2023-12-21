import difflib
from math import radians, sin, cos, sqrt, atan2
from deep_translator import GoogleTranslator

# Hamming distance function
def find_closest_match(input_str, target_list):
    """Find the closest match in a list using Hamming distance."""
    return difflib.get_close_matches(input_str, target_list, n=1, cutoff=0.5)

# Replace name of location by the closest match from the geo dataframe
def match_country_name(df,unique_loc,unique_state):
    # Init dropped breweries (to motinor the dropped elements)
    dropped_brew = []

    # Loop through the 'brewery_country' column and replace values if needed
    for i, location in enumerate(df['country']):
        # Check if in USA --> (USA, state)
        try:
            location, state = location.split(', ')
        except:
            state = location  # if not in USA, state = location
        
        # Find closest match with Hamming distance
        closest_match_country = find_closest_match(location, unique_loc)
        
        if closest_match_country:
            # If closest match is USA --> match state      
            if closest_match_country[0] == 'United States of America':
                df.at[i, 'country'] = closest_match_country[0]
                
                # Find state
                closest_match_state = find_closest_match(state, unique_state)
                if closest_match_state:
                    df.at[i, 'state'] = closest_match_state[0]
                else:
                    df = df.drop(index=i)
            else:
                # If not in USA --> state = location 
                df.at[i, 'country'] = closest_match_country[0]
                df.at[i, 'state'] = closest_match_country[0]
        else:
            #print(i)
            #print(breweries_loc.at[i, 'brewery_country'])
            # If no match, drop
            dropped_brew.append(location)
            df = df.drop(index=i)
    return df, dropped_brew

# Function to calculate Haversine distance
def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0  # Radius of the Earth in kilometers
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance

# Computes mean and std for size categories
def compute_stats_for_categories(df,col): 
    df_small_breweries = df[df['size_category']=='small']
    df_medium_breweries = df[df['size_category']=='medium']
    df_big_breweries = df[df['size_category']=='big']
    means = []
    std_devs = []
    # Calculate mean and standard deviation for each dataframe
    means.append(df_small_breweries[col].mean())
    std_devs.append(df_small_breweries[col].std())

    means.append(df_medium_breweries[col].mean())
    std_devs.append(df_medium_breweries[col].std())

    means.append(df_big_breweries[col].mean())
    std_devs.append(df_big_breweries[col].std())

    return means, std_devs

# Split in categories
def categorize_size(value):
    if value < 0.3:
        return 'small'
    elif 0.3 <= value < 0.7:
        return 'medium'
    else:
        return 'big'

# Normalize metrics
def normalize_column(column):
    return column / column.max()

# English translation
def translate_to_english(text, source='auto', target='en'):
    """
    Translates the input text to English.

    Parameters:
        text (str): The input text to be translated.
        source (str): The source language (default is 'auto' for automatic detection).
        target (str): The target language (default is 'en' for English).

    Returns:
        The translated text in English.
    """
    translated = GoogleTranslator(source=source, target=target).translate(text)
    return translated

# Function to plot on a subplot
def plot_on_subplot(ax, j):
    for i in range(len(size) - 1):
        # Plot background color spans for size categories
        ax.axvspan(size[i], size[i + 1], color=colors[i], alpha=0.5)
        
        # Plot mean and standard deviation for each size category and year
        ax.errorbar(mid[i], means[f"mean_{categories[i]}_{years_list[j]}"],
                    yerr=stds[f"std_{categories[i]}_{years_list[j]}"], fmt='o-', color=dark_colors[i],
                    ecolor=dark_colors[i], label='Mean and std rating ' + str(categories[i]),
                    capsize=5, alpha=1.0)
        
        # Scatter plot for individual breweries' rating distribution
        ax.scatter(dfs[f"df_{categories[i]}_breweries_{years_list[j]}"]['size_metrics'],
                   dfs[f"df_{categories[i]}_breweries_{years_list[j]}"]['avg_rating'], color='darkgray', s=point_size)
        
        # Label each category
        ax.text(mid[i], 1.7, labels[i], color=dark_colors[i], ha='center', va='center', fontsize=12)

        # Set subplot properties
        ax.set_title('Avg. rating distribution ' + str(years_list[j]))
        ax.set_ylim([1.5, 5])
        ax.set_xlim([0, 1])
        ax.set_xlabel('Size metrics')
        ax.set_ylabel('Avg. rating')