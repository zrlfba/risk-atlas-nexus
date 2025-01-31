

# Slot: numTrainingTokens


_The number of tokens a AI model was trained on._





URI: [nexus:numTrainingTokens](http://research.ibm.com/ontologies/aiont/numTrainingTokens)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LargeLanguageModel](LargeLanguageModel.md) | A large language model (LLM) is an AI model which supports a range of languag... |  no  |







## Properties

* Range: [Integer](Integer.md)

* Minimum Value: 0





## Identifier and Mapping Information







### Schema Source


* from schema: http://research.ibm.com/ontologies/aiont/ai-risk-ontology




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nexus:numTrainingTokens |
| native | nexus:numTrainingTokens |




## LinkML Source

<details>
```yaml
name: numTrainingTokens
description: The number of tokens a AI model was trained on.
from_schema: http://research.ibm.com/ontologies/aiont/ai-risk-ontology
rank: 1000
alias: numTrainingTokens
domain_of:
- LargeLanguageModel
range: integer
minimum_value: 0

```
</details>