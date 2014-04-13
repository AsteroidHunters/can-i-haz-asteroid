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
                controller.deactivate(movement)
                movement.force = [0.0, 0.0, 0.0]
            else:
                print("[ACTION]:  compressing", owner.name, "and", sensor.name)
                brother = bpy.data.objects[sensor.name]
                
                #computing wires motion simulation
                #(this is the buggy stuff)
                vector = [0.0, 0.0, 0.0] #the force that will be applied 
                distance = 0 #the distance between 'this and 'brother'
                #not a big deal, i need this to compute the force applied to owner.
        
                for i in range(3):
                    vector[i] += (owner.localPosition[i] - brother.location[i])*-1
                    distance += vector[i]**2
                
                strength = bpy.data.objects[owner.name][sensor.name]
                distance = (distance ** (0.5)) * strength
                
                for i in range(3):
                    vector[i] += movement.force[i]

                movement.force = vector
                #end of buggy part? someone have to rethink the equations
                #i'm using coulomb's law to calculate the motion of the nodes
                #but it doesnt seem to be enough to emulate wires :(
                #here is the equation: 
                #owner.force = (brother.position - owner.position)/distance

                controller.activate(movement)
                print("done! distance: ", distance, " vector ", vector)
