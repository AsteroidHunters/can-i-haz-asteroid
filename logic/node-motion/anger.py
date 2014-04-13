import bpy
import bge

print("SENSOR SHOT!-------------")

controller = bge.logic.getCurrentController()
owner = controller.owner
movement = controller.actuators["motion"]

for sensor in controller.sensors:
    print("i'm with ", sensor.name)

    if(sensor.name != "me"):
        brother = bpy.data.objects[sensor.name]
        #    distance = owner.dLoc[0]**2 + owner.dLoc[1]**2 + owner.
        vector = [0.0, 0.0, 0.0]
        distance = 0

        for i in range(3) :
            vector[i] += owner.localPosition[i] - brother.location[i]
            distance += vector[i]**2
        
        distance = distance ** (0.5)
        
        for i in range(3):
            vector[i] = (vector[i]/distance) * 
        
        
