import time
import pygame


pygame.init()
pygame.mixer.init()


alarm_sound = pygame.mixer.Sound("music.mp3")


minutes = int(input("Enter the number of minutes for the alarm: "))

seconds = minutes * 60

print(f"Alarm set for {minutes} minutes. Waiting...")


while seconds >= 0:
    print(f"{seconds} seconds remaining...")
    time.sleep(1)  
    seconds = seconds - 1


print("WAKE UP !!!")
alarm_sound.play()
time.sleep(100)


