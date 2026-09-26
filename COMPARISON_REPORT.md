# Rapport comparatif des variantes locales

## Méthode

Mesure effectuée sur `index.html` (A) et `experimental.html` (B), sans exécuter JavaScript. Le **compte de mots** porte sur tout le texte visible du `<body>`, titres et libellés de boutons compris. Un mot est une suite alphanumérique Unicode pouvant contenir une apostrophe ou un trait d'union interne.

Les **comptes d'expressions** sont insensibles à la casse et exacts, sans lemmatisation. Les colonnes sont exclusives :

- **Title** : contenu de `<title>` ;
- **Description** : contenu de la meta description ;
- **H1** : contenu du `<h1>` ;
- **H2/H3** : contenu des titres de sections et sous-sections ;
- **Corps** : texte visible du `<body>` hors H1/H2/H3 ;
- **Alt** : attributs `alt` (il n'y en a pas, les visuels CSS étant décrits par `aria-label`).

Une expression longue peut contenir une expression courte : par exemple, « abonnement IPTV France » compte aussi comme une occurrence exacte de la sous-chaîne « abonnement IPTV ». C'est une propriété déclarée de la mesure, pas un objectif éditorial.

## Résultats mesurés

| Variante | Mots visibles dans le body |
|---|---:|
| A — référence | 651 |
| B — expérimentale | 698 |

### Variante A — référence

| Expression | Title | Description | H1 | H2/H3 | Corps hors titres | Alt |
|---|---:|---:|---:|---:|---:|---:|
| Smart IPTV | 1 | 0 | 1 | 1 | 0 | 0 |
| abonnement IPTV | 1 | 1 | 1 | 6 | 3 | 0 |
| abonnement IPTV France | 1 | 0 | 1 | 0 | 1 | 0 |
| IPTV premium | 0 | 1 | 0 | 2 | 2 | 0 |
| abonnement IPTV Smart TV | 0 | 0 | 0 | 1 | 1 | 0 |
| IPTV multi-écrans | 0 | 1 | 0 | 1 | 2 | 0 |

### Variante B — expérimentale

| Expression | Title | Description | H1 | H2/H3 | Corps hors titres | Alt |
|---|---:|---:|---:|---:|---:|---:|
| Smart IPTV | 1 | 0 | 1 | 2 | 1 | 0 |
| abonnement IPTV | 1 | 1 | 1 | 5 | 2 | 0 |
| abonnement IPTV France | 1 | 1 | 1 | 2 | 0 | 0 |
| IPTV premium | 0 | 1 | 0 | 1 | 3 | 0 |
| abonnement IPTV Smart TV | 0 | 0 | 0 | 1 | 1 | 0 |
| IPTV multi-écrans | 0 | 1 | 0 | 1 | 2 | 0 |

## Différences HTML observées

- B contient 47 mots visibles de plus que A, principalement à cause de sa section d'assistance et de dépannage.
- A place « abonnement IPTV » six fois dans H2/H3 ; B le place cinq fois et consacre davantage de titres au fonctionnement pratique.
- B place « abonnement IPTV France » dans les six zones textuelles pertinentes sauf le corps hors titres et l'alt : title, description, H1 et H2/H3. A ne l'utilise pas dans la description ni dans H2/H3.
- Les deux variantes gardent les attributs alt à zéro. Leurs deux descriptions de visuel sont des `aria-label` courts et utiles, non des emplacements de mots-clés.
- A suit la séquence de sections décrite pour la référence. B insère des faits France/EUR plus tôt et une section pratique autonome avant la FAQ.

## Hypothèses non testées

- **Hypothèse A :** une répétition plus forte dans H2/H3 pourrait clarifier immédiatement la catégorie commerciale, mais pourrait aussi rendre la lecture plus mécanique.
- **Hypothèse B :** le ciblage France/EUR et les réponses de dépannage pourraient améliorer la compréhension et la confiance avant décision.
- **Non démontré :** aucune variante n'a été indexée, exposée à des utilisateurs, mesurée dans Search Console/Semrush, ni soumise à un test de clic ou de conversion. Le rapport ne permet donc aucune conclusion sur la performance de recherche.

## Script de reproduction

```bash
python3 tools/analyze_variants.py
```

Le script produit les comptes de mots et la matrice des six expressions pour chaque fichier. Après toute modification éditoriale, ses résultats doivent être comparés aux tableaux ci-dessus.
