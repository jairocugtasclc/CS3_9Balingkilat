"""Interactive music playlist manager.

Run with: python main.py
"""

from Cugtas import Collection
from Cruz import Song


def prompt_song_details():
    """Ask for a song's five properties and return a Song object."""
    print("\nEnter song details:")
    title = input("Title: ").strip()
    artist = input("Artist: ").strip()
    album = input("Album: ").strip()
    duration = input("Duration (e.g., 3:45): ").strip()
    language = input("Language: ").strip()
    return Song(title, artist, album, duration, language)


def main():
    playlist = Collection()

    while True:
        print("\n--- Music Playlist ---")
        print("1. Add a song")
        print("2. Find a song by title")
        print("3. Show all songs")
        print("4. Remove a song by title")
        print("5. Count songs")
        print("0. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            song = prompt_song_details()
            playlist.add(song)
            print(f"Added: {song}")
        elif choice == "2":
            title = input("Enter the song title: ").strip()
            song = playlist.getBy(title)
            if song is None:
                print(f'No song found with the title "{title}".')
            else:
                print(f"Found: {song}")
        elif choice == "3":
            songs = playlist.getAll()
            if not songs:
                print("The playlist is empty.")
            else:
                print("\nSongs in your playlist:")
                for song in songs:
                    print(song)
        elif choice == "4":
            title = input("Enter the title of the song to remove: ").strip()
            song = playlist.getBy(title)
            if song is None:
                print(f'No song found with the title "{title}".')
            elif playlist.removeBy(title):
                print(f"Removed: {song}")
            else:
                print("The song could not be removed.")
        elif choice == "5":
            print(f"There are {playlist.count()} song(s) in the playlist.")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose one of the listed options.")


if __name__ == "__main__":
    main()
