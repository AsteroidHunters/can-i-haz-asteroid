import bpy
import bge

controller = bge.logic.getCurrentController()
owner = controller.owner
movement = controller.actuators["motion"]

for sensor in controller.sensors:
    print(sensor)
    print("ok, showing the object now")
    print(bpy.data.objects[sensor.name].location)

