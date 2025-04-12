import aiopg

dsn = "dbname=nuts_db user=nuts_user password=nuts_pass host=localhost port=5432"

async def save_message(content):
    async with aiopg.connect(dsn) as conn:
        async with conn.cursor() as cur:
            await cur.execute("INSERT INTO messages (content) VALUES (%s);", (content,))
            print("Message saved.")
