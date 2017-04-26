import threading

import serial


def read(serial_port, max_reads):
    def run():
        ser = serial.Serial(port=serial_port, baudrate=115200, timeout=1)
        reads = 0
        while reads <  max_reads:
            print('[writer {}] Sending'.format(serial_port), 'A')
            ser.write('A'.encode())
            data = ser.readline()
            if data:
                c = chr(int(data.decode().strip()))
                assert c == 'A', 'Got an expected value back from echo node'
                reads += 1
        else:
            print('[node] Finished', serial_port)

    t = threading.Thread(target=run, args=())
    t.start()
    print('[node] Started node on', serial_port)

def main():
    ser_ports = ['/dev/cu.usbmodem142421', '/dev/cu.usbmodem142411', '/dev/cu.usbmodem14231']
    [read(port, 30) for port in ser_ports]


if __name__ == '__main__':
    main()
