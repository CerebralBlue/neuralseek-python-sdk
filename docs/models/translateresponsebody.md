# TranslateResponseBody

Success


## Fields

| Field                                                                        | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `word_count`                                                                 | *Optional[int]*                                                              | :heavy_minus_sign:                                                           | The word count.                                                              |
| `character_count`                                                            | *Optional[int]*                                                              | :heavy_minus_sign:                                                           | The word count.                                                              |
| `detected_language`                                                          | *Optional[str]*                                                              | :heavy_minus_sign:                                                           | The 2-digit language code for the detected language.                         |
| `detected_language_confidence`                                               | *Optional[float]*                                                            | :heavy_minus_sign:                                                           | The detected language confidence.                                            |
| `translation_glossary`                                                       | *Optional[bool]*                                                             | :heavy_minus_sign:                                                           | Returns true if a glossary is loaded and matched any input.                  |
| `translation_glossary_exact`                                                 | *Optional[bool]*                                                             | :heavy_minus_sign:                                                           | Returns true if a glossary is loaded and an entry exactly matched the input. |
| `translations`                                                               | List[[models.Translations](../models/translations.md)]                       | :heavy_minus_sign:                                                           | N/A                                                                          |