# Simulation de Création Système Solaire 2D (Moteur Physique)

Une simulation interactive d'accrétion gravitationnelle codée en Python avec **Pygame**. Ce projet simule une nébuleuse primitive composée de 3 000 particules de poussière en orbite autour d'une étoile massive. Sous l'effet de la gravité, ces poussières entrent en collision et fusionnent progressivement pour donner naissance à des protoplanètes.

## Fonctionnalités
- **Physique Gravitationnelle Réelle** : Calcul des forces d'attraction basé sur la loi universelle de la gravitation de Newton (F = G * (m1 * m2) / d²) appliqué entre toutes les particules en mouvement.
- **Gestion des Collisions & Accrétion** : Lorsque deux corps célestes se touchent, ils fusionnent. Le script applique le principe de la **conservation de la quantité de mouvement** pour calculer la nouvelle vitesse et la trajectoire du corps combiné : m_total * v_final = (m1 * v1) + (m2 * v2).
- **Génération Orbitale Stable** : Calcul automatique de la vitesse orbitale théorique nécessaire pour chaque particule lors de la génération de la nébuleuse, garantissant un mouvement circulaire stable autour du Soleil dès le lancement.

## Code Couleur de la Simulation
L'interface s'appuie sur un dégradé de couleurs dynamique qui reflète la masse et l'évolution des astres en temps réel :
- **Blanc / Jaune éclatant** : L'étoile centrale (Le Soleil).
- **Orange de fusion** : Les grosses planètes en cours de formation active.
- **Bleu néon** : Les protoplanètes et gros embryons d'astéroïdes.
- **Gris de roche spatiale** : Les poussières fines de la nébuleuse primitive.

## Prérequis
Pour faire tourner la simulation sur votre machine, vous devez disposer de Python et de la bibliothèque Pygame.

Installez Pygame facilement via votre terminal :
```bash
pip install pygame```
