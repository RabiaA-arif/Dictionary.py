song_organizer={"song1":{"artist":"atif",
                          "genre":"happy"},
                "song2":{"artist":"arsalan",
                          "genre":"sad"},
                 "song3":{"artist":"haseeb",
                           "genre":"rape"},
                  "song4":{"artist":"abrar",
                           "genre":"melody"}}

songs_list = [(title, details) for title, details in song_organizer.items()]


# Define sorting functions
def sort_by_title(song):
    return song[0]  # Sort by song title

def sort_by_artist(song):
    return song[1]['artist']  # Sort by artist name

def sort_by_genre(song):
    return song[1]['genre']  # Sort by genre
sorted_by_title = sorted(songs_list, key=sort_by_title)
sorted_by_artist = sorted(songs_list, key=sort_by_artist)
sorted_by_genre = sorted(songs_list, key=sort_by_genre)

print("Sorted by Title:", sorted_by_title)
print("Sorted by Artist:", sorted_by_artist)
print("Sorted by Genre:", sorted_by_genre)



