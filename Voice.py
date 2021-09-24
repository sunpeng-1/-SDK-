import pyttsx3
#import win32con,win32api
#实现语音播报功能
class Voice:

    def __init__(self):
        self.engine = pyttsx3.init()#初始化引擎
        self.rate = self.engine.getProperty('rate')#获取rate属性  rate：播报速度
        self.engine.setProperty('rate', self.rate - 30)#减慢播报速度
        self.content=''

    def voice1(self,custom):#用户custom存在时调用
        self.content=custom
        self.engine.say(self.content)
        self.engine.runAndWait()







