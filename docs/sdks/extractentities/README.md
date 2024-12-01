# ExtractEntities
(*extract_entities*)

## Overview

### Available Operations

* [post](#post) - Extract entitites from text

## post

Extract entitites from text

### Example Usage

```python
from neuralseek import Neuralseek
import os

with Neuralseek(
    api_key=os.getenv("NEURALSEEK_API_KEY", ""),
) as s:
    res = s.extract_entities.post(request={
        "entities": "[{\"name\":\"dog-breeds\",\"description\":\"Types of Dogs\", \"format\":\"string\"}]",
    })

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `request`                                                                       | [models.ExtractEntitiesRequestBody](../../models/extractentitiesrequestbody.md) | :heavy_check_mark:                                                              | The request object to use for the request.                                      |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[models.ExtractEntitiesResponseBody](../../models/extractentitiesresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |