import subprocess

def python_call_powershell(ip):
    try:
        args = [r"powershell", r"mstsc", r"/v:" + ip, r"/f"]
        p = subprocess.Popen(args, stdout=subprocess.PIPE)
        dt = p.stdout.read()
        return dt
    except Exception as e:
        print(e)
    return False

def add_cmdkey(ip):
    try:
        username = "chenzhengang"
        password = "test"
        args = [
            r"powershell", r"cmdkey", r"/generic:TERMSRV/" + ip,
            r"/user:" + username, r"/pass:" + password
        ]
        p = subprocess.Popen(args, stdout=subprocess.PIPE)
        dt = p.stdout.read()
        python_call_powershell(ip)
        return dt
    except Exception as e:
        print(e)
    return False

ip = "10.193.225.7"
add_cmdkey(ip)

