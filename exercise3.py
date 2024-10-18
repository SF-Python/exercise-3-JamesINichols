def get_manufacturer(hex_digits):
    manufacturers = {
        "00:00:17": "Oracle",
        "00:07:E9": "Intel Corporation",
        "04:27:28": "Microsoft Corporation",
        "04:26:65": "Apple, Inc.",
        "04:33:89": "Huawei Technologies Co., Ltd.",
        "00:00:0C": "Cisco Systems, Inc."
    }
    
    return manufacturers.get(hex_digits.upper(), "Unknown Manufacturer")

def main():
    hex_input = input("Please enter the first 6 hex digits of the MAC address (format: XX:XX:XX): ").strip()
    
    if len(hex_input) != 8 or hex_input[2] != ':' or hex_input[5] != ':':
        print("Invalid format. Please ensure you enter in the format XX:XX:XX.")
        return
    
    manufacturer = get_manufacturer(hex_input)
    
    print(f"The manufacturer for the NIC card with hex digits {hex_input} is: {manufacturer}")

if __name__ == "__main__":
    main()
