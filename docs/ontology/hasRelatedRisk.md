

# Slot: hasRelatedRisk


_A relationship where an entity relates to a risk_





URI: [nexus:hasRelatedRisk](http://research.ibm.com/ontologies/aiont/hasRelatedRisk)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Action](Action.md) | Action to remediate a risk |  no  |
| [Question](Question.md) | An evaluation where a question has to be answered |  no  |
| [AiEval](AiEval.md) | An AI Evaluation, e |  no  |
| [Questionnaire](Questionnaire.md) | A questionnaire groups questions |  no  |







## Properties

* Range: [Risk](Risk.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: http://research.ibm.com/ontologies/aiont/ai-risk-ontology




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nexus:hasRelatedRisk |
| native | nexus:hasRelatedRisk |




## LinkML Source

<details>
```yaml
name: hasRelatedRisk
description: A relationship where an entity relates to a risk
from_schema: http://research.ibm.com/ontologies/aiont/ai-risk-ontology
rank: 1000
alias: hasRelatedRisk
domain_of:
- Action
- AiEval
range: Risk
multivalued: true
inlined: false

```
</details>