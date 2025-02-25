<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from neuralseek import Neuralseek
import os

with Neuralseek(
    api_key=os.getenv("NEURALSEEK_API_KEY", ""),
) as n_client:

    res = n_client.seek.execute()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from neuralseek import Neuralseek
import os

async def main():
    async with Neuralseek(
        api_key=os.getenv("NEURALSEEK_API_KEY", ""),
    ) as n_client:

        res = await n_client.seek.execute_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->