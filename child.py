# import base

# from pybricks import ev3brick as brick
# from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
#                                  InfraredSensor, UltrasonicSensor, GyroSensor)
# from pybricks.parameters import (Port, Stop, Direction, Button, Color,
#                                  SoundFile, ImageFile, Align)
# from pybricks.tools import print, wait, StopWatch
# from pybricks.robotics import DriveBase

# class TrackerImpl(Tracker):

#    def __init__(self):
#         self.obstacle_sensor = InfraredSensor(Port.S1)
#         self.left_motor = Motor(Port.B)
#         self.right_motor = Motor(Port.C)
#         self.head_motor = Motor(Port.A)
#         wheel_diameter = 56
#         axle_track = 114
#         self.robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)
#         self.head_motor.run_until_stalled(-100)
#         self.head_motor.reset_angle(0)

#     def start_driving(self, coordinate):
#         self.robot.drive(coordinate, 0)
#         return

#     def drive(self, coordinate, time):
#         self.robot.drive_time(coordinate, 0, time)
#         return

#     def turn(self, index):
#         self.robot.drive_time(0, index, 2000)
#         return

#     def read_infrared_sensor(self):
#         return self.obstacle_sensor.distance()

#     def head_up(self):
#         self.head_motor.run_target(50, 90) 
#         return

#     def head_down(self):
#         self.head_motor.run_target(50, 120) 
#         return




# t = TrackerImpl()
# t.do_work()        