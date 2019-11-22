import nmap as e

SCANNER = 0
CHOICE = 1
IP_ADDRESS = 2
"""
You need to start this script with root access.
"""


def enable_scan():
    """
    This function will enable the scanner
    :return:
    """
    scanner = e.PortScanner()
    print("Welcome this is only one feature of nmap tools ")
    return scanner


def get_user_information(scanner):
    """
    This function get IP Address from the user and the choice.
    :param scanner: Nmap Scanner already initialized
    :return:
    """
    ip_addr = input("Please can you enter the ip address to scan ")
    print("The ip address to scan is {} ".format(ip_addr))
    type(ip_addr)
    choice = input(""" \n Please enter your choice :
                      1) SYN ACK Scan
                      2) UDP Scan
                      3) Comprehensive Scan \n""")

    print("You have choice {} ".format(choice))
    return (scanner,choice,ip_addr)


def define_choice(scanner,choice,ip_addr):
    """
    This function made a switch between the user choice.
    :param scanner: nmap scanner
    :param choice: user choice 1,2,3
            1 - SYN ACK SCAN to detect the port open
            2 - UDP Scan
            3 - Comprehensive Scan
    :param ip_addr:
    :return:
    """
    if choice == "1":
        print("nmap version {}".format(scanner.nmap_version()))
        scanner.scan(ip_addr,'1-1024','-v -sS')
        res = scanner.scaninfo()
        print(res)
        print("IP status is {}".format(scanner[ip_addr].state()))
        print(scanner[ip_addr].all_protocols())
        print(scanner[ip_addr]['tcp'].keys())
    elif choice == "2":
        print("nmap version {}".format(scanner.nmap_version()))
        scanner.scan(ip_addr, '1-1024', '-v -sU')
        print(scanner.scaninfo())
        print("IP status is {}".format(scanner[ip_addr].state()))
        print(scanner[ip_addr].all_protocols())
    elif choice == "3":
        print("nmap version {}".format(scanner.nmap_version()))
        scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
        print(scanner.scaninfo())
        print("IP status is {}".format(scanner[ip_addr].state()))
        print(scanner[ip_addr].all_protocols())
    else:
        print("enter another option")


def main():
    scanner = enable_scan()
    results = get_user_information(scanner)
    scanner = results[SCANNER]
    user_choice = results[CHOICE]
    ip = results[IP_ADDRESS]
    define_choice(scanner,user_choice,ip)


if __name__ == "__main__":
    main()