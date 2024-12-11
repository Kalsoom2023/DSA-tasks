from poodle import Object, schedule  # Assuming the poodle module is available
from typing import Set

class Position(Object):
    def __str__(self):
        if not hasattr(self, "locname"):
            return "unknown"
        return self.locname

class HasHeight(Object):
    height: int

class HasPosition(Object):
    at: Position

class Monkey(HasHeight, HasPosition):
    pass

class PalmTree(HasHeight, HasPosition):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.height = 2

class Box(HasHeight, HasPosition):
    pass

class Banana(HasHeight, HasPosition):
    owner: Monkey
    attached: PalmTree

class World(Object):
    locations: Set[Position]

# Creating positions
p1 = Position()
p1.locname = "Position A"
p2 = Position()
p2.locname = "Position B"
p3 = Position()
p3.locname = "Position C"

# Creating world and adding positions to locations
w = World()
w.locations.add(p1)
w.locations.add(p2)
w.locations.add(p3)

# Creating monkey, box, palm tree, and banana
m = Monkey()
m.height = 0  # Monkey starts on the ground
m.at = p1

box = Box()
box.height = 2
box.at = p2

p = PalmTree()
p.at = p3

b = Banana()
b.attached = p

# Actions
def go(monkey: Monkey, where: Position):
    assert where in w.locations
    assert monkey.height < 1, "Monkey can only move while on the ground"
    monkey.at = where
    return f"Monkey moved to {where}"

def push(monkey: Monkey, box: Box, where: Position):
    assert monkey.at == box.at
    assert where in w.locations
    assert monkey.height < 1, "Monkey can only move the box while on the ground"
    monkey.at = where
    box.at = where
    return f"Monkey moved box to {where}"

def climb_up(monkey: Monkey, box: Box):
    assert monkey.at == box.at
    monkey.height += box.height
    return "Monkey climbs the box"

def grasp(monkey: Monkey, banana: Banana):
    assert monkey.height == banana.height
    assert monkey.at == banana.at
    banana.owner = monkey
    return "Monkey takes the banana"

def infer_owner_at(palmtree: PalmTree, banana: Banana):
    assert banana.attached == palmtree
    banana.at = palmtree.at
    return "Remembered that if banana is on palm tree, its location is where palm tree is"

def infer_banana_height(palmtree: PalmTree, banana: Banana):
    assert banana.attached == palmtree
    banana.height = palmtree.height
    return "Remembered that if banana is on the tree, its height equals tree's height"

# Assuming schedule is a function that takes the list of functions and their arguments
# and returns a sequence of tasks to be executed.
print('\n'.join(x() for x in schedule(
    [go, push, climb_up, grasp, infer_banana_height, infer_owner_at],
    [w, p1, p2, p3, m, box, p, b],
    goal=lambda: b.owner == m
)))
