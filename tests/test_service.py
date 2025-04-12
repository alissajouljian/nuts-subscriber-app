import asyncio
from service.processor import handle_message

async def test_valid_message():
    await handle_message({"content": "Hello"})
    print("✓ Service test passed.")

asyncio.run(test_valid_message())
