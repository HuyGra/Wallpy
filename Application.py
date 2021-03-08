'''Here is an example. I hope you can do better.'''
import WallpyLib
import threading, time, wmi
import vlc
from tkinter import *
	
url = "Fubuki_Sirakami.mp4"
hwndFrame = ""
loop = False
def Play(event):
	global loop
	if event.type == vlc.EventType.MediaPlayerEndReached:
		loop = True

def SimpleMediaPlayer(url):
	global loop
	Instance = vlc.Instance()
	player = Instance.media_player_new()
	player.set_fullscreen(True)
	media = Instance.media_new(url)
	player.set_media(media)
	em = player.event_manager()
	em.event_attach(vlc.EventType.MediaPlayerEndReached, Play)
	player.play()
	time.sleep(2)
	f = wmi.WMI()
	WallpyLib.Wallpy("VLC (Direct3D11 output)")
	while True:
		if loop:
			player.set_media(media)
			player.play()
			loop = False

SimpleMediaPlayer(url)

