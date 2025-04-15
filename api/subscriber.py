import os
import asyncio
import aiopg
from nats.aio.client import Client as NATS

nats_url = os.getenv("NATS_URL", "nats://18.234.166.68:4222")
dsn = "dbname=nuts_db user=nuts_user password=nuts_pass host=localhost port=5432"

async def save_message(content):
    async with aiopg.connect(dsn) as conn:
        async with conn.cursor() as cur:
            await cur.execute("INSERT INTO messages (content) VALUES (%s);", (content,))
            print("Message saved to database.")

async def subscribe_and_receive():
    print("Starting to connect to NATS...")
    nc = NATS()
    await nc.connect(nats_url)
    subject = "alissa_jouljian"
    print(f"Subscribed to subject: {subject} on {nats_url}")

    async def message_handler(msg):
        data = msg.data.decode()
        print(f"Received: {data}")
        await save_message(data)

    await nc.subscribe(subject, cb=message_handler)

    while True:
        # print("⏳ Waiting for messages...")
        await asyncio.sleep(1)

asyncio.run(subscribe_and_receive())
