"""
i t n o A
MyWiFi , by Shakil Ibne Shaikh
https://github.com/ShakilShaikh/


wifi=WiFi()
To Connect with wifi use
wifi.connect() // for default case
wifi.connect(name) // for saved self . name =saved_wifi_name
wifi.connect(name,password) // To connect with new wifi. name=ssid password=password

To Turn Off or disconnect the wifi use
wifi.disconnect()

To Scan available networks use
wifi.scan()      // to scan ssids and save in self.res
wifi.get_ssid()  // returns scanned networks [[id,name]]
wifi.getProfile[wifi_name] // to see details of scanned network
   |__ ssid      // wifi name
   |__ id        // id
   |__ ntypes    // type of network
   |__ bssid     // mac
   |__ signal    // how strong the signal is
   |__ radio     // type of radio
   |__ channel   // which channel on it
   |__ BasicRate // rates as Array
   |__ OtherRate // rates as Array

wifi.defname(string) // to setup default case

"""

# ==================== Imports ====================
import subprocess
import sys
from Exceptions import *
from Profiles import *
import warnings
# --------------------- X -------------------------

__version__ = '3.0.1'

class WiFi:
    def __init__(self):
        import subprocess,sys,warnings
        from Exceptions import *
        from Profiles import *
        
        self.spk=''
        self.res=''
        self.ssid=[]
        self.prof=[]
        self.__default=''
        self.getProfiles()
        self.getProfile={}
        self.__names=[]
        #if defaultValue=='':
            #warnings.warn("Default name is Empty run SetupMode",StartupError)
        self.__default='' #defaultValue
    def defname(self,string):
        self.__default=string
    def scan(self): # Scan networks
        try:
            x=subprocess.check_output(('netsh wlan show networks mode=Bssid'),shell=True)
            self.spk=x[49:88]
            self.res=x[89:].strip()
            ww=self.res.split('\n')
            self.ssid=[]
            for w in ww:
                aa=w.split()
                if not aa:
                    pass
                elif aa[0]=='SSID':
                    ID=aa[1]
                    name = ' '.join(aa[3:])
                    self.ssid.append([ID,name])
                    self.__names.append(name)
                    self.getProfile[name]=Profiles()
                    self.getProfile[name].ssid=name
                    self.getProfile[name].id=ID
                elif aa[0]+aa[1]=='Networktype':
                    self.getProfile[name].ntype=aa[3]
                elif aa[0]=='Encryption':
                    self.getProfile[name].encryption=aa[2]
                elif aa[0]=='BSSID':
                    self.getProfile[name].bssid=aa[-1]
                elif aa[0]=='Signal':
                    self.getProfile[name].signal=aa[-1]
                elif aa[0]=='Radio':
                    self.getProfile[name].radio=aa[-1]
                elif aa[0]=='Channel':
                    self.getProfile[name].channel=aa[-1]
                elif aa[0]+aa[1]=='Basicrates':
                    self.getProfile[name].BasicRate=aa[4:]
                elif aa[0]+aa[1]=='Otherrates':
                    self.getProfile[name].BasicRate=aa[4:]
        except subprocess.CalledProcessError:
            raise WiFiScanningError,WiFiScanningError('WiFi was unable to connect'),sys.exc_info()[2]            

    def getProfiles(self): # Show Details
        x=subprocess.check_output(('netsh wlan show profiles'),shell=True)
        x=x[-90:].replace('\r','')
        x=x.split('\n')[1:]
        n=len(x)
        self.prof=[]
        for i in range(n):
            if x[i]!='':
                net=x[i].split()
                net=' '.join(net[4:])
                self.prof.append([i+1,net])
                self.prof.sort()
    def showProfiles(self):
        self.getProfiles()
        for w in self.prof:
            print w

    def profile_id(self,*id): # Saved Profile by ID
        if not id:
            self.showProfiles(network)
        else:
            id=id[0]-1
            return self.prof[(id)][1]


    def get_ssid(self,*num): # SSIDs by ID
        if not num:
            return self.ssid
                
        else:
            num=num[0]
            return self.ssid[num-1][1]
            
    def connect(self,*arg): # Connects and auto connect
        self.scan()
        if not arg:
            wssid=self.__default
            if wssid=='':
                raise DefaultKeyError,DefaultKeyError("Missing Default Network name"),sys.exc_info()[2]
        elif len(arg)==1:
            wssid=arg[0]
        try:
            if self.default in self.prof:
                if self.default in self.__names:
                    x=subprocess.check_output(('netsh wlan connect name="'+wssid+'"'),shell=True)
                else:
                    raise WiFiOutOfRange,WiFiOutOfRange('This one is not saved in profile'),sys.exc_info()[2]
            else:
                raise AuthenticationError,AuthenticationError('\''+wssid+'\' This one is not saved in profile'),sys.exc_info()[2]
        except subprocess.CalledProcessError:
            raise WiFiConnectionError,WiFiConnectionError('WiFi was unable to connect'),sys.exc_info()[2]
        else:
            self.b_connect(arg[0],arg[1])
    def b_connect(self,ssid,key):
        try:
            x=subprocess.check_output(('netsh wlan set hostednetwork mode=allow ssid="'+ssid+'" key="'+key+'"'),shell=True)
            self.res=True
        except subprocess.CalledProcessError:
            self.res=False
            raise DriverError,DriverError('\''+wssid+'\' This one is not saved in profile'),sys.exc_info()[2]
    def credit(self):
         print "MyWiFi the WiFi module for python.\nVersion 3.0.1\nMade By Shakil Ibne Shaikh\nGithub : https://github.com/ShakilShaikh/"

    def disconnect(self):
        x=subprocess.check_output(('netsh wlan disconnect'),shell=True)

#default=''
network='profiles'
wifi=WiFi()

