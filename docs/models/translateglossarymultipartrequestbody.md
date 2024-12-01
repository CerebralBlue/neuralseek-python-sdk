# TranslateGlossaryMultipartRequestBody

This endpoint will accept either a file upload (TMX or JSON), or a direct JSON payload following IBM's JSON file format https://cloud.ibm.com/docs/language-translator?topic=language-translator-customizing#json.  Only one file may be saved. Subsequent files will overwrite.


## Fields

| Field                                      | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `file`                                     | [Optional[models.File]](../models/file.md) | :heavy_minus_sign:                         | N/A                                        |