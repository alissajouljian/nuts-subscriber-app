import asyncio
from service.processor import handle_message

async def subscribe_and_receive():
    print("Subscribed to Nuts service.")
    while True:
        await asyncio.sleep(3)
        message = {"content": "Sample message"}
        await handle_message(message)
