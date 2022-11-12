# import math
# import random

# width = 10
# height = int(5)
# dict = {}
# # print(type(width))
# for x in range(width + 1):
#     for y in range(height + 1):
#         dict[(x, y)] = 10
# #x, y = self.room.get_room_width(), self.room.get_room_height()
# print(math.floor(random.random() * 360))

theprince@Oluwapelumis-MacBook-Air PS_3 % /usr/bin/python3 "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f
16.py"
test_clean_tile_at_position_PosToPos (__main__.ps3_P1A)
Test if clean_tile_at_position removes all dirt ... ok
test_clean_tile_at_position_PosToZero (__main__.ps3_P1A)
Test if clean_tile_at_position removes all dirt ... ok
test_clean_tile_at_position_ZeroToZero (__main__.ps3_P1A)
Test if clean_tile_at_position removes all dirt ... ok
test_get_num_cleaned_tiles_FullIn1 (__main__.ps3_P1A)
Test get_num_cleaned_tiles for cleaning subset of room completely with 1 call ... ok
test_get_num_cleaned_tiles_FullIn2 (__main__.ps3_P1A)
Test get_num_cleaned_tiles for cleaning subset of room in two calls ... ok
test_get_num_cleaned_tiles_OverClean (__main__.ps3_P1A)
Test cleaning already clean tiles does not increment counter ... ok
test_get_num_cleaned_tiles_Partial (__main__.ps3_P1A)
Test get_num_cleaned_tiles for cleaning subset of room incompletely ... ok
test_is_position_in_room (__main__.ps3_P1A)
Test is_position_in_room ... /Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py:179: DeprecationWarning: Please use assertEqual instead.
  self.assertEquals(solution_room.is_position_in_room(pos), room.is_position_in_room(pos),
ok
test_is_tile_cleaned_clean (__main__.ps3_P1A)
Test is_tile_cleaned ... ok
test_is_tile_cleaned_dirty (__main__.ps3_P1A)
Test is_tile_cleaned ... ok
test_room_dirt_clean (__main__.ps3_P1A)
Can fail either because get_dirt_amount is working incorrectly ... /Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py:51: DeprecationWarning: Please use assertEqual instead.
  self.assertEquals(room.get_dirt_amount(x, y),dirt_amount,
ok
test_room_dirt_dirty (__main__.ps3_P1A)
Can fail either because get_dirt_amount is working incorrectly ... /Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py:39: DeprecationWarning: Please use assertEqual instead.
  self.assertEquals(room.get_dirt_amount(x, y),dirt_amount,
ok
test_unimplemented_methods (__main__.ps3_P1A)
Test if student implemented methods in RectangularRoom abstract class that should not be implemented ... ok
test_getset_robot_direction (__main__.ps3_P1B)
Test get_robot_direction and set_robot_direction ... ERROR
test_unimplemented_methods (__main__.ps3_P1B)
Test if student implemented methods in Robot abstract class that should not be implemented ... ERROR
test_get_num_tiles (__main__.ps3_P2_ER)
test get_num_tiles method ... /Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py:245: DeprecationWarning: Please use assertEqual instead.
  self.assertEquals(room_num_tiles, sol_room_tiles,
ok
test_get_random_position (__main__.ps3_P2_ER)
Test get_random_position ... ok
test_is_position_valid (__main__.ps3_P2_ER)
Test is_position_valid ... /Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py:260: DeprecationWarning: Please use assertEqual instead.
  self.assertEquals(solution_room.is_position_valid(pos), room.is_position_valid(pos),
ok
test_get_num_tiles (__main__.ps3_P2_FR)
test get_num_tiles method ... /Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py:329: DeprecationWarning: Please use assertEqual instead.
  self.assertEquals(room_num_tiles, sol_room_num_tiles,
ok
test_get_random_position (__main__.ps3_P2_FR)
Test get_random_position for FurnishedRoom ... ok
test_is_position_furnished (__main__.ps3_P2_FR)
test_is_position_furnished ... /Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py:293: DeprecationWarning: Please use assertEqual instead.
  self.assertEquals(room.is_position_furnished(pos),sol_room.is_position_furnished(pos),
ok
test_is_position_valid (__main__.ps3_P2_FR)
Test is_position_valid ... /Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py:310: DeprecationWarning: Please use assertEqual instead.
  self.assertEquals(sol_room.is_position_valid(pos), room.is_position_valid(pos),
ok
test_is_tile_furnished (__main__.ps3_P2_FR)
test is_tile_furnished ... /Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py:277: DeprecationWarning: Please use assertEqual instead.
  self.assertEquals(room.is_tile_furnished(x,y),sol_room.is_tile_furnished(x,y),
ok
testRobot (__main__.ps3_P3)
Test StandardRobot ... ERROR
test_BoundaryConditions (__main__.ps3_P3)
Test strict inequalities in random positions for the EmptyRoom and StandardRobot ... ERROR
test_update_position_and_cleanStandardRobot (__main__.ps3_P3)
Test StandardRobot.update_position_and_clean ... ERROR
testSimulation1 (__main__.ps3_P5_Standard)
Test cleaning 100% of a 5x5 room ... Unexpected error: 'SimulationThread' object has no attribute 'isAlive'
ERROR
testSimulation10 (__main__.ps3_P5_Standard)
Test multiple robots (95% of a 10x10 room with 5 robots (Standard Robot)) capacity = 2, 6 dirt/tile ... ERROR
testSimulation11 (__main__.ps3_P5_Standard)
Test multiple robots and different speeds (90% of a 5x5 room with 3 robots of speed 0.5 ... ERROR
testSimulation2 (__main__.ps3_P5_Standard)
Test cleaning 75% of a 10x10 room (Standard Robot) ... ERROR
testSimulation3 (__main__.ps3_P5_Standard)
Test cleaning 90% of a 10x10 room (Standard Robot) ... ERROR
testSimulation4 (__main__.ps3_P5_Standard)
Test multiple robots (95% of a 20x20 room with 5 robots (Standard Robot)) ... ERROR
testSimulation5 (__main__.ps3_P5_Standard)
Test different speeds (90% of a 5x20 room with a robot of speed 0.2 (Standard Robot)) ... ERROR
testSimulation6 (__main__.ps3_P5_Standard)
Test multiple robots and different speeds (90% of a 10x10 room with 3 robots of speed 0.5 (Standard Robot)) ... ERROR
testSimulation7 (__main__.ps3_P5_Standard)
Test cleaning 100% of a 5x5 room (Standard Robot, 5 dirt/tile, capcity = 3) ... ERROR
testSimulation8 (__main__.ps3_P5_Standard)
Test cleaning 100% of a 5x5 room (Standard Robot, 6 dirt/tile, capacity = 3) ... ERROR
testSimulation9 (__main__.ps3_P5_Standard)
Test different speeds (90% of a 3x10 room with a robot of speed 0.2 (Standard Robot)), ... ERROR
testSimulation1 (__main__.ps3_P5_Faulty)
Test cleaning 100% of a 5x5 room with FaultyRobot ... ERROR
testSimulation2 (__main__.ps3_P5_Faulty)
Test cleaning 75% of a 10x10 room with FaultyRobot ... ERROR
testSimulation3 (__main__.ps3_P5_Faulty)
Test cleaning 90% of a 10x10 room with FaultyRobot ... ERROR
testSimulation4 (__main__.ps3_P5_Faulty)
Test cleaning 100% of a 5x5 room with FaultyRobot ... ERROR
testSimulation5 (__main__.ps3_P5_Faulty)
Test cleaning 75% of a 10x10 room with FaultyRobot ... ERROR
testSimulation6 (__main__.ps3_P5_Faulty)
Test cleaning 90% of a 10x10 room with FaultyRobot ... ERROR

======================================================================
ERROR: test_getset_robot_direction (__main__.ps3_P1B)
Test get_robot_direction and set_robot_direction
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py", line 197, in test_getset_robot_direction
    robots = [ps3.Robot(solution_room, 1.0, 1) for i in range(4)]
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py", line 197, in <listcomp>
    robots = [ps3.Robot(solution_room, 1.0, 1) for i in range(4)]
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3.py", line 242, in __init__
    self.position = Position(room.get_random_position())
TypeError: __init__() missing 1 required positional argument: 'y'

======================================================================
ERROR: test_unimplemented_methods (__main__.ps3_P1B)
Test if student implemented methods in Robot abstract class that should not be implemented
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py", line 188, in test_unimplemented_methods
    robot = ps3.Robot(room,1,1)
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3.py", line 242, in __init__
    self.position = Position(room.get_random_position())
TypeError: __init__() missing 1 required positional argument: 'y'

======================================================================
ERROR: testRobot (__main__.ps3_P3)
Test StandardRobot
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py", line 380, in testRobot
    r, robots = self.createRoomAndRobots(4)
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py", line 352, in createRoomAndRobots
    robots = [ps3.StandardRobot(r, 1.0, 1) for i in range(num_robots)]
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py", line 352, in <listcomp>
    robots = [ps3.StandardRobot(r, 1.0, 1) for i in range(num_robots)]
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3.py", line 242, in __init__
    self.position = Position(room.get_random_position())
TypeError: __init__() missing 1 required positional argument: 'y'

======================================================================
ERROR: test_BoundaryConditions (__main__.ps3_P3)
Test strict inequalities in random positions for the EmptyRoom and StandardRobot
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py", line 358, in test_BoundaryConditions
    r, robots = self.createRoomAndRobots(4)
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py", line 352, in createRoomAndRobots
    robots = [ps3.StandardRobot(r, 1.0, 1) for i in range(num_robots)]
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py", line 352, in <listcomp>
    robots = [ps3.StandardRobot(r, 1.0, 1) for i in range(num_robots)]
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3.py", line 242, in __init__
    self.position = Position(room.get_random_position())
TypeError: __init__() missing 1 required positional argument: 'y'

======================================================================
ERROR: test_update_position_and_cleanStandardRobot (__main__.ps3_P3)
Test StandardRobot.update_position_and_clean
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py", line 418, in test_update_position_and_cleanStandardRobot
    robot = ps3.StandardRobot(r, 1.0, 1)
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3.py", line 242, in __init__
    self.position = Position(room.get_random_position())
TypeError: __init__() missing 1 required positional argument: 'y'

======================================================================
ERROR: testSimulation1 (__main__.ps3_P5_Standard)
Test cleaning 100% of a 5x5 room
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py", line 519, in testSimulation1
    self.run_simulation(((142, 173),), (1, 1.0, 1, 5, 5, 1, 1.0, 100, ps3.StandardRobot))
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py", line 497, in run_simulation
    if thr.isAlive():
AttributeError: 'SimulationThread' object has no attribute 'isAlive'

======================================================================
ERROR: testSimulation10 (__main__.ps3_P5_Standard)
Test multiple robots (95% of a 10x10 room with 5 robots (Standard Robot)) capacity = 2, 6 dirt/tile
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py", line 551, in testSimulation10
    self.run_simulation(((137, 198),(130, 190)), (5, 1.0, 2, 10, 10, 6, 0.95, 100, ps3.StandardRobot))
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py", line 497, in run_simulation
    if thr.isAlive():
AttributeError: 'SimulationThread' object has no attribute 'isAlive'

======================================================================
ERROR: testSimulation11 (__main__.ps3_P5_Standard)
Test multiple robots and different speeds (90% of a 5x5 room with 3 robots of speed 0.5
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py", line 555, in testSimulation11
    self.run_simulation(((48, 108), (45, 104)), (3, 0.5, 2, 5, 5, 6, 0.9, 100, ps3.StandardRobot))
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py", line 497, in run_simulation
    if thr.isAlive():
AttributeError: 'SimulationThread' object has no attribute 'isAlive'

======================================================================
ERROR: testSimulation2 (__main__.ps3_P5_Standard)
Test cleaning 75% of a 10x10 room (Standard Robot)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py", line 525, in testSimulation2
    self.run_simulation(((183, 198),), (1, 1.0, 1, 10, 10, 1, 0.75, 100, ps3.StandardRobot))
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py", line 497, in run_simulation
    if thr.isAlive():
AttributeError: 'SimulationThread' object has no attribute 'isAlive'

======================================================================
ERROR: testSimulation3 (__main__.ps3_P5_Standard)
Test cleaning 90% of a 10x10 room (Standard Robot)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py", line 528, in testSimulation3
    self.run_simulation(((298, 327),), (1, 1.0, 1, 10, 10, 1, 0.9, 100, ps3.StandardRobot))
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py", line 497, in run_simulation
    if thr.isAlive():
AttributeError: 'SimulationThread' object has no attribute 'isAlive'

======================================================================
ERROR: testSimulation4 (__main__.ps3_P5_Standard)
Test multiple robots (95% of a 20x20 room with 5 robots (Standard Robot))
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py", line 531, in testSimulation4
    self.run_simulation(((289, 303),), (5, 1.0, 1, 20, 20, 1, 0.95, 100, ps3.StandardRobot))
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py", line 497, in run_simulation
    if thr.isAlive():
AttributeError: 'SimulationThread' object has no attribute 'isAlive'

======================================================================
ERROR: testSimulation5 (__main__.ps3_P5_Standard)
Test different speeds (90% of a 5x20 room with a robot of speed 0.2 (Standard Robot))
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py", line 534, in testSimulation5
    self.run_simulation(((1095, 1228),), (1, 0.2, 1, 5, 20, 1, 0.9, 100, ps3.StandardRobot))
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py", line 497, in run_simulation
    if thr.isAlive():
AttributeError: 'SimulationThread' object has no attribute 'isAlive'

======================================================================
ERROR: testSimulation6 (__main__.ps3_P5_Standard)
Test multiple robots and different speeds (90% of a 10x10 room with 3 robots of speed 0.5 (Standard Robot))
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py", line 537, in testSimulation6
    self.run_simulation(((155, 180),), (3, 0.5, 1, 10, 10, 1, 0.9, 100, ps3.StandardRobot))
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py", line 497, in run_simulation
    if thr.isAlive():
AttributeError: 'SimulationThread' object has no attribute 'isAlive'

======================================================================
ERROR: testSimulation7 (__main__.ps3_P5_Standard)
Test cleaning 100% of a 5x5 room (Standard Robot, 5 dirt/tile, capcity = 3)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py", line 541, in testSimulation7
    self.run_simulation(((206, 266),(180, 240)), (1, 1.0, 3, 5, 5, 5, 1.0, 100, ps3.StandardRobot))
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py", line 497, in run_simulation
    if thr.isAlive():
AttributeError: 'SimulationThread' object has no attribute 'isAlive'

======================================================================
ERROR: testSimulation8 (__main__.ps3_P5_Standard)
Test cleaning 100% of a 5x5 room (Standard Robot, 6 dirt/tile, capacity = 3)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py", line 544, in testSimulation8
    self.run_simulation(((206, 266),(180, 240)), (1, 1.0, 3, 5, 5, 6, 1.0, 100, ps3.StandardRobot))
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py", line 497, in run_simulation
    if thr.isAlive():
AttributeError: 'SimulationThread' object has no attribute 'isAlive'

======================================================================
ERROR: testSimulation9 (__main__.ps3_P5_Standard)
Test different speeds (90% of a 3x10 room with a robot of speed 0.2 (Standard Robot)),
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py", line 548, in testSimulation9
    self.run_simulation(((387, 447),(384, 444)), (1, 0.2, 2, 3, 10, 6, 0.9, 100, ps3.StandardRobot))
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py", line 497, in run_simulation
    if thr.isAlive():
AttributeError: 'SimulationThread' object has no attribute 'isAlive'

======================================================================
ERROR: testSimulation1 (__main__.ps3_P5_Faulty)
Test cleaning 100% of a 5x5 room with FaultyRobot
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py", line 561, in testSimulation1
    x = ps3.run_simulation(1, 1.0, 1, 5, 5, 1, 1.0, 100, ps3.FaultyRobot)
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3.py", line 508, in run_simulation
    raise NotImplementedError
NotImplementedError

======================================================================
ERROR: testSimulation2 (__main__.ps3_P5_Faulty)
Test cleaning 75% of a 10x10 room with FaultyRobot
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py", line 566, in testSimulation2
    x = ps3.run_simulation(1, 1.0, 1, 10, 10, 1, 0.75, 100, ps3.FaultyRobot)
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3.py", line 508, in run_simulation
    raise NotImplementedError
NotImplementedError

======================================================================
ERROR: testSimulation3 (__main__.ps3_P5_Faulty)
Test cleaning 90% of a 10x10 room with FaultyRobot
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py", line 570, in testSimulation3
    x = ps3.run_simulation(1, 1.0, 1, 10, 10, 1, 0.9, 100, ps3.FaultyRobot)
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3.py", line 508, in run_simulation
    raise NotImplementedError
NotImplementedError

======================================================================
ERROR: testSimulation4 (__main__.ps3_P5_Faulty)
Test cleaning 100% of a 5x5 room with FaultyRobot
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py", line 574, in testSimulation4
    x = ps3.run_simulation(2, 1.0, 2, 5, 5, 5, 1.0, 100, ps3.FaultyRobot)
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3.py", line 508, in run_simulation
    raise NotImplementedError
NotImplementedError

======================================================================
ERROR: testSimulation5 (__main__.ps3_P5_Faulty)
Test cleaning 75% of a 10x10 room with FaultyRobot
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py", line 578, in testSimulation5
    x = ps3.run_simulation(4, 1.0, 3, 10, 10, 5, 0.75, 100, ps3.FaultyRobot)
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3.py", line 508, in run_simulation
    raise NotImplementedError
NotImplementedError

======================================================================
ERROR: testSimulation6 (__main__.ps3_P5_Faulty)
Test cleaning 90% of a 10x10 room with FaultyRobot
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3_tests_f16.py", line 582, in testSimulation6
    x = ps3.run_simulation(5, 1.0, 3, 10, 10, 10, 0.9, 100, ps3.FaultyRobot)
  File "/Users/theprince/Desktop/Problem sets/6.0002/PS_3/ps3.py", line 508, in run_simulation
    raise NotImplementedError
NotImplementedError

----------------------------------------------------------------------
Ran 43 tests in 0.715s

FAILED (errors=22)
theprince@Oluwapelumis-MacBook-Air PS_3 % 