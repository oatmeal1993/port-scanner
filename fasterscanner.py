import sys
import socket
from datetime import datetime
import time
import concurrent.futures

# Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])  # Translate hostname to IPv4
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py")
    sys.exit(1)

print("Scanning target " + target)

# Add a pretty banner
print("-" * 50)
print("Scanning target " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)
time.sleep(2)  # Adding a pause for dramatic effect

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))  # Returns an error indicator - if port is open it throws a 0, otherwise 1
    if result == 0:
        print("Port {} is open. Knock, knock! Who's there? It's an open port! Keep exploring!".format(port))
        time.sleep(0.5)  # Adding a slight delay before the next port
    s.close()

try:
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Adjust the range below to the desired port range
        ports = range(1, 1000)
        executor.map(scan_port, ports)

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved. Are you sure this is a real target?")
    sys.exit()

except socket.error:
    print("Could not connect to the server. Maybe it's hiding behind a firewall?")
    sys.exit()

# Completion message
print("-" * 50)
print("Scanning completed! Time to unleash your inner hacker! But also hey it's Ryan")
print("-" * 50)