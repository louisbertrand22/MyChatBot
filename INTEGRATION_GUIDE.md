# Guide d'intégration NLP pour MyChatBot

Ce guide explique comment les bibliothèques NLP (NLTK, spaCy, Transformers) ont été intégrées dans le chatbot et comment les utiliser.

## 📚 Bibliothèques intégrées

### 1. NLTK (Natural Language Toolkit)
**Version** : 3.9+

**Fonctionnalités utilisées** :
- **Tokenisation** : Découpe le texte en mots individuels
- **Lemmatisation** : Réduit les mots à leur forme de base (ex: "running" → "run")
- **Stopwords** : Filtre les mots communs sans signification (ex: "le", "la", "un")
- **POS Tagging** : Identifie la nature grammaticale des mots (nom, verbe, adjectif, etc.)

**Exemple d'utilisation** :
```python
from nlp_utils import get_nlp_processor

nlp = get_nlp_processor()

# Tokenisation
tokens = nlp.tokenize("Hello, how are you today?")
# Résultat: ['hello', ',', 'how', 'are', 'you', 'today', '?']

# Prétraitement complet
processed = nlp.preprocess_text("I am running in the park")
# Résultat: ['run', 'park'] (après stopwords et lemmatisation)
```

### 2. spaCy
**Version** : 3.7.0+
**Modèle requis** : `en_core_web_sm`

**Fonctionnalités utilisées** :
- **Named Entity Recognition (NER)** : Extraction d'entités nommées (personnes, lieux, organisations, etc.)
- **Similarité sémantique** : Calcul de similarité entre deux textes basé sur le sens
- **Pipeline NLP avancé** : Analyse linguistique complète

**Exemple d'utilisation** :
```python
from nlp_utils import get_nlp_processor

nlp = get_nlp_processor()

# Extraction d'entités nommées
entities = nlp.extract_entities("Apple Inc. was founded by Steve Jobs in California")
# Résultat: [('Apple Inc.', 'ORG'), ('Steve Jobs', 'PERSON'), ('California', 'GPE')]

# Similarité sémantique
similarity = nlp.compute_similarity(
    "I love programming",
    "I enjoy coding"
)
# Résultat: ~0.85 (score élevé = très similaire)
```

### 3. Transformers (Hugging Face)
**Version** : 4.48.0+
**Modèles utilisés** : 
- `distilbert-base-uncased-finetuned-sst-2-english` (analyse de sentiment)
- `gpt2` (génération de texte)

**Fonctionnalités utilisées** :
- **Analyse de sentiment** : Détermine si un texte est positif ou négatif
- **Génération de texte (GPT-2)** : Génère du texte naturel à partir d'un prompt
- **Modèles pré-entraînés** : Utilise des modèles de deep learning pour l'analyse de texte

**Exemple d'utilisation** :
```python
from nlp_utils import get_nlp_processor

nlp = get_nlp_processor()

# Analyse de sentiment
sentiment = nlp.analyze_sentiment("I love this chatbot! It's amazing!")
# Résultat: {'label': 'POSITIVE', 'score': 0.9998}

sentiment = nlp.analyze_sentiment("This is terrible and disappointing.")
# Résultat: {'label': 'NEGATIVE', 'score': 0.9995}

# Génération de texte avec GPT-2
generated = nlp.generate_text(
    "Once upon a time",
    max_length=50,
    num_return_sequences=1,
    temperature=0.7
)
# Résultat: ["Once upon a time, there was a small village..."]
```

## 🚀 Installation complète

### Étape 1 : Installer les dépendances Python

```bash
pip install -r requirements.txt
```

Cette commande installera :
- nltk >= 3.9
- spacy >= 3.7.0
- transformers >= 4.48.0
- torch >= 2.6.0

**Note** : L'installation peut prendre 5-10 minutes et nécessiter 2-3 GB d'espace disque.

### Étape 2 : Télécharger le modèle spaCy

```bash
python -m spacy download en_core_web_sm
```

Ce modèle est nécessaire pour les fonctionnalités spaCy (NER, similarité).

