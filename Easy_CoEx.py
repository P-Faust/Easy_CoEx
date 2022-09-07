from unittest import TestResult, result
import iperf3

client = iperf3.Client()
client.duration = 1
client.server_hostname = 'ping.online.net'
client.port = 5200
result = client.run()
if result.error:
    print(result.error)
else:
    print("{:.2f}".format(float(result.received_Mbps)))