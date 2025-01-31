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

    def get_risk_by_tag(self, tag=None):
        """Get all risk definitions from the LinkML

        Args:
            tag: str
                The string tag for a risk

        Returns:
            Risk
                Result containing a list of AI risks
        """
        matching_risks = list(filter(lambda risk: risk.tag == tag, self._risks))
        if len(matching_risks) > 0:
            return matching_risks[0]
        else:
            print("No matching risk found")
            return None

    def get_risk_by_id(self, id=None):
        """Get all risk definitions from the LinkML

        Args:
            id: str
                The string id for a risk

        Returns:
            Risk
                Result containing an AI risks
        """
        matching_risks = list(filter(lambda risk: risk.id == id, self._risks))

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

        related_risks = [j for i in related_risks for j in i]
        return related_risks

    def get_related_risk_ids_by_atlas_tag(self, tag=None, taxonomy=None):
        """Get all related risk definitions from the LinkML by the IBM risk atlas tag

        Args:
            tag: str
                The string tag for a risk
            taxonomy: str
                (Optional) The string label for a taxonomy

        Returns:
            list[str]
                Result containing a list of AI risks IDs
        """
        atlas_risk = list(filter(lambda risk: risk.tag == tag, self._risks))

        if len(atlas_risk) > 0:
            initial_risk: Risk = atlas_risk[0]
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

    def get_related_risks_by_atlas_tag(self, tag=None, taxonomy=None):
        """Get all risk definitions from the LinkML

        Args:
            tag: str
                The string tag for a risk
            taxonomy: str
                (Optional) The string label for a taxonomy

        Returns:
            list[Risk]
                Result containing a list of AI risks
        """
        related_risk_ids = self.get_related_risk_ids_by_atlas_tag(tag, taxonomy)
        if related_risk_ids is not None:
            related_risks = [self.get_risk_by_id(id) for id in related_risk_ids]
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

    def get_related_risk_ids_by_risk_id(self, id=None, taxonomy=None):
        """Get all risk definitions from the LinkML

        Args:
            id: str
                (Optional) The string label for a risk
            taxonomy: str
                (Optional) The string label for a taxonomy

        Returns:
            list[str]
                Result containing a list of AI risk IDs
        """
        risks = list(filter(lambda risk: risk.id == id, self._risks))

        if len(risks) > 0:
            initial_risk: Risk = risks[0]
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

    def get_related_risks_by_risk_id(self, id=None, taxonomy=None):
        """Get related risk definitions from the LinkML from a given risk id

        Args:
            id: str
                (Optional) The string id for a risk

        Returns:
            list[Risk]
                Result containing a list of AI risks
        """
        related_risk_ids = self.get_related_risk_ids_by_risk_id(id)
        if related_risk_ids is not None:
            related_risks = [self.get_risk_by_id(id) for id in related_risk_ids]

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

    def get_risk_actions_by_risk_id(self, id, taxonomy=None):
        """Get actions for a risk from the LinkML

        Args:
            id: str
                The string id for a risk
            taxonomy: str
                (Optional) The string label for a taxonomy

        Returns:
            list[Action]
                Result containing a list of AI risks actions
        """
        risks = list(filter(lambda risk: risk.id == id, self._risks))

        if len(risks) > 0:
            risk: Risk = risks[0]
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
