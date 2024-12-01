# MaistroRequestBody

The request object.


## Fields

| Field                                                                       | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `ntl`                                                                       | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | The NTL script to evaluate.  Include either this or templateName - not both |
| `template_name`                                                             | *Optional[str]*                                                             | :heavy_minus_sign:                                                          | The templateName to use. Include either this or input                       |
| `params`                                                                    | List[[models.MaistroParams](../models/maistroparams.md)]                    | :heavy_minus_sign:                                                          | An array of parameters to use in evaluation of the NTL                      |
| `options`                                                                   | [Optional[models.MaistroOptions]](../models/maistrooptions.md)              | :heavy_minus_sign:                                                          | Override options                                                            |