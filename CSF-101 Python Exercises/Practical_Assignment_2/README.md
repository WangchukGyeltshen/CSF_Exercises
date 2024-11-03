# Programming the Farming Drone

## Introduction

The Farmer Was Replaced is a coding game where we need to program a robotic drone to take over a farmer’s duties. Our task is to write code that guides the robot as it plants seeds, waters crops, and navigates around obstacles in the field. 
This game is a fun way to practice coding by solving puzzles and automating tasks on a virtual farm. It’s perfect for learning how to break down problems and improve your programming skills in an interactive setting.

## Table of Contents
- [Code Snippets and Explanation](#code-snippets-and-explanation)
- [Challenges and Learnings](#challenges-and-learnings)
- [References](#references)

### Code Snippets and Explanation
### Step One: Farming on one tile
**Code:**

```python
while True:
    if can_harvest():
        harvest()
```

**Explanation:**
When this command is called, the drone will perform the action of collecting all the fully grown crops in its vicinity. This is a fundamental task in managing the farm’s resources.

**Demo:**
![](./Farming1.mp4)

### Step Two: Farming on three tiles
```python
while True:
    plant(Entities.Bush)
    if can_harvest():
        harvest()
        move(North)
    else:
        move(North)
```

**Explaination:**
This code creates a loop where the robot continuously plants bushes, checks if they’re ready to harvest, and moves north. If a bush is ready, the robot harvests it; if not, it just moves north and repeats the process.

**Demo:**
![](./Farming1.mp4)

### Step 4: Farming on  nine tiles
**Code:**
```python
clear()
move(South)

WaterTankCap = 100
HayCap 500
WoodCap 300
CarrotCap 100

while True:
    for i in range(get_world_size()):
        move(North)
        if can_harvest():
            harvest()

            if num_items(Items.Water_Tank) <    WaterTankCap 
                trade(Items.Empty_Tank)

            if get_water() < 0.75: 
                use_item(Items.Water_Tank)

            if num_items(Items.Hay) < HayCap: 
                if get_ground_type() == Grounds.Soil: till()
                    plant(Entities.Grass)

            elif num_items(Items.Wood) < WoodCap: 
                if get_ground_type() == Grounds.Soil: 
                    till()
                plant(Entities.Bush)

            elif num_items(Items.Carrot) < CarrotCap: 
                if num_items(Items.Carrot_Seed) == 0: 
                    trade(Items.Carrot_Seed) 
                if get_ground_type() == Grounds.Turf: 
                    till()
                plant(Entities.Carrots)
    move(East)
```
**Explanation:**
 This code makes the robot manage resources and farm systematically. It moves north, harvesting crops and checking inventory levels. Based on the available stock, it trades or refills water, tills soil and plants grass, bushes, or carrots if below capacity. After each northward run, the robot shifts east to cover the next row. This process repeats continuously.

**Demo:**
![](./Farming1.mp4)

### Step 5: Farming on sixteen tiles
**Code:**
```python
clear()
do_a_flip()
move(South)
Water TankCap 100
HayCap 20000
WoodCap 10000
CarrotCap
5000
Pumpkin Cap 1000
while True:
    for i in range(get_world_size()):
        move(North)
        x = get pos_x()
        y = get pos_y()
        if can_harvest():
            harvest()
            Watering()
            Planting()
        else:
            if get ground type() Grounds.Soil:
                till()
    move(East)
```
**Explanation:**
It clears the field and performs a flip before moving south. Sets capacity limits for various resources: water tank (100), hay (20,000), wood (10,000), carrots (5,000), and pumpkins (1,000). The robot continuously moves north across the field. It checks if crops can be harvested and performs the harvest if ready. If the ground is soil, it tills the soil to prepare for planting and then moves east to the next row. The functions Watering(), and Planting() were defined as shown in the demo video below.

**Demo:**
![](./Farming1.mp4)

### Step 6: Farming on 25 tiles
**Code:**
```Python
clear()
do_a_flip()
move(South)
WaterTankCap 100
HayCap 20000
WoodCap 10000
CarrotCap 5000
Pumpkin Cap 1000
while True:
    for i in range(get_world_size()):
        move(North)
        x = get_pos_x()
        y = get_pos_y()
        if can_harvest():
            harvest()
            Watering()
            Planting()
        else:
            if get_ground_type() Grounds.Soil:
                till()
    move(East)
```
**Explanation:**
The robot clears the field, performs a flip, and moves south. It defines maximum capacities for water tanks (100), hay (20,000), wood (10,000), carrots (5,000), and pumpkins (1,000). The robot continuously moves north across the field. It checks if crops can be harvested. If so, it harvests them, waters the plants, and then plants new ones. If the ground type is soil, it tills the soil to prepare for planting. After moving north, the robot moves east to start working on the next row.
**Demo:**
![](./Farming2.mp4)

### Step 7: Farming on 36 tiles
**Code:**
```python
clear()
do_a_flip()
move(South)
WaterTankCap = 100
HayCap 30000
WoodCap 20000
CarrotCap 10000
Pumpkin Cap 5000
while True:
    for i in range(get_world_size()):
        if num_items(Items.Sunflower_Seed) < 100: 
            trade(Items.Sunflower_Seed, get_world_size() 
        if num_items(Items.Carrot_Seed) < 100: 
            trade(Items.Carrot_Seed, get_world_size()) 
        if num_items(Items.Pumpkin_Seed) < 100: 
            trade(Items.Pumpkin_Seed, get_world_size())
        move(North)
        x=get_pos_x()
        y=get_pos_y()
        if can_harvest():
            harvest()
            Watering()
            Planting()
        else:
            if get_ground_type() Grounds.Soil:
                till()
    move(East)
```
**Explanation:**
It sets maximum capacities for resources like water tanks, hay, wood, carrots, and pumpkins. Within a continuous loop, the robot checks if it has fewer than 100 seeds for sunflowers, carrots, or pumpkins, trading for more if necessary. It then moves north, checks its position, and harvests crops if they are ready, followed by watering and planting new crops. If the ground is soil, the robot tills it for planting. After finishing one row, the robot moves east to start the next row, ensuring efficient management of the farm.
**Demo:**
![](./Farming2.mp4)

# Challenges and Learning
## Challenges
While doing this assignment the most challenging thing was figuring out how to use the different code in a way that was most efficient and harmonic way possible. It was very challenging for me as it required a lot of critical thinking and problem solving which, however, made the results more satisfying.

One thing I have done to make the harvesting faster was implementing checks for resource quantities (eg., seeds, water) and utilized trade functions to maintain stock levels, ensuring the robot has enough supplies for farming tasks.
## Learnings
Used functions to get the robot's position (get_pos_x(), get_pos_y()) to inform decisions and actions based on its current location within the field.

Employed if statements to implement decision-making processes based on current conditions (e.g., whether crops can be harvested or if ground preparation is needed), allowing for responsive farming actions.

Employed while and for loops to create continuous processes and iterate through each tile in the field. For example, using for i in range(get_world_size()) to traverse the entire area.

## References
1. [YouTube Video](https://www.youtube.com/watch?v=gmJ357XAAdE)
2. [WiKi](https://thefarmerwasreplaced.wiki.gg/wiki/Tooltips_Code)
3. [Reddit](https://www.reddit.com/r/WhatsOnSteam/comments/10yxnbkthe_farmer_was_replaced_program_and_optimize_a/)






