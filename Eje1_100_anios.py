# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 23:17:28 2021

@author: User
"""
Nombre = input("¿Cual es tu nombre? : ")
edad = int(input("¿Cuantos años tienes o cuantos cumples este año ? : "))

nacimiento = 2021 - edad

cien = nacimiento + 100


if edad <= 100:

    print(Nombre, "cumpliras 100 años en", cien)
    
elif edad >= 2122:
    p = cien * -1
    print(Nombre, "cumpliste 100, en el año", p, "antes de cristo, si estuvieses vivo tendrias:", edad, "años")
else:

    print(Nombre, "cumpliste 100 años en el", cien)
