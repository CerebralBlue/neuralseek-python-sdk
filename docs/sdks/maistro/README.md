# Maistro
(*maistro*)

## Overview

### Available Operations

* [execute](#execute) - Run mAistro NTL or agent

## execute

Freeform prompting using NeuralSeek Template Language or a saved agent

### Example Usage

```python
from neuralseek import Neuralseek
import os

with Neuralseek(
    api_key=os.getenv("NEURALSEEK_API_KEY", ""),
) as n_client:

    res = n_client.maistro.execute(request_body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                | Type                                                                                                                                                                                                     | Required                                                                                                                                                                                                 | Description                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request_body`                                                                                                                                                                                           | [models.MaistroRequestBody](../../models/maistrorequestbody.md)                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                       | The request object.                                                                                                                                                                                      |
| `overrideschema`                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                       | Find variables based on post body.  Return all variables as the base presponse body, overriding the normal NS schema. All POST options will be ignored. Set this to a string value of 'true' to activate |
| `overrideagent`                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                       | If using overrideSchema you must pass your agent name here. All other POST options will be ignored.                                                                                                      |
| `debug`                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                       | Include NS debug information in a field named 'neuralseek'. Set this to a string value of 'true' to activate                                                                                             |
| `retries`                                                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                                                      |

### Response

**[models.MaistroResponseBody](../../models/maistroresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |