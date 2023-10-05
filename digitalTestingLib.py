from WF_SDK import device, static, supplies, logic       # import instruments
import time
class digitalOutput:
  # Define the constructor of the class
    def __init__(self, device_data, channel, initial_state = 0):
        self.device_data = device_data
        self.channel = channel
        static.set_mode(self.device_data, self.channel, True)
        static.set_state(self.device_data, self.channel, initial_state)
        self.state = initial_state
    def on(self):
        static.set_state(self.device_data, self.channel, 1)
        self.state = 1
    def off(self):
        static.set_state(self.device_data, self.channel, 0)
        self.state = 0
    def set(self, new_state):
        static.set_state(self.device_data, self.channel, new_state)
        self.state = new_state
    def print_info(self):
        print("Channel: ",self.channel,"Type: DigitalIO Output", "State: ",self.state)
class digitalInput:
    # Define the constructor of the class
    def __init__(self, device_data, channel):
        self.device_data = device_data
        self.channel = channel
        #static.set_mode(device_data, channel, False)
        logic.trigger(self.device_data, enable=False, channel=channel)
    def read(self):
        return logic.record(self.device_data, self.channel)[0]
    def print_info(self):
        print("Channel: ",self.channel,"Type: Digital Input", "State: ",self.read())

class digitalSimClock:
    def __init__(self, device_data, channel, period):
        self.device_data = device_data
        self.channel = channel
        self.t = period/2
        static.set_mode(self.device_data, self.channel, True)
        static.set_state(self.device_data, self.channel, 0)
        self.state = 0
    # Define a method to print the car's information
    def high(self):
        static.set_state(self.device_data, self.channel, 1)
        self.state = 1
    def low(self):
        static.set_state(self.device_data, self.channel, 0)
        self.state = 0
    def flip(self):
        if (self.state == 1):
            self.low()
        else:
            self.high()
    def posedge(self):
        if (self.state == 0):
            self.high()
            time.sleep(self.t)
        else:
            self.low()
            time.sleep(self.t)
            self.high()
            time.sleep(self.t)
    def negedge(self):
        if (self.state == 1):
            self.low()
            time.sleep(self.t)
        else:
            self.high()
            time.sleep(self.t)
            self.low()
            time.sleep(self.t)
    def run(self, cycles):
        for i in range(cycles):
            self.flip()
            time.sleep(self.t)
            self.flip()
            time.sleep(self.t)

    def print_info(self):
        print("Channel: ",self.channel,"Type: Digital Sim Clock")