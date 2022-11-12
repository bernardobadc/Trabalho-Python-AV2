def converter_hora(horas, min):
  nova_hora = hora if hora <=12 else hora - 12
  AM_PM = "AM" if hora <12 else "PM"
  return str(nova_hora)+":"+str(min) + AM_PM
  
while True:
   hora = int(input("Digite a hora ou digite hora negativa para encerrar o programa:"))
   if hora < 0:
    break
   min = int(input("Digite os minutos:"))
   print(converter_hora(hora,min))