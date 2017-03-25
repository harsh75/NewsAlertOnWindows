from bs4 import BeautifulSoup as bs
import urllib.request
import sys
from PyQt5 import Qt
import subprocess
import threading

notification_text=[]
class ShowNotification(threading.Thread):
    def __init__(self,notificationText,Appname):
        threading.Thread.__init__(self)
        self.text=notificationText
        self.Appname = Appname
 
    def run(self):
        systemtray_icon.show()
        systemtray_icon.showMessage(self.Appname,self.text)   

link=#could not give the website name from where I extracted the news from. Email at harshseth75@live.com
with urllib.request.urlopen(link) as response:
        raw_data=response.read()
        soup=bs(raw_data,"lxml")
        top_stories=soup.find("ul",{"data-vr-zone":"top_stories"})
        for top_story in top_stories:
            soup2=bs(str(top_story))
            anchors=soup2.find_all("a")
            for anchor in anchors:
                str1=anchor.text
                if(str1!=""):
                    notification_text.append(str1)
        print(notification_text)
        
        thread_list=[]
        note_text="——————————————————————-" + "\n"
        for v in notification_text[:]:
                note_text=note_text+ v + "\n" + "——————————————————————-" + "\n"
        t_name = ShowNotification(note_text,"Harsh Please Catch the Live Updates")
        app = Qt.QApplication(sys.argv)
        systemtray_icon = Qt.QSystemTrayIcon(app)
        t_name.start()
                
            
        

