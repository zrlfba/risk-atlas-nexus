from typing import  Union
from pydantic import BaseModel

from linkml_runtime.dumpers.dumper_root import Dumper
from linkml_runtime.utils.context_utils import CONTEXTS_PARAM_TYPE
from linkml_runtime.utils.yamlutils import YAMLRoot


class LatexDumper(Dumper):

    def dump(self, element: Union[BaseModel, YAMLRoot], to_file: str, contexts: CONTEXTS_PARAM_TYPE = None,
             **kwargs) -> None:
        """
        Write element as latex to to_file
        
        Args:
            element: Union[BaseModel, YAMLRoot]
                LinkML object to be output
            to_file: str
                file to write to
        """
        if isinstance(element, BaseModel):
            element = element.dict()
            
        print("ok")
        super().dump(element, to_file, contexts=contexts, **kwargs)

    def dumps(self, element: Union[BaseModel, YAMLRoot]) -> str:
        """
        Return element as latex string

        Args:
            element: Union[BaseModel, YAMLRoot],
                LinkML object to be emitted
            inject_type: 
                if True (default), add a @type at the top level
        Returns: 
            str
        """
        if isinstance(element, BaseModel):
            element = element.dict()
            element = self._to_tex_from_dict(element)
        return element


    def _to_tex_from_dict(self, element_dict) -> str:
        """
        Format as tex

        Args:
            element_dict: dict
        
        Returns:
            str
        """
        tex = []
        tex.append("\\documentclass{article}\n")
        tex.append("\\begin{document}\n")
        tex.append("\\section{IBM AI Risk Atlas}\n")
        tex.append("Explore this atlas to understand some of the risks of working with generative AI, foundation models, and machine learning models. Risks are categorized with one of these tags:\n")
        tex.append("\\begin{itemize}\n")
        tex.append("\\item Traditional AI risks (applies to traditional models as well as generative AI)\n")
        tex.append("\\item Risks amplified by generative AI (might also apply to traditional models)\n")
        tex.append("\\item New risks specifically associated with generative AI\n")
        tex.append("\\end{itemize}\n")
        tex.append("\\subsection*{AI risks}\n")
        for risk in element_dict["risks"]:
            tex.append("\\subsubsection*{" + risk["name"] + "}\n")
            tex.append(risk["description"].replace("’", "'").replace(" ", " ")+ "\\newline\n")
            tex.append("\\textit{Concern: }" + risk["concern"].replace("’", "'").replace(" ", " ")+ "\\newline\\newline\n")
            tex.append("\\textit{Type: }" + risk["type"].replace("’", "'").replace(" ", " ")+ "\\newline\n")
            tex.append("\\textit{Descriptor: }" + risk["descriptor"] + " \\newline\\newline\n")
            tex.append("\\textit{Implementation details:}" + " \\newline\n")
            tex.append("Descriptor: " + risk["descriptor"] + " \\newline\n")
            tex.append("ID: " + risk["id"] + " \\newline\n")
            tex.append("Tag: " + risk["tag"] + " \\newline\n")
            tex.append("URI:  " + risk["url"] + "\\newline\n")
        tex.append("\\end{document}\n")
        tex_all = "".join(tex)
        return tex_all
