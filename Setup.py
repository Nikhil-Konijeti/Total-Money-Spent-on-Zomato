# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 16:15:19 2021

@author: nkonijeti

Run below command in cmd to generate the build folder which contains 
the executable file which can be ran on any Windows machine with Firefox/Chrome

python Setup.py build
"""

from cx_Freeze import setup, Executable
  
setup(name = "Zomato_Cost" ,
      version = "1.0" ,
      description = "Total Cost Spent Estimation in Zomato" ,
      executables = [Executable("Total_Money_Spent_On_Zomato.py")])