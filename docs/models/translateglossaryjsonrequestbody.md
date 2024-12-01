# TranslateGlossaryJSONRequestBody

This endpoint will accept either a file upload (TMX or JSON), or a direct JSON payload following IBM's JSON file format https://cloud.ibm.com/docs/language-translator?topic=language-translator-customizing#json.  Only one file may be saved. Subsequent files will overwrite.


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `sentences`                                             | List[List[[models.Sentences](../models/sentences.md)]]  | :heavy_minus_sign:                                      | Instead of a file upload you may pass sentence mappings |