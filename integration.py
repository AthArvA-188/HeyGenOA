import asyncio
from client import VideoTranslationClient

async def main():
    # Exapmle for the client with your base URL
    client = VideoTranslationClient(base_url="http://127.0.0.1:5000")

    # Wait for completion, this will return the final result - either 'completed' or 'error'
    result = await client.wait_for_completion(max_wait=120)
    print(f"Final Result: {result}")

if __name__ == "__main__":
    asyncio.run(main())
