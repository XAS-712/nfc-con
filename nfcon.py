import subprocess
import time
import os
import random

FUNC_TEXT=[
    "[A] Call \"nfc-list\" to show the card info.",
    "[B] Read Mifare Classic card to a dump file.",
    "[C] Write Mifare Classic card with a dump file.",
    "[D] Format Mifare Classic card with the key file.",
    "[E] Crack half-encrypted Mifare classic card and export the key file.",
    "[F] Reset Uid.",
]

def Ls():
    subprocess.call("ls -lAh mfd | grep \.mfd$",shell=True)

def funcA():
    subprocess.call("nfc-list",shell=True)

def funcB():
    cmdline="nfc-mfclassic"
    IsMCard=input("Is your card a magic card?(y/N)")
    IsMCard=IsMCard.upper()
    if IsMCard=="Y":
        print("[Using magic card]")
        cmdline = cmdline + " R"
    else:
        print("[Using normal card]")
        cmdline = cmdline + " r"
    KeyAB=input("Use KeyA or KeyB?(A/b)").upper()
    if KeyAB == "B":
        print("[Using KeyB]")
        cmdline = cmdline + " b"
    else:
        print("[Using KeyA]")
        cmdline = cmdline + " a"
    cmdline = cmdline + " u"		#if your version does not contain this param, comment this line.
    mfdName = input("Dump filename:(Enter for datetime-named)") + ".mfd"
    if mfdName == ".mfd":
        mfdName = time.strftime('%Y%m%d_%H:%M:%S',time.localtime(time.time())) + mfdName
    cmdline = cmdline+" mfd/"+mfdName
    if IsMCard != "Y":
        Ls()
        keyFile = input("You should provide a dump file with correct keys so that we can access the card.\nKey file:(without \".mfd\",Enter for default)")
        if keyFile is not "":
            keyFile="mfd/" +keyFile+".mfd"
            if os.path.exists(keyFile):
                cmdline=cmdline+" "+keyFile + " f" #use f to pass uid verify
            else:
                print("[Key file not found. Use default keys]")
        else:
            print("[Using default keys]")
    subprocess.call(cmdline,shell=True)

def funcE():
    cmdline="mfoc"
    mfdName = input("Dump filename:(Enter for datetime-named)") + ".mfd"
    if mfdName==".mfd":
        mfdName = time.strftime('ck_%Y%m%d_%H:%M:%S',time.localtime(time.time())) + mfdName
    cmdline=cmdline + " -O mfd/"+mfdName
    subprocess.call(cmdline,shell=True)

def funcF():
    cmdline="nfc-mfsetuid"
    uid=input("Reset Uid(like E627AC10) to:(Enter for a random one)").upper()
    if uid=="":
        randomint=random.randint(0,4294967295)
        uid="%08X" % randomint
        print("[Generated Uid " + uid +"]")
    formatcard=input("Do you want to format it?(y/N)").upper()
    if formatcard=="Y":
        cmdline=cmdline+" -f"
    if len(uid)==12:
        datestr=str(int(uid[-4:]))
        uid=uid[0:8]
        print("[Using custom produce date %s]" % datestr)
        cmdline=cmdline+" "+uid+"2B0804000129013AF604"+datestr
    else:
        datestr=time.strftime("%W%y")
        cmdline=cmdline+" "+uid+"2B0804000129013AF604"+datestr
    subprocess.call(cmdline,shell=True)

print("-"*24)
print("#"*7 + "NFCConsole" + "#"*7)
print("-"*24)
print("Hi, it's " + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + " now.")
print("This is a interactive CLI for nfc tools.")
while True:
    print("-"*24)
    print("Functions:")
    for functext in FUNC_TEXT:
        print(functext)
    print("-"*24)
    choice=input("Select a function:(Q for quit,L for list dumps) ")
    choice=choice.upper()
    if choice=="Q":
        exit()
    elif choice=="L":
        Ls()
    elif choice=="A":
        funcA()
    elif choice=="B":
        funcB()
    elif choice=="F":
        funcF()
    else:
        print("Func not supported.")
        continue
