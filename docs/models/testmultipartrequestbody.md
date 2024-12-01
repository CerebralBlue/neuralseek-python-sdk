# TestMultipartRequestBody

The questions csv.  Must adhere to the template https://api.neuralseek.com/q.csv After upload you will receive a 202 response and the server will begin processing.  Check for your completed results on the getTestResults endpoint.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `file`                                                               | [Optional[models.TestMultipartFile]](../models/testmultipartfile.md) | :heavy_minus_sign:                                                   | N/A                                                                  |