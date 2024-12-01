# MaistroStreamRender


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `node`                                                               | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The node type                                                        |
| `vars`                                                               | [Optional[models.MaistroStreamVars]](../models/maistrostreamvars.md) | :heavy_minus_sign:                                                   | The variable values                                                  |
| `out`                                                                | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The output                                                           |
| `chained`                                                            | *Optional[bool]*                                                     | :heavy_minus_sign:                                                   | True if the step is chained                                          |