# MaistroResponseBody

Success


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `answer`                                                                       | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | The generated response                                                         |
| `source_parts`                                                                 | List[*str*]                                                                    | :heavy_minus_sign:                                                             | N/A                                                                            |
| `render`                                                                       | List[[models.Render](../models/render.md)]                                     | :heavy_minus_sign:                                                             | The steps used to render the result.                                           |
| `variables`                                                                    | [Optional[models.MaistroVariables]](../models/maistrovariables.md)             | :heavy_minus_sign:                                                             | The returned variable.                                                         |
| `variables_expanded`                                                           | List[[models.MaistroVariablesExpanded](../models/maistrovariablesexpanded.md)] | :heavy_minus_sign:                                                             | The returned variable, in the format of the input params                       |