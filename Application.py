import WallpyLib, os

os.startfile("WallpyVideoPlayer.exe")

while True:
    try:
        f = open('cache/IntPtr.txt', 'r')
        IntPtr = f.read()
        f.close()
        WallpyLib.Wallpy(IntPrt=int(IntPtr))
        break
    except:
        pass
