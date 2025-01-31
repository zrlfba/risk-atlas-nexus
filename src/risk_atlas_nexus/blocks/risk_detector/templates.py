IBM_PROMPT_TEMPLATE = """You are an expert at AI risk classification. Study the JSON below containing list of risk category and its description. 

{risks}

The task is to identify the potential risks associated with the Input context and classify it into the given risk categories. If input doesn't fit into any of the above categories, classify it as Unknown. Respond with a  list of attribute 'category' containing the classification labels.

Input: In a medical chatbot, generative AI can be employed to create a triage system that assesses patients' symptoms and provides immediate, contextually relevant advice based on their medical history and current condition. The chatbot can analyze the patient's input, identify potential medical issues, and offer tailored recommendations or insights to the patient or healthcare provider. This can help streamline the triage process, ensuring that patients receive the appropriate level of care and attention, and ultimately improving patient outcomes.
Output:  ["Improper usage", "Incomplete advice", "Lack of model transparency", "Lack of system transparency", "Lack of training data transparency", "Data bias", "Uncertain data provenance", "Lack of data transparency", "Impact on human agency", "Impact on affected communities", "Improper retraining", "Inaccessible training data"]<|eom_id|>

Input: {query}
Output:"""

MIT_PROMPT_TEMPLATE = """You are an expert at AI risk classification. Study the JSON below containing list of risk category and its description. 

{risks}

The task is to identify the potential risks associated with the Input context and classify it into the given risk categories. If input doesn't fit into any of the above categories, classify it as Unknown. Respond with a  list of attribute 'category' containing the classification labels.

Input: In a medical chatbot, generative AI can be employed to create a triage system that assesses patients' symptoms and provides immediate, contextually relevant advice based on their medical history and current condition. The chatbot can analyze the patient's input, identify potential medical issues, and offer tailored recommendations or insights to the patient or healthcare provider. This can help streamline the triage process, ensuring that patients receive the appropriate level of care and attention, and ultimately improving patient outcomes.
Output:  ["Loss of human agency and autonomy", "Lack of transparency or interpretability", "Overreliance and unsafe use"]<|eom_id|>

Input: {query}
Output:"""

NIST_PROMPT_TEMPLATE = """You are an expert at AI risk classification. Study the JSON below containing list of risk category and its description. 

{risks}

The task is to identify the potential risks associated with the Input context and classify it into the given risk categories. If input doesn't fit into any of the above categories, classify it as Unknown. Respond with a  list of attribute 'category' containing the classification labels.

Input: In a medical chatbot, generative AI can be employed to create a triage system that assesses patients' symptoms and provides immediate, contextually relevant advice based on their medical history and current condition. The chatbot can analyze the patient's input, identify potential medical issues, and offer tailored recommendations or insights to the patient or healthcare provider. This can help streamline the triage process, ensuring that patients receive the appropriate level of care and attention, and ultimately improving patient outcomes.
Output:  ["Harmful Bias or Homogenization", "Information Security", "Value Chain and Component Integration"]<|eom_id|>

Input: {query}
Output:"""

GG_PROMPT_TEMPLATE = """You are an expert at AI risk classification. Study the JSON below containing list of risk category and its description. 

{risks}

The task is to identify the potential risks associated with the Input context and classify it into the given risk categories. If input doesn't fit into any of the above categories, classify it as Unknown. Respond with a  list of attribute 'category' containing the classification labels.

Input: In a medical chatbot, generative AI can be employed to create a triage system that assesses patients' symptoms and provides immediate, contextually relevant advice based on their medical history and current condition. The chatbot can analyze the patient's input, identify potential medical issues, and offer tailored recommendations or insights to the patient or healthcare provider. This can help streamline the triage process, ensuring that patients receive the appropriate level of care and attention, and ultimately improving patient outcomes.
Output:  ['Harm', 'Social Bias', 'Violence', 'Answer Relevance', 'Context Relevance', 'Function Calling Hallucination']

Input: {query}
Output:"""

PROMPT_TEMPLATE = """You are an expert at AI risk classification. Study the JSON below containing list of risk category and its description. 

{risks}

The task is to identify the potential risks associated with the Input context and classify it into the given risk categories. If input doesn't fit into any of the above categories, classify it as Unknown. Respond with a  list of attribute 'category' containing the classification labels.

Input: {query}
Output:"""
