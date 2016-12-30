import subprocess
import re

ip = input("Please enter the IP address to trace: ")
max_ttl = input("Please enter the max hops to trace: ")
ttl = 1

while ttl <= int(max_ttl):
    raw_output = subprocess.Popen(['ping', '-c', '1', '-m', str(ttl), '-i', '0.1', '-t', '1', ip], stdout=subprocess.PIPE)
    output = raw_output.communicate()[0].decode()
    if 'Time to live exceeded' in output:
        output_list = output.split('\n')
        hop = re.search(r'(\d+\.\d+\.\d+\.\d+)', output_list[1]).group(1)
        print(hop)
        ttl += 1
    elif '1 packets received' in output:
        print(ip)
        break
    else:
        print('*')
        ttl += 1
print('End of Trace')

