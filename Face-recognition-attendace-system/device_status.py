from boltiot import Bolt
import main
api_key = "botlapikey"
device_id  = "BOLTdeviec id"
mybolt = Bolt(api_key, device_id)
response = mybolt.isOnline()
aktemp=mybolt.analogRead('A0')
#print(aktemp[11:14])
aktemp_final=int(aktemp[11:14])*0.0977
if(34.1<=aktemp_final<=38):
    main.mainMenu()
else:
    print("Your Body Temperature is so High Please go to Hospital or take some rest")
print (response)

