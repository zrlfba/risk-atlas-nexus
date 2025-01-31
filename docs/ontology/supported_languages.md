

# Slot: supported_languages


_A list of languages, expressed as ISO two letter codes. For example, 'jp, fr, en, de'_





URI: [nexus:supported_languages](http://research.ibm.com/ontologies/aiont/supported_languages)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LargeLanguageModel](LargeLanguageModel.md) | A large language model (LLM) is an AI model which supports a range of languag... |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: http://research.ibm.com/ontologies/aiont/ai-risk-ontology




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nexus:supported_languages |
| native | nexus:supported_languages |




## LinkML Source

<details>
```yaml
name: supported_languages
description: A list of languages, expressed as ISO two letter codes. For example,
  'jp, fr, en, de'
from_schema: http://research.ibm.com/ontologies/aiont/ai-risk-ontology
rank: 1000
alias: supported_languages
domain_of:
- LargeLanguageModel
range: string
multivalued: true
inlined: true
inlined_as_list: true

```
</details>