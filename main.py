import asyncio
from api.subscriber import subscribe_and_receive

if __name__ == "__main__":
    asyncio.run(subscribe_and_receive())
