import asyncio
from data.repository import save_message

async def test_save():
    await save_message("Test")
    print("✓ Data layer test passed.")

asyncio.run(test_save())
