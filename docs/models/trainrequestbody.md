# TrainRequestBody

The request object.  Must include the question and a context.


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `train`                                          | *Optional[str]*                                  | :heavy_minus_sign:                               | The training token. Get this from passages/train |
| `score`                                          | *Optional[int]*                                  | :heavy_minus_sign:                               | The relevancy score. An integer, 0-100           |