# Jaden Donda
# F24 COP2002.0T1: PROGRAM LOGIC
# 9/21/24
# MAC Manufacturer Program - A program that asks the user for the first 6 hex digits formatted as XX:XX:XX and provides the manufacturer

def main():
   # creating chart to connect hex digits to manufacturers
    mac_manufacturers = {
        "00:00:17": "Oracle",
        "00:07:E9": "Intel Corporation",
        "04:27:28": "Microsoft Corporation",
        "04:26:65": "Apple, Inc.",
        "04:33:89": "Huawei Technologies Co.,Ltd",
        "00:00:0C": "Cisco Systems, Inc"
    }

       # program title
    print("MAC Manufacturer Program")  # MAC output statement
    print("-------------------------")  # dashes output statement
    print()  # (blank line)
    
       # asking for MAC address using the first 6 hex digits
    mac_input = input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ").upper()

       # find manufacturer based on the provided input
    manufacturer = mac_manufacturers.get(mac_input, "< Invalid value or not found>")
    
       # display result
    if manufacturer != "<Invalid value or not found>":
        print(f"\nFor {mac_input}, the MAC manufacturer is {manufacturer}.")
    else:
        print(f"\n{mac_input} is invalid or not found.")

    # calling main function
if __name__ == "__main__":
    main()

