# Convenience script to export a loaded graph from all the yaml 
# in src/risk_atlas_nexus/data/knowledge_graph

import os
from risk_atlas_nexus import RiskAtlasNexus
from risk_atlas_nexus.toolkit.logging import configure_logger

logger = configure_logger(__name__)

ran = RiskAtlasNexus()

# export the graph to yaml
ran.export('graph_export/yaml/')
