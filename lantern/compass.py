from sense_hat import SenseHat
from time import sleep

import time



sense = SenseHat()

sense.clear()

sense.set_rotation(180)

#orientation = sense.get_orientation_degrees()

heading=sense.get_compass()



if heading <45 or  heading >315:#north

        sense.show_message("Go Right")#directions

elif heading < 135:#east

        sense.show_message("Go Ahead")

elif heading<225:#south

        sense.show_message("Turn Back")

        time.sleep(5)

        sense.show_message("Go Ahead")

else:#west

        sense.show_message("Turn Right")

        time.sleep(5)

        sense.show_message("Go Right")
