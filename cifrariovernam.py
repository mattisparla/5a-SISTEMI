#cifrario di vernam
#chiave, parola che le due persone che devono comunicare devono conoscere
import socket

chiave="biboplayer"
parola="ciao"
convFinal=""

if(len(parola) < len(chiave)):
    for k,lettera in enumerate(parola):
        convFinal+=chr(((ord(lettera)-97)+(ord(chiave[k])-97))%26 + 97)

else:
    print("La parola e troppo lunga \n");

print(convFinal)

convFinal="ccpbvtoprf"
conv=""
if(len(parola) < len(chiave)):
    for k,lettera in enumerate(convFinal):
        conv+=chr(((ord(lettera)-97)-(ord(chiave[k])-97))%26 + 97)

else:
    print("La parola e troppo lunga \n");

print(conv)

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while(True):
    stringa=input("Inserisic una stringas")
    s.sendto(stringa.encode(),("192.168.188.107",5000))