# MyChatBot

Un chatbot simple en Python basé sur des règles prédéfinies.

## 📋 Description

Ce projet implémente un chatbot simple capable de répondre à des questions basiques en utilisant un système de correspondance de motifs (pattern matching). Le chatbot reconnaît certains mots-clés dans les messages de l'utilisateur et répond avec des réponses prédéfinies.

## 🎯 Fonctionnalités

- Interface en ligne de commande interactive
- Système de gestion de conversations basé sur des règles
- Réponses automatiques à des questions fréquemment posées
- Base de connaissances facilement extensible via JSON
- Support du français et de l'anglais
- **Nouvelles fonctionnalités NLP** :
  - **NLTK** : Tokenisation, lemmatisation, suppression de mots vides, étiquetage POS
  - **spaCy** : Reconnaissance d'entités nommées (NER), similarité sémantique
  - **Transformers** : Analyse de sentiment avec modèles pré-entraînés

## 🏗️ Structure du projet

```
MyChatBot/
│
├── main.py           # Point d'entrée du programme
├── bot.py            # Logique du chatbot (réponses, gestion du dialogue)
├── nlp_utils.py      # Module d'utilitaires NLP (NLTK, spaCy, transformers)
├── nlp_demo.py       # Script de démonstration des fonctionnalités NLP
├── data/
│   └── faq.json      # Fichier de questions/réponses
├── requirements.txt  # Dépendances Python (incluant NLTK, spaCy, transformers)
└── README.md         # Documentation du projet
```

## 🚀 Installation

### Prérequis

- Python 3.6 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes

1. Clonez le dépôt :
```bash
git clone https://github.com/louisbertrand22/MyChatBot.git
cd MyChatBot
```

2. (Optionnel mais recommandé) Créez un environnement virtuel :
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

3. Installez les dépendances :
```bash
pip install -r requirements.txt
```

4. (Optionnel) Pour utiliser toutes les fonctionnalités spaCy, téléchargez le modèle anglais :
```bash
python -m spacy download en_core_web_sm
```

**Note** : L'installation des dépendances NLP (NLTK, spaCy, transformers) peut prendre plusieurs minutes car elles incluent de gros modèles pré-entraînés.

## 💻 Utilisation

### Démarrer le chatbot

**Mode simple (sans NLP) :**
```bash
python main.py
```

**Mode avec NLP activé :**
```bash
python main.py --nlp
```

**Mode avec NLP et analyse détaillée :**
```bash
python main.py --nlp-info
```

**Ou directement :**
```bash
python bot.py
```

### Démonstration des fonctionnalités NLP

Pour voir une démonstration complète des capacités NLP :
```bash
python nlp_demo.py
```

Pour tester le chatbot avec NLP en mode démonstration :
```bash
python nlp_demo.py --chatbot
```

### Exemples d'interaction

```
Vous: Bonjour
Bot: Salut ! Que puis-je faire pour vous ?

Vous: Comment ça va ?
Bot: Je vais bien, merci ! Et vous ?

Vous: Quel est ton nom ?
Bot: Je m'appelle ChatBot. Je suis là pour répondre à vos questions.

Vous: Merci
Bot: De rien ! Heureux de vous aider.

Vous: Au revoir
Bot: À bientôt ! Bonne journée !
```

### Quitter le chatbot

Tapez `quit`, `exit` ou `quitter` pour terminer la conversation, ou utilisez `Ctrl+C`.

## 📚 Personnalisation

### Ajouter de nouvelles réponses

Éditez le fichier `data/faq.json` pour ajouter de nouveaux patterns et réponses :

```json
{
  "nom_intention": {
    "patterns": ["mot-clé1", "mot-clé2", "expression"],
    "responses": [
      "Réponse 1",
      "Réponse 2",
      "Réponse 3"
    ]
  }
}
```

Le chatbot choisit aléatoirement une réponse parmi celles disponibles pour chaque intention.

### Fonctionnalités NLP disponibles

Le module `nlp_utils.py` fournit une classe `NLPProcessor` avec les méthodes suivantes :

- **NLTK** :
  - `tokenize(text)` : Tokenisation du texte
  - `remove_stopwords(tokens)` : Suppression des mots vides
  - `lemmatize(tokens)` : Lemmatisation des tokens
  - `preprocess_text(text)` : Pipeline complet de prétraitement
  - `get_pos_tags(text)` : Étiquetage grammatical (POS tagging)

- **spaCy** :
  - `extract_entities(text)` : Extraction d'entités nommées
  - `compute_similarity(text1, text2)` : Calcul de similarité sémantique

- **Transformers** :
  - `analyze_sentiment(text)` : Analyse de sentiment

Exemple d'utilisation :
```python
from nlp_utils import get_nlp_processor

nlp = get_nlp_processor()
tokens = nlp.tokenize("Hello, how are you?")
sentiment = nlp.analyze_sentiment("I love this!")
entities = nlp.extract_entities("Apple Inc. is in California")
```

## 🔮 Améliorations futures

- [x] ~~Ajouter un modèle d'apprentissage automatique (NLTK, spaCy)~~ ✅
- [x] ~~Ajouter le traitement du langage naturel (NLP)~~ ✅
- [ ] Créer une interface web avec Flask ou Streamlit
- [ ] Implémenter un système de contexte pour les conversations
- [ ] Sauvegarder l'historique des conversations
- [ ] Support multilingue amélioré avec modèles spaCy français
- [ ] Intégration de modèles de génération de texte (GPT-2, etc.)
- [ ] Système de dialogue basé sur l'intention avec apprentissage automatique

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou un pull request.

## 📝 Licence

Ce projet est libre d'utilisation pour l'apprentissage et l'éducation.

## 👨‍💻 Auteur

Louis Bertrand