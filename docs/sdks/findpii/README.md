# FindPII
(*find_pii*)

## Overview

### Available Operations

* [detect](#detect) - Find PII in a user utterance

## detect

Find PII in a user utterance

### Example Usage

```python
from neuralseek import Neuralseek
import os

with Neuralseek(
    api_key=os.getenv("NEURALSEEK_API_KEY", ""),
) as n_client:

    res = n_client.find_pii.detect()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.PiiRequestBody](../../models/piirequestbody.md)             | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.PiiResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |