<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from neuralseek import Neuralseek
import os

with Neuralseek(
    api_key=os.getenv("NEURALSEEK_API_KEY", ""),
) as s:
    res = s.seek.execute()

    if res is not None:
        # handle response
        pass
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
    ) as s:
        res = await s.seek.execute_async()

        if res is not None:
            # handle response
            pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->