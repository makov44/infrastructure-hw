import asyncio
import random
import redis
import os
import logging
from redis.exceptions import ConnectionError, TimeoutError

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

MAX_RETRIES = 5
RETRY_DELAY = 5  # seconds

async def broadcast_message():
    retries = 0
    while retries < MAX_RETRIES:
        try:
            r = redis.Redis(host=os.getenv('REDIS_HOST', 'localhost'), port=6379, db=0)
            r.ping()  # Test the connection
            logger.info("Connected to Redis successfully")
            
            while True:
                try:
                    r.publish('hello_channel', 'Hello world')
                    logger.info("Message broadcasted")
                    await asyncio.sleep(random.randint(1, 10))
                except (ConnectionError, TimeoutError) as e:
                    logger.error(f"Lost connection to Redis: {e}")
                    break  # Break the inner loop to attempt reconnection
                except Exception as e:
                    logger.error(f"An error occurred while broadcasting: {e}")
                    await asyncio.sleep(1)  # Wait a bit before retrying
        
        except (ConnectionError, TimeoutError) as e:
            retries += 1
            logger.error(f"Failed to connect to Redis (attempt {retries}/{MAX_RETRIES}): {e}")
            if retries < MAX_RETRIES:
                logger.info(f"Retrying in {RETRY_DELAY} seconds...")
                await asyncio.sleep(RETRY_DELAY)
            else:
                logger.critical("Max retries reached. Exiting.")
                break
        except Exception as e:
            logger.critical(f"An unexpected error occurred: {e}")
            break

if __name__ == "__main__":
    asyncio.run(broadcast_message())