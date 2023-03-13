import argparse
from random import randint
from .file_maker import new_file_maker
import zipfile
from os import makedirs

def main():
    def validated(desc,type):
            while(True):
                print("\n"+desc)
                temp = input("=> ").strip()
                if (temp != ""):
                    if type=='str' and not any([i.isnumeric() for i in list(temp)]):
                        return temp
                    if type=='num' and temp.isnumeric():
                        return temp

    file_num = validated("How many files would you need ?",'num')
    assn_num = validated("Which assignment is this ?",'num')
    name = validated("What is the programmer's full name ?",'str')

    makedirs("assignment"+assn_num.zfill(2))
    for i in range(1,int(file_num)+1):
        file_props = [] 
        print("\n----------------Generating file no."+str(i)+"------------------------]\n")
        file_props.append(validated("What is the name of the program",'str'))
        file_props.append(validated("What is this program about ?(This program ...)",'str'))
        file_props.append(validated("How many functions does it have ?",'num'))
        file_props.append(randint(10,30))
        file_props.append(name)
        file_props.append(assn_num)
        file_name = 'assignment'+assn_num.zfill(2)+'p'+str(i).zfill(2)
        

        new_file_maker(file_name,file_props)


