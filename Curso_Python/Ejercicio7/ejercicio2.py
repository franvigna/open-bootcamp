from datetime import datetime
now = datetime.now()


hora = now.hour
minutos = now.minute
segundos = now.second

if hora >= 19:
    print('Es la hora de ir a casa')
    
else:
    print('faltan {} horas, {} minutos y {} segundos para ir a casa'.format(18 - hora,59 - minutos, 59 - segundos))
