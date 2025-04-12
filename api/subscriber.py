import asyncio
from nats.aio.client import Client as NATS
from service.processor import handle_message

async def subscribe_and_receive():
    nc = NATS()
    await nc.connect("nats://localhost:4222")

    async def message_handler(msg):
        data = msg.data.decode()
        print(f"Received message: {data}")
        await handle_message({"content": data})

    await nc.subscribe("messages", cb=message_handler)
    print("📡 Subscribed to NATS topic: messages")

    while True:
        await asyncio.sleep(1)
