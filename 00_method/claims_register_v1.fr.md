---
title: Registre des affirmations
subtitle: Chaque affirmation substantielle de l'archive, avec son niveau de preuve, son document source et son statut
author: Robin
date: 2026-11-25
version: v1
status: actif — sept candidates résolues ; C1a affaiblie par l'audit probatoire
source_files: 00_method/research_frame_v1.md ; 08_evidential_audit/proof_failure_modes_v1.md
---

# Objet

Un registre unique de ce que cette archive affirme réellement. Chaque affirmation porte un
identifiant, un niveau de preuve, le document qui l'étaye et un statut. Rien ne peut être
repris dans une synthèse publiée sans figurer ici avec le statut ÉTAYÉE ou ÉTAYÉE COMME
INFÉRENCE.

Valeurs de statut : `NON ÉPROUVÉE` · `ÉTAYÉE` · `ÉTAYÉE COMME INFÉRENCE` · `AFFAIBLIE` ·
`REJETÉE`

# Résultat

Sept affirmations candidates avaient été rédigées avant le début de la recherche. Sur ces
sept, **trois ont été rejetées telles qu'énoncées** (C1, C2, C4), **une a été scindée, sa
moitié étant rejetée** (C6), et **trois ont survécu sous une forme resserrée ou reformulée**
(C3, C5, C7). Six affirmations de remplacement, plus étroites, ont été rédigées à partir de
ce que la preuve étayait réellement.

Pas une seule des sept n'a survécu dans sa formulation d'origine. Les deux que le projet
tenait pour les plus solides au départ — C1 et C2 — figurent parmi les rejetées.

# Registre

| ID | Affirmation | Niveau | Document | Statut |
|---|---|---|---|---|
| C1 | ~~ATLAS et CMS sont présentés comme une confirmation mutuellement indépendante alors qu'ils partagent outils de simulation, générateurs et méthodologie ; leurs erreurs systématiques sont donc corrélées et leur accord vaut moins que ce qui est présenté~~ | C | 04_software_algorithmic | **REJETÉE** — voir C1a, C1b |
| C1a | Le coefficient de corrélation appliqué aux termes de modélisation partagés paraît calibré sur la différence de procédure entre collaborations plutôt que sur l'ascendance commune des modèles, où la vraie valeur pour l'hadronisation serait plausiblement plus près de 1 que de 0,5 | C | 04_software_algorithmic | **AFFAIBLIE** — voir C1a′ |
| C1a′ | La valeur de corrélation est un choix documenté reposant sur des motifs procéduraux et non généalogiques — confirmé mot pour mot dans les articles — mais là où elle a été balayée, la conséquence numérique est faible ; aucun balayage n'a été publié pour la signification de la découverte de 2012 | A | 08_evidential_audit | ÉTAYÉE |
| C1b | L'hadronisation nominale des deux expériences descend d'un seul ajustement manuel ; CMS en fixe les paramètres et ATLAS en ajuste dix autres par-dessus | A | 04_software_algorithmic | ÉTAYÉE |
| C2 | ~~Le déclenchement de niveau 1 encode un présupposé théorique au point de destruction irréversible des données, rendant une partie de la physique inobservable en principe et non simplement non mesurée~~ | C | 03_hardware_systems | **REJETÉE** — voir C2a, C2b |
| C2a | Les menus de déclenchement sont construits à partir d'attentes théoriques et les événements écartés sont irrécupérables ; l'erreur de déclenchement est donc structurellement asymétrique : les faux positifs coûtent une bande passante mesurée et budgétée, les faux négatifs coûtent des événements irrécupérables et ne sont jamais intégrés sur l'espace des signatures | C | 03_hardware_systems | ÉTAYÉE COMME INFÉRENCE |
| C2b | La conception du déclenchement a démontrablement empêché certaines mesures, et non simplement retardées | A | 03_hardware_systems | ÉTAYÉE |
| C3 | Des générateurs ajustés sur les données servent à calculer les corrections d'acceptance par lesquelles les nouvelles données sont interprétées, et le domaine nomme le risque qui en découle dans sa propre documentation | C | 04_software_algorithmic | ÉTAYÉE COMME INFÉRENCE (resserrée) |
| C4 | ~~L'hyper-cosignature jointe à l'évaluation interne préalable rend l'évaluation par les pairs extérieure structurellement incapable de vérifier un résultat~~ | C | 05_publication_governance | **REJETÉE** — mécanisme erroné ; voir C4a |
| C4a | La vérification extérieure d'un résultat du LHC est irréalisable parce que les éléments qu'elle exigerait sont en grande partie non publiés, et non à cause du nombre d'auteurs ou de la qualité de l'évaluation interne | A | 05_publication_governance | ÉTAYÉE |
| C5 | Un régime de conflits d'intérêts existe mais sa portée est étroite, et les chiffres de coûts figurant dans les documents justifiant les machines sont fournis par les promoteurs à une instance privée du droit de produire les siens | A | 05_publication_governance | ÉTAYÉE (resserrée) |
| C6a | La concentration des fournisseurs sur des composants spécialisés crée des points de défaillance uniques documentés | A | 03_hardware_systems | ÉTAYÉE |
| C6b | ~~Les règles d'équilibre des marchés publics font que certains choix techniques découlent d'une répartition politique plutôt que du mérite technique~~ | C | 03_hardware_systems | **REJETÉE** |
| C7 | Le retrait de la naturalité est explicite dans la littérature théorique et se reflète inégalement dans les documents justifiant les machines — paraphrasé sans son vocabulaire dans l'un, rétabli dans l'autre | B | 02_theory_critique | ÉTAYÉE COMME INFÉRENCE (reformulée) |

