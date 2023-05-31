año_actual=2023
import datetime
nombre=input('¿Cuál es tu nombre(s)?')
apellido=input('¿Cuál es tu primer apellido?')
segundoapellido=input('¿Cuál es tu segundo apellido?')
año=input('¿En qué año naciste?')
mesdia=input('¿En qué mes y día naciste? (en el siguiente formato “mm-dd”)')
mesdia = datetime.datetime.strptime(mesdia, '%M-%d')

#Impresión A
nombreyapellidomayusc=nombre+" "+apellido+" "+segundoapellido
print('Este es tu nombre completo en mayúsculas ',nombreyapellidomayusc.upper())

#Impresión B
nombreyapellidominusc=nombre+" "+apellido+" "+segundoapellido
print('Este es tu nombre completo en minúsculas ',nombreyapellidominusc.lower())

#Impresión C no he visto el uso de datetime completamente aún

#Impresión D va relacionado a datetime, no lo he visto aún

#Impresión E
vocales = "aeiou"
conteo = 0
for comparar in nombreyapellidomayusc:
  if comparar in vocales:
    conteo = conteo + 1
print('Tu nombre completo tiene ',str(conteo),' vocales')

#Impresión F
nombrecompleto=nombre+apellido+segundoapellido
print('Tu nombre completo tiene ',len(nombrecompleto),' letras')

#Impresión H
nombreyapellidos=nombre + ' ' + apellido + ' ' + segundoapellido
esalfa=nombreyapellidos.isalpha()
print('¿Tu nombre completo es un carácter de tipo alfanumérico? ', esalfa)

#Las fechas no las he visto aún (prueba2)
