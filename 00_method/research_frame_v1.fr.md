---
title: Cadre de recherche et normes de preuve
subtitle: Comment cette enquête est structurée, ce qui compte comme preuve, et le piège méthodologique inscrit dans sa propre prémisse
author: Robin
date: 2026-11-25
version: v1
status: actif — régit tous les autres documents de cette archive
source_files: aucun (document de méthode)
---

# La question de recherche

Sur toute la pile de la physique des particules à haute énergie — motivation théorique,
matériel des machines, instrumentation des détecteurs, logiciels de simulation et
d'analyse, publication, gouvernance du financement — où sont les faiblesses, et sont-elles
reconnues ?

L'enquête opère à cinq niveaux, chacun doté de son propre dossier :

1. **Théorie** — les notions qui motivent les machines sont-elles falsifiables, et
   qu'advient-il d'un argument motivant lorsque sa prédiction échoue ?
2. **Matériel** — ce que les instruments ne peuvent physiquement pas voir, et qui les
   construit.
3. **Logiciel** — quelles hypothèses théoriques sont encodées dans le code qui convertit
   les signaux du détecteur en affirmations physiques.
4. **Publication** — la littérature est-elle structurellement capable de se vérifier
   elle-même.
5. **Gouvernance** — qui décide de ce qui se construit, et quel est son intérêt.

# Le piège inscrit dans la prémisse de ce projet

Le mandat est « d'exposer les faiblesses ». Cette formulation préengage la conclusion, ce
qui est précisément la défaillance méthodologique que l'enquête entend documenter chez les
autres. Une critique bâtie sur un raisonnement motivé peut être écartée exactement sur le
terrain qu'elle avance.

Deux conséquences en découlent, et elles lient chaque document de cette archive :

**Le niveau D est obligatoire.** Chaque document de recherche doit se clore sur les
affirmations qui ont été examinées et qui n'ont *pas* pu être étayées. Un document sans
section de niveau D est incomplet, non pas plus fort. La présence d'affirmations rejetées
est ce qui distingue le travail d'enquête du plaidoyer militant, et c'est la seule chose
qui rende coûteux le rejet des affirmations survivantes.

**Les explications ordinaires priment sur les explications motivées.** La contrainte
budgétaire, l'inertie institutionnelle, la dépendance au sentier et le conservatisme
technique expliquent la plus grande part de ce qui ressemble à de la suppression. Une
explication faisant intervenir l'intérêt ou la captation doit l'emporter sur l'explication
ordinaire par la preuve, non par l'attrait du récit.

# Une correction terminologique

« Biais dans les algorithmes » importe un sens issu de l'éthique de l'apprentissage
automatique — le biais social dans les données d'entraînement — qui ne décrit pas ce qui se
produit ici et induirait en erreur un lecteur technique.

Le phénomène réel est le **présupposé théorique encodé dans l'instrumentation et dans le
code** : les hypothèses d'un modèle sont intégrées à l'appareil et au logiciel qui servent
ensuite à éprouver ce modèle. C'est une affirmation plus nette, plus défendable et plus
grave que « biais ». L'archive emploie partout la formulation précise. Là où un véritable
biais de sélection ou de représentation existe, il est nommé comme tel et distingué.

# Niveaux de preuve

Chaque affirmation substantielle, dans chaque document, porte une étiquette de niveau.

| Niveau | Signification | Norme de preuve |
|---|---|---|
| **A** | Documenté et reconnu à l'intérieur du domaine | Littérature primaire, rapports techniques de collaboration, documents officiels de laboratoire ou d'agence, dossiers de marchés publics ou de justice |
| **B** | Contesté à l'intérieur du domaine, avec des tenants nommés de part et d'autre | Les deux positions citées d'après leurs propres auteurs, non d'après des caractérisations |
| **C** | Inférence structurelle — découle de faits de niveau A mais n'a pas été assemblée ni éprouvée par le domaine | Doit énoncer les faits de niveau A sur lesquels elle repose et ce qui la falsifierait. Jamais présentée comme un constat. |
| **D** | Examiné et rejeté | Consigné avec la raison de son échec, pour qu'il ne soit pas réexaminé |

Le niveau C est là où réside la contribution originale de ce projet, et c'est aussi le
niveau le plus dangereux. Une affirmation de niveau C présentée comme établie transforme
l'archive entière en polémique. Les affirmations de niveau C doivent être rédigées de telle
sorte qu'un spécialiste hostile dise « cette inférence est disponible à partir de ces
faits », et non « cela n'est pas étayé ».

# Exigence de falsifiabilité

Chaque niveau d'analyse doit énoncer ce qui montrerait que sa critique est fausse :

- **La critique théorique** échoue si les arguments motivants ont effectivement été
  abandonnés ouvertement et au grand jour lorsque leurs prédictions ont échoué, et si cet
  abandon se reflète dans les demandes de financement ultérieures.
- **La critique du matériel** échoue si les angles morts instrumentaux sont publiés,
  quantifiés et intégrés aux affirmations de découverte.
- **La critique du logiciel** échoue si les incertitudes liées au choix de générateur et à
  la dépendance à la simulation sont propagées avec un traitement correct des corrélations
  entre expériences.
- **La critique de la publication** échoue s'il existe un mécanisme opérant par lequel un
  spécialiste extérieur peut vérifier un résultat signé par plusieurs milliers d'auteurs et
  imposer une correction.
- **La critique de la gouvernance** échoue si les instances stratégiques comportent des
  membres sans intérêt prospectif, et si leurs recommandations sont historiquement allées à
  l'encontre de l'intérêt de leur propre composition.

Ce sont de véritables épreuves. Certaines peuvent être réussies. Le consigner est le
travail.

# Limites du périmètre

Dans le périmètre : les accélérateurs terrestres et leurs détecteurs ; la pile logicielle
qui convertit les signaux en affirmations ; les systèmes de publication et de financement
qui les entourent ; les instruments d'accélération astrophysique là où les mêmes questions
reparaissent.

Hors périmètre, et explicitement : toute affirmation selon laquelle les résultats
expérimentaux seraient fabriqués, selon laquelle les prédictions confirmées du Modèle
standard seraient invalides, ou selon laquelle la physique des détecteurs serait truquée.
Ce ne sont pas des versions faibles de l'argument ; c'est un argument différent et
indéfendable, et l'inclure discréditerait par association le matériel défendable. Le Modèle
standard est la théorie la plus précisément éprouvée de l'histoire de la physique. La
critique menée ici porte sur ce qui *entoure* ce noyau : motivation, limites
instrumentales, hypothèses encodées, reddition de comptes et intérêt.

## Une exception permanente à la règle du niveau D

`10_financial_investigation/` est un **document de phase de collecte** et ne comporte
délibérément aucune section « Affirmations examinées et non étayées ». Il a été commandé
sur la consigne explicite que la collecte et l'évaluation soient séparées, et que rien de
ce qui est rencontré ne soit écarté — y compris les affirmations issues de sources faibles
ou anonymes, qui sont consignées avec leur provenance plutôt que filtrées.

À la place du niveau D, il se clôt sur une liste énumérée de ce qui n'a pu être établi,
chaque élément nommant le document qui y répondrait. Chaque entrée porte une classe de
source (audit, justice, officiel, presse, plaidoyer, anonyme) et un statut (vérifié,
rapporté, allégué, invérifiable), de sorte que la phase d'évaluation dispose de ce qu'il
lui faut.

C'est une exception au cadre, non un manquement. Une révision ultérieure ne doit pas la
« corriger » en ajoutant une section de rejet : l'évaluation appartient à un document
distinct, établi face au matériel collecté.
