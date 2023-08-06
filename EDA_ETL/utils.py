# Calculate the mode of the 'genres' column
def get_mode_list(lst):
    # Use the Counter class from collections to count the occurrences of each list in the 'genres' column
    from collections import Counter
    counter = Counter(lst)
    # Find the most common list (the mode) and return it
    mode_list = counter.most_common(1)[0][0]
    return mode_list

def join_genres(genre_list):
    return " ".join(genre_list).replace("[", "").replace("]", "").replace("'", "")