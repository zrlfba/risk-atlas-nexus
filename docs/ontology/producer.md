

# Slot: producer


_A relationship to the Organization instance which produces this instance._





URI: [nexus:producer](http://research.ibm.com/ontologies/aiont/producer)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AiModel](AiModel.md) | A base AI Model class |  no  |
| [AiSystem](AiSystem.md) | A compound AI System composed of one or more AI capablities |  no  |
| [LargeLanguageModel](LargeLanguageModel.md) | A large language model (LLM) is an AI model which supports a range of languag... |  no  |
| [BaseAi](BaseAi.md) | Any type of AI, be it a LLM, RL agent, SVM, etc |  no  |







## Properties

* Range: [Organization](Organization.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://research.ibm.com/ontologies/aiont/ai-risk-ontology




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nexus:producer |
| native | nexus:producer |




## LinkML Source

<details>
```yaml
name: producer
description: A relationship to the Organization instance which produces this instance.
from_schema: http://research.ibm.com/ontologies/aiont/ai-risk-ontology
rank: 1000
alias: producer
domain_of:
- BaseAi
range: Organization

```
</details>