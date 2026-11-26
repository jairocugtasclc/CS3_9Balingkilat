"""
Cugtas, Jairo Vincent M.
Latoga, Dianne R.
Soriano, Marriane Audrey F.
main.py
CS3 SA4
26/11/26
"""


# Music Playlist Class

class Collection:
    def __init__(self):
        self.items = []
        
    def add(self, item):
        self.items.append(item)
        
    def getByTitle(self, propertyValue):
        for item in self.items:
            if item.title() == propertyValue():
                return item
            else:
                return none
            
    def getAll(self):
        return self.items
    
    def removeByTitle(self, propertyValue):
        item = self.getByTitle(propertyValue)
        if song is not None:
            self.items.remove(item)
            return True
        else:
            return False
        
    def count(self):
        return len(self.items)


#Main Code

playlist = Collection()

while True:
    print("\n--- Dianne's Music Playlist ---")
    print("1. Add a song")
    print("2. Get a song by property")
    print("3. Get all songs")
    print("4. Remove a song by property")
    print("5. Count songs")
    print("6. Exit")

    a = 1
    while a == 1:
        choice = int(input("Choose an option (number, e.g.: 2): "))

        if choice == 1:
            title = input("Title: ")
            artist = input("Artist: ")
            album = input("Album: ")
            duration = input("Duration: ")
            language = input("Language: ")

            playlist.append(Song(title, artist, album, duration, language))
            print("Song added.")

        elif choice == 2:
            title = input("Enter the song title: ")
            song = playlist.getByTitle(title)
            if song is not None:
                print(song)
            else:
                print("Song not found.")
                        
        elif choice == 3:
            if playlist.count() == 0:
                print("The playlist is empty.")
            else:
                for song in playlist.getAll():
                    print(song)

        elif choice == 4:
            title = input("Enter the title of the song to remove: ")
            if playlist.removeByTitle(title):
                print("Song removed.")
            else:
                print("Song not found.")

        elif choice == 5:
            print(f"Number of songs: {playlist.count()}")

        elif choice == 0:
            print("Adios!")
            break

        else:
            print("\nInvalid option. Please try again.")

        
        

        
        
    
    
