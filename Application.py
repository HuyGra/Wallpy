'''Here is an example. I hope you can do better.'''
import WallpyLib
import vlc
	
video = "Test~1.mp4" #You video
loop = False
def Play(event):
	global loop
	if event.type == vlc.EventType.MediaPlayerEndReached:
		loop = True

def SimpleMediaPlayer(video):
	global loop
	Instance = vlc.Instance()
	player = Instance.media_player_new()
	player.set_fullscreen(True)
	media = Instance.media_new(video)
	player.set_media(media)
	em = player.event_manager()
	em.event_attach(vlc.EventType.MediaPlayerEndReached, Play)
	player.play()
	WallpyLib.Wallpy("VLC (Direct3D11 output)")
	while True:
		if loop:
			player.set_media(media)
			player.play()
			loop = False

SimpleMediaPlayer(video)

