print("MAC Manufactgurer Program")
print("--------------------------")
print()
user_answer=input("Enter the first 6 hex values for MAC address (format as XX:XX:XX): ")
if ("00:00:17"==user_answer):
    print("For 00:00:17 the MAC manufacturer is Oracle.")
elif ("00:07:E9"==user_answer):
    print("For 00:07:E9 the MAC manufacturer is Intel Corporation.")
elif ("04:27:28"==user_answer):
    print("For 04:27:28 the MAC manufacturer is Microsoft Corporation.")
elif ("04:26:65"==user_answer):
    print("For 04:26:65 the MAC manufacturer is Apple, Inc..")
elif ("04:33:89"==user_answer):
    print("For 04:33:89 the MAC manufacturer is Huawei Technologies Co.,Ltd.")
elif ("00:00:0C"==user_answer):
    print("For 00:00:0C the MAC manufacturer is Cisco Systems, Inc.")
else:
    ("<Not valid value or not found>")