#!/usr/bin/env python
import socket
import time
import sys
import random
import numpy as np

# application constants
TCP_IP = '192.168.0.110'
TCP_PORT = 9999
BUFFER_SIZE = 1024
BASE_UNIT_ID = 1


def gen_temp_data(t):
    rand = random.uniform(1, 10)
    rand_deg = random.uniform(5, 10)
    y = np.sin(2 * np.pi * t) * np.exp(- (rand_deg/10)/ rand)
    return y

def make_cwf_msg(dev_id):
    # array template without CHK byte
    arr = [0x02, 0x30, 0x33, 0x30, 0x30, 0x30, 0x30, 0x31, 0x30, 0x31, 0x43, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30,
           0x30, 0x30, 0x30, 0x31, 0x03]
    chk = arr[0]
    arr[2] = 0x30 + dev_id
    for m in arr:
        chk = chk ^ m
    arr.append(chk)
    return arr

def get_temp_from_cwf(cwf_data):
    temperature = -1
    # convert temerature from string
    raw_data = cwf_data[19:-2]
    str_data = str(raw_data)
    try:
        temperature = int(str_data, 16)
    except Exception as ex:
         print("Can't parse integer value. ")
    return temperature

def save_data_to_file(fname, temp):
    try:
        f = open(fname, 'a')
        f.write(str(temp / 10.0) + "\n")
        f.close()
    except IOError:
        print ("No file")

def connect():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((TCP_IP, TCP_PORT))
    except socket.error, exc:
        sock = None
        print("Caught exception socket.error : %s" % exc)
    return sock

def main():
    sock = connect()
    if sock is None:
        sys.exit(1)

    delta = 0
    while True:
        dev_id = BASE_UNIT_ID + delta
        array = make_cwf_msg(dev_id)
        message = ''.join(chr(ch) for ch in array)
        print("send data: " + message.decode("ascii"))

        try:
            sock.settimeout(1.5)
            sock.send(message)
            data = sock.recv(BUFFER_SIZE)

            t = get_temp_from_cwf(data)  # temperature as integer value
            if t > 0:
                fname = "y" + str(message[2]) + ".rtf"
                save_data_to_file(fname, t)
        except socket.error, exc:
            print("Caught exception socket.error : %s" % exc)
        # increment OMRON module ID
        delta = (delta + 1) % 5
        time.sleep(0.2)
    sock.close()

if __name__ == '__main__':
    main()
