def hex_to_bin(hex):
    if(hex=='0'):
        return 0,0,0,0
    elif(hex=='1'):
        return 0,0,0,1
    elif(hex=='2'):
        return [0,0,1,0]
    elif(hex=='3'):
        return [0,0,1,1]
    elif(hex=='4'):
        return [0,1,0,0]
    elif(hex=='5'):
        return [0,1,0,1]
    elif(hex=='6'):
        return [0,1,1,0]
    elif(hex=='7'):
        return [0,1,1,1]
    elif(hex=='8'):
        return [1,0,0,0]
    elif(hex=='9'):
        return [1,0,0,1]
    elif(hex=='A'):
        return [1,0,1,0]
    elif(hex=='B'):
        return [1,0,1,1]
    elif(hex=='C'):
        return [1,1,0,0]
    elif(hex=='D'):
        return [1,1,0,1]
    elif(hex=='E'):
        return [1,1,1,0]
    elif(hex=='F'):
        return [1,1,1,1]
def print_data_(list_of_spaces,k,start):
    for i in range(list_of_spaces[-1]+1):
        if(i in list_of_spaces):
            print("| ",end="")
        if(i<list_of_spaces[-1]):
            print(k[start+i],end=" ")

   
def show_ipv4(l):
    k=[]
    for i in l:
        k=k+list(hex_to_bin(i[0]))+list(hex_to_bin(i[1]))
    print("\n\n******************************IPv4 header************************************")
    print("---------------------------------------------------------------------")
    print("|version  | header  | type_of_Service |     total_length                |")
    print("|(4bits)  | (4bits) |      (8bits)    |     (16bits)                    |")
    print_data_([0,4,8,16,32],k,0)
    print("\n---------------------------------------------------------------------")
    print("|        identification           | 0 | DF| MF|    fragment offset        |")
    print("|        (16bits)                 |   |   |   |     (13bits)              |")
    print_data_([0,16,17,18,19,32],k,32)
    print("\n---------------------------------------------------------------------")
    print("|  time to live   |protocol         |     header checksum             |")
    print("|        (8bits)  |   (8 bits)      |           (16bits)              |")
    print_data_([0,8,16,32],k,64)
    print("\n---------------------------------------------------------------------")
    print("|    source IP address                                            |")
    print_data_([0,32],k,96)
    print("\n-------------------------------------------------------------------")
    print("|    Destination IP address                                       |")
    print_data_([0,32],k,128)
    print("\n-------------------------------------------------------------------")
    for i in range(128,len(k)):
        if(i%32==0):
            print("|",k[i],end=" ")
        else:
            print(k[i],end=" ")
def show_tcp(l):
    k=[]
    for i in l:
        k=k+list(hex_to_bin(i[0]))+list(hex_to_bin(i[1]))
    print("\n\n\n\n\n\n******************************TCP header************************************")
    print("---------------------------------------------------------------------")
    print("|        source port              |     Destination port            |")
    print("|         (16bits)                |     (16bits)                    |")
    print_data_([0,16,32],k,0)
    print("\n---------------------------------------------------------------------")
    print("|                            sequence number                      |")
    print("|                                (32bits)                         |")
    print_data_([0,32],k,32)
    print("\n---------------------------------------------------------------------")
    print("|                            Acknowledgement                      |")
    print("|                                (32bits)                         |")
    print_data_([0,32],k,64)
    print("\n-----------------------------------------------------------------------------------")
    print("|headerlen|   Reserved  |URG|ACK|PSH|RST|SYN|FIN|             WINDOW SIZE         |")
    print("| (4bits) |   (6 bits)  |   |   |   |   |   |   |               (16 bits)         |")
    print_data_([0,4,10,11,12,13,14,15,16,32],k,96)
    print("\n----------------------------------------------------------------------------------")
    print("|        TCP checksum             |      Urgent pointers            |")
    print("|         (16bits)                |     (16bits)                    |")
    print_data_([0,16,32],k,128)
    print("\n---------------------------------------------------------------------")
    print("|                          option and padding                     |")
    for i in range(128,len(k)):
        if(i%32==0):
            print("|",k[i],end=" ")
        else:
            print(k[i],end=" ")
    print("|")
    
    
while(1):
    k=input("Enter the Hex packet : ")
    k=k.split(" ")
    ip=k[14:34]
    l=k[34:54]
    show_ipv4(ip)
    show_tcp(l)
