# flake8: noqa
from langchain.prompts import PromptTemplate

# Use a shorter template to reduce the number of tokens in the prompt
template = """Créez une réponse finale aux questions données en utilisant les extraits de documents fournis (dans un ordre quelconque) comme références. Incluez TOUJOURS une section "SOURCES" dans votre réponse, comprenant uniquement l'ensemble minimal de sources nécessaires pour répondre à la question. Si vous ne pouvez pas répondre à la question, indiquez simplement que vous ne savez pas. N'essayez pas de fabriquer une réponse et laissez la section SOURCES vide.

---------

QUESTION: Quel est le but d'ARPA-H ?
=========
Contenu : Plus de soutien pour les patients et les familles. \n\nPour y parvenir, j'appelle le Congrès à financer ARPA-H, l'Agence pour les projets de recherche avancée en santé. \n\nElle est basée sur DARPA, le projet du Département de la Défense qui a conduit à Internet, au GPS et bien plus encore. \n\nARPA-H aura un objectif unique : favoriser les percées dans le cancer, la maladie d'Alzheimer, le diabète, et bien d'autres domaines.
Source : 1-32
Contenu : Pendant que nous y sommes, assurons-nous que chaque Américain puisse obtenir les soins de santé dont il a besoin. \n\nNous avons déjà fait des investissements historiques dans les soins de santé. \n\nNous avons facilité l'accès des Américains aux soins dont ils ont besoin, quand ils en ont besoin. \n\nNous avons facilité l'accès des Américains aux traitements dont ils ont besoin, quand ils en ont besoin. \n\nNous avons facilité l'accès des Américains aux médicaments dont ils ont besoin, quand ils en ont besoin.
Source : 1-33
Contenu : Le V.A. est à la pointe de nouvelles façons de relier les expositions toxiques aux maladies, aidant déjà les anciens combattants à obtenir les soins qu'ils méritent. \n\nNous devons étendre les mêmes soins à tous les Américains. \n\nC'est pourquoi j'appelle le Congrès à adopter une législation qui établirait un registre national des expositions toxiques et fournirait des soins de santé et une aide financière aux personnes touchées.
Source : 1-30
=========
RÉPONSE FINALE : Le but d'ARPA-H est de favoriser les percées dans le cancer, la maladie d'Alzheimer, le diabète, et bien d'autres domaines.
SOURCES : 1-32

---------

QUESTION: {question}
=========
{summaries}
=========
FINAL ANSWER:"""

STUFF_PROMPT = PromptTemplate(
    template=template, input_variables=["summaries", "question"]
)