# Notes de résolution

## C1 — rejetée, et l'affirmation plus étroite qui l'a remplacée

L'affirmation d'origine soutenait que les combinaisons présentent ATLAS et CMS comme
indépendants tout en ignorant l'erreur systématique corrélée par le logiciel partagé. C'est
faux, et documenté en sens contraire [A]. La combinaison de la masse du quark top attribue
une corrélation de 0,5 aux termes d'élément de matrice, de rayonnement QCD, d'hadronisation,
de reconnexion de couleur et d'événement sous-jacent, et de 0,85 aux PDF et à l'empilement,
et publie un balayage par catégorie montrant des déplacements de modélisation de quelques
MeV face à un total de 0,33 GeV.

Ce qui survit est C1a′, qui porte sur les *motifs* plutôt que sur une négligence : le
coefficient paraît calibré sur la différence de travail entre les deux collaborations, non
sur l'ascendance de modèle qu'elles partagent. Pour la masse du top, la distinction est
numériquement sans effet, la réponse étant linéaire. Qu'elle importe ailleurs n'a pas été
éprouvé, aucune étude publiée ne balayant conjointement la corrélation et la variance de
modèle.

## C2 — rejetée, et pourquoi cela compte

L'affirmation d'origine soutenait qu'une partie de la physique est **inobservable en
principe**. C'est faux [A] : les flux à biais nul, à biais enrichi et d'empilement ne sont
pas sélectionnés sur des signatures physiques et donnent un préfacteur de réduction effectif
voisin de 40 000 — un échantillon non biaisé de l'ordre de 0,5 à 1 fb⁻¹. La physique hors
menu est *mal échantillonnée*, non inobservable.

