# ScoreRequestBody

The request object.  Must include the question and a context.


## Fields

| Field                                                                                              | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `text`                                                                                             | *Optional[str]*                                                                                    | :heavy_minus_sign:                                                                                 | The text to score                                                                                  |
| `passages`                                                                                         | List[*str*]                                                                                        | :heavy_minus_sign:                                                                                 | The rating score. An integer, 0-5. 0 is worst, 5 is best.  For Thumbs up / Thumbs down send 0 or 5 |