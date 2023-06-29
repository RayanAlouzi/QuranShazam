from fuzzywuzzy import fuzz

def search_quran(query):
    closest_match = None
    highest_similarity = 0

    with open('quran-simple.txt', 'r', encoding='utf-8') as file:
        for verse in file:
            similarity = fuzz.ratio(query, verse)
            if similarity > highest_similarity:
                highest_similarity = similarity
                closest_match = verse

    return closest_match

# Example usage
def searching(): 
    with open('transcript.txt', 'r', encoding='utf-8') as transcript_file:
        search_query = transcript_file.read().strip()
    closest_verse = search_quran(search_query)
    print("Closest verse to the query:")
    print(closest_verse)