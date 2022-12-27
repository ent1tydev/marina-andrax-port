
import os


from marina_modules.info import *
from marina_modules.scan import *

from ctypes import *
import socket

###
#
NRM  = "\x1B[0m"
RED  = "\x1B[31m"
GRN  = "\x1B[32m"
YEL  = "\x1B[33m"
BLU  = "\x1B[34m"
MAG  = "\x1B[35m"
CYN  = "\x1B[36m"
WHT  = "\x1B[37m"
#
###

print("\nANDRAX")
print("\nTHANKS TO Weidsom Nascimento")
print("\033];M.A.R.I.N.A\007")

banner_lib = "marina-libs/banner.so"

print("edited by @gamingflexer ")


workmodelist = ("passive", "low", "high", "intrusive")
has_sec_system = 0

# global variables

host = ""
domain = 0
ip = ""
host_ports = []
datas = []
products = []
scan_services = []
web_tech = {}
isp = ""
asn = ""
device_type = ""
isrouter = 0
workmode = "passive"
# end global variables

def show(show_full):
    
    print("\n=========================\x1B[1m\x1B[31mSTART\x1B[0m=========================")
    
    print("\nWorkmode: {}{}{}".format(RED, workmode, NRM))
    print("Host: {}{}{}".format(RED, host, NRM))
    
    if(domain):
        print("Domain IP Addres: {}{}{}".format(RED, ip, NRM))

    if(asn != ""):
        print("ASN: {}{}{}".format(RED, asn, NRM))
    
    if(isp == ""):
        print("ISP: {}NULL{}".format(RED, NRM))
    else:
        if("sucuri" in isp.lower() or "akamai" in isp.lower() or "incapsula" in isp.lower() or "cloudfront" in isp.lower() or "stackpath" in isp.lower() or "fastly" in isp.lower() or "cloudflare" in isp.lower()):
            has_sec_system = 1
            print("ISP: {}{}{} {}[{} {}Security system{} {}]{}".format(RED, isp, NRM, WHT, NRM, YEL, NRM, WHT, NRM))
        else:
            print("ISP: {}{}{}".format(RED, isp, NRM))

    if(host_ports[0]):
        print("Ports: {}{}{}".format(RED, host_ports, NRM))
    
    if(device_type != ""):
        print("Possible device type: {}{}{}".format(RED, device_type, NRM))

    if(host_ports[0]):
        num=0
        num2=0
        num3=0

        for z in host_ports:
            try:
                products.insert(num2, datas[num2]['product'])
            except:
                try:
                    products.insert(num2, scan_services[num2])
                except:
                    products.insert(num2, "Unknown")
            num2=num2+1
        
        print("Products: {}[{}\n".format(WHT, NRM))
        for y in host_ports:
            print("     {}{}{} == {}{}{}".format(RED, host_ports[num3], NRM, YEL, products[num3], NRM))
            num3=num3+1

        print("\n{}]{}".format(WHT, NRM))
        
        if(show_full == 1):
            for x in host_ports:
                try:
                    if(datas[num]['data'] == ""):
                        print("\nPort {}{}{} has no data".format(RED, host_ports[num], NRM))
                    else:
                        print("\nPort {}{}{} has data:\n{}{}{}".format(RED, host_ports[num], NRM, YEL, datas[num]['data'], NRM))
                except:
                    print("\nPort {}{}{} has no data".format(RED, host_ports[num], NRM))
                num=num+1
            print("Web technologies: {}", web_tech)

    print("\n==========================\x1B[1m\x1B[31mEND\x1B[0m==========================")


