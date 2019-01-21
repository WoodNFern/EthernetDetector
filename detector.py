#!/usr/bin/env python3
import sys

IN_FILE = "/dev/urandom"


def detect_preamble(file):
    # Detect Preamble (1st to 7th byte)
    for i in range(0, 7):
        byte = f.read(1)
        if byte == b'\xAA':
            if i > 1:
                print("Detected " + str(i + 1) + " correct preamble bytes!")
            continue
        else:
            return False

    # Check 'Start Frame Delimiter' (8th Byte)
    byte = f.read(1)
    return byte == b'\xAB'


def is_length_legal(length):
    if length < 42:
        print("Invalid length: advertised length is too short.")
        print("Must be >= 42, was: " + str(length))
        return False
    elif length > 1497:
        print("Invalid length: advertised length is too large.")
        print("Must be < 1497, was: " + str(length))
        return False
    else:
        return True


def print_frame_contents(dst_address, src_address, dsap, ssap, control, data, fcs):
    print("Destination MAC Address: " + str(dst_address))
    print("Source MAC Address: " + str(src_address))
    print("Destination Service Access Point (DSAP): " + str(dsap))
    print("Source Service Access Point (SSAP): " + str(ssap))
    print("Logical Link (LLC): " + str(control))
    print("Data (may be encrypted): " + str(data))
    print("Frame check sequence (FCS): " + str(fcs))


with open(IN_FILE, "rb") as f:
    while not detect_preamble(f):
        pass
    print("Detected legal preamble & SFD!")

    dst_address = f.read(6)
    src_address = f.read(6)
    length = int.from_bytes(f.read(2), byteorder='little')
    dsap = f.read(1)
    ssap = f.read(1)
    control = f.read(1)
    data = f.read(int(length))
    fcs = f.read(4)

    if is_length_legal(length):
        print_frame_contents(dst_address, src_address, dsap, ssap, control, data, fcs)





