# Jordan Griffin (jordangriffin800)
# COP2002-0T1
# September 23, 2024
# Exercise 3: If Statements
# Create a program that asks students to enter a hex digit code from a NIC card to see which manufacturer it belongs to.

print("MAC Manufacturer Program")

print("------------------------")

print()

# get OUI from user

userHexDigits = input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ")

if("00:00:17" == userHexDigits):
    print(f"For {userHexDigits} the MAC manufacturer is Oracle.")

elif("00:07:E9" == userHexDigits):
    print(f"For {userHexDigits} the MAC manufacturer is Intel Corporation.")

elif("04:27:28" == userHexDigits):
    print(f"For {userHexDigits} the MAC manufacturer is Microsoft Corporation.")

elif("04:26:65" == userHexDigits):
    print(f"For {userHexDigits} the MAC manufacturer is Apple, Inc.")

elif("04:33:89" == userHexDigits):
    print(f"For {userHexDigits} the MAC manufacturer is Huawei Technologies Co.,Ltd.")

elif("00:00:0C" == userHexDigits):
    print(f"For {userHexDigits} the MAC manufacturer is Cisco Systems, Inc.")

else:
    print("Unknown")