#Linuxhacker07
#COP2002.0T1 Exercise 2: Variables
#September 25, 2024
#Mac Manufacture Program
#program tells user what mac manufacturer is.
print("Mac Manufacture Program")
print("-----------------------")
print("Type exit to leave")
print("")
print("")
def main():
    MacNum = input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ")
    if MacNum == "00:00:17":
        print(f"For {MacNum} the MAC manufacturer is Oracle.")
        main()
    elif MacNum == "00:07:E9":
        print(f"For {MacNum} the MAC manufacturer is Intel Corporation.")
        main()
    elif MacNum == "04:27:28":
        print(f"For {MacNum} the MAC manufacturer is Microsoft Corporation.")
        main()
    elif MacNum == "04:26:65":
        print(f"For {MacNum} the MAC manufacturer is Apple, Inc.")
        main()
    elif MacNum == "04:33:89":
        print(f"For {MacNum} the MAC manufacturer is Huawei Technologies Co.,Ltd.")
        main()
    elif MacNum == "00:00:0C":
        print(f"For {MacNum} the MAC manufacturer is Cisco Systems, Inc.")
        main()
    elif MacNum == "exit":
        print("Goodbye!")
    else:
        print("Unknown")
        main()
if(__name__=="__main__"):
    main()