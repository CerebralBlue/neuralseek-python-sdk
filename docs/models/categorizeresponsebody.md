# CategorizeResponseBody

Success


## Fields

| Field                                                                                     | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `intent`                                                                                  | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | The matched Intent                                                                        |
| `category`                                                                                | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | The matched Category                                                                      |
| `category_id`                                                                             | *Optional[int]*                                                                           | :heavy_minus_sign:                                                                        | The Category id                                                                           |
| `top_intents`                                                                             | [Optional[models.TopIntents]](../models/topintents.md)                                    | :heavy_minus_sign:                                                                        | If Vector Similarity is set as the Intent Match type, this will provide the top 3 matches |