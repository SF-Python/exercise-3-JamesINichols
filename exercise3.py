# checks the MAC address and displays the manufacturer
def main():
    # Create a list that maps hex digits to manufacturers
    mac_manufacturers = [
        ("00:00:17", "Oracle"),
        ("00:07:E9", "Intel Corporation"),
        ("04:27:28", "Microsoft Corporation"),
        ("04:26:65", "Apple, Inc."),
        ("04:33:89", "Huawei Technologies Co., Ltd"),
        ("00:00:0C", "Cisco Systems, Inc")
    ]
    
    # Print a welcome message
    print("MAC Manufacturer Program")
    print("------------------------")
    print()  # Print a blank line for better readability
    
    # Ask the user for the first 6 hex values of the MAC address
    user_input = input("Enter the first 6 hex values of the MAC address (format as XX:XX:XX): ")
    
    # Search through the list of tuples
    manufacturer = "Unknown"  # Default value
    for mac_prefix, name in mac_manufacturers:
        if user_input == mac_prefix:
            manufacturer = name
            break
    
    # Print the result
    print(f"For {user_input} the MAC manufacturer is {manufacturer}.")
    
# Call the main function if this file is run directly
if __name__ == "__main__":
    main()
