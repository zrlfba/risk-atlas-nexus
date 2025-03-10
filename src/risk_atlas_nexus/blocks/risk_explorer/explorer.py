from risk_atlas_nexus.blocks.risk_explorer.base import ExplorerBase
from risk_atlas_nexus.ai_risk_ontology.datamodel.ai_risk_ontology import Risk
from risk_atlas_nexus.data.knowledge_graph import *


class RiskExplorer(ExplorerBase):

    def __init__(self, ontology):

        # load the data into the graph
        self._ontology = ontology
        self._risks = ontology.risks
        self._actions = ontology.actions
        self._taxonomies = ontology.taxonomies

    def get_all_risks(self, taxonomy=None):
        """Get all risk definitions from the LinkML

        Args:
            taxonomy: str
                (Optional) The string label for a taxonomy

        Returns:
            list[Risk]
                Result containing a list of AI risks
        """
        risk_instances = self._risks
        if taxonomy is not None:
            risk_instances = list(
                filter(
                    lambda risk: risk.isDefinedByTaxonomy == taxonomy, risk_instances
                )
            )

        return risk_instances

    def get_risk(self, tag=None, id=None, name=None, taxonomy=None):
        """Get a risk definition from the LinkML by tag, id or name

        Args:
            id: (Optional) str
                The string ID identifying the risk
            tag: (Optional) str
                The string tag identifying the risk
            name: (Optional) str
                The string name identifying the risk
            taxonomy: str
                (Optional) The string label for a taxonomy

        Returns:
            Risk
                An AI risk result
        """
        matching_risks = self._risks
        if tag is not None:
            matching_risks = list(filter(lambda risk: risk.tag == tag, matching_risks))
        if id is not None:
            matching_risks = list(filter(lambda risk: risk.id == id, matching_risks))
        if name is not None:
            matching_risks = list(
                filter(lambda risk: risk.name == name, matching_risks)
            )
        if taxonomy is not None:
            matching_risks = list(
                filter(
                    lambda risk: risk.isDefinedByTaxonomy == taxonomy, matching_risks
                )
            )

        if len(matching_risks) > 0:
            return matching_risks[0]
        else:
            print("No matching risk found")
            return None

    def _combine_related_risks(self, initial_risk):
        """Convenience function to combine the related risks from a Risk

        Args:
            initial_risk: Risk
                The risk to parse for related risks

        Returns:
            list[str]
                Result containing a list of AI risk IDs
        """
        related_risks = []
        if initial_risk.broadMatch is not None:
            related_risks.append(initial_risk.broadMatch)
        if initial_risk.closeMatch is not None:
            related_risks.append(initial_risk.closeMatch)
        if initial_risk.exactMatch is not None:
            related_risks.append(initial_risk.exactMatch)
        if initial_risk.narrowMatch is not None:
            related_risks.append(initial_risk.narrowMatch)
        if initial_risk.relatedMatch is not None:
            related_risks.append(initial_risk.relatedMatch)

        related_risk_ids = [j for i in related_risks for j in i]
        related_risks = list(
            filter(lambda risk: risk.id in related_risk_ids, self._risks)
        )
        return related_risks

    def get_related_risks(self, risk=None, tag=None, id=None, name=None, taxonomy=None):
        """Get all related risk definitions from the LinkML by the IBM risk atlas tag

        Args:
            risk: (Optional) Risk
                The Risk object to find related risks for
            id: (Optional) str
                The string ID identifying the risk
            tag: (Optional) str
                The string tag identifying the risk
            name: (Optional) str
                The string name identifying the risk
            taxonomy: str
                (Optional) The string label for a taxonomy

        Returns:
            list[str]
                Result containing a list of AI risks IDs
        """
        matching_risks = self._risks

        if risk is not None:
            matching_risks = [risk]
        if tag is not None:
            matching_risks = list(filter(lambda risk: risk.tag == tag, matching_risks))
        if id is not None:
            matching_risks = list(filter(lambda risk: risk.id == id, matching_risks))
        if name is not None:
            matching_risks = list(
                filter(lambda risk: risk.name == name, matching_risks)
            )

        if len(matching_risks) > 0:
            initial_risk: Risk = matching_risks[0]
            related_risks = self._combine_related_risks(initial_risk)

            if taxonomy is not None:
                related_risks = list(
                    filter(
                        lambda risk: risk.isDefinedByTaxonomy == taxonomy, related_risks
                    )
                )

            return related_risks
        else:
            print("No matching risk found")
            return None

    def get_related_actions(
        self, risk=None, tag=None, id=None, name=None, taxonomy=None
    ):
        """Get actions for a risk from the LinkML

        Args:
            risk: (Optional) Risk
                The Risk object to find related actions for
            id: (Optional) str
                The string ID identifying the risk to find related actions for
            tag: (Optional) str
                The string tag identifying the risk to find related actions for
            name: (Optional) str
                The string name identifying the risk to find related actions for
            taxonomy: str
                (Optional) The string label for a taxonomy, to filter action results by

        Returns:
            list[Action]
                Result containing a list of the actions which are marked as related to the specified AI risk
        """
        matching_risks = self._risks

        if risk is not None:
            matching_risks = [risk]
        if tag is not None:
            matching_risks = list(filter(lambda risk: risk.tag == tag, matching_risks))
        if id is not None:
            matching_risks = list(filter(lambda risk: risk.id == id, matching_risks))
        if name is not None:
            matching_risks = list(
                filter(lambda risk: risk.name == name, matching_risks)
            )

        if len(matching_risks) > 0:
            risk: Risk = matching_risks[0]
            actions = []

            if risk.hasRelatedAction is not None:
                actions.append(risk.hasRelatedAction)

            actions = [j for i in actions for j in i]

            if taxonomy is not None:
                actions = list(
                    filter(
                        lambda action: action.isDefinedByTaxonomy == taxonomy, actions
                    )
                )

            return actions
        else:
            print("No matching actions found")
            return None

    def get_all_actions(self, taxonomy=None):
        """Get all actions definitions from the LinkML

        Args:
            taxonomy: str
                (Optional) The string label for a taxonomy

        Returns:
            list[Action]
                Result containing a list of AI actions
        """
        action_instances = self._actions

        if taxonomy is not None:
            action_instances = list(
                filter(
                    lambda action: action.isDefinedByTaxonomy == taxonomy,
                    action_instances,
                )
            )

        return action_instances

    def get_action_by_id(self, id):
        """Get action definition from the LinkML by ID

        Args:
            id: str
                The string id for an action

        Returns:
            Action
                Result containing an AI actions
        """
        matching_actions = list(filter(lambda action: action.id == id, self._actions))

        if len(matching_actions) > 0:
            return matching_actions[0]
        else:
            print("No matching risk found")
            return None

    def get_all_taxonomies(self):
        """Get all taxonomy definitions from the LinkML

        Returns:
            list[RiskTaxonomy]
                Result containing a list of risk taxonomies
        """
        return self._taxonomies

    def get_taxonomy_by_id(self, id):
        """Get taxonomy definition from the LinkML by ID

        Args:
            id: str
                The string id for a taxonomy

        Returns:
            RiskTaxonomy
                Result containing an AI RiskTaxonomy
        """
        matching_taxonomies = list(
            filter(lambda taxonomy: taxonomy.id == id, self._taxonomies)
        )

        if len(matching_taxonomies) > 0:
            return matching_taxonomies[0]
        else:
            print("No matching taxonomy found")
            return None
