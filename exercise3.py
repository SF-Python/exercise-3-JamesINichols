# Kameron Kinsman(Kam33-class)
# COP2002.OT1
# 9/21/2024
# exercise3
# This Program will use if statemnts to help students determine who the manufacturer is for the NIC card the user inputs.

# Defining main as the program to get the MAC manufacturer.
def main():
    print("MAC Manufacturer Program")
    print("------------------------\n")
    
    # Prompting the user to enter the first 6 hex values of the MAC address and assigning that input to the variable hex_digits.
    hex_digits = input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ")

    # Using if...elif...else statements to check the hex_digits.
    if hex_digits == "00:00:17":
        manufacturer = "Oracle"
    elif hex_digits == "00:07:E9":
        manufacturer = "Intel Corporation"
    elif hex_digits == "04:27:28":
        manufacturer = "Microsoft Corporation"
    elif hex_digits == "04:26:65":
        manufacturer = "Apple, Inc."
    elif hex_digits == "04:33:89":
        manufacturer = "Huawei Technologies Co.,Ltd"
    elif hex_digits == "00:00:0C":
        manufacturer = "Cisco Systems, Inc"
    else:
        manufacturer = "Unknown"

    # Printing the manufacturer result.
    print(f"For {hex_digits} the MAC manufacturer is {manufacturer}.")

# Calling main function to execute.
if(__name__=="__main__"):
    main()
