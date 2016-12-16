#!/usr/bin/env python
import socket
import time


def makeMSG(dev_id):
    ARRAY = [0x02, 0x30, 0x33, 0x30, 0x30, 0x30, 0x30, 0x31, 0x30, 0x31, 0x43, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30,
             0x30, 0x30, 0x30, 0x31, 0x03]
    chk = ARRAY[0]
    ARRAY[2] = 0x30 + dev_id
    for m in ARRAY:
        chk = chk ^ m
    ARRAY.append(chk)
    return ARRAY


TCP_IP = '192.168.0.110'
TCP_PORT = 9999
BUFFER_SIZE = 1024
#ARRAY = [0x02, 0x30, 0x33, 0x30, 0x30, 0x30, 0x30, 0x31, 0x30, 0x31, 0x43, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x31, 0x03, 0x42]
#MESSAGE = b'\x02\x30\x33\x30\x30\x30\x30\x31\x30\x31\x43\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x31\x03\x42'
#                 30  33  30  30  30  30  31  30  31  43  30  30  30  30  30  30  30  30  30  30  31

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

while True:
  dev_id = 3

  ARRAY = makeMSG(dev_id)

  MESSAGE = ''.join(chr(ch) for ch in ARRAY)
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


