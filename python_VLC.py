# Import VLC
import vlc
import time
import sys
import os

# Create VLC media player object
media_player = vlc.MediaPlayer("Stopwatch  Count Up Timer 1 Hour_1080p.mp4")

# Print type of media player variable
print(type(media_player))

# Start playing video
media_player.play()

# Wait so the video can be played for 5 seconds irrespective for length of video
time.sleep(5)

player = vlc.Instance()

# Create a new media
media = player.media_new("no_480p.mp4")

# Create a media player object
media_player = player.media_player_new()
media_player.set_media(media)

# Set the video scale
media_player.scale = 0.6

# Start playback
media_player.play()

# Wait so the video can be played for 5 seconds irrespective for length of video
time.sleep(5)

# Create Instance class object
player = vlc.Instance()

# Create a new media list
media_list = player.media_list_new()

# Create a new media player object
media_player = player.media_list_player_new()

# Create a new media
media = player.media_new("no_480p.mp4")

# Add media to media list
media_list.add_media(media)

# Set media list to the mediaplayer
media_player.set_media_list(media_list)

# Start playing video
media_player.play()

# Wait so the video can be played for 5 seconds irrespective for length of video
time.sleep(5)

# https://www.geeksforgeeks.org/python-vlc-creating-mediaplayer-object/
# https://www.geeksforgeeks.org/python-vlc-instance-creating-medialistplayer-instance/