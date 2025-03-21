

# Slot: hasLicense


_Indicates licenses associated with a resource_





URI: [airo:hasLicense](https://w3id.org/airo#hasLicense)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AiAgent](AiAgent.md) | An artificial intelligence (AI) agent refers to a system or program that is c... |  no  |
| [LargeLanguageModel](LargeLanguageModel.md) | A large language model (LLM) is an AI model which supports a range of languag... |  no  |
| [AiEval](AiEval.md) | An AI Evaluation, e |  no  |
| [AiSystem](AiSystem.md) | A compound AI System composed of one or more AI capablities |  no  |
| [Questionnaire](Questionnaire.md) | A questionnaire groups questions |  no  |
| [AiModel](AiModel.md) | A base AI Model class |  no  |
| [Dataset](Dataset.md) | A body of structured information describing some topic(s) of interest |  no  |
| [Question](Question.md) | An evaluation where a question has to be answered |  no  |
| [RiskTaxonomy](RiskTaxonomy.md) | A taxonomy of AI system related risks |  no  |
| [BaseAi](BaseAi.md) | Any type of AI, be it a LLM, RL agent, SVM, etc |  no  |







## Properties

* Range: [License](License.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://research.ibm.com/ontologies/aiont/ai-risk-ontology




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | airo:hasLicense |
| native | nexus:hasLicense |




## LinkML Source

<details>
```yaml
name: hasLicense
description: Indicates licenses associated with a resource
from_schema: http://research.ibm.com/ontologies/aiont/ai-risk-ontology
rank: 1000
slot_uri: airo:hasLicense
alias: hasLicense
domain_of:
- Dataset
- RiskTaxonomy
- AiEval
- BaseAi
range: License

```
</details>