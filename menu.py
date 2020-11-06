import os
import getpass
import time

os.system("tput setaf 4")
print("--------------------------------------------------------------------")
os.system("tput setaf 3")
print("\t\t\tWelcome to World Automation")
os.system("tput setaf 4")
print("--------------------------------------------------------------------")

password = getpass.getpass("Enter ur password : ")

os.system("tput setaf 1")
if password != "soul":
    print("password is incorrect ... ")
    exit()

# for remote and local system

operating_sys = input("Where u want to run prog ? (local/Remote) : ")
print(operating_sys)

while True:

    os.system("clear")
    os.system("tput setaf 2")
    print("""
    Press 1 : To deal  with linux 
    Press 2 : To deal with Docker 
    Press 3 : To deal with Hadoop
    Press 4 : To deal with AWS(Cloud)
    Press 5 : To exit from Prog
    """)

    choice = input("Enter your Choice : ")
    print(choice)

    if operating_sys == "local":
        if int(choice) == 1:
            os.system("clear")

            print("""
                 Press 1 : To run date
                 Press 2 : To run calendar
                 Press 3 : To check free ram
                 Press 4 : To check ip address
                 Press 5 : To exit from Prog
                 """)
            ch = input("Enter what  u want to do : ")

            if int(ch) == 1:
                os.system("date")
                time.sleep(10)
            elif int(ch) == 2:
                os.system("cal")
                time.sleep(10)

            elif int(ch) == 3:
                os.system("free -m")
                time.sleep(10)

            elif int(ch) == 4:
                os.system("ifconfig enp0s3")
                time.sleep(10)

            elif int(ch) == 5:
                exit()

            else:
                print("Not Supported")
                time.sleep(10)

        elif int(choice) == 2:
            os.system("clear")
            os.system("tput setaf 5")

            print("""
                         Press 1 : To start docker
                         Press 2 : To stop docker
                         Press 3 : To check docker info
                         Press 4 : To check docker help
                         Press 5 : To download image 
                         Press 6 : To check list of all images
                         Press 7 : To run docker os  
                         Press 8 : To run docker os in background
                         Press 9 : To run docker os for single command
                         Press 10 : To check current running os
                         Press 11 : To check all running os 
                         Press 12 : To exit 
                         """)
            ch = input("Enter what  u want to do : ")

            if int(ch) == 1:
                os.system("systemctl start docker")
                time.sleep(10)

            elif int(ch) == 2:
                os.system("systemctl stop docker")
                time.sleep(10)

            elif int(ch) == 3:
                os.system("docker info")
                time.sleep(10)

            elif int(ch) == 4:
                os.system("docker --help")
                time.sleep(10)
            elif int(ch) == 5:
                print("""
                image example 
                1. Centos 
                2. Fedora
                3. Ubuntu
                ...etc..
                     """)
                image = input("Enter the name of image ")
                os.system("docker pull {}".format(image))

            elif int(ch) == 6:
                os.system("docker images")
                time.sleep(10)
            elif int(ch) == 7:
                name = input("Enter the name of os")
                img = input("Enter the name of img")
                os.system("docker run -it --name {} {}".format(name, img))
            elif int(ch) == 8:
                name = input("Enter the name of os")
                img = input("Enter the name of image")
                os.system("docker run -dit --name {} {}".format(name, img))
            elif int(ch) == 9:
                name = input("Enter the name of os")
                img = input("Enter the name of image")
                cmd = input("Enter the command u want to run ")
                os.system("docker run -it --name {} {} {}".format(name, img, cmd))
                time.sleep(10)
            elif int(ch) == 10:
                os.system("docker ps")
                time.sleep(10)
            elif int(ch) == 11:
                os.system("docker ps -a")
                time.sleep(10)
            elif int(ch) == 11:
                exit()
            else:
                print("Not supported ")
                
        elif int(choice) == 3:     # hadoop local
            print("hadoop under process")
        elif int(choice) == 4:     # cloud local
            print("cloud under process")
        elif int(choice) == 5:
            exit()
        else:
            print("Not Supported")


# for remote stuff
    elif operating_sys == "remote":
        ip = input("Enter remote ip :")
        print(ip)
        if int(choice) == 1:
            os.system("clear")

            print("""
                 Press 1 : To run date
                 Press 2 : To run calendar
                 Press 3 : To check free ram
                 Press 4 : To check ip address
                 Press 5 : To exit from Prog
                 """)
            ch = input("Enter what  u want to do : ")

            if int(ch) == 1:
                os.system("ssh  {} date".format(ip))
                time.sleep(10)
            elif int(ch) == 2:
                os.system("ssh {} cal".format(ip))
                time.sleep(10)

            elif int(ch) == 3:
                os.system("ssh {} free -m".format(ip))
                time.sleep(10)

            elif int(ch) == 4:
                os.system("ssh {} ifconfig enp0s3".format(ip))
                time.sleep(10)

            elif int(ch) == 5:
                exit()

            else:
                print("Not Supported")
                time.sleep(10)

        elif int(choice) == 2:
            os.system("clear")
            os.system("tput setaf 5")

            print("""
                         Press 1 : To start docker
                         Press 2 : To stop docker
                         Press 3 : To check docker info
                         Press 4 : To check docker help
                         Press 5 : To download image 
                         Press 6 : To check list of all images
                         Press 7 : To run docker os  
                         Press 8 : To run docker os in background
                         Press 9 : To run docker os for single command
                         Press 10 : To check current running os
                         Press 11 : To check all running os 
                         Press 12 : To exit 
                         """)
            ch = input("Enter what  u want to do : ")

            if int(ch) == 1:
                os.system("ssh {} systemctl start docker".format(ip))
                time.sleep(10)

            elif int(ch) == 2:
                os.system("ssh {} systemctl stop docker".format(ip))
                time.sleep(10)

            elif int(ch) == 3:
                os.system("ssh {} docker info".format(ip))
                time.sleep(10)

            elif int(ch) == 4:
                os.system("ssh {} docker --help".format(ip))
                time.sleep(10)
            elif int(ch) == 5:
                print("""
                image example 
                1. Centos 
                2. Fedora
                3. Ubuntu
                ...etc..
                     """)
                image = input("Enter the name of image ")
                os.system("ssh {} docker pull {}".format(ip,image))

            elif int(ch) == 6:
                os.system("ssh {} docker images".format(ip))
                time.sleep(10)
            elif int(ch) == 7:
                name = input("Enter the name of os")
                img = input("Enter the name of os")
                os.system("ssh {} docker run -it --name {} {}".format(ip,name, img))
            elif int(ch) == 8:
                name = input("Enter the name of os")
                img = input("Enter the name of image")
                os.system("ssh {} docker run -dit --name {} {}".format(ip,name, img))
            elif int(ch) == 9:
                name = input("Enter the name of os")
                img = input("Enter the name of image")
                cmd = input("Enter the command u want to run ")
                os.system("ssh {} docker run -it --name {} {} {}".format(ip ,name, img, cmd))
                time.sleep(10)
            elif int(ch) == 10:
                os.system("ssh {} docker ps".format(ip))
                time.sleep(10)
            elif int(ch) == 11:
                os.system("ssh {} docker ps -a".format(ip))
                time.sleep(10)
            elif int(ch) == 12:
                exit()
            else:
                print("Not supported ")
            
        elif int(choice) == 3:     # hadoop remote
            print("hadoop under process")
        elif int(choice) == 4:     # cloud remote
            print("cloud under process")
        elif int(choice) == 5:
            exit()
        else:
            print("Not Supported")

    else:
        print("Not supported")
