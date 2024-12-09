import time
import asyncio
import aiohttp

class VideoTranslationClient:
    def __init__(self, base_url):
        self.base_url = base_url

    async def get_status(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.base_url}/status") as response:
                response.raise_for_status()
                return await response.json()

    async def wait_for_completion(self, max_wait=60):
        polling_interval = 1  # Start polling every second
        max_interval = 8      
        start_time = time.time()

        while time.time() - start_time < max_wait:
            status_data = await self.get_status()
            status = status_data["result"]
            progress = status_data["progress"]
            print(f"Status: {status}, Progress: {progress}%")
            
            if status in ["completed", "error"]:
                return status
            await asyncio.sleep(polling_interval)
            polling_interval = min(polling_interval * 2, max_interval)

        raise TimeoutError("Job did not complete within the maximum wait time.")