while True:
    line = input('\n\001\x1B[37m\002M\001\x1B[0m\002\001\x1B[31m\002.\001\x1B[37m\002A\001\x1B[0m\002\001\x1B[31m\002.\001\x1B[37m\002R\001\x1B[0m\002\001\x1B[31m\002.\001\x1B[37m\002I\001\x1B[0m\002\001\x1B[31m\002.\001\x1B[37m\002N\001\x1B[0m\002\001\x1B[31m\002.\001\x1B[37m\002A\001\x1B[0m\002 \001\x1B[31m\002:\001\x1B[37m\002>\001\x1B[0m\002 ')
    
    line = line.split()

    try:

        if line[0] == 'quit' or line[0] == 'q' or line[0] == 'exit':
            break

        if line[0] == 'set':
            
            try:

                if line[1] == "host":

                    host_ports[:] = []
                    datas[:] = []
                    products[:] = []
                    scan_services[:] = []
                    web_tech.clear()
                    isp = ""
                    asn = ""
                    has_sec_system = 0
                    domain = 0
                    device_type = ""


                    try:
                    
                        isdomain = socket.gethostbyname_ex(line[2])
                    
                        if isdomain[0] == isdomain[2][0]:
                            print("\n[ \x1B[1m+\x1B[0m ] Setting host to: {}{}{}".format(YEL,line[2],NRM))
                            ip = isdomain[0]
                            host = line[2]
                        else:
                            print("\n[ \x1B[1m+\x1B[0m ] Setting host to: {}{}{} as a domain name".format(YEL,line[2],NRM))
                            ip = isdomain[2][0]
                            host = line[2]
                            domain = 1

                    except:
                        print("\n[ \x1B[1m\x1B[31mERROR\x1B[0m ] \"{}{}{}\" not appear be a valid domain or ip address".format(RED,line[2],NRM))

                elif line[1] == "workmode":

                    try:

                        if line[2] in workmodelist:
                            print("\n[ \x1B[1m+\x1B[0m ] Using: {}{}{} as workmode".format(YEL, line[2], NRM))
                            workmode = line[2]
                        else:
                            print("\n[ \x1B[1m\x1B[31mERROR\x1B[0m ] \"{}{}{}\" not found in workmode\n\n{}[{}{}{}]{}".format(RED,line[2],NRM, RED, MAG, workmodelist, RED, NRM))

                    except:
                        print("\n[ \x1B[1m\x1B[31mERROR\x1B[0m ] \"{}{}{}\" not appear be a valid workmode".format(RED, line[2],NRM))


                else:
                    print("\n[ \x1B[1m\x1B[31mERROR\x1B[0m ] \"{}{}{}\" not found in set options".format(RED,line[1],NRM)) 
                            

            except:
                print("\n[ \x1B[1m\x1B[31mERROR\x1B[0m ] Syntax {}ERROR{} in set".format(RED, NRM))

        elif line[0] == 'show':

            try:
                if(line[1] == 'full'):
                    show(1)
            except:
                show(0)

        elif line[0] == 'info':
            print("\n[ \x1B[1m+\x1B[0m ] Running information module")
            print("\n\t[ \x1B[1minfo\x1B[0m ] Starting passive information")
            jsonresult = get_info(ip)
            host_ports[:] = jsonresult['ports']
            datas[:] = jsonresult['data']
            isp = jsonresult['isp']
            asn = jsonresult['asn']
            print("\t[ \x1B[1minfo\x1B[0m ] Checking device type by passive analysis")
            num=0
            for x in host_ports:
                try:
                    if("wap" in jsonresult['data'][num]['devicetype'].lower()):
                        device_type="router"
                except:
                    None
                num=num+1
 
            num2=0
            print("\t[ \x1B[1minfo\x1B[0m ] Try find Web technologies")  
            #print(jsonresult['data'][3]['http']['components']) 
            for x in host_ports:
                try:
                    if(len(jsonresult['data'][num2]['http']['components']) != 0):
                        web_tech[num2] = jsonresult['data'][num2]['http']['components']
                        print("\t\t[ \x1B[1m\x1B[31mFound\x1B[0m ] {}{}{} as Web technology in {}{}{}".format(RED, web_tech[num2], NRM, RED, host_ports[num2], NRM))
                except:
                    None
                num2=num2+1

            print("\n[ \x1B[1mDONE\x1B[0m ]")

        elif line[0] == 'scan':
            datas[:] = []
            scan_services[:] = []
            print("\n[ \x1B[1m+\x1B[0m ] Running Scan module")
            print("\n\t[ \x1B[1minfo\x1B[0m ] Scan with mode: {}{}{}".format(RED, workmode, NRM))
            if(workmode == 'passive'):
                print("\t\t[ Scan ] this can take a while...")
                host_ports[:], scan_services = scan_passive(ip)
            if(workmode == 'low'):
                print("\t\t[ Scan ] this can take a while...")
                host_ports[:], device_type, scan_services = scan_low(ip)
            if(workmode == 'high'):
                print("\t\t[ Scan ] this realy can take a while...")
                host_ports[:], device_type, scan_services = scan_high(ip)

            if(workmode == 'intrusive'):
                print("\t\t[ Scan ] Holy... this realy, realy will take a while...")
                host_ports[:], device_type, scan_services = scan_high(ip)
            
            print("\n[ \x1B[1mDONE\x1B[0m ]")

        elif line[0] == 'anal':
            print("\n[ \x1B[1m+\x1B[0m ] Running analysis module")
            print("\n\t[ \x1B[1minfo\x1B[0m ] Analysis with mode: {}{}{}".format(RED, workmode, NRM))

            if("wap" in device_type.lower() or "router" in device_type.lower() or "switch" in device_type.lower() or "embedded" in device_type.lower() or "Cisco" in device_type.lower()):
                isrouter = 1
                print("\n\t\t[ \x1B[1mROUTER ] The device is a router type")
                print("\n\t\t[ \x1B[1mROUTER ] Checking the exploitability")
                



        elif line[0] == 'help' or line[0] == '?':
            print("\x1B[32mReal Hackers don't need help, get out!...  This said Weidsom XD.., but how to become one without knowledge?! (he even did not typed commands here -_-) ")
            print("\n") 
            print("\nset --> workmode passive/low/high/intrusive")
            print("\nset --> host xxx")
            print("\nscan --> for scan host")
            print("\nshow --> for see what MARINA found out!")
            print("\n") 
            print("\x1B[31mInstagram: GAMING FLEXER")
            print("\n") 
            print("And matej_sochan")


        else:
            print("\n[ \x1B[1m\x1B[31mERROR\x1B[0m ] Command \"{}{}{}\" not found".format(RED, line[0], NRM))
            
    except Exception as e:
        print("\n[ Error ] %s" % e)
