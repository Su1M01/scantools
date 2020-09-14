#!/usr/bin/sudo python3

import nmap

scanner = nmap.PortScanner()

print("Welcome, this is a simple nmap automation tool")
print("<----------------------------------------------------->")

ip_addr = input("Please enter the IP address you want to scan: ")
print("The IP you entered is: ", ip_addr)
(type(ip_addr))

plage = input("Please, enter the plage of IP you want to scan: ")
print("You wanna scan ", plage, " plage of IP")
(type(plage))

options = input("Please, enter the options of scan: ")
print("The options you mentionned are ", options)
print(type(options))

print("Nmap Version: ", scanner.nmap_version())
result = scanner.scan(ip_addr, plage, options)

for i in result:
    print();
    print(i);
    print()

    for j in result[i]:
        print();
        print("        ", j);
        print()

        if (i != "scan"):
            print((result[i])[j])
        else:
            for k in (result[i])[j]:
                print();
                print("   ", k);
                print()

                if (k != "tcp"):
                    print(((result[i])[j])[k])
                else:
                    print(type(((result[i])[j])[k]))
                    for l in ((result[i])[j])[k]:
                        print();
                        print(l);
                        print()
                        print();
                        print((((result[i])[j])[k])[l]);
                        print()

        print()
