

# Slot: detectsRiskConcept


_The property airo:detectsRiskConcept indicates the control used for detecting risks, risk sources, consequences, and impacts._





URI: [nexus:detectsRiskConcept](http://research.ibm.com/ontologies/aiont/detectsRiskConcept)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RiskControl](RiskControl.md) | A measure that maintains and/or modifies risk (and risk concepts) |  no  |







## Properties

* Range: [Any](Any.md)&nbsp;or&nbsp;<br />[Risk](Risk.md)&nbsp;or&nbsp;<br />[RiskGroup](RiskGroup.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: http://research.ibm.com/ontologies/aiont/ai-risk-ontology




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nexus:detectsRiskConcept |
| native | nexus:detectsRiskConcept |
| exact | airo:detectsRiskConcept |




## LinkML Source

<details>
```yaml
name: detectsRiskConcept
description: The property airo:detectsRiskConcept indicates the control used for detecting
  risks, risk sources, consequences, and impacts.
from_schema: http://research.ibm.com/ontologies/aiont/ai-risk-ontology
exact_mappings:
- airo:detectsRiskConcept
rank: 1000
alias: detectsRiskConcept
domain_of:
- RiskControl
range: Any
multivalued: true
inlined: false
any_of:
- range: Risk
- range: RiskGroup

```
</details>