### Étape 3 : Télécharger les ressources NLTK

Les ressources NLTK sont téléchargées automatiquement au premier lancement. Vous pouvez aussi les télécharger manuellement :

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
```

## 💡 Utilisation du chatbot avec NLP

### Mode standard (sans NLP)
```bash
python main.py
```

### Mode avec NLP activé
```bash
python main.py --nlp
```

### Mode avec analyse NLP détaillée
```bash
python main.py --nlp-info
```

En mode `--nlp-info`, chaque réponse inclut :
- Le sentiment détecté (positif/négatif)
- Les entités nommées trouvées
- Les mots-clés extraits

### Mode avec génération de texte GPT
```bash
python main.py --gpt
```

En mode `--gpt`, le chatbot utilise GPT-2 pour générer des réponses plus naturelles et créatives au lieu d'utiliser des réponses prédéfinies.

### Exemple de conversation avec NLP

```
Vous: Hello! I'm John from New York and I'm feeling great!
Bot: Bonjour ! Comment puis-je vous aider ?

--- Analyse NLP ---
Sentiment: Positif (0.99)
Entités détectées: John (PERSON), New York (GPE)
Mots-clés: hello, john, new, york, feel, great
```

## 🔧 Architecture du code

### Structure modulaire

```
MyChatBot/
│
├── nlp_utils.py          # Module NLP principal
│   ├── NLPProcessor      # Classe principale d'intégration NLP
│   └── get_nlp_processor() # Singleton pour accès global
│
├── bot.py                # Chatbot amélioré avec NLP
│   ├── ChatBot.__init__(use_nlp=True/False)
│   ├── find_intent()     # Recherche d'intention (avec ou sans NLP)
│   ├── _find_intent_nlp() # Recherche d'intention améliorée par NLP
│   └── _get_nlp_analysis() # Analyse NLP détaillée
│
└── nlp_demo.py           # Scripts de démonstration
    ├── demo_nlp_features() # Démo des fonctionnalités NLP
    └── demo_chatbot_nlp()  # Démo du chatbot avec NLP
```

### Classe NLPProcessor

La classe `NLPProcessor` dans `nlp_utils.py` encapsule toutes les fonctionnalités NLP :

```python
class NLPProcessor:
    def __init__(self):
        # Initialise NLTK, spaCy et transformers
        
    # NLTK methods
    def tokenize(self, text) -> list
    def remove_stopwords(self, tokens) -> list
    def lemmatize(self, tokens) -> list
    def preprocess_text(self, text) -> list
    def get_pos_tags(self, text) -> list
    
    # spaCy methods
    def extract_entities(self, text) -> list
    def compute_similarity(self, text1, text2) -> float
    
    # Transformers methods
    def analyze_sentiment(self, text) -> dict
    def generate_text(self, prompt, max_length, num_return_sequences, temperature) -> list
```

### Intégration dans le chatbot

Le chatbot (`bot.py`) intègre NLP de manière optionnelle :

1. **Initialisation** : `ChatBot(use_nlp=True)` active les fonctionnalités NLP
2. **Recherche d'intention améliorée** : Utilise la lemmatisation et la similarité sémantique
3. **Analyse contextuelle** : Extrait le sentiment et les entités pour mieux comprendre l'utilisateur

## 📊 Démonstrations

### 1. Démonstration des fonctionnalités NLP

```bash
python nlp_demo.py
```

Cette commande affiche des exemples détaillés de toutes les fonctionnalités NLP sur plusieurs textes d'exemple.

### 2. Démonstration du chatbot avec NLP

```bash
python nlp_demo.py --chatbot
```

Cette commande teste le chatbot avec plusieurs messages et affiche l'analyse NLP pour chacun.

### 3. Démonstration de la génération de texte GPT

```bash
python nlp_demo.py --gpt
```

Cette commande démontre la génération de texte avec GPT-2 sur plusieurs prompts.

### 4. Démonstration du chatbot avec GPT

```bash
python nlp_demo.py --chatbot-gpt
```

Cette commande teste le chatbot en mode génération GPT pour des réponses plus naturelles.

## 🎯 Cas d'usage

### 1. Recherche d'intention améliorée

**Avant (pattern matching simple)** :
- "bonjour" → match
- "coucou" → match
- "hey" → match

**Après (avec NLP)** :
- "bonjour" → match exact
- "salutations" → match par lemmatisation (salutation → salut)
- "good morning" → match par similarité sémantique (si similarity > 0.7)

### 2. Extraction d'informations

```python
user_input = "I live in Paris and work at Google"
entities = nlp.extract_entities(user_input)
# Résultat: [('Paris', 'GPE'), ('Google', 'ORG')]

# Le chatbot peut utiliser ces informations pour personnaliser la réponse
```

### 3. Analyse de sentiment pour adapter les réponses

```python
user_input = "I'm very disappointed with this service"
sentiment = nlp.analyze_sentiment(user_input)
# Résultat: {'label': 'NEGATIVE', 'score': 0.98}

# Le chatbot peut détecter l'insatisfaction et adapter sa réponse
```

### 4. Génération de texte naturel avec GPT-2

```python
from bot import ChatBot

# Créer un chatbot avec GPT activé
bot = ChatBot(use_gpt=True)

# Générer une réponse avec GPT
response = bot.get_response("Tell me about AI", use_generation=True)
# Le chatbot utilise GPT-2 pour générer une réponse naturelle
```

## 🔍 Gestion des erreurs

Le code inclut une gestion robuste des erreurs :

1. **Dépendances manquantes** : Si les bibliothèques NLP ne sont pas installées, le chatbot fonctionne en mode basique avec un avertissement.

2. **Modèles manquants** : Si le modèle spaCy n'est pas téléchargé, les fonctionnalités spaCy sont désactivées mais le reste fonctionne.

3. **Fallback gracieux** : Toutes les méthodes ont des valeurs de retour par défaut en cas d'erreur.

## 📈 Performance

### Temps de démarrage

- **Mode basique** : < 1 seconde
- **Mode NLP** : 3-5 secondes (chargement des modèles)

### Temps de réponse

- **Mode basique** : < 10ms
- **Mode NLP** : 50-200ms (selon les fonctionnalités utilisées)

### Mémoire

- **Mode basique** : ~20 MB
- **Mode NLP** : ~500 MB (modèles chargés en mémoire)

## 🛠️ Développement futur

### Améliorations possibles

1. **Support multilingue**
   - Modèles spaCy français (`fr_core_news_sm`)
   - Détection automatique de langue

2. **Amélioration de la génération de texte**
   - Utilisation de modèles GPT plus grands (GPT-2 Medium, Large)
   - Intégration de GPT-3 ou modèles similaires via API
   - Fine-tuning sur des données de conversation spécifiques
   - Ajout de mémoire conversationnelle pour plus de cohérence

3. **Apprentissage en ligne**
   - Sauvegarde des conversations
   - Amélioration automatique des réponses

4. **Classification d'intentions par ML**
   - Entraînement d'un classifieur custom
   - Meilleure compréhension des intentions complexes

## 📝 Licence et crédits

Ce projet utilise :
- **NLTK** : Apache License 2.0
- **spaCy** : MIT License
- **Transformers** : Apache License 2.0
- **PyTorch** : BSD License

## 🤝 Contribution

Pour ajouter de nouvelles fonctionnalités NLP :

1. Ajoutez les méthodes dans `nlp_utils.py`
2. Intégrez-les dans `bot.py` si nécessaire
3. Créez des tests dans `test_nlp_integration.py`
4. Mettez à jour la documentation

## 📞 Support

Pour des questions ou des problèmes :
- Consultez les issues GitHub
- Vérifiez que toutes les dépendances sont installées
- Vérifiez les versions des bibliothèques

## 🎓 Ressources d'apprentissage

- [NLTK Book](https://www.nltk.org/book/)
- [spaCy Documentation](https://spacy.io/usage)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/)
