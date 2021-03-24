import aiohttp
import asyncio
import pysmartthings

token = ''

async def print_devices():
    async with aiohttp.ClientSession() as session:
        api = pysmartthings.SmartThings(session, token)
        devices = await api.devices()
        device = devices[0]
        for device in devices:
            print("{}: {}".format(device.device_id, device.label))


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(print_devices())


if __name__ == '__main__':
    main()
