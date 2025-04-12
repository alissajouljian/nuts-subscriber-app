import asyncio
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.repository import save_message

async def test_save():
    await save_message("Test")
    print("✓ Data layer test passed.")

asyncio.run(test_save())
