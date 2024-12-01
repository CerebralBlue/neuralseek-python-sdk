# Maistro
(*maistro*)

## Overview

### Available Operations

* [execute](#execute) - Run mAistro NTL or template
* [stream](#stream) - Stream mAIstro NTL or a template

## execute

Freeform prompting using NeuralSeek Template Language

### Example Usage

```python
from neuralseek import Neuralseek
import os

with Neuralseek(
    api_key=os.getenv("NEURALSEEK_API_KEY", ""),
) as s:
    res = s.maistro.execute(request_body={})

    if res is not None:
        # handle response
        pass

```

### Parameters

| Parameter                                                                                                                                                                                                | Type                                                                                                                                                                                                     | Required                                                                                                                                                                                                 | Description                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request_body`                                                                                                                                                                                           | [models.MaistroRequestBody](../../models/maistrorequestbody.md)                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                       | The request object.                                                                                                                                                                                      |
| `overrideschema`                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                       | Find variables based on post body.  Return all variables as the base presponse body, overriding the normal NS schema. All POST options will be ignored. Set this to a string value of 'true' to activate |
| `templatename`                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                       | If using overrideSchema you must pass your template name here. All other POST options will be ignored.                                                                                                   |
| `debug`                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                       | Include NS debug information in a field named 'neuralseek'. Set this to a string value of 'true' to activate                                                                                             |
| `retries`                                                                                                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                       | Configuration to override the default retry behavior of the client.                                                                                                                                      |

### Response

**[models.MaistroResponseBody](../../models/maistroresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## stream

Freeform prompting using NeuralSeek Template Language

### Example Usage

```python
from neuralseek import Neuralseek
import os

with Neuralseek(
    api_key=os.getenv("NEURALSEEK_API_KEY", ""),
) as s:
    res = s.maistro.stream()

    if res is not None:
        with res as event_stream:
            for event in event_stream:
                # handle event
                print(event, flush=True)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.MaistroStreamRequestBody](../../models/maistrostreamrequestbody.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[Union[eventstreaming.EventStream[models.MaistroStreamResponseBody], eventstreaming.EventStreamAsync[models.MaistroStreamResponseBody]]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |