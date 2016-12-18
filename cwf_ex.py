#!/usr/bin/env python
import socket
import time


def make_cwf_msg(dev_id):
    arr = [0x02, 0x30, 0x33, 0x30, 0x30, 0x30, 0x30, 0x31, 0x30, 0x31, 0x43, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30,
           0x30, 0x30, 0x30, 0x31, 0x03]
    chk = arr[0]
    arr[2] = 0x30 + dev_id
    for m in arr:
        chk = chk ^ m
    arr.append(chk)
    return arr

def get_temp_from_cwf(cwf_data):
    raw_data = cwf_data[19:-2]
    str_data = str(raw_data)
    temperature = int(str_data, 16)
    return temperature

def save_data_to_file(fname, temp):
    try:
        f = open(fname, 'a')
        f.write(str(temp / 10.0) + "\n")
        f.close()
    except IOError:
        print ("No file")


TCP_IP = '192.168.0.110'
TCP_PORT = 9999
BUFFER_SIZE = 1024
# MESSAGE = b'\x02\x30\x33\x30\x30\x30\x30\x31\x30\x31\x43\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x31\x03\x42'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT))

delta = 0
base_id = 3
while True:
    dev_id = base_id + delta
    array = make_cwf_msg(dev_id)
    message = ''.join(chr(ch) for ch in array)
    print("send data: " + message.decode("ascii"))

    try:
        sock.settimeout(1.5)
        sock.send(message)
        data = sock.recv(BUFFER_SIZE)

        t = get_temp_from_cwf(data)  # temperature as integer value
        fname = "y" + str(message[2]) + ".rtf"
        save_data_to_file(fname, t)
    except socket.error, exc:
        print("Caught exception socket.error : %s" % exc)

    # increment OMRON module ID
    delta = (delta + 1) % 5
    print("Delta: " + str(delta))
    # print("Dev ID: " + str(dev_id))

    time.sleep(0.7)

sock.close()
