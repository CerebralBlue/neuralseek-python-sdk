# OneTimePassword
(*one_time_password*)

## Overview

### Available Operations

* [create](#create) - Create a One Time Password

## create

Create a One Time Password for use instead of an api key in unsecure environments, such as the browser. The password will expire after one use, and is valid for 30 minutes. This password can only be used for seek, mAIstro, extract, categorize, score, and logs operations.

### Example Usage

```python
from neuralseek import Neuralseek
import os

with Neuralseek(
    api_key=os.getenv("NEURALSEEK_API_KEY", ""),
) as n_client:

    res = n_client.one_time_password.create()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.OtpResponseBody](../../models/otpresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |