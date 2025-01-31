

# Slot: provider


_A relationship to the Organization instance that provides this instance._





URI: [schema:provider](http://schema.org/provider)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dataset](Dataset.md) | A body of structured information describing some topic(s) of interest |  no  |







## Properties

* Range: [Organization](Organization.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://research.ibm.com/ontologies/aiont/ai-risk-ontology




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:provider |
| native | nexus:provider |




## LinkML Source

<details>
```yaml
name: provider
description: A relationship to the Organization instance that provides this instance.
from_schema: http://research.ibm.com/ontologies/aiont/ai-risk-ontology
rank: 1000
slot_uri: schema:provider
alias: provider
domain_of:
- Dataset
range: Organization

```
</details>