import bpy
import bge

controller = bge.logic.getCurrentController()
owner = controller.owner
movement = controller.actuators["motion"]

if controller.sensors["me"].positive:
    for sensor in controller.sensors:
        if sensor.name != "me" and sensor.name != "stop" and sensor.positive:
            if controller.sensors["stop"].positive:
                print("[ACTION]: stopping motion betweeen", 
                      owner.name, "and", sensor.name)
                movement.force = [0.0, 0.0, 0.0]
                movement.dLoc = [0.0, 0.0, 0.0]
                controller.activate(movement)
            else:
                print("[ACTION]:  compressing", owner.name, "and", sensor.name)
                brother = bpy.data.objects[sensor.name]
                vector = [0.0, 0.0, 0.0]
                distance = 0
        
                for i in range(3):
                    vector[i] += owner.localPosition[i] - brother.location[i]
                    distance += vector[i]**2
                
                strength = bpy.data.objects[owner.name][sensor.name]
                distance = (distance ** (0.5)) * strength
                
                for i in range(3):
                    vector[i] += movement.dLoc[i]

                movement.dLoc = vector
                controller.activate(movement)
                print("done! distance: ", distance, " vector ", vector)