Trois arguments de soutien ont également échoué : que la bande passante soit une limite
physique dure (LHCb et ALICE ont renoncé au déclenchement matériel, c'est donc un choix
d'ingénierie) ; que les détecteurs astrophysiques partagent le problème (IceCube archive
toutes les formes d'onde brutes) ; et que le domaine n'en ait pas conscience (il en a
conscience, par écrit).

C2a est falsifiable par une seule intégrale de couverture sur l'espace des signatures, avec
une mesure énoncée. Une telle intégrale ne semble pas exister.

## C3 — étayée, resserrée

La circularité est réelle et le domaine la nomme. La documentation d'ajustement d'ATLAS
avertit elle-même qu'un ajustement excessif des paramètres non perturbatifs peut masquer une
nouvelle physique [A]. En déconvolution itérative, les valeurs de départ sont la vérité de
la simulation elle-même, et le domaine énonce clairement que cette dépendance *constitue* la
régularisation [A]. L'écart entre deux générateurs, employé pour estimer l'incertitude de
modèle, est documenté comme ne bornant pas l'écart à un troisième [A].

Deux versions plus fortes ont été rejetées : que les ajustements soient calés sur les
signaux qu'ils corrigent, et que les spectres déconvolués soient des artefacts dictés par
l'a priori. L'estimation du bruit de fond à partir des données et la validation en régions
de contrôle existent précisément pour réduire la dépendance à la simulation, et elles
fonctionnent.

## C4 — rejetée quant au mécanisme, conclusion reconstruite

L'hyper-cosignature n'est pas ce qui empêche la vérification extérieure. L'évaluation
interne comme simple formalité a été rejetée, et l'épisode OPERA va en sens contraire : une
collaboration de cette taille a publié sa propre anomalie puis sa propre réfutation.

La conclusion survit par une autre voie, mieux documentée [A]. L'inventaire de
réinterprétation du domaine lui-même recense les fonctions de vraisemblance complètes
publiées pour deux analyses, des cartes d'efficacité dans très peu de cas, des données de
réajustement souvent non fournies, et des analyses par apprentissage automatique
irreproductibles hors de la collaboration qui les a produites. En 2025, la reproductibilité
de certaines recherches antérieures était perdue *à l'intérieur* de ces collaborations. Un
tiers ne peut vérifier parce que les éléments n'existent pas publiquement, non parce que
trois mille personnes ont signé l'article.

## C5 — étayée, resserrée

Deux versions fortes ont été rejetées : qu'il n'existe aucun régime de conflits d'intérêts
(il en existe un), et qu'aucun membre d'instance ne soit sans intérêt (il existe au moins un
contre-exemple documenté).

Ce qui est documenté [A] : le régime récuse quatre membres sur trente-deux, au motif d'un
emploi en laboratoire national, pour un seul vote d'acceptation ; les trente-deux sont tous
physiciens des particules ou des accélérateurs ; le mandat de la stratégie européenne ne
comporte aucune disposition sur les conflits d'intérêts ; et les chiffres de coûts sont
fournis par les promoteurs, le sous-comité étant privé du droit de produire ses propres
estimations. Le point le plus net est le dernier, et il ne porte sur les motivations de
personne.

## C6 — scindée

C6a tient [A] : un seul fournisseur qualifié de Nb₃Sn aux spécifications du HL-LHC contre
huit pour ITER ; environ 93 % de la production minière mondiale de niobium issue d'un seul
pays, dont 77 à 90 % détenus par une seule firme ; deux entreprises au monde fabriquant des
turbo-détendeurs à hélium de la taille requise ; aucune production américaine de niobium.

C6b ne tient pas. Les États membres reçoivent 94 % des contrats directs mais 77 % de la
valeur ajoutée, et l'Allemagne comme le Royaume-Uni sont documentés comme mal équilibrés,
c'est-à-dire sous-servis. La captation des marchés par les plus gros contributeurs a été
examinée et rejetée.

## C7 — étayée, reformulée

La formulation d'origine affirmait que le retrait ne se reflétait pas dans les
justifications des machines successives. C'est excessif. Le retrait est explicite et consigné
dans la littérature théorique [A] : une borne sous le TeV publiée en 2008 avec une condition
d'échec énoncée, et le même auteur concédant une « ère post-naturalité » en 2017.

Ce qui est inégal, c'est le reflet. Le rapport stratégique américain de 2023 ne contient
aucune occurrence de « naturalité », « problème de hiérarchie », « ajustement fin » ou « non
naturel » sur 379 741 caractères, tout en paraphrasant l'argument que ces mots désignent ;
le cahier européen de 2025 rétablit le terme. Également rejeté : que la naturalité n'ait été
qu'esthétique (son fondement en théorie effective des champs est un argument réel), et que
les critères n'aient été déplacés qu'après les exclusions (la supersymétrie scindée a
abandonné la naturalité en 2004, avant que le LHC ne fonctionne).

## C1a — affaiblie par l'audit probatoire, et reformulée

La première moitié de C1a est confirmée dans les mots mêmes des articles : les catégories de
modélisation partagée reçoivent ρ = 0,5 et la justification donnée est que les expériences
emploient des générateurs et des schémas de variation différents — une différence de
procédure, non d'ascendance [A].

La seconde moitié ne survit pas. Les balayages de sensibilité publiés montrent la valeur
centrale de la masse du top se déplaçant d'au plus 41 MeV sous des hypothèses de corrélation
défavorables, face à une incertitude totale de 0,33 GeV, et la combinaison énonce
explicitement qu'« aucune catégorie n'a été identifiée avec ρ = 1 » [A]. Quels que soient les
motifs, la conséquence numéri­que, là où elle a été éprouvée, est faible.

Ce qui demeure est plus étroit et devient C1a′ : **aucun balayage des hypothèses de
corrélation n'a été publié pour la signification de la découverte de 2012** — la seule
grandeur pour laquelle l'indépendance des deux expériences était porteuse sur le plan
rhétorique. La robustesse démontrée pour une combinaison de précision de 2024 est empruntée,
implicitement, par une affirmation de découverte de 2012. Falsifiable par la production
d'une telle étude.
