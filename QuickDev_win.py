import os
import time
import ctypes

 
displayMenu = True

print("    //    ) )                                 //    ) )                                ")
print("   //    / /          ( )  ___     / ___     //    / /  ___                            ")
print("  //    / / //   / / / / //   ) ) //\ \     //    / / //___) ) ||  / /                 ")
print(" //  \ \ / //   / / / / //       //  \ \   //    / / //        || / /                  ")
print("((____\ \ ((___( ( / / ((____   //    \ \ //____/ / ((____     ||/ /                   ")
print("        -by dillonf.me                                                                 ")
print(" ")
print("QuickDev is an easy to use dev menu for people who are getting started with or don't like CMD")
print(" ")
print(" ")



while displayMenu == True:
    print("           Menu            ")
    print("---------------------------")
    print("1) IP Info ")
    print("2) Traceroute")
    print("3) Ping")
    print("4) Group Policy Update")
    print("98) Custom Command")
    print("99) Exit")
    option = int(input("Choose an option: "))
    displayMenu = False


while True:
       
    if option == 1:
        os.system("cls")
        os.system("ipconfig")
        input("Press enter to continue")
        os.system("cls")
        displayMenu = True
        while displayMenu == True:
            print("           Menu            ")
            print("---------------------------")
            print("1) IP Info ")
            print("2) Traceroute")
            print("3) Ping")
            print("4) Group Policy Update")
            print("98) Custom Command")
            print("99) Exit")
            option = int(input("Choose an option: "))
            displayMenu = False
       
    if option == 2:
        os.system("cls")
        traceadd = input("Address to trace, for example, dillonf.me: ")
        os.system("tracert " +traceadd)
        input("Press enter to continue...")
        os.system("cls")
        displayMenu = True
        while displayMenu == True:
            print("           Menu            ")
            print("---------------------------")
            print("1) IP Info ")
            print("2) Traceroute")
            print("3) Ping")
            print("4) Group Policy Update")
            print("98) Custom Command")
            print("99) Exit")
            option = int(input("Choose an option: "))
            displayMenu = False
       

    if option == 3:
        os.system("cls")
        pingadd = input("Address to ping, for example, dillonf.me: ")
        os.system("ping " +pingadd)
        input("Press enter to continue...")
        os.system("cls")
        displayMenu = True
        while displayMenu == True:
            print("           Menu            ")
            print("---------------------------")
            print("1) IP Info ")
            print("2) Traceroute")
            print("3) Ping")
            print("4) Group Policy Update")
            print("98) Custom Command")
            print("99) Exit")
            option = int(input("Choose an option: "))
            displayMenu = False
       

    if option == 4:
        os.system("cls")
        os.system("gpupdate")
        os.system("cls")
        displayMenu = True
        while displayMenu == True:
            print("           Menu            ")
            print("---------------------------")
            print("1) IP Info ")
            print("2) Traceroute")
            print("3) Ping")
            print("4) Group Policy Update")
            print("98) Custom Command")
            print("99) Exit")
            option = int(input("Choose an option: "))
            displayMenu = False
       
        
    
    if option == 98:
        customcmd = input("Custom Command:")
        os.system("cmd")
        displayMenu = True
        while displayMenu == True:
            print("           Menu            ")
            print("---------------------------")
            print("1) IP Info ")
            print("2) Traceroute")
            print("3) Ping")
            print("4) Group Policy Update")
            print("98) Custom Command")
            print("99) Exit")
            option = int(input("Choose an option: "))
            displayMenu = False
       
       

    if option == 99:
        os.system("cls")
        print("Goodbye!")
        time.sleep(2)
        raise SystemExit()

else:
    print("ERROR")
