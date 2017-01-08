import serial
import database

ser = serial.Serial('/dev/ttyUSB0',9600)
db =database.DataBase()
while True:
    data = ser.read(3)
    db.UpdateData( int(3) )
