import asyncio
from nats.aio.client import Client as NATS

async def run():
    nc = NATS()
    await nc.connect("nats://18.234.166.68:4222")

    subject = "alissa_jouljian"  
    message = input("Enter your message to send: ")
    await nc.publish(subject, message.encode())

    await nc.close()
    print(f" Sent message to [{subject}]: {message}")

asyncio.run(run())
