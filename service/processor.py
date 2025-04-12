from data.repository import save_message

async def handle_message(message):
    content = message.get("content")
    if not content:
        print("Invalid message. Skipping.")
        return
    print(f"Processing message: {content}")
    await save_message(content)
