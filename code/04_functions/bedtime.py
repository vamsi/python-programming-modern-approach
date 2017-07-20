from datetime import datetime


def alarm_bedtime(bedtime="22:00:00", wake="06:00:00"):
    fmt = "%H:%M:%S"
    diff = datetime.strptime(wake, fmt) - datetime.strptime(bedtime, fmt)
    print("The amount of time you are in bed and asleep is {}".format(diff))


alarm_bedtime()
