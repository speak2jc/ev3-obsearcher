
from threading import Thread
from time import sleep
from random import randrange
from collections import deque

class Tracker:

    def __init__(self):
        self.moveHeadCommandQueue = deque()
        self.detectObstacleCommandQueue = deque()
        self.obstacleDetectedQueue = deque()

    def start_driving(self, coordinate):
        text = "FORWARDS"
        if coordinate < 0:
            text = "BACKWARDS"
        print("DRIVING " + text + " continuously: " + str(coordinate))
        return

    def drive(self, coordinate, time):
        text = "FORWARDS"
        if coordinate < 0:
            text = "BACKWARDS"
        print("DRIVING " + text + " for " + str(time) + " seconds:  " + str(coordinate))
        return

    def turn(self, index):
        print('TURNING - best directional index: ' + str(index))
        sleep(15)
        return

    def head_up(self):
        print('HEAD - moving up '
        return

    def head_down(self):
        print('HEAD - moving down '
        return

    def read_infrared_sensor(self):
        random_distance = randrange(100)
        return random_distance

    def detect_obstacle(self):

        state = "pending"
        current_message = ""

        while True:

            if not len(self.detectObstacleCommandQueue) == 0:
                command = self.detectObstacleCommandQueue.pop()
                if command == "activate":
                    state = "activated"
                elif command == "pause":
                    state = "paused"

            if state == "activated":

                obstacle_detected = False

                # Simulate obstacle detected
                distance_reading = self.read_infrared_sensor()

                if distance_reading < 30:
                    obstacle_detected = True

                # Post message on queue
                if obstacle_detected:
                    print('      Obstacle detected at distance: ' + str(distance_reading))
                    current_message = "obstacle_detected_" + str(distance_reading)
                    self.obstacleDetectedQueue.append(current_message)
            elif state == "paused":
                print('      Obstacle detection paused (last message: ' + current_message + ')')
            sleep(3)

    def horizontal_scan(self):

        # This simulates a robot turning through an angle / index-range
        # The best index is the one resulting in the largest obstacle distance

        best_index = 0
        best_distance = -1

        for index in range(-100, 100, 10):
            # print(index)
            current_distance = self.read_infrared_sensor()
            if current_distance > best_distance:
                best_distance = current_distance
                best_index = index

        return best_index

    def move_head_up_down(self):

        state = "pending"
        up_position = True

        while True:

            if not len(self.moveHeadCommandQueue) == 0:
                command = self.moveHeadCommandQueue.pop()
                if command == "activate":
                    state = "activated"
                elif command == "pause":
                    state = "paused"

            if state == "activated":
                if up_position:
                    up_position = False
                    #print('        move_head down')
                    head_down()
                    sleep(3)
                else:
                    up_position = True
                    # print('        move_head up')
                    head_up()
                    sleep(3)
            elif state == "paused":
                print('      Move head state: paused')
                sleep(5)

    def do_work(self):

        # Start head movement
        t1 = Thread(target=self.move_head_up_down)
        t1.daemon = True
        t1.start()
        self.moveHeadCommandQueue.append("activate")

        t2 = Thread(target=self.detect_obstacle)
        t2.daemon = True
        t2.start()
        self.detectObstacleCommandQueue.append("activate")

        self.start_driving(100)

        while True:
            obstacle_detected_message = ""

            if len(self.obstacleDetectedQueue) > 0:
                obstacle_detected_message = self.obstacleDetectedQueue.pop()

            if obstacle_detected_message.startswith("obstacle_detected"):
                print('RESPONDING TO OBSTACLE DETECTED: ' + obstacle_detected_message)
                self.detectObstacleCommandQueue.append("pause")
                self.moveHeadCommandQueue.append("pause")

                self.drive(-100, 2000)
                index = self.horizontal_scan()
                self.turn(index)

                self.start_driving(100)
                self.detectObstacleCommandQueue.append("activate")
                self.moveHeadCommandQueue.append("activate")

            elif obstacle_detected_message != "":
                print('Unknown message - de-queuing')


# tracker = Tracker()
# tracker.do_work()

