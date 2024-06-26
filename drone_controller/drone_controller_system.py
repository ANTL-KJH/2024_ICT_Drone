from drone_controller.drone_controller_switch import *
from drone_controller.drone_controller_joystick import *
from drone_controller.drone_controller_information import *
from drone_controller.drone_controller_videostreamer import *
from drone_controller.drone_controller_datasender import *
from drone_controller.drone_controller_button import *
from threading import Thread, Lock
from drone_controller.drone_controller_display import *
import os


class class_Drone_Controller_System:
    def __init__(self):
        self.info = class_Drone_Controller_Information()
        self.controllerJoystick_L = class_Drone_Controller_Joystick(0, 0, 1, 2, 0, 1, self.info)
        self.controllerJoystick_R = class_Drone_Controller_Joystick(1, 0, 1, 2, 0, 2, self.info)
        self.videoStreamer = class_Drone_Controller_VideoStreamer()
        self.dataSender = class_drone_controller_datasender(self.info)
        self.button = class_drone_controller_button(self.info)
        self.switch = class_Drone_Controller_Switch(self.info)
        self.dc_display = class_drone_controller_display(self.info)

    def start_Drone_Controller(self):
        print("SYSTEM ALARM::Drone Controller Started")
        thread_Joystick_Left = Thread(target=self.controllerJoystick_L.run_joystick)
        thread_Joystick_Right = Thread(target=self.controllerJoystick_R.run_joystick)
        thread_VideoStream = Thread(target=self.videoStreamer.run_VideoStreamer)
        thread_dataSender = Thread(target=self.dataSender.run_data_sender)
        thrad_button = Thread(target=self.button.run_button)
        thread_switch = Thread(target=self.switch.runSwitch())
        thread_Joystick_Left.start()
        thread_Joystick_Right.start()
        thread_VideoStream.start()
        thread_dataSender.start()
        thrad_button.start()

    def print_system_log(self):
        print("=" * 50)
        print("Drone Controller State")
        print("Joystick Left(x:{}, y:{}, val:{}".format(self.info.joystick_Left_x, self.info.joystick_Left_y,
                                                        self.info.joystick_Left_val))
        print("Joystick Right(x:{}, y:{}, val:{}".format(self.info.joystick_Right_x, self.info.joystick_Right_y,
                                                         self.info.joystick_Right_val))
        print(
            f"button state 1: {self.info.button1}  2: {self.info.button2}  3: {self.info.button3} 4: {self.info.button4} 5: {self.info.button5} 6: {self.info.button6}")
        print("=" * 50)
        time.sleep(0.5)
        os.system('clear')

    def run_drone_controller_system(self):
        # controllerSwitch = drone_controller_switch.class_Drone_Controller_Switch(self)
        self.start_Drone_Controller()
        while True:
            self.print_system_log()