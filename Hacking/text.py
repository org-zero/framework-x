#testeado con un ZTE N720
#!/usr/bin/env python
import gammu
import sys
 
sm = gammu.StateMachine() #stateMachine para comunicacion con el dispositivo
sm.ReadConfig() # lee (~/.gammurc)
sm.Init() # inicializar conexion al dispositivo

# armado de la estructura para el sms
message = {
    'Number': '+50660143284',# aca numero de telefono de destino (incluir codigo de pais '+58' = venezuela)
    'SMSC': {'Number': '+581234567891'},# numero de telefono de origen
    'Text': 'Hola gammu dese piton!',# texto del mensaje a enviar
    'Class': 0,
}

sm.SendSMS(message) #funcion para enviar el mensaje