import bpy
import colorsys

def delete_all():
  """Delete all objects and materials in the scene"""
  bpy.ops.object.select_all(action='SELECT')
  bpy.ops.object.delete() 
  for material in bpy.data.materials:
      material.user_clear()
      bpy.data.materials.remove(material)
        
def add_emission(obj, name):
    """Adds a material with emission to an object TODO this is just pink now!"""
    pink = bpy.data.materials.new(name=name)
    pink.use_nodes = True
    pink.node_tree.nodes.clear() # important to clear defaults

    node_emission = pink.node_tree.nodes.new(type='ShaderNodeEmission')
    node_emission.inputs[0].default_value = (0,1,0,1)
    bpy.data.materials[pink_name].node_tree.nodes["Emission"].inputs[0].default_value = (1, 0.0089906, 0.651206, 1)
    obj.data.materials.append(bpy.data.materials[name])
