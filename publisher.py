import asyncio
from nats.aio.client import Client as NATS

async def run():
    nc = NATS()
    await nc.connect("nats://localhost:4222")
    await nc.publish("messages", b"Hello from NATS!")
    await nc.close()

asyncio.run(run())
