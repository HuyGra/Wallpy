'''Wallpy Version 0.0.3 Dev. \n
Please install pywin32 using pip install pywin32 to use library'''
import win32gui, win32con, time

class Wallpy():
	"""Class of Wallpy"""
	# Looks simple, right =))
	def __init__(self, WindowsName=""):
		self.worker = ""
		self.hwndChild = ""
		self.WindowsName = WindowsName
		progman = win32gui.FindWindow("Progman", None)
		win32gui.SendMessageTimeout(progman, 0x052C, 0, 0, win32con.SMTO_NORMAL, 1000)
		win32gui.EnumWindows(self.GetHandleWorkerW,None)
		for x in range(0, 10000):
			time.sleep(0.1)
			win32gui.EnumWindows(self.GetHandleWallpaperWindows,None)
			if self.hwndChild != "":
				print("IntPtr Worker = ", self.worker)
				print("IntPtr hwndChild = ", self.hwndChild)
				print("Done!!!")
				win32gui.SetParent(self.hwndChild, self.worker)
				break
			elif x == 10000:
				print("Not Found")
		

	def GetHandleWorkerW(self, hwnd, ctx):
		"""Get the WorkerW windows handle"""
		p = win32gui.FindWindowEx(hwnd, 0, "SHELLDLL_DefView", None)
		if p != 0:
			self.worker = win32gui.FindWindowEx(0, hwnd, "WorkerW", None)		
		return True

	def GetHandleWallpaperWindows(self, hwnd, ctx):
		"""Take the window handle you want to set it as wallpaper"""
		if win32gui.GetWindowText(hwnd) == self.WindowsName: 
			self.hwndChild = hwnd
		return True