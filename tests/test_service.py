import asyncio
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from service.processor import handle_message


async def test_valid_message():
    await handle_message({"content": "Hello"})
    print("✓ Service test passed.")

asyncio.run(test_valid_message())
