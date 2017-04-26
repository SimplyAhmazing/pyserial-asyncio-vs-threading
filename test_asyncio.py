import asyncio
import serial_asyncio


def main():
    loop = asyncio.get_event_loop()

    async def write(writer, serial_port, char):
        print('[writer {}] Sending'.format(serial_port), char)
        writer.write(char.encode())
        await writer.drain()

    async def read(reader):
        return await reader.readline()

    async def safe_read(reader):
        try:
            return await asyncio.wait_for(reader.readline(), timeout=1)
        except Exception as e:
            print('did not find data', e)

    async def node(serial_port, max_reads):
        print('[node] Started node on', serial_port)
        reader, writer = await serial_asyncio.open_serial_connection(url=serial_port, baudrate=115200, loop=loop)
        reads = 0
        try:
            while not reader.at_eof() and reads < max_reads:
                await write(writer, serial_port, 'A')
                data = await safe_read(reader)
                if data:
                    c = chr(int(data.decode().strip()))
                    assert c == 'A', 'Got an expected value back from echo node'
                    reads += 1
            else:
                print('[node] Finished', serial_port)
        except Exception as e:
            print('[node] Failed', serial_port, e)

    ser_ports = ['/dev/cu.usbmodem142421', '/dev/cu.usbmodem142411', '/dev/cu.usbmodem14231']
    tasks = [node(port, 100) for port in ser_ports]
    loop.run_until_complete(asyncio.wait(tasks))


if __name__ == '__main__':
    main()
