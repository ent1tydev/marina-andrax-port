import subprocess

def scan_passive(host):
    ports_list = []
    services_list = []
    stdoutdata = subprocess.getoutput("nmap -sS -T2 {} --open | grep \"open\"".format(host))
    str=stdoutdata.splitlines()
    for line in str:
        line = line.split()
        services_list.append(line[2])
    
    return ports_list, services_list

def scan_low(host):
    ports_list = []
    services_list = []
    device_type = ""
    stdoutdata = subprocess.getoutput("nmap -sS -O {} --open".format(host))
    str=stdoutdata.splitlines()
    for line in str:
        if "open" in line:
            line = line.split()
            try:
                ports_list.append(int(line[0].split("/")[0]))
                services_list.append(line[2])
            except:
                None
        if "Device type:" in line:
            line = line.split("Device type:")
            device_type=line[1].split()[0]


    return ports_list, device_type, services_list

def scan_high(host):
    ports_list = []
    services_list = []
    device_type = ""
    stdoutdata = subprocess.getoutput("nmap -sS -sV -O --top-ports 10000 {} --open".format(host))
    str=stdoutdata.splitlines()
    for line in str:
        if "open" in line:
            try:
                services_list.append(line.split("  ")[len(line.split("  "))-1])
            except:
                None
            line = line.split()
            try:
                ports_list.append(int(line[0].split("/")[0]))
            except:
                None
        if "Device type:" in line:
            line = line.split("Device type:")
            device_type=line[1].split()[0]



    return ports_list, device_type, services_list

def scan_intrusive(host):
    ports_list = []
    services_list = []
    device_type = ""
    stdoutdata = subprocess.getoutput("nmap -sS -sV -O -p- {} --open".format(host))
    str=stdoutdata.splitlines()
    for line in str:
        if "open" in line:
            try:
                services_list.append(line.split("  ")[len(line.split("  "))-1])
            except:
                None
            line = line.split()
            try:
                ports_list.append(int(line[0].split("/")[0]))
            except:
                None
        if "Device type:" in line:
            line = line.split("Device type:")
            device_type=line[1].split()[0]



    return ports_list, device_type, services_list
