import bpy
import bge

controller = bge.logic.getCurrentController()
owner = controller.owner
movement = controller.actuators["motion"]

print(":  got the signal")
if controller.sensors["me"].positive:
    for sensor in controller.sensors:
        if sensor.name != "me" and sensor.positive:
            print(":  i'm with", sensor.name)
            brother = bpy.data.objects[sensor.name]
            vector = [0.0, 0.0, 0.0]
            distance = 0
            
            for i in range(3):
                vector[i] += owner.localPosition[i] - brother.location[i]
                distance += vector[i]**2
                
            strength = bpy.data.objects[owner.name][sensor.name]
            distance = (distance ** (0.5)) * strength

            print("done! distance: ", distance, " vector ", vector)
