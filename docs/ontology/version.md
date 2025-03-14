

# Slot: version


_The version of the entity embodied by a specified resource._





URI: [schema:version](http://schema.org/version)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RiskTaxonomy](RiskTaxonomy.md) | A taxonomy of AI system related risks |  no  |
| [License](License.md) | The general notion of a license which defines terms and grants permissions to... |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://research.ibm.com/ontologies/aiont/ai-risk-ontology




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:version |
| native | nexus:version |




## LinkML Source

<details>
```yaml
name: version
description: The version of the entity embodied by a specified resource.
from_schema: http://research.ibm.com/ontologies/aiont/ai-risk-ontology
rank: 1000
slot_uri: schema:version
alias: version
domain_of:
- License
- RiskTaxonomy
range: string

```
</details>