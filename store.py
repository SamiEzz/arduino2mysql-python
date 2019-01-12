# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 13:44:08 2019

@author: Sami
"""


import mysql.connector
import serial
from time import sleep
import datetime

db_name = "smarthome_baby"
step_time = 60



def serial_parser(string):
    string = string.decode("utf-8") 
    string = string[0:len(string)-2]
    string = float(string)
    return string

def connect_to_db(db):
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      database=db
    )
    return mydb

def create_table(mydb):
    sql = "CREATE TABLE `smarthome_baby`.`temperature` ( `id` INT(255) NOT NULL AUTO_INCREMENT , `time` TEXT NULL DEFAULT NULL , `temperature` FLOAT NULL DEFAULT NULL ,  INDEX `id_h` (`id`)) ENGINE = InnoDB;"
    mycursor = mydb.cursor()
    mycursor.execute(sql)

def send_data(_val):
    mydb = connect_to_db(db_name)
    #create_table(mydb)
    val=_val
    timern=datetime.datetime.now()
    timern=timern.strftime("%Y-%m-%d %H:%M:%S")
    mycursor = mydb.cursor()
    sql = "INSERT INTO `temperature` (`time`, `temperature`) VALUES "
    sql = sql + "('"+timern +"','" + str(val) + "');"
    #print(sql)
    mycursor.execute(sql)
    mydb.commit()
    mydb.disconnect()
    
def get_data():
    ser = serial.Serial(port='COM4',baudrate=9600)
    val = ""
    val=ser.readline()
    val=serial_parser(val)    
    ser.close()
    return val


#---------------------------------------------------------------------


while(1):
    table=[]
    for i in range(3):
        val = get_data()
        table.append(val)
        print("#"+str(val))
        sleep(step_time)
        
    data2send=int(table[0]+table[1]+table[2])/3
    data2send=int(data2send)
    print(data2send)
    send_data(data2send)