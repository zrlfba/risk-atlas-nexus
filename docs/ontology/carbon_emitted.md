

# Slot: carbon_emitted


_The number of tons of carbon dioxide equivalent that are emitted during training_





URI: [nexus:carbon_emitted](http://research.ibm.com/ontologies/aiont/carbon_emitted)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LargeLanguageModel](LargeLanguageModel.md) | A large language model (LLM) is an AI model which supports a range of languag... |  no  |
| [AiModel](AiModel.md) | A base AI Model class |  no  |







## Properties

* Range: [Float](Float.md)

* Minimum Value: 0





## Identifier and Mapping Information







### Schema Source


* from schema: http://research.ibm.com/ontologies/aiont/ai-risk-ontology




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nexus:carbon_emitted |
| native | nexus:carbon_emitted |




## LinkML Source

<details>
```yaml
name: carbon_emitted
description: The number of tons of carbon dioxide equivalent that are emitted during
  training
from_schema: http://research.ibm.com/ontologies/aiont/ai-risk-ontology
rank: 1000
alias: carbon_emitted
domain_of:
- AiModel
range: float
minimum_value: 0
unit:
  symbol: t CO2-eq
  descriptive_name: tons of CO2 equivalent

```
</details>