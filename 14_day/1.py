# import asyncio
# async def handle_echo(reader, writer):
#     data = await reader.read(1024)
#     message = data.decode()
#     addr = writer.get_extra_info("peername")
#     print("received %r from %r" % (message, addr))
#     writer.close()
#
# loop = asyncio.get_event_loop()
# coro = asyncio.start_server(handle_echo, "127.0.0.1", 10001,
#                             loop=loop)
# server = loop.run_until_complete(coro)
# try:
#     loop.run_forever()
# except KeyboardInterrupt:
#     print("Already leaving??? Sad...")
# server.close()
# loop.run_until_complete(server.wait_closed())
# loop.close()
#

import asyncio
from urllib.request import urlopen
a synchronous function
def sync_get_url(url):
   return urlopen(url).read()
async def load_url(url, loop=None):
    future = loop.run_in_executor(None, sync_get_url, url)
    response = await future
    print(len(response))
loop = asyncio.get_event_loop()
loop.run_until_complete(load_url("https://vk.com/id50141963 ", loop=loop))

