'''
This module will move the "owner" node in the direction of one of the linked "brothers" it has.

I'm not very familiar with this technology, so this code could be more pretty, anyway, this approach can provide a bit of customization (you can add nodes without extending the code).

Think on this network as a graph with vertex (nodes) and edges (connections) between them. 

you can plug nodes between them like this:
   -> Create the new node by putting a new object on blender, and 'name' it
   -> "plug it" to 'another' node
        -> add a sensor and name it with the 'another's name.
        -> add another sensor and name it "me"
        -> add another sensor and name it "stop"
        -> add a python controller and link it to this script
        -> add an actuator and call it "motion".
        -> plug all the sensors to the python controller
        -> plug the controller to the "motion" actuator
        -> for each node plugged to it, add a custom property to 'this' node, and name it as the plugged node, this is the compressing force of the wire that joins this node with the 'another'.
WARNING: the rate of compression of A between B is not necessarily the same as the rate of compression of B between A. A has a motor to compress the wire, and B has another motor to compress the wire. But if you gonna use a chemical wire, and the rate of compression of A with B has to be the same as B with A, be aware of this.

The owner has sensors, each sensor is named with the name of the node with whom the owner is linked. Also, the owner is linked to a "stop" sensor, and a "me" sensor, which reffers to activation of "owner".  When two sensors get positive, they approach (simulating wires compression). And all of this sensors are linked into a python controller, and this controller is linked to a motion action, which allows him to move.

There is a better approach. I don't know how to inherit Blender's objects primitives, but you could extend them adding a vector of adjacency with all the connected nodes into it. (like a graph).

Then, you add a method to compress 'this' node with the 'connected' node (by formulating a new equation).

anyway, i don't know how to do this with blender :(

'''

import bpy
import bge

controller = bge.logic.getCurrentController()
owner = controller.owner
movement = controller.actuators["motion"]

#this code isnt complete. The constraints are missing, wires are infinitely wide.
#wires doesnt stay compressed.

if controller.sensors["me"].positive:
    for sensor in controller.sensors:
        if sensor.name != "me" and sensor.name != "stop" and sensor.positive:
            print("[ACTION]:  compressing", owner.name, "and", sensor.name)
            brother = bpy.data.objects[sensor.name]
            
            #computing wires motion simulation
            vector = [0.0, 0.0, 0.0] #the movement that will be applied 
            distance = 0 #the distance between 'owner' and 'brother'
            
            for i in range(3):
                vector[i] += (owner.localPosition[i] - brother.location[i])*-1
                distance += vector[i]**2
                
            strength = bpy.data.objects[owner.name][sensor.name]*0.1
            distance = (distance ** (0.5))

            for i in range(3):
                vector[i] = (vector[i] * strength) / distance;
            #vector is now pointing to brother, 
            #and its dimension is defined by the strength
            
            for i in range(3):
                vector[i] += movement.dLoc[i]
                
            movement.dLoc = vector
            #here is the equation used to make them closer: 
            #owner.force = (brother.position - owner.position)/distance

            controller.activate(movement)
            print("done! distance: ", distance, " vector ", vector)
else:
    print("[ACTION]: stopping motion betweeen", 
          owner.name)
    controller.deactivate(movement)
    movement.dLoc = [0.0, 0.0, 0.0]    
