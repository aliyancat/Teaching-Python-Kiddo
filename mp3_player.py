import pygame

import random

pygame.init()

pygame.mixer.init()


songs = ["faded.mp3", "michaeljackson.mp3", "goldenbrown.mp3"] 


current_song = 0


while True:
    print("=============================================\n")
    print("MP3 Player\n")
    print("1.Show Playlist")
    print("2. Play a Song") 
    print("3. Play next Song")
    print("4. Shuffle the Playlist")
    print("5. Remove a song")
    print("6. Exit\n")


    choice = input("Enter your choice: ")

    if choice == "1":
        print("=============================================\n")
        print("Playlist:\n")
        for song  in songs:
            print(song)

    elif choice == "2":
        musicchoice = int(input("Enter the song you want to play: "))
        current_song = musicchoice-1
        print(f"Playing {songs[current_song]}...\n")
        pygame.mixer.music.load(songs[current_song])
        pygame.mixer.music.play()

    elif choice == "3":
        current_song =  (current_song + 1) % 3
        print(f"Playing {songs[current_song]}...\n")
        pygame.mixer.music.load(songs[current_song])
        pygame.mixer.music.play()

    elif choice == "4":
        random.shuffle(songs)
        current_song = 0
        print("Playlist shuffled!\n")

    elif choice == "5": 
        removechoice = int(input("Enter the song you want to remove: "))
        removechoice = removechoice - 1
        removed =  songs.pop(removechoice)
        print(f"song {removed} has been removed from the playlist\n")

    elif choice == "6":
        pygame.mixer.music.stop()
        print("Exiting...")
        break
    
    else:
        print("Invalid choice. Please try again.\n")