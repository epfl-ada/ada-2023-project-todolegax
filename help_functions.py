import difflib

# Hamming distance function
def find_closest_match(input_str, target_list):
    """Find the closest match in a list using Hamming distance."""
    return difflib.get_close_matches(input_str, target_list, n=1, cutoff=0.5)


def match_country_name(df,country,state,unique_loc,unique_state):
    # Init dropped breweries
    dropped_brew = []

    # Loop through the 'brewery_location' column and replace values if needed
    for i, location in enumerate(df[country]):
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
                df.at[i, country] = closest_match_country[0]
                
                # Find state
                closest_match_state = find_closest_match(state, unique_state)
                if closest_match_state:
                    df.at[i, state] = closest_match_state[0]
                else:
                    df = df.drop(index=i)
            else:
                # If not in USA --> state = location 
                df.at[i, country] = closest_match_country[0]
                df.at[i, state] = closest_match_country[0]
        else:
            #print(i)
            #print(breweries_loc.at[i, 'brewery_location'])
            # If no match, drop
            dropped_brew.append(location)
            df = df.drop(index=i)
    return df, dropped_brew