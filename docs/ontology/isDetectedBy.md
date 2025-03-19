

# Slot: isDetectedBy


_A relationship where a risk, risk source, consequence, or impact is detected by a risk control._





URI: [nexus:isDetectedBy](http://research.ibm.com/ontologies/aiont/isDetectedBy)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RiskGroup](RiskGroup.md) | A group of AI system related risks that are part of a risk taxonomy |  no  |
| [Risk](Risk.md) | The state of uncertainty associated with an AI system, that has the potential... |  no  |
| [RiskConcept](RiskConcept.md) | An umbrella term for refering to risk, risk source, consequence and impact |  no  |







## Properties

* Range: [RiskControl](RiskControl.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: http://research.ibm.com/ontologies/aiont/ai-risk-ontology




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nexus:isDetectedBy |
| native | nexus:isDetectedBy |




## LinkML Source

<details>
```yaml
name: isDetectedBy
description: A relationship where a risk, risk source, consequence, or impact is detected
  by a risk control.
from_schema: http://research.ibm.com/ontologies/aiont/ai-risk-ontology
rank: 1000
alias: isDetectedBy
domain_of:
- RiskConcept
inverse: detectsRiskConcept
range: RiskControl
multivalued: true
inlined: false

```
</details>