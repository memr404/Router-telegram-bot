import telnetlib, time

def get():
	telnet = telnetlib.Telnet('192.168.0.1')
	time.sleep(0.1)
	telnet.write(b'login\n')
	time.sleep(0.1)
	telnet.write(b'password\n')
	time.sleep(0.1)
	telnet.write(b'cd /proc/net/\n')
	time.sleep(0.1)
	trash = telnet.read_very_eager().decode('utf-8')
	time.sleep(0.1)
	telnet.write(b'cat arp\n')
	time.sleep(0.1)
	info = telnet.read_very_eager().decode('utf-8')
	telnet.close()
	return info

def off():
	telnet = telnetlib.Telnet('192.168.0.1')
	time.sleep(0.1)
	telnet.write(b'login\n')
	time.sleep(0.1)
	telnet.write(b'password\n')
	time.sleep(0.2)
	telnet.write(b'reboot\n')
	