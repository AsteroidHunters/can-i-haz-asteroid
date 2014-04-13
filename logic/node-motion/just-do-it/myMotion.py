import bge
import bgy

controller = bge.logic.getCurrentController()
owner = controller.owner
movement = controller.actuators["motion"]

if controller.sensors["me"].positive:
    for sensor in controller.sensors:
        if sensor.name != "me" and sensor.positive:
            brother = bpy.data.objects[sensor.name]
            vector[0.0, 0.0, 0.0]
            distance = 0
            
            for i in range(3):
                vector[i] += owner.localPosition[i] - brother.location[i]
                distance += vector[i]**2
                
            distance = distance ** (0.5)
            
