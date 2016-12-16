#!/usr/bin/env python
import socket
import time

TCP_IP = '192.168.0.110'
TCP_PORT = 9999
BUFFER_SIZE = 1024
#MESSAGE = bytes([0x02, 0x30, 0x33, 0x30, 0x30, 0x30, 0x30, 0x38, 0x30, 0x31, 0x74, 0x74, 0x74, 0x74, 0x74, 0x03, 0x4D])
#MESSAGE = b'\x02\x30\x33\x30\x30\x30\x30\x38\x30\x31\x74\x74\x74\x74\x74\x03\x4D'
MESSAGE = b'\x02\x30\x33\x30\x30\x30\x30\x31\x30\x31\x43\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x31\x03\x42'
#                 30  33  30  30  30  30  31  30  31  43  30  30  30  30  30  30  30  30  30  30  31

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))


while True:
  s.send(MESSAGE)
  print("send data: " + MESSAGE.decode("ascii"))
  data = s.recv(BUFFER_SIZE)
  #show data
  raw_temp = data[19:-2]
  s_temp = str(raw_temp)
  temp = int(s_temp, 16)

  print "received data:", data
  print("TEMP: " + str(temp/10.0))

  filename = "y" + str(MESSAGE[2]) + ".rtf"
  try:
    f = open(filename, 'a')
    f.write(str(temp/10.0) + "\n")
    f.close()
  except IOError:
    print ("No file")



  time.sleep(0.7)

s.close()


