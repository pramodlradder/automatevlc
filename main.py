import time
import os
import pyautogui  #pip install pyautogui
import win32con   #pip install pypiwin32
import win32gui   #pip install win32gui


file = r"start C:\Users\dell5567\Desktop\Skillet" #file name of your music folder
mi=None
option=None

def play():
      os.system(file)
      pyautogui.click()
      pyautogui.hotkey('ctrl','a')
      pyautogui.press('enter')
      time.sleep(2)
      global mi
      mi=win32gui.GetForegroundWindow()
      #print(mi) object id of vlc
      win32gui.ShowWindow(mi,win32con.SW_MINIMIZE) #minimize the vlc window
      os.system(file)
      pyautogui.hotkey('alt','f4')

def pause():
      win32gui.ShowWindow(mi,win32con.SW_MAXIMIZE)#maximize the vlc window
      time.sleep(2)
      pyautogui.press('playpause')
      win32gui.ShowWindow(mi,win32con.SW_MINIMIZE)

def resume():
      win32gui.ShowWindow(mi,win32con.SW_MAXIMIZE)
      time.sleep(2)
      pyautogui.click()
      pyautogui.press('playpause')
      win32gui.ShowWindow(mi,win32con.SW_MINIMIZE)

def next():
      win32gui.ShowWindow(mi,win32con.SW_MAXIMIZE)
      time.sleep(2)
      pyautogui.press('nexttrack')
      win32gui.ShowWindow(mi,win32con.SW_MINIMIZE)

def previous():
      win32gui.ShowWindow(mi,win32con.SW_MAXIMIZE)
      time.sleep(2)
      pyautogui.press('prevtrack')
      win32gui.ShowWindow(mi,win32con.SW_MINIMIZE)
def close():
      win32gui.ShowWindow(mi,win32con.SW_MAXIMIZE)
      time.sleep(2)
      pyautogui.hotkey('alt','f4')
      
  

def main():
  if option=="play" :
      play()
  elif option=="pause":
      pause()
  elif option=="resume":
      resume()
  elif option=="next":
      next()
  elif option=="previous":
      previous() 
  elif option=="close":
      close()

                
if __name__=='__main__':
  while option !="close":
    option = input("Enter the option:")
    if option=="close":
      close()
    main() 
    
