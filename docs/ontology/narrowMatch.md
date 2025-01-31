

# Slot: narrowMatch


_The property is used to state a hierarchical mapping link between two concepts, indicating that the concept linked to, is a narrower concept than the originating concept._





URI: [skos:narrowMatch](skos:narrowMatch)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Risk](Risk.md) | The state of uncertainty associated with an AI system, that has the potential... |  no  |







## Properties

* Range: [Risk](Risk.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: http://research.ibm.com/ontologies/aiont/ai-risk-ontology




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | skos:narrowMatch |
| native | nexus:narrowMatch |




## LinkML Source

<details>
```yaml
name: narrowMatch
description: The property is used to state a hierarchical mapping link between two
  concepts, indicating that the concept linked to, is a narrower concept than the
  originating concept.
from_schema: http://research.ibm.com/ontologies/aiont/ai-risk-ontology
rank: 1000
slot_uri: skos:narrowMatch
alias: narrowMatch
domain_of:
- Risk
range: Risk
multivalued: true
inlined: false

```
</details>