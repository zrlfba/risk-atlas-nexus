

# Slot: hasOutputModality


_A relationship indicating the output modalities supported by an AI component. Examples include text, image, video._





URI: [nexus:hasOutputModality](http://research.ibm.com/ontologies/aiont/hasOutputModality)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LargeLanguageModel](LargeLanguageModel.md) | A large language model (LLM) is an AI model which supports a range of languag... |  no  |







## Properties

* Range: [Modality](Modality.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: http://research.ibm.com/ontologies/aiont/ai-risk-ontology




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nexus:hasOutputModality |
| native | nexus:hasOutputModality |




## LinkML Source

<details>
```yaml
name: hasOutputModality
description: A relationship indicating the output modalities supported by an AI component.
  Examples include text, image, video.
from_schema: http://research.ibm.com/ontologies/aiont/ai-risk-ontology
rank: 1000
alias: hasOutputModality
domain_of:
- LargeLanguageModel
range: Modality
multivalued: true
inlined: false

```
</details>