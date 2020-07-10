# MyWiFi
This bot was created for Discord Hack Week. Heimdallr Bot allows you to monitor your server and it's members and also allows you to communicate with developers without sending DM or joining the home server. It will share reports only with server owner and moderators.

# Requires
[Python 2.7](http://python.org/getit) 32bit,


# How To Use:

To Connect with wifi use
wifi.connect() // for default case
wifi.connect(name) // for saved . name ="saved wifi name"
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
