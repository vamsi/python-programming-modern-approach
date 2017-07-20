import time
import random


class VirtualMachine:

    def start(self):
        print("Virtual machine is now starting...")
        time.sleep(random.randrange(2, 6))
        print("VM Started")

    def stop(self):
        print("Virtual machine is now stopping...")
        time.sleep(random.randrange(2, 6))
        print("VM Stopped")

    def destroy(self):
        print("Virtual machine is now being destroy...")
        time.sleep(random.randrange(2, 6))
        print("VM destoyed successfully")

    def restart(self):
        print("Virtual machine restart in progress...")
        self.stop()
        self.start()

    def run(self):
        print("Enter the command you wish to run")
        command = input()
        print("Running {} command on VM".format(command))
        print("Executed successfully")

    def status(self):
        print("All ok.")


v1 = VirtualMachine()
v1.start()
v1.start()
v1.run()

v8 = VirtualMachine()
v8.stop()
v8.destroy()
