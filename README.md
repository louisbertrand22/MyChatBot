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

## 🏗️ Structure du projet

```
MyChatBot/
│
├── main.py           # Point d'entrée du programme
├── bot.py            # Logique du chatbot (réponses, gestion du dialogue)
├── data/
│   └── faq.json      # Fichier de questions/réponses
├── requirements.txt  # Dépendances Python
└── README.md         # Documentation du projet
```

## 🚀 Installation

### Prérequis

- Python 3.6 ou supérieur

### Étapes

1. Clonez le dépôt :
```bash
git clone https://github.com/louisbertrand22/MyChatBot.git
cd MyChatBot
```

2. (Optionnel) Créez un environnement virtuel :
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

3. Installez les dépendances (aucune dépendance externe n'est requise pour cette version) :
```bash
pip install -r requirements.txt
```

## 💻 Utilisation

### Démarrer le chatbot

```bash
python main.py
```

ou directement :

```bash
python bot.py
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

## 🔮 Améliorations futures

- [ ] Ajouter un modèle d'apprentissage automatique (NLTK, spaCy)
- [ ] Créer une interface web avec Flask ou Streamlit
- [ ] Implémenter un système de contexte pour les conversations
- [ ] Ajouter le traitement du langage naturel (NLP)
- [ ] Sauvegarder l'historique des conversations
- [ ] Support multilingue amélioré

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou un pull request.

## 📝 Licence

Ce projet est libre d'utilisation pour l'apprentissage et l'éducation.

## 👨‍💻 Auteur

Louis Bertrand