# Score
(*score*)

## Overview

### Available Operations

* [post](#post) - Run the Semantic Scoring model on text against an array of passages

## post

Run the Semantic Scoring model on text against an array of passages

### Example Usage

```python
from neuralseek import Neuralseek
import os

with Neuralseek(
    api_key=os.getenv("NEURALSEEK_API_KEY", ""),
) as n_client:

    n_client.score.post()

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.ScoreRequestBody](../../models/scorerequestbody.md)         | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |