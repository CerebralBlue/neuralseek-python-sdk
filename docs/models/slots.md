# Slots

Provide an object of variable names, with a type property set to an entity type to match to in total across multiple turns of a conversation. NeuralSeek will return a promptEntity to display to the user to continue to fil the slots.  As slots are filled the value field will be populated.  Continue to send this entire filed back as input thru the multiple turns of the conversation, untill Complete is set to true.  Complete will be set to true when all slots are filled


## Fields

| Field       | Type        | Required    | Description |
| ----------- | ----------- | ----------- | ----------- |