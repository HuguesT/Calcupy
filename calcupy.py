# -*- coding:utf-8 -*-
import time
ope = ""
while True:
  print("Calcupy v1 by Hugues THOMAS \n Pour une addition tapez + \n Pour une soustration tapez - \n Pour faire une multiplication tapez x \n Pour une division tapez /")
  ope = input("Que souhaitez-vous faire ? : ")

  if ope == "+":
   print("Vous avez choisi de faire une addition.")
   a1 = float(input("Quel est le premier nombre ? : "))
   a2 = float(input("Quel est le deuxième nombre ? : "))
   a3 = a1 + a2
   print( a3 )
   break
  elif ope == "-":
   print("Vous avez choisi de faire une soustraction")
   a1 = float(input("Quel est le premier nombre ? : "))
   a2 = float(input("Quel est le deuxième nombre ? : "))
   a3 = a1 - a2
   print( a3 )
   break
  elif ope == "x":
   print("Vous avez choisi de faire une multiplication")
   a1 = float(input("Quel est le premier nombre ? : "))
   a2 = float(input("Quel est le deuxième nombre ? : "))
   a3 = a1 * a2
   print( a3 )
   break
  elif ope == "/":
   print("Vous avez choisi de faire une division")
   a1 = float(input("Quel est le premier nombre ? : "))
   a2 = float(input("Quel est le deuxième nombre ? : "))
   a3 = a1 / a2
   print( a3 )
   break
  else:
   print("! Veuillez choisir une opération valide !")
   print("----")
   continue 

