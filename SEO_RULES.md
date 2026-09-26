# Règles SEO de la maquette de recherche

## Périmètre et source

Cette livraison est une **maquette locale de recherche**, non une reproduction ni un site officiel. Les fichiers de référence annoncés (`smartiptvtv.html`, `iptvcanada.html` et `omniptv.html`) ne sont pas présents dans le dépôt. Il n'a donc pas été possible d'inspecter leur HTML. Les règles ci-dessous reposent uniquement sur les observations et le vocabulaire fournis dans le brief. Aucun texte, prix ou fait commercial externe n'a été inventé ou copié.

Les deux pages affichent l'identité de référence SmartIPTVTV afin d'isoler la variable étudiée : la structure du contenu et le placement des expressions. Elles portent une bannière persistante de non-affiliation et la directive `noindex, nofollow`. Elles ne doivent pas être publiées.

## Règles issues de chaque référence

| Référence | Observation fournie | Règle retenue | Variante A | Variante B |
|---|---|---|---|---|
| SmartIPTVTV | Le parcours commercial s'organise autour des formules, du contenu, des appareils et des écrans simultanés, avec des modificateurs sémantiques propres à chaque section. | Présenter d'abord les durées, puis le contenu, la compatibilité, l'activation et la FAQ. Employer les six expressions dans un contexte qui répond au titre de la section. | Suit au plus près cet ordre et place davantage d'occurrences dans les titres de cartes et la FAQ. | Conserve le parcours de décision, mais regroupe appareils et multi-écrans pour dégager de la place aux questions pratiques. |
| IPTVV Canada | Le titre, le H1 et l'introduction alignent produit et territoire ; devise, disponibilité et assistance rendent le ciblage géographique concret. | Remplacer le Canada par la France, afficher EUR, et signaler les faits locaux qui restent à confirmer. | Mentionne France et EUR dans le hero et le bandeau de contexte. | Renforce le ciblage dans le title, la description, le H1, la bande de faits et le titre de l'offre annuelle. |
| OmniIPTV | Le fonctionnement, l'installation, le débit et le dépannage font l'objet de réponses pratiques regroupées. Les guides ne sont liés que s'ils existent. | Donner des étapes utilisables et des limites honnêtes, sans créer de faux guides. | Activation en quatre étapes et réponses pratiques concentrées dans la FAQ. | Ajoute une section dédiée au débit, à l'assistance et au dépannage avant une FAQ plus développée. |

## Application technique commune

- Un seul `<h1>` par page ; les sections principales utilisent des `<h2>` et les offres/sous-thèmes des `<h3>`.
- Les informations essentielles restent dans le HTML et les FAQ utilisent des éléments natifs `<details>`/`<summary>`.
- La bannière « Maquette de recherche indépendante — non affiliée à SmartIPTVTV. » reste visible au défilement.
- Les pages déclarent `lang="fr-FR"` et `<meta name="robots" content="noindex, nofollow">`.
- Il n'y a ni canonical, ni Open Graph pointant vers un domaine, ni JSON-LD : le prototype ne se présente pas comme l'entreprise officielle.
- Tous les boutons d'achat, de connexion et de contact sont des boutons locaux `type="button"`. Le JavaScript affiche seulement un message ; aucun formulaire, réseau, stockage ou paiement n'est utilisé.
- Les liens relient uniquement les deux variantes et les documents locaux, ou mènent vers des ancres présentes.
- Les données commerciales non établies sont marquées `[À CONFIRMER]`, `[PRIX]` ou explicitement décrites comme données de référence.
- Les illustrations sont construites en CSS. Leur `role="img"` possède une description courte ; aucun texte promotionnel ni liste d'expressions n'est placé dans un attribut `alt`.

## Différences intentionnelles

### Variante A — référence (`index.html`)

La page reproduit **la structure décrite** pour SmartIPTVTV : hero commercial, formules, comparaison, contenu de l'abonnement, compatibilité et multi-écrans, activation, FAQ, CTA. Elle emploie plus souvent « abonnement IPTV » dans les H2/H3 afin de créer une base de comparaison fidèle au placement demandé.

### Variante B — expérimentale (`experimental.html`)

La page garde la même identité et le même système visuel, mais rend la France, l'euro et les limites commerciales plus visibles. Elle ajoute avant la FAQ une section pratique sur le débit, l'activation, l'application et le dépannage. Le vocabulaire est légèrement moins concentré dans les titres afin de tester une lecture plus naturelle.

## Pratiques rejetées

- Pas de densité cible : les comptes mesurent la livraison ; ils ne prescrivent pas une fréquence.
- Pas de liste artificielle de villes françaises, de titre répété ou de paragraphe de remplissage.
- Pas d'avis, note, nombre de clients, nombre de chaînes, licence, prix, remise, garantie ou disponibilité inventés.
- Pas de lien d'achat, connexion ou contact qui envoie des données.
- Pas de page guide vide, de faux lien juridique ou d'ancre sans destination.
- Pas de Product, Offer, Review, AggregateRating, FAQPage ou Organization JSON-LD.
- Pas de promesse de classement, d'extrait enrichi ou de performance de recherche.

## Mesure et hypothèses

Les différences de structure, les comptes de mots et les occurrences consignés dans `COMPARISON_REPORT.md` sont des **mesures reproductibles du HTML local**. En revanche, toute conclusion sur le clic, la compréhension, la conversion, l'indexation ou le classement est une **hypothèse non testée**. Une expérience valide demanderait notamment un protocole, une audience comparable, des variantes publiables avec autorisation, des données analytiques conformes et un contrôle des autres variables.

## Vérifications nécessaires avant toute utilisation ultérieure

- Obtenir et auditer les trois vrais fichiers de référence ; relever leurs titres, sections et informations commerciales sans supposer leur actualité.
- Faire confirmer par le titulaire de la marque toute utilisation de l'identité SmartIPTVTV. À défaut, conserver strictement cette étude hors ligne.
- Vérifier légalité, droits de contenus, zone desservie, devise, TVA, prix, moyens de paiement, applications et appareils.
- Confirmer connexions simultanées, restrictions de foyer, débits par résolution, activation, renouvellement, essai, annulation et remboursement.
- Confirmer canaux, langues, horaires et délais d'assistance, puis tester réellement les étapes de dépannage.
- Si un site distinct est un jour autorisé, remplacer l'identité, ajouter ses coordonnées et politiques réelles, puis seulement préparer canonical, Open Graph et éventuel balisage structuré fondé sur des faits visibles.
- Tester le rendu et l'accessibilité au clavier, au lecteur d'écran et sur des navigateurs/téléphones réels.

## Principe SEO final

“Clear product-and-market targeting, useful buying information, relevant practical answers, natural keyword usage and accurate technical markup.”
