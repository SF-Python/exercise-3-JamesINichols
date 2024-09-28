# Jordan Colefield (Jordan-sfcollege)
# COP2002-0T1
# September 19, 2024
# Exercise 3
# This program helps the user identify a NIC card manufacturer using the first 6 hex digits of it's MAC address

# Create variables to store the manufacturer table
oracle="00:00:17"
intelCorporation="00:07:E9"
microsoftCorporation="04:27:28"
appleInc="04:26:65"
huaweiTechnologies="04:33:89"
ciscoSystems="00:00:0C"

# List of variables and the corresponding names for reference in the following lines of code
hexValues=[oracle, intelCorporation, microsoftCorporation, appleInc, huaweiTechnologies, ciscoSystems]
brands=["Oracle", "Intel Corporation", "Microsoft Corporation", "Apple, Inc", "Huawei Technologies Co.,Ltd", "Cisco Systems, Inc"]

# Printing information about the program
print("MAC Manufacturer Program")
print("------------------------")
print()

macAddress=input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ") # Allows the user to input the hex values

# Comparison of user input to lists above
if(macAddress==hexValues[0]):
    answer=brands[0]
elif(macAddress.upper()==hexValues[1]):
    answer=brands[1]
elif(macAddress==hexValues[2]):
    answer=brands[2]
elif(macAddress==hexValues[3]):
    answer=brands[3]
elif(macAddress==hexValues[4]):
    answer=brands[4]
elif(macAddress.upper()==hexValues[5]):
    answer=brands[5]
else:
    answer="Unknown"

print(f"For {macAddress} the MAC manufacturer is {answer}.") # Prints the manufacturer based on the above comparisons