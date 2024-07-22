import asyncio
import random
import redis
import os

async def broadcast_message():
    r = redis.Redis(host=os.getenv('REDIS_HOST', 'localhost'), port=6379, db=0)
    while True:
        r.publish('hello_channel', 'Hello world')
        await asyncio.sleep(random.randint(1, 10))

if __name__ == "__main__":
    asyncio.run(broadcast_message())
