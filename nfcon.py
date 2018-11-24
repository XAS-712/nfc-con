import subprocess
import time

FUNC_TEXT=[
    "[A] Call \"nfc-list\" to show the card info.",
    "[B] Read Mifare Classic card to a dump file.",
    "[C] Write Mifare Classic card with a dump file.",
    "[D] Format Mifare Classic card with the key file."
    "[E] Crack half-encrypted Mifare classic card and export the key file.",
]

def funcA():
    subprocess.call("nfc-list",shell=True)

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
    choice=input("Select a function:(Q for quit) ")
    choice=choice.upper()
    if choice=="Q":
        exit()
    elif choice=="A":
        funcA()
    else:
        print("Func not supported.")
        continue
