# Dragon Adventure Game

## Overview
In this adventure game, you find yourself in a mystical land with various paths to choose from. Each decision you make will lead you to different encounters and ultimately determine your fate.

## Storyline

### Introduction
Welcome to the Dragon Adventure Game! You find yourself in a mystical forest. Legend has it that a dragon lives nearby, guarding a hidden treasure. There are two paths ahead: one leading deeper into the forest and another towards the mountains.

- Do you want to go to the **forest** or the **mountains**? (forest/mountains)

### Forest Path
You walk deeper into the forest, the trees becoming denser. Suddenly, you come across a small, hidden clearing with a glimmering pond. Near the pond, you see a wise old owl perched on a tree.

- Do you want to **talk** to the owl or **continue** walking? (talk/continue)

#### Talk to the Owl
The owl tells you about a secret path that leads to the dragon's cave but warns of dangers along the way. 

- Do you want to **follow** the secret path or **ignore** the owl's advice? (follow/ignore)

**Follow the Secret Path**
You follow the owl's instructions and find the secret path. After a while, you reach the dragon's cave. The dragon is friendly and offers to share its treasure if you answer a riddle.

- Do you want to **answer** the riddle or **refuse** the offer? (answer/refuse)

**Answer the Riddle**
The dragon asks, "What has keys but can't open locks?" You answer correctly, "A piano!" The dragon is impressed and shares its treasure with you. **You win!**

**Refuse the Offer**
You refuse to answer the riddle. The dragon is disappointed and sends you away. **Game over.**

**Ignore the Owl's Advice**
You continue walking and get lost in the dense forest. Eventually, you find your way out but miss the chance to find the dragon. **Game over.**

#### Continue Walking
You continue walking and suddenly fall into a hidden trap. You are unable to escape. **Game over.**

### Mountains Path
You head towards the mountains, the terrain becoming rocky. You see a cave entrance guarded by a fierce-looking dragon.

- Do you want to **approach** the dragon or **find another way**? (approach/find)

#### Approach the Dragon
The dragon asks, "Why are you here?" 

- Do you want to **explain** your quest for treasure or **fight** the dragon? (explain/fight)

**Explain Your Quest**
The dragon is intrigued by your bravery and decides to help you find the treasure. It guides you to a hidden chamber filled with gold and jewels. **You win!**

**Fight the Dragon**
You decide to fight the dragon, but it's too powerful. You are defeated. **Game over.**

#### Find Another Way
You search for another way into the mountains and find a narrow path leading to a hidden cave. Inside, you discover the dragon's treasure, unguarded. **You win!**

## Game Flow Diagram
```plaintext
Start
  |
  |---> Forest or Mountains? (forest/mountains)
  |      |
  |      |---> Forest Path
  |      |      |
  |      |      |---> Talk or Continue? (talk/continue)
  |      |             |
  |      |             |---> Talk to the Owl
  |      |             |      |
  |      |             |      |---> Follow or Ignore? (follow/ignore)
  |      |             |             |
  |      |             |             |---> Follow the Secret Path
  |      |             |             |      |
  |      |             |             |      |---> Answer or Refuse? (answer/refuse)
  |      |             |             |             |
  |      |             |             |             |---> Answer the Riddle (You win!)
  |      |             |             |             |
  |      |             |             |             |---> Refuse the Offer (Game over)
  |      |             |             |
  |      |             |             |---> Ignore the Owl's Advice (Game over)
  |      |             |
  |      |             |---> Continue Walking (Game over)
  |      |
  |      |---> Mountains Path
  |             |
  |             |---> Approach or Find Another Way? (approach/find)
  |                    |
  |                    |---> Approach the Dragon
  |                    |      |
  |                    |      |---> Explain or Fight? (explain/fight)
  |                    |             |
  |                    |             |---> Explain Your Quest (You win!)
  |                    |             |
  |                    |             |---> Fight the Dragon (Game over)
  |                    |
  |                    |---> Find Another Way (You win!)
  |
End
