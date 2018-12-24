def add(radius=1.0,
        type='EMPTY',
        view_align=False,
        enter_editmode=False,
        location=(0.0, 0.0, 0.0),
        rotation=(0.0, 0.0, 0.0)):
    '''Add an object to the scene 

    :param radius: Radius 
    :type radius: float in [0, inf], (optional)
    :param type: Type 
    :type type: enum in ['MESH', 'CURVE', 'SURFACE', 'META', 'FONT', 'ARMATURE', 'LATTICE', 'EMPTY', 'GPENCIL', 'CAMERA', 'LIGHT', 'SPEAKER', 'LIGHT_PROBE'], (optional)
    :param view_align: Align to View, Align the new object to the view 
    :type view_align: boolean, (optional)
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object 
    :type enter_editmode: boolean, (optional)
    :param location: Location, Location for the newly added object 
    :type location: float array of 3 items in [-inf, inf], (optional)
    :param rotation: Rotation, Rotation for the newly added object 
    :type rotation: float array of 3 items in [-inf, inf], (optional)
    '''

    pass


def add_named(linked=False, name=""):
    '''Add named object 

    :param linked: Linked, Duplicate object but not object data, linking to the original data 
    :type linked: boolean, (optional)
    :param name: Name, Object name to add 
    :type name: string, (optional, never None)
    '''

    pass


def align(bb_quality=True,
          align_mode='OPT_2',
          relative_to='OPT_4',
          align_axis={}):
    '''Align Objects 

    :param bb_quality: High Quality, Enables high quality calculation of the bounding box for perfect results on complex shape meshes with rotation/scale (Slow) 
    :type bb_quality: boolean, (optional)
    :param align_mode: Align Mode:, Side of object to use for alignment 
    :type align_mode: enum in ['OPT_1', 'OPT_2', 'OPT_3'], (optional)
    :param relative_to: Relative To:, Reference location to align toOPT_1 Scene Origin, Use the Scene Origin as the position for the selected objects to align to.OPT_2 3D Cursor, Use the 3D cursor as the position for the selected objects to align to.OPT_3 Selection, Use the selected objects as the position for the selected objects to align to.OPT_4 Active, Use the active object as the position for the selected objects to align to. 
    :type relative_to: enum in ['OPT_1', 'OPT_2', 'OPT_3', 'OPT_4'], (optional)
    :param align_axis: Align, Align to axis 
    :type align_axis: enum set in {'X', 'Y', 'Z'}, (optional)
    '''

    pass


def anim_transforms_to_deltas():
    '''Convert object animation for normal transforms to delta transforms 

    '''

    pass


def armature_add(radius=1.0,
                 view_align=False,
                 enter_editmode=False,
                 location=(0.0, 0.0, 0.0),
                 rotation=(0.0, 0.0, 0.0)):
    '''Add an armature object to the scene 

    :param radius: Radius 
    :type radius: float in [0, inf], (optional)
    :param view_align: Align to View, Align the new object to the view 
    :type view_align: boolean, (optional)
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object 
    :type enter_editmode: boolean, (optional)
    :param location: Location, Location for the newly added object 
    :type location: float array of 3 items in [-inf, inf], (optional)
    :param rotation: Rotation, Rotation for the newly added object 
    :type rotation: float array of 3 items in [-inf, inf], (optional)
    '''

    pass


def assign_property_defaults(process_data=True, process_bones=True):
    '''Assign the current values of custom properties as their defaults, for use as part of the rest pose state in NLA track mixing 

    :param process_data: Process data properties 
    :type process_data: boolean, (optional)
    :param process_bones: Process bone properties 
    :type process_bones: boolean, (optional)
    '''

    pass


def bake(type='COMBINED',
         pass_filter={},
         filepath="",
         width=512,
         height=512,
         margin=16,
         use_selected_to_active=False,
         cage_extrusion=0.0,
         cage_object="",
         normal_space='TANGENT',
         normal_r='POS_X',
         normal_g='POS_Y',
         normal_b='POS_Z',
         save_mode='INTERNAL',
         use_clear=False,
         use_cage=False,
         use_split_materials=False,
         use_automatic_name=False,
         uv_layer=""):
    '''Bake image textures of selected objects 

    :param type: Type, Type of pass to bake, some of them may not be supported by the current render engine 
    :type type: enum in ['COMBINED', 'AO', 'SHADOW', 'NORMAL', 'UV', 'ROUGHNESS', 'EMIT', 'ENVIRONMENT', 'DIFFUSE', 'GLOSSY', 'TRANSMISSION', 'SUBSURFACE'], (optional)
    :param pass_filter: Pass Filter, Filter to combined, diffuse, glossy, transmission and subsurface passes 
    :type pass_filter: enum set in {'NONE', 'AO', 'EMIT', 'DIRECT', 'INDIRECT', 'COLOR', 'DIFFUSE', 'GLOSSY', 'TRANSMISSION', 'SUBSURFACE'}, (optional)
    :param filepath: File Path, Image filepath to use when saving externally 
    :type filepath: string, (optional, never None)
    :param width: Width, Horizontal dimension of the baking map (external only) 
    :type width: int in [1, inf], (optional)
    :param height: Height, Vertical dimension of the baking map (external only) 
    :type height: int in [1, inf], (optional)
    :param margin: Margin, Extends the baked result as a post process filter 
    :type margin: int in [0, inf], (optional)
    :param use_selected_to_active: Selected to Active, Bake shading on the surface of selected objects to the active object 
    :type use_selected_to_active: boolean, (optional)
    :param cage_extrusion: Cage Extrusion, Distance to use for the inward ray cast when using selected to active 
    :type cage_extrusion: float in [0, inf], (optional)
    :param cage_object: Cage Object, Object to use as cage, instead of calculating the cage from the active object with cage extrusion 
    :type cage_object: string, (optional, never None)
    :param normal_space: Normal Space, Choose normal space for bakingOBJECT Object, Bake the normals in object space.TANGENT Tangent, Bake the normals in tangent space. 
    :type normal_space: enum in ['OBJECT', 'TANGENT'], (optional)
    :param normal_r: R, Axis to bake in red channel 
    :type normal_r: enum in ['POS_X', 'POS_Y', 'POS_Z', 'NEG_X', 'NEG_Y', 'NEG_Z'], (optional)
    :param normal_g: G, Axis to bake in green channel 
    :type normal_g: enum in ['POS_X', 'POS_Y', 'POS_Z', 'NEG_X', 'NEG_Y', 'NEG_Z'], (optional)
    :param normal_b: B, Axis to bake in blue channel 
    :type normal_b: enum in ['POS_X', 'POS_Y', 'POS_Z', 'NEG_X', 'NEG_Y', 'NEG_Z'], (optional)
    :param save_mode: Save Mode, Choose how to save the baking mapINTERNAL Internal, Save the baking map in an internal image data-block.EXTERNAL External, Save the baking map in an external file. 
    :type save_mode: enum in ['INTERNAL', 'EXTERNAL'], (optional)
    :param use_clear: Clear, Clear Images before baking (only for internal saving) 
    :type use_clear: boolean, (optional)
    :param use_cage: Cage, Cast rays to active object from a cage 
    :type use_cage: boolean, (optional)
    :param use_split_materials: Split Materials, Split baked maps per material, using material name in output file (external only) 
    :type use_split_materials: boolean, (optional)
    :param use_automatic_name: Automatic Name, Automatically name the output file with the pass type 
    :type use_automatic_name: boolean, (optional)
    :param uv_layer: UV Layer, UV layer to override active 
    :type uv_layer: string, (optional, never None)
    '''

    pass


def bake_image():
    '''Bake image textures of selected objects 

    '''

    pass


def camera_add(view_align=False,
               enter_editmode=False,
               location=(0.0, 0.0, 0.0),
               rotation=(0.0, 0.0, 0.0)):
    '''Add a camera object to the scene 

    :param view_align: Align to View, Align the new object to the view 
    :type view_align: boolean, (optional)
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object 
    :type enter_editmode: boolean, (optional)
    :param location: Location, Location for the newly added object 
    :type location: float array of 3 items in [-inf, inf], (optional)
    :param rotation: Rotation, Rotation for the newly added object 
    :type rotation: float array of 3 items in [-inf, inf], (optional)
    '''

    pass


def collection_add():
    '''Add an object to a new collection 

    '''

    pass


def collection_instance_add(name="Collection",
                            collection='',
                            view_align=False,
                            location=(0.0, 0.0, 0.0),
                            rotation=(0.0, 0.0, 0.0)):
    '''Add a collection instance 

    :param name: Name, Collection name to add 
    :type name: string, (optional, never None)
    :param collection: Collection 
    :type collection: enum in [], (optional)
    :param view_align: Align to View, Align the new object to the view 
    :type view_align: boolean, (optional)
    :param location: Location, Location for the newly added object 
    :type location: float array of 3 items in [-inf, inf], (optional)
    :param rotation: Rotation, Rotation for the newly added object 
    :type rotation: float array of 3 items in [-inf, inf], (optional)
    '''

    pass


def collection_link(collection=''):
    '''Add an object to an existing collection 

    :param collection: Collection 
    :type collection: enum in [], (optional)
    '''

    pass


def collection_objects_select():
    '''Select all objects in collection 

    '''

    pass


def collection_remove():
    '''Remove the active object from this collection 

    '''

    pass


def collection_unlink():
    '''Unlink the collection from all objects 

    '''

    pass


def constraint_add(type=''):
    '''Add a constraint to the active object 

    :param type: TypeCAMERA_SOLVER Camera Solver.FOLLOW_TRACK Follow Track.OBJECT_SOLVER Object Solver.COPY_LOCATION Copy Location, Copy the location of a target (with an optional offset), so that they move together.COPY_ROTATION Copy Rotation, Copy the rotation of a target (with an optional offset), so that they rotate together.COPY_SCALE Copy Scale, Copy the scale factors of a target (with an optional offset), so that they are scaled by the same amount.COPY_TRANSFORMS Copy Transforms, Copy all the transformations of a target, so that they move together.LIMIT_DISTANCE Limit Distance, Restrict movements to within a certain distance of a target (at the time of constraint evaluation only).LIMIT_LOCATION Limit Location, Restrict movement along each axis within given ranges.LIMIT_ROTATION Limit Rotation, Restrict rotation along each axis within given ranges.LIMIT_SCALE Limit Scale, Restrict scaling along each axis with given ranges.MAINTAIN_VOLUME Maintain Volume, Compensate for scaling one axis by applying suitable scaling to the other two axes.TRANSFORM Transformation, Use one transform property from target to control another (or same) property on owner.TRANSFORM_CACHE Transform Cache, Look up the transformation matrix from an external file.CLAMP_TO Clamp To, Restrict movements to lie along a curve by remapping location along curve’s longest axis.DAMPED_TRACK Damped Track, Point towards a target by performing the smallest rotation necessary.IK Inverse Kinematics, Control a chain of bones by specifying the endpoint target (Bones only).LOCKED_TRACK Locked Track, Rotate around the specified (‘locked’) axis to point towards a target.SPLINE_IK Spline IK, Align chain of bones along a curve (Bones only).STRETCH_TO Stretch To, Stretch along Y-Axis to point towards a target.TRACK_TO Track To, Legacy tracking constraint prone to twisting artifacts.ACTION Action, Use transform property of target to look up pose for owner from an Action.CHILD_OF Child Of, Make target the ‘detachable’ parent of owner.FLOOR Floor, Use position (and optionally rotation) of target to define a ‘wall’ or ‘floor’ that the owner can not cross.FOLLOW_PATH Follow Path, Use to animate an object/bone following a path.PIVOT Pivot, Change pivot point for transforms (buggy).SHRINKWRAP Shrinkwrap, Restrict movements to surface of target mesh.ARMATURE Armature, Apply weight-blended transformation from multiple bones like the Armature modifier. 
    :type type: enum in ['CAMERA_SOLVER', 'FOLLOW_TRACK', 'OBJECT_SOLVER', 'COPY_LOCATION', 'COPY_ROTATION', 'COPY_SCALE', 'COPY_TRANSFORMS', 'LIMIT_DISTANCE', 'LIMIT_LOCATION', 'LIMIT_ROTATION', 'LIMIT_SCALE', 'MAINTAIN_VOLUME', 'TRANSFORM', 'TRANSFORM_CACHE', 'CLAMP_TO', 'DAMPED_TRACK', 'IK', 'LOCKED_TRACK', 'SPLINE_IK', 'STRETCH_TO', 'TRACK_TO', 'ACTION', 'CHILD_OF', 'FLOOR', 'FOLLOW_PATH', 'PIVOT', 'SHRINKWRAP', 'ARMATURE'], (optional)
    '''

    pass


def constraint_add_with_targets(type=''):
    '''Add a constraint to the active object, with target (where applicable) set to the selected Objects/Bones 

    :param type: TypeCAMERA_SOLVER Camera Solver.FOLLOW_TRACK Follow Track.OBJECT_SOLVER Object Solver.COPY_LOCATION Copy Location, Copy the location of a target (with an optional offset), so that they move together.COPY_ROTATION Copy Rotation, Copy the rotation of a target (with an optional offset), so that they rotate together.COPY_SCALE Copy Scale, Copy the scale factors of a target (with an optional offset), so that they are scaled by the same amount.COPY_TRANSFORMS Copy Transforms, Copy all the transformations of a target, so that they move together.LIMIT_DISTANCE Limit Distance, Restrict movements to within a certain distance of a target (at the time of constraint evaluation only).LIMIT_LOCATION Limit Location, Restrict movement along each axis within given ranges.LIMIT_ROTATION Limit Rotation, Restrict rotation along each axis within given ranges.LIMIT_SCALE Limit Scale, Restrict scaling along each axis with given ranges.MAINTAIN_VOLUME Maintain Volume, Compensate for scaling one axis by applying suitable scaling to the other two axes.TRANSFORM Transformation, Use one transform property from target to control another (or same) property on owner.TRANSFORM_CACHE Transform Cache, Look up the transformation matrix from an external file.CLAMP_TO Clamp To, Restrict movements to lie along a curve by remapping location along curve’s longest axis.DAMPED_TRACK Damped Track, Point towards a target by performing the smallest rotation necessary.IK Inverse Kinematics, Control a chain of bones by specifying the endpoint target (Bones only).LOCKED_TRACK Locked Track, Rotate around the specified (‘locked’) axis to point towards a target.SPLINE_IK Spline IK, Align chain of bones along a curve (Bones only).STRETCH_TO Stretch To, Stretch along Y-Axis to point towards a target.TRACK_TO Track To, Legacy tracking constraint prone to twisting artifacts.ACTION Action, Use transform property of target to look up pose for owner from an Action.CHILD_OF Child Of, Make target the ‘detachable’ parent of owner.FLOOR Floor, Use position (and optionally rotation) of target to define a ‘wall’ or ‘floor’ that the owner can not cross.FOLLOW_PATH Follow Path, Use to animate an object/bone following a path.PIVOT Pivot, Change pivot point for transforms (buggy).SHRINKWRAP Shrinkwrap, Restrict movements to surface of target mesh.ARMATURE Armature, Apply weight-blended transformation from multiple bones like the Armature modifier. 
    :type type: enum in ['CAMERA_SOLVER', 'FOLLOW_TRACK', 'OBJECT_SOLVER', 'COPY_LOCATION', 'COPY_ROTATION', 'COPY_SCALE', 'COPY_TRANSFORMS', 'LIMIT_DISTANCE', 'LIMIT_LOCATION', 'LIMIT_ROTATION', 'LIMIT_SCALE', 'MAINTAIN_VOLUME', 'TRANSFORM', 'TRANSFORM_CACHE', 'CLAMP_TO', 'DAMPED_TRACK', 'IK', 'LOCKED_TRACK', 'SPLINE_IK', 'STRETCH_TO', 'TRACK_TO', 'ACTION', 'CHILD_OF', 'FLOOR', 'FOLLOW_PATH', 'PIVOT', 'SHRINKWRAP', 'ARMATURE'], (optional)
    '''

    pass


def constraints_clear():
    '''Clear all the constraints for the active Object only 

    '''

    pass


def constraints_copy():
    '''Copy constraints to other selected objects 

    '''

    pass


def convert(target='MESH', keep_original=False):
    '''Convert selected objects to another type 

    :param target: Target, Type of object to convert to 
    :type target: enum in ['CURVE', 'MESH'], (optional)
    :param keep_original: Keep Original, Keep original objects instead of replacing them 
    :type keep_original: boolean, (optional)
    '''

    pass


def correctivesmooth_bind(modifier=""):
    '''Bind base pose in Corrective Smooth modifier 

    :param modifier: Modifier, Name of the modifier to edit 
    :type modifier: string, (optional, never None)
    '''

    pass


def data_transfer(use_reverse_transfer=False,
                  use_freeze=False,
                  data_type='',
                  use_create=True,
                  vert_mapping='NEAREST',
                  edge_mapping='NEAREST',
                  loop_mapping='NEAREST_POLYNOR',
                  poly_mapping='NEAREST',
                  use_auto_transform=False,
                  use_object_transform=True,
                  use_max_distance=False,
                  max_distance=1.0,
                  ray_radius=0.0,
                  islands_precision=0.1,
                  layers_select_src='ACTIVE',
                  layers_select_dst='ACTIVE',
                  mix_mode='REPLACE',
                  mix_factor=1.0):
    '''Transfer data layer(s) (weights, edge sharp, …) from active to selected meshes 

    :param use_reverse_transfer: Reverse Transfer, Transfer from selected objects to active one 
    :type use_reverse_transfer: boolean, (optional)
    :param use_freeze: Freeze Operator, Prevent changes to settings to re-run the operator, handy to change several things at once with heavy geometry 
    :type use_freeze: boolean, (optional)
    :param data_type: Data Type, Which data to transferVGROUP_WEIGHTS Vertex Group(s), Transfer active or all vertex groups.BEVEL_WEIGHT_VERT Bevel Weight, Transfer bevel weights.SHARP_EDGE Sharp, Transfer sharp mark.SEAM UV Seam, Transfer UV seam mark.CREASE Subsurf Crease, Transfer crease values.BEVEL_WEIGHT_EDGE Bevel Weight, Transfer bevel weights.FREESTYLE_EDGE Freestyle Mark, Transfer Freestyle edge mark.CUSTOM_NORMAL Custom Normals, Transfer custom normals.VCOL VCol, Vertex (face corners) colors.UV UVs, Transfer UV layers.SMOOTH Smooth, Transfer flat/smooth mark.FREESTYLE_FACE Freestyle Mark, Transfer Freestyle face mark. 
    :type data_type: enum in ['VGROUP_WEIGHTS', 'BEVEL_WEIGHT_VERT', 'SHARP_EDGE', 'SEAM', 'CREASE', 'BEVEL_WEIGHT_EDGE', 'FREESTYLE_EDGE', 'CUSTOM_NORMAL', 'VCOL', 'UV', 'SMOOTH', 'FREESTYLE_FACE'], (optional)
    :param use_create: Create Data, Add data layers on destination meshes if needed 
    :type use_create: boolean, (optional)
    :param vert_mapping: Vertex Mapping, Method used to map source vertices to destination onesTOPOLOGY Topology, Copy from identical topology meshes.NEAREST Nearest vertex, Copy from closest vertex.EDGE_NEAREST Nearest Edge Vertex, Copy from closest vertex of closest edge.EDGEINTERP_NEAREST Nearest Edge Interpolated, Copy from interpolated values of vertices from closest point on closest edge.POLY_NEAREST Nearest Face Vertex, Copy from closest vertex of closest face.POLYINTERP_NEAREST Nearest Face Interpolated, Copy from interpolated values of vertices from closest point on closest face.POLYINTERP_VNORPROJ Projected Face Interpolated, Copy from interpolated values of vertices from point on closest face hit by normal-projection. 
    :type vert_mapping: enum in ['TOPOLOGY', 'NEAREST', 'EDGE_NEAREST', 'EDGEINTERP_NEAREST', 'POLY_NEAREST', 'POLYINTERP_NEAREST', 'POLYINTERP_VNORPROJ'], (optional)
    :param edge_mapping: Edge Mapping, Method used to map source edges to destination onesTOPOLOGY Topology, Copy from identical topology meshes.VERT_NEAREST Nearest Vertices, Copy from most similar edge (edge which vertices are the closest of destination edge’s ones).NEAREST Nearest Edge, Copy from closest edge (using midpoints).POLY_NEAREST Nearest Face Edge, Copy from closest edge of closest face (using midpoints).EDGEINTERP_VNORPROJ Projected Edge Interpolated, Interpolate all source edges hit by the projection of destination one along its own normal (from vertices). 
    :type edge_mapping: enum in ['TOPOLOGY', 'VERT_NEAREST', 'NEAREST', 'POLY_NEAREST', 'EDGEINTERP_VNORPROJ'], (optional)
    :param loop_mapping: Face Corner Mapping, Method used to map source faces’ corners to destination onesTOPOLOGY Topology, Copy from identical topology meshes.NEAREST_NORMAL Nearest Corner And Best Matching Normal, Copy from nearest corner which has the best matching normal.NEAREST_POLYNOR Nearest Corner And Best Matching Face Normal, Copy from nearest corner which has the face with the best matching normal to destination corner’s face one.NEAREST_POLY Nearest Corner Of Nearest Face, Copy from nearest corner of nearest polygon.POLYINTERP_NEAREST Nearest Face Interpolated, Copy from interpolated corners of the nearest source polygon.POLYINTERP_LNORPROJ Projected Face Interpolated, Copy from interpolated corners of the source polygon hit by corner normal projection. 
    :type loop_mapping: enum in ['TOPOLOGY', 'NEAREST_NORMAL', 'NEAREST_POLYNOR', 'NEAREST_POLY', 'POLYINTERP_NEAREST', 'POLYINTERP_LNORPROJ'], (optional)
    :param poly_mapping: Face Mapping, Method used to map source faces to destination onesTOPOLOGY Topology, Copy from identical topology meshes.NEAREST Nearest Face, Copy from nearest polygon (using center points).NORMAL Best Normal-Matching, Copy from source polygon which normal is the closest to destination one.POLYINTERP_PNORPROJ Projected Face Interpolated, Interpolate all source polygons intersected by the projection of destination one along its own normal. 
    :type poly_mapping: enum in ['TOPOLOGY', 'NEAREST', 'NORMAL', 'POLYINTERP_PNORPROJ'], (optional)
    :param use_auto_transform: Auto Transform, Automatically compute transformation to get the best possible match between source and destination meshes (WARNING: results will never be as good as manual matching of objects) 
    :type use_auto_transform: boolean, (optional)
    :param use_object_transform: Object Transform, Evaluate source and destination meshes in global space 
    :type use_object_transform: boolean, (optional)
    :param use_max_distance: Only Neighbor Geometry, Source elements must be closer than given distance from destination one 
    :type use_max_distance: boolean, (optional)
    :param max_distance: Max Distance, Maximum allowed distance between source and destination element, for non-topology mappings 
    :type max_distance: float in [0, inf], (optional)
    :param ray_radius: Ray Radius, ‘Width’ of rays (especially useful when raycasting against vertices or edges) 
    :type ray_radius: float in [0, inf], (optional)
    :param islands_precision: Islands Precision, Factor controlling precision of islands handling (the higher, the better the results) 
    :type islands_precision: float in [0, 10], (optional)
    :param layers_select_src: Source Layers Selection, Which layers to transfer, in case of multi-layers typesACTIVE Active Layer, Only transfer active data layer.ALL All Layers, Transfer all data layers.BONE_SELECT Selected Pose Bones, Transfer all vertex groups used by selected pose bones.BONE_DEFORM Deform Pose Bones, Transfer all vertex groups used by deform bones. 
    :type layers_select_src: enum in ['ACTIVE', 'ALL', 'BONE_SELECT', 'BONE_DEFORM'], (optional)
    :param layers_select_dst: Destination Layers Matching, How to match source and destination layersACTIVE Active Layer, Affect active data layer of all targets.NAME By Name, Match target data layers to affect by name.INDEX By Order, Match target data layers to affect by order (indices). 
    :type layers_select_dst: enum in ['ACTIVE', 'NAME', 'INDEX'], (optional)
    :param mix_mode: Mix Mode, How to affect destination elements with source valuesREPLACE Replace, Overwrite all elements’ data.ABOVE_THRESHOLD Above Threshold, Only replace destination elements where data is above given threshold (exact behavior depends on data type).BELOW_THRESHOLD Below Threshold, Only replace destination elements where data is below given threshold (exact behavior depends on data type).MIX Mix, Mix source value into destination one, using given threshold as factor.ADD Add, Add source value to destination one, using given threshold as factor.SUB Subtract, Subtract source value to destination one, using given threshold as factor.MUL Multiply, Multiply source value to destination one, using given threshold as factor. 
    :type mix_mode: enum in ['REPLACE', 'ABOVE_THRESHOLD', 'BELOW_THRESHOLD', 'MIX', 'ADD', 'SUB', 'MUL'], (optional)
    :param mix_factor: Mix Factor, Factor to use when applying data to destination (exact behavior depends on mix mode) 
    :type mix_factor: float in [0, 1], (optional)
    '''

    pass


def datalayout_transfer(modifier="",
                        data_type='',
                        use_delete=False,
                        layers_select_src='ACTIVE',
                        layers_select_dst='ACTIVE'):
    '''Transfer layout of data layer(s) from active to selected meshes 

    :param modifier: Modifier, Name of the modifier to edit 
    :type modifier: string, (optional, never None)
    :param data_type: Data Type, Which data to transferVGROUP_WEIGHTS Vertex Group(s), Transfer active or all vertex groups.BEVEL_WEIGHT_VERT Bevel Weight, Transfer bevel weights.SHARP_EDGE Sharp, Transfer sharp mark.SEAM UV Seam, Transfer UV seam mark.CREASE Subsurf Crease, Transfer crease values.BEVEL_WEIGHT_EDGE Bevel Weight, Transfer bevel weights.FREESTYLE_EDGE Freestyle Mark, Transfer Freestyle edge mark.CUSTOM_NORMAL Custom Normals, Transfer custom normals.VCOL VCol, Vertex (face corners) colors.UV UVs, Transfer UV layers.SMOOTH Smooth, Transfer flat/smooth mark.FREESTYLE_FACE Freestyle Mark, Transfer Freestyle face mark. 
    :type data_type: enum in ['VGROUP_WEIGHTS', 'BEVEL_WEIGHT_VERT', 'SHARP_EDGE', 'SEAM', 'CREASE', 'BEVEL_WEIGHT_EDGE', 'FREESTYLE_EDGE', 'CUSTOM_NORMAL', 'VCOL', 'UV', 'SMOOTH', 'FREESTYLE_FACE'], (optional)
    :param use_delete: Exact Match, Also delete some data layers from destination if necessary, so that it matches exactly source 
    :type use_delete: boolean, (optional)
    :param layers_select_src: Source Layers Selection, Which layers to transfer, in case of multi-layers typesACTIVE Active Layer, Only transfer active data layer.ALL All Layers, Transfer all data layers.BONE_SELECT Selected Pose Bones, Transfer all vertex groups used by selected pose bones.BONE_DEFORM Deform Pose Bones, Transfer all vertex groups used by deform bones. 
    :type layers_select_src: enum in ['ACTIVE', 'ALL', 'BONE_SELECT', 'BONE_DEFORM'], (optional)
    :param layers_select_dst: Destination Layers Matching, How to match source and destination layersACTIVE Active Layer, Affect active data layer of all targets.NAME By Name, Match target data layers to affect by name.INDEX By Order, Match target data layers to affect by order (indices). 
    :type layers_select_dst: enum in ['ACTIVE', 'NAME', 'INDEX'], (optional)
    '''

    pass


def delete(use_global=False, confirm=True):
    '''Delete selected objects 

    :param use_global: Delete Globally, Remove object from all scenes 
    :type use_global: boolean, (optional)
    :param confirm: Confirm, Prompt for confirmation 
    :type confirm: boolean, (optional)
    '''

    pass


def drop_named_image(filepath="",
                     relative_path=True,
                     name="",
                     view_align=False,
                     location=(0.0, 0.0, 0.0),
                     rotation=(0.0, 0.0, 0.0)):
    '''Add an empty image type to scene with data 

    :param filepath: Filepath, Path to image file 
    :type filepath: string, (optional, never None)
    :param relative_path: Relative Path, Select the file relative to the blend file 
    :type relative_path: boolean, (optional)
    :param name: Name, Image name to assign 
    :type name: string, (optional, never None)
    :param view_align: Align to View, Align the new object to the view 
    :type view_align: boolean, (optional)
    :param location: Location, Location for the newly added object 
    :type location: float array of 3 items in [-inf, inf], (optional)
    :param rotation: Rotation, Rotation for the newly added object 
    :type rotation: float array of 3 items in [-inf, inf], (optional)
    '''

    pass


def drop_named_material(name="Material"):
    '''Undocumented contribute <https://developer.blender.org/T51061> 

    :param name: Name, Material name to assign 
    :type name: string, (optional, never None)
    '''

    pass


def duplicate(linked=False, mode='TRANSLATION'):
    '''Duplicate selected objects 

    :param linked: Linked, Duplicate object but not object data, linking to the original data 
    :type linked: boolean, (optional)
    :param mode: Mode 
    :type mode: enum in ['INIT', 'DUMMY', 'TRANSLATION', 'ROTATION', 'RESIZE', 'SKIN_RESIZE', 'TOSPHERE', 'SHEAR', 'BEND', 'SHRINKFATTEN', 'TILT', 'TRACKBALL', 'PUSHPULL', 'CREASE', 'MIRROR', 'BONE_SIZE', 'BONE_ENVELOPE', 'BONE_ENVELOPE_DIST', 'CURVE_SHRINKFATTEN', 'MASK_SHRINKFATTEN', 'GPENCIL_SHRINKFATTEN', 'BONE_ROLL', 'TIME_TRANSLATE', 'TIME_SLIDE', 'TIME_SCALE', 'TIME_EXTEND', 'BAKE_TIME', 'BWEIGHT', 'ALIGN', 'EDGESLIDE', 'SEQSLIDE'], (optional)
    '''

    pass


def duplicate_move(OBJECT_OT_duplicate=None, TRANSFORM_OT_translate=None):
    '''Duplicate selected objects and move them 

    :param OBJECT_OT_duplicate: Duplicate Objects, Duplicate selected objects 
    :type OBJECT_OT_duplicate: OBJECT_OT_duplicate, (optional)
    :param TRANSFORM_OT_translate: Move, Move selected items 
    :type TRANSFORM_OT_translate: TRANSFORM_OT_translate, (optional)
    '''

    pass


def duplicate_move_linked(OBJECT_OT_duplicate=None,
                          TRANSFORM_OT_translate=None):
    '''Duplicate selected objects and move them 

    :param OBJECT_OT_duplicate: Duplicate Objects, Duplicate selected objects 
    :type OBJECT_OT_duplicate: OBJECT_OT_duplicate, (optional)
    :param TRANSFORM_OT_translate: Move, Move selected items 
    :type TRANSFORM_OT_translate: TRANSFORM_OT_translate, (optional)
    '''

    pass


def duplicates_make_real(use_base_parent=False, use_hierarchy=False):
    '''Make dupli objects attached to this object real 

    :param use_base_parent: Parent, Parent newly created objects to the original duplicator 
    :type use_base_parent: boolean, (optional)
    :param use_hierarchy: Keep Hierarchy, Maintain parent child relationships 
    :type use_hierarchy: boolean, (optional)
    '''

    pass


def editmode_toggle():
    '''Toggle object’s editmode 

    '''

    pass


def effector_add(type='FORCE',
                 radius=1.0,
                 view_align=False,
                 enter_editmode=False,
                 location=(0.0, 0.0, 0.0),
                 rotation=(0.0, 0.0, 0.0)):
    '''Add an empty object with a physics effector to the scene 

    :param type: Type 
    :type type: enum in ['FORCE', 'WIND', 'VORTEX', 'MAGNET', 'HARMONIC', 'CHARGE', 'LENNARDJ', 'TEXTURE', 'GUIDE', 'BOID', 'TURBULENCE', 'DRAG', 'SMOKE'], (optional)
    :param radius: Radius 
    :type radius: float in [0, inf], (optional)
    :param view_align: Align to View, Align the new object to the view 
    :type view_align: boolean, (optional)
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object 
    :type enter_editmode: boolean, (optional)
    :param location: Location, Location for the newly added object 
    :type location: float array of 3 items in [-inf, inf], (optional)
    :param rotation: Rotation, Rotation for the newly added object 
    :type rotation: float array of 3 items in [-inf, inf], (optional)
    '''

    pass


def empty_add(type='PLAIN_AXES',
              radius=1.0,
              view_align=False,
              location=(0.0, 0.0, 0.0),
              rotation=(0.0, 0.0, 0.0)):
    '''Add an empty object to the scene 

    :param type: Type 
    :type type: enum in ['PLAIN_AXES', 'ARROWS', 'SINGLE_ARROW', 'CIRCLE', 'CUBE', 'SPHERE', 'CONE', 'IMAGE'], (optional)
    :param radius: Radius 
    :type radius: float in [0, inf], (optional)
    :param view_align: Align to View, Align the new object to the view 
    :type view_align: boolean, (optional)
    :param location: Location, Location for the newly added object 
    :type location: float array of 3 items in [-inf, inf], (optional)
    :param rotation: Rotation, Rotation for the newly added object 
    :type rotation: float array of 3 items in [-inf, inf], (optional)
    '''

    pass


def explode_refresh(modifier=""):
    '''Refresh data in the Explode modifier 

    :param modifier: Modifier, Name of the modifier to edit 
    :type modifier: string, (optional, never None)
    '''

    pass


def face_map_add():
    '''Add a new face map to the active object 

    '''

    pass


def face_map_assign():
    '''Assign faces to a face map 

    '''

    pass


def face_map_deselect():
    '''Deselect faces belonging to a face map 

    '''

    pass


def face_map_move(direction='UP'):
    '''Move the active face map up/down in the list 

    :param direction: Direction, Direction to move, UP or DOWN 
    :type direction: enum in ['UP', 'DOWN'], (optional)
    '''

    pass


def face_map_remove():
    '''Remove a face map from the active object 

    '''

    pass


def face_map_remove_from():
    '''Remove faces from a face map 

    '''

    pass


def face_map_select():
    '''Select faces belonging to a face map 

    '''

    pass


def forcefield_toggle():
    '''Toggle object’s force field 

    '''

    pass


def gpencil_add(radius=1.0,
                view_align=False,
                location=(0.0, 0.0, 0.0),
                rotation=(0.0, 0.0, 0.0),
                type='EMPTY'):
    '''Add a Grease Pencil object to the scene 

    :param radius: Radius 
    :type radius: float in [0, inf], (optional)
    :param view_align: Align to View, Align the new object to the view 
    :type view_align: boolean, (optional)
    :param location: Location, Location for the newly added object 
    :type location: float array of 3 items in [-inf, inf], (optional)
    :param rotation: Rotation, Rotation for the newly added object 
    :type rotation: float array of 3 items in [-inf, inf], (optional)
    :param type: TypeEMPTY Blank, Create an empty grease pencil object.STROKE Stroke, Create a simple stroke with basic colors.MONKEY Monkey, Construct a Suzanne grease pencil object. 
    :type type: enum in ['EMPTY', 'STROKE', 'MONKEY'], (optional)
    '''

    pass


def gpencil_modifier_add(type='CURVE'):
    '''Add a procedural operation/effect to the active grease pencil object 

    :param type: TypeDATA_TRANSFER Data Transfer.MESH_CACHE Mesh Cache.MESH_SEQUENCE_CACHE Mesh Sequence Cache.NORMAL_EDIT Normal Edit.WEIGHTED_NORMAL Weighted Normal.UV_PROJECT UV Project.UV_WARP UV Warp.VERTEX_WEIGHT_EDIT Vertex Weight Edit.VERTEX_WEIGHT_MIX Vertex Weight Mix.VERTEX_WEIGHT_PROXIMITY Vertex Weight Proximity.ARRAY Array.BEVEL Bevel.BOOLEAN Boolean.BUILD Build.DECIMATE Decimate.EDGE_SPLIT Edge Split.MASK Mask.MIRROR Mirror.MULTIRES Multiresolution.REMESH Remesh.SCREW Screw.SKIN Skin.SOLIDIFY Solidify.SUBSURF Subdivision Surface.TRIANGULATE Triangulate.WIREFRAME Wireframe, Generate a wireframe on the edges of a mesh.ARMATURE Armature.CAST Cast.CURVE Curve.DISPLACE Displace.HOOK Hook.LAPLACIANDEFORM Laplacian Deform.LATTICE Lattice.MESH_DEFORM Mesh Deform.SHRINKWRAP Shrinkwrap.SIMPLE_DEFORM Simple Deform.SMOOTH Smooth.CORRECTIVE_SMOOTH Smooth Corrective.LAPLACIANSMOOTH Smooth Laplacian.SURFACE_DEFORM Surface Deform.WARP Warp.WAVE Wave.CLOTH Cloth.COLLISION Collision.DYNAMIC_PAINT Dynamic Paint.EXPLODE Explode.FLUID_SIMULATION Fluid Simulation.OCEAN Ocean.PARTICLE_INSTANCE Particle Instance.PARTICLE_SYSTEM Particle System.SMOKE Smoke.SOFT_BODY Soft Body.SURFACE Surface. 
    :type type: enum in ['DATA_TRANSFER', 'MESH_CACHE', 'MESH_SEQUENCE_CACHE', 'NORMAL_EDIT', 'WEIGHTED_NORMAL', 'UV_PROJECT', 'UV_WARP', 'VERTEX_WEIGHT_EDIT', 'VERTEX_WEIGHT_MIX', 'VERTEX_WEIGHT_PROXIMITY', 'ARRAY', 'BEVEL', 'BOOLEAN', 'BUILD', 'DECIMATE', 'EDGE_SPLIT', 'MASK', 'MIRROR', 'MULTIRES', 'REMESH', 'SCREW', 'SKIN', 'SOLIDIFY', 'SUBSURF', 'TRIANGULATE', 'WIREFRAME', 'ARMATURE', 'CAST', 'CURVE', 'DISPLACE', 'HOOK', 'LAPLACIANDEFORM', 'LATTICE', 'MESH_DEFORM', 'SHRINKWRAP', 'SIMPLE_DEFORM', 'SMOOTH', 'CORRECTIVE_SMOOTH', 'LAPLACIANSMOOTH', 'SURFACE_DEFORM', 'WARP', 'WAVE', 'CLOTH', 'COLLISION', 'DYNAMIC_PAINT', 'EXPLODE', 'FLUID_SIMULATION', 'OCEAN', 'PARTICLE_INSTANCE', 'PARTICLE_SYSTEM', 'SMOKE', 'SOFT_BODY', 'SURFACE'], (optional)
    '''

    pass


def gpencil_modifier_apply(apply_as='DATA', modifier=""):
    '''Apply modifier and remove from the stack 

    :param apply_as: Apply as, How to apply the modifier to the geometryDATA Object Data, Apply modifier to the object’s data.SHAPE New Shape, Apply deform-only modifier to a new shape on this object. 
    :type apply_as: enum in ['DATA', 'SHAPE'], (optional)
    :param modifier: Modifier, Name of the modifier to edit 
    :type modifier: string, (optional, never None)
    '''

    pass


def gpencil_modifier_copy(modifier=""):
    '''Duplicate modifier at the same position in the stack 

    :param modifier: Modifier, Name of the modifier to edit 
    :type modifier: string, (optional, never None)
    '''

    pass


def gpencil_modifier_move_down(modifier=""):
    '''Move modifier down in the stack 

    :param modifier: Modifier, Name of the modifier to edit 
    :type modifier: string, (optional, never None)
    '''

    pass


def gpencil_modifier_move_up(modifier=""):
    '''Move modifier up in the stack 

    :param modifier: Modifier, Name of the modifier to edit 
    :type modifier: string, (optional, never None)
    '''

    pass


def gpencil_modifier_remove(modifier=""):
    '''Remove a modifier from the active grease pencil object 

    :param modifier: Modifier, Name of the modifier to edit 
    :type modifier: string, (optional, never None)
    '''

    pass


def hide_collection(collection_index=-1, toggle=False):
    '''Show only objects in collection (Shift to extend) 

    :param collection_index: Collection Index, Index of the collection to change visibility 
    :type collection_index: int in [-1, inf], (optional)
    :param toggle: Toggle, Toggle visibility 
    :type toggle: boolean, (optional)
    '''

    pass


def hide_render_clear_all():
    '''Reveal all render objects by setting the hide render flag 

    '''

    pass


def hide_view_clear(select=True):
    '''Reveal temporarily hidden objects 

    :param select: Select 
    :type select: boolean, (optional)
    '''

    pass


def hide_view_set(unselected=False):
    '''Temporarily hide objects from the viewport 

    :param unselected: Unselected, Hide unselected rather than selected objects 
    :type unselected: boolean, (optional)
    '''

    pass


def hook_add_newob():
    '''Hook selected vertices to a newly created object 

    '''

    pass


def hook_add_selob(use_bone=False):
    '''Hook selected vertices to the first selected object 

    :param use_bone: Active Bone, Assign the hook to the hook objects active bone 
    :type use_bone: boolean, (optional)
    '''

    pass


def hook_assign(modifier=''):
    '''Assign the selected vertices to a hook 

    :param modifier: Modifier, Modifier number to assign to 
    :type modifier: enum in [], (optional)
    '''

    pass


def hook_recenter(modifier=''):
    '''Set hook center to cursor position 

    :param modifier: Modifier, Modifier number to assign to 
    :type modifier: enum in [], (optional)
    '''

    pass


def hook_remove(modifier=''):
    '''Remove a hook from the active object 

    :param modifier: Modifier, Modifier number to remove 
    :type modifier: enum in [], (optional)
    '''

    pass


def hook_reset(modifier=''):
    '''Recalculate and clear offset transformation 

    :param modifier: Modifier, Modifier number to assign to 
    :type modifier: enum in [], (optional)
    '''

    pass


def hook_select(modifier=''):
    '''Select affected vertices on mesh 

    :param modifier: Modifier, Modifier number to remove 
    :type modifier: enum in [], (optional)
    '''

    pass


def instance_offset_from_cursor():
    '''Set offset used for collection instances based on cursor position 

    '''

    pass


def isolate_type_render():
    '''Hide unselected render objects of same type as active by setting the hide render flag 

    '''

    pass


def join():
    '''Join selected objects into active object 

    '''

    pass


def join_shapes():
    '''Merge selected objects to shapes of active object 

    '''

    pass


def join_uvs():
    '''Transfer UV Maps from active to selected objects (needs matching geometry) 

    '''

    pass


def laplaciandeform_bind(modifier=""):
    '''Bind mesh to system in laplacian deform modifier 

    :param modifier: Modifier, Name of the modifier to edit 
    :type modifier: string, (optional, never None)
    '''

    pass


def light_add(type='POINT',
              radius=1.0,
              view_align=False,
              location=(0.0, 0.0, 0.0),
              rotation=(0.0, 0.0, 0.0)):
    '''Add a light object to the scene 

    :param type: TypePOINT Point, Omnidirectional point light source.SUN Sun, Constant direction parallel ray light source.SPOT Spot, Directional cone light source.AREA Area, Directional area light source. 
    :type type: enum in ['POINT', 'SUN', 'SPOT', 'AREA'], (optional)
    :param radius: Radius 
    :type radius: float in [0, inf], (optional)
    :param view_align: Align to View, Align the new object to the view 
    :type view_align: boolean, (optional)
    :param location: Location, Location for the newly added object 
    :type location: float array of 3 items in [-inf, inf], (optional)
    :param rotation: Rotation, Rotation for the newly added object 
    :type rotation: float array of 3 items in [-inf, inf], (optional)
    '''

    pass


def lightprobe_add(type='CUBEMAP',
                   radius=1.0,
                   view_align=False,
                   enter_editmode=False,
                   location=(0.0, 0.0, 0.0),
                   rotation=(0.0, 0.0, 0.0)):
    '''Add a light probe object 

    :param type: TypeCUBEMAP Reflection Cubemap, Reflection probe with spherical or cubic attenuation.PLANAR Reflection Plane, Planar reflection probe.GRID Irradiance Volume, Irradiance probe to capture diffuse indirect lighting. 
    :type type: enum in ['CUBEMAP', 'PLANAR', 'GRID'], (optional)
    :param radius: Radius 
    :type radius: float in [0, inf], (optional)
    :param view_align: Align to View, Align the new object to the view 
    :type view_align: boolean, (optional)
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object 
    :type enter_editmode: boolean, (optional)
    :param location: Location, Location for the newly added object 
    :type location: float array of 3 items in [-inf, inf], (optional)
    :param rotation: Rotation, Rotation for the newly added object 
    :type rotation: float array of 3 items in [-inf, inf], (optional)
    '''

    pass


def link_to_collection(collection_index=-1,
                       is_new=False,
                       new_collection_name=""):
    '''Link objects to a collection 

    :param collection_index: Collection Index, Index of the collection to move to 
    :type collection_index: int in [-1, inf], (optional)
    :param is_new: New, Move objects to a new collection 
    :type is_new: boolean, (optional)
    :param new_collection_name: Name, Name of the newly added collection 
    :type new_collection_name: string, (optional, never None)
    '''

    pass


def load_background_image(filepath="",
                          filter_image=True,
                          filter_folder=True,
                          view_align=True):
    '''Add a reference image into the background behind objects 

    :param filepath: filepath 
    :type filepath: string, (optional, never None)
    :param filter_image: filter_image 
    :type filter_image: boolean, (optional)
    :param filter_folder: filter_folder 
    :type filter_folder: boolean, (optional)
    :param view_align: Align to view 
    :type view_align: boolean, (optional)
    '''

    pass


def load_reference_image(filepath="",
                         filter_image=True,
                         filter_folder=True,
                         view_align=True):
    '''Add a reference image into the scene between objects 

    :param filepath: filepath 
    :type filepath: string, (optional, never None)
    :param filter_image: filter_image 
    :type filter_image: boolean, (optional)
    :param filter_folder: filter_folder 
    :type filter_folder: boolean, (optional)
    :param view_align: Align to view 
    :type view_align: boolean, (optional)
    '''

    pass


def location_clear(clear_delta=False):
    '''Clear the object’s location 

    :param clear_delta: Clear Delta, Clear delta location in addition to clearing the normal location transform 
    :type clear_delta: boolean, (optional)
    '''

    pass


def make_dupli_face():
    '''Convert objects into dupli-face instanced 

    '''

    pass


def make_links_data(type='OBDATA'):
    '''Apply active object links to other selected objects 

    :param type: Type 
    :type type: enum in ['OBDATA', 'MATERIAL', 'ANIMATION', 'GROUPS', 'DUPLICOLLECTION', 'MODIFIERS', 'FONTS'], (optional)
    '''

    pass


def make_links_scene(scene=''):
    '''Link selection to another scene 

    :param scene: Scene 
    :type scene: enum in [], (optional)
    '''

    pass


def make_local(type='SELECT_OBJECT'):
    '''Make library linked data-blocks local to this file 

    :param type: Type 
    :type type: enum in ['SELECT_OBJECT', 'SELECT_OBDATA', 'SELECT_OBDATA_MATERIAL', 'ALL'], (optional)
    '''

    pass


def make_override_static(object='DEFAULT'):
    '''Make local override of this library linked data-block 

    :param object: Override Object, Name of lib-linked/collection object to make an override from 
    :type object: enum in ['DEFAULT'], (optional)
    '''

    pass


def make_single_user(type='SELECTED_OBJECTS',
                     object=False,
                     obdata=False,
                     material=False,
                     animation=False):
    '''Make linked data local to each object 

    :param type: Type 
    :type type: enum in ['SELECTED_OBJECTS', 'ALL'], (optional)
    :param object: Object, Make single user objects 
    :type object: boolean, (optional)
    :param obdata: Object Data, Make single user object data 
    :type obdata: boolean, (optional)
    :param material: Materials, Make materials local to each data-block 
    :type material: boolean, (optional)
    :param animation: Object Animation, Make animation data local to each object 
    :type animation: boolean, (optional)
    '''

    pass


def material_slot_add():
    '''Add a new material slot 

    '''

    pass


def material_slot_assign():
    '''Assign active material slot to selection 

    '''

    pass


def material_slot_copy():
    '''Copy material to selected objects 

    '''

    pass


def material_slot_deselect():
    '''Deselect by active material slot 

    '''

    pass


def material_slot_move(direction='UP'):
    '''Move the active material up/down in the list 

    :param direction: Direction, Direction to move the active material towards 
    :type direction: enum in ['UP', 'DOWN'], (optional)
    '''

    pass


def material_slot_remove():
    '''Remove the selected material slot 

    '''

    pass


def material_slot_select():
    '''Select by active material slot 

    '''

    pass


def meshdeform_bind(modifier=""):
    '''Bind mesh to cage in mesh deform modifier 

    :param modifier: Modifier, Name of the modifier to edit 
    :type modifier: string, (optional, never None)
    '''

    pass


def metaball_add(type='BALL',
                 radius=1.0,
                 view_align=False,
                 enter_editmode=False,
                 location=(0.0, 0.0, 0.0),
                 rotation=(0.0, 0.0, 0.0)):
    '''Add an metaball object to the scene 

    :param type: Primitive 
    :type type: enum in ['BALL', 'CAPSULE', 'PLANE', 'ELLIPSOID', 'CUBE'], (optional)
    :param radius: Radius 
    :type radius: float in [0, inf], (optional)
    :param view_align: Align to View, Align the new object to the view 
    :type view_align: boolean, (optional)
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object 
    :type enter_editmode: boolean, (optional)
    :param location: Location, Location for the newly added object 
    :type location: float array of 3 items in [-inf, inf], (optional)
    :param rotation: Rotation, Rotation for the newly added object 
    :type rotation: float array of 3 items in [-inf, inf], (optional)
    '''

    pass


def mode_set(mode='OBJECT', toggle=False):
    '''Sets the object interaction mode 

    :param mode: ModeOBJECT Object Mode.EDIT Edit Mode.POSE Pose Mode.SCULPT Sculpt Mode.VERTEX_PAINT Vertex Paint.WEIGHT_PAINT Weight Paint.TEXTURE_PAINT Texture Paint.PARTICLE_EDIT Particle Edit.EDIT_GPENCIL Edit Mode, Edit Grease Pencil Strokes.SCULPT_GPENCIL Sculpt Mode, Sculpt Grease Pencil Strokes.PAINT_GPENCIL Draw, Paint Grease Pencil Strokes.WEIGHT_GPENCIL Weight Paint, Grease Pencil Weight Paint Strokes. 
    :type mode: enum in ['OBJECT', 'EDIT', 'POSE', 'SCULPT', 'VERTEX_PAINT', 'WEIGHT_PAINT', 'TEXTURE_PAINT', 'PARTICLE_EDIT', 'EDIT_GPENCIL', 'SCULPT_GPENCIL', 'PAINT_GPENCIL', 'WEIGHT_GPENCIL'], (optional)
    :param toggle: Toggle 
    :type toggle: boolean, (optional)
    '''

    pass


def mode_set_or_submode(mode='OBJECT', toggle=False):
    '''Sets the object interaction mode 

    :param mode: ModeOBJECT Object Mode.EDIT Edit Mode.POSE Pose Mode.SCULPT Sculpt Mode.VERTEX_PAINT Vertex Paint.WEIGHT_PAINT Weight Paint.TEXTURE_PAINT Texture Paint.PARTICLE_EDIT Particle Edit.EDIT_GPENCIL Edit Mode, Edit Grease Pencil Strokes.SCULPT_GPENCIL Sculpt Mode, Sculpt Grease Pencil Strokes.PAINT_GPENCIL Draw, Paint Grease Pencil Strokes.WEIGHT_GPENCIL Weight Paint, Grease Pencil Weight Paint Strokes. 
    :type mode: enum in ['OBJECT', 'EDIT', 'POSE', 'SCULPT', 'VERTEX_PAINT', 'WEIGHT_PAINT', 'TEXTURE_PAINT', 'PARTICLE_EDIT', 'EDIT_GPENCIL', 'SCULPT_GPENCIL', 'PAINT_GPENCIL', 'WEIGHT_GPENCIL'], (optional)
    :param toggle: Toggle 
    :type toggle: boolean, (optional)
    '''

    pass


def modifier_add(type='SUBSURF'):
    '''Add a procedural operation/effect to the active object 

    :param type: TypeDATA_TRANSFER Data Transfer.MESH_CACHE Mesh Cache.MESH_SEQUENCE_CACHE Mesh Sequence Cache.NORMAL_EDIT Normal Edit.WEIGHTED_NORMAL Weighted Normal.UV_PROJECT UV Project.UV_WARP UV Warp.VERTEX_WEIGHT_EDIT Vertex Weight Edit.VERTEX_WEIGHT_MIX Vertex Weight Mix.VERTEX_WEIGHT_PROXIMITY Vertex Weight Proximity.ARRAY Array.BEVEL Bevel.BOOLEAN Boolean.BUILD Build.DECIMATE Decimate.EDGE_SPLIT Edge Split.MASK Mask.MIRROR Mirror.MULTIRES Multiresolution.REMESH Remesh.SCREW Screw.SKIN Skin.SOLIDIFY Solidify.SUBSURF Subdivision Surface.TRIANGULATE Triangulate.WIREFRAME Wireframe, Generate a wireframe on the edges of a mesh.ARMATURE Armature.CAST Cast.CURVE Curve.DISPLACE Displace.HOOK Hook.LAPLACIANDEFORM Laplacian Deform.LATTICE Lattice.MESH_DEFORM Mesh Deform.SHRINKWRAP Shrinkwrap.SIMPLE_DEFORM Simple Deform.SMOOTH Smooth.CORRECTIVE_SMOOTH Smooth Corrective.LAPLACIANSMOOTH Smooth Laplacian.SURFACE_DEFORM Surface Deform.WARP Warp.WAVE Wave.CLOTH Cloth.COLLISION Collision.DYNAMIC_PAINT Dynamic Paint.EXPLODE Explode.FLUID_SIMULATION Fluid Simulation.OCEAN Ocean.PARTICLE_INSTANCE Particle Instance.PARTICLE_SYSTEM Particle System.SMOKE Smoke.SOFT_BODY Soft Body.SURFACE Surface. 
    :type type: enum in ['DATA_TRANSFER', 'MESH_CACHE', 'MESH_SEQUENCE_CACHE', 'NORMAL_EDIT', 'WEIGHTED_NORMAL', 'UV_PROJECT', 'UV_WARP', 'VERTEX_WEIGHT_EDIT', 'VERTEX_WEIGHT_MIX', 'VERTEX_WEIGHT_PROXIMITY', 'ARRAY', 'BEVEL', 'BOOLEAN', 'BUILD', 'DECIMATE', 'EDGE_SPLIT', 'MASK', 'MIRROR', 'MULTIRES', 'REMESH', 'SCREW', 'SKIN', 'SOLIDIFY', 'SUBSURF', 'TRIANGULATE', 'WIREFRAME', 'ARMATURE', 'CAST', 'CURVE', 'DISPLACE', 'HOOK', 'LAPLACIANDEFORM', 'LATTICE', 'MESH_DEFORM', 'SHRINKWRAP', 'SIMPLE_DEFORM', 'SMOOTH', 'CORRECTIVE_SMOOTH', 'LAPLACIANSMOOTH', 'SURFACE_DEFORM', 'WARP', 'WAVE', 'CLOTH', 'COLLISION', 'DYNAMIC_PAINT', 'EXPLODE', 'FLUID_SIMULATION', 'OCEAN', 'PARTICLE_INSTANCE', 'PARTICLE_SYSTEM', 'SMOKE', 'SOFT_BODY', 'SURFACE'], (optional)
    '''

    pass


def modifier_apply(apply_as='DATA', modifier=""):
    '''Apply modifier and remove from the stack 

    :param apply_as: Apply as, How to apply the modifier to the geometryDATA Object Data, Apply modifier to the object’s data.SHAPE New Shape, Apply deform-only modifier to a new shape on this object. 
    :type apply_as: enum in ['DATA', 'SHAPE'], (optional)
    :param modifier: Modifier, Name of the modifier to edit 
    :type modifier: string, (optional, never None)
    '''

    pass


def modifier_convert(modifier=""):
    '''Convert particles to a mesh object 

    :param modifier: Modifier, Name of the modifier to edit 
    :type modifier: string, (optional, never None)
    '''

    pass


def modifier_copy(modifier=""):
    '''Duplicate modifier at the same position in the stack 

    :param modifier: Modifier, Name of the modifier to edit 
    :type modifier: string, (optional, never None)
    '''

    pass


def modifier_move_down(modifier=""):
    '''Move modifier down in the stack 

    :param modifier: Modifier, Name of the modifier to edit 
    :type modifier: string, (optional, never None)
    '''

    pass


def modifier_move_up(modifier=""):
    '''Move modifier up in the stack 

    :param modifier: Modifier, Name of the modifier to edit 
    :type modifier: string, (optional, never None)
    '''

    pass


def modifier_remove(modifier=""):
    '''Remove a modifier from the active object 

    :param modifier: Modifier, Name of the modifier to edit 
    :type modifier: string, (optional, never None)
    '''

    pass


def move_to_collection(collection_index=-1,
                       is_new=False,
                       new_collection_name=""):
    '''Move objects to a scene collection 

    :param collection_index: Collection Index, Index of the collection to move to 
    :type collection_index: int in [-1, inf], (optional)
    :param is_new: New, Move objects to a new collection 
    :type is_new: boolean, (optional)
    :param new_collection_name: Name, Name of the newly added collection 
    :type new_collection_name: string, (optional, never None)
    '''

    pass


def multires_base_apply(modifier=""):
    '''Modify the base mesh to conform to the displaced mesh 

    :param modifier: Modifier, Name of the modifier to edit 
    :type modifier: string, (optional, never None)
    '''

    pass


def multires_external_pack():
    '''Pack displacements from an external file 

    '''

    pass


def multires_external_save(filepath="",
                           check_existing=True,
                           filter_blender=False,
                           filter_backup=False,
                           filter_image=False,
                           filter_movie=False,
                           filter_python=False,
                           filter_font=False,
                           filter_sound=False,
                           filter_text=False,
                           filter_btx=True,
                           filter_collada=False,
                           filter_alembic=False,
                           filter_folder=True,
                           filter_blenlib=False,
                           filemode=9,
                           relative_path=True,
                           display_type='DEFAULT',
                           sort_method='FILE_SORT_ALPHA',
                           modifier=""):
    '''Save displacements to an external file 

    :param filepath: File Path, Path to file 
    :type filepath: string, (optional, never None)
    :param check_existing: Check Existing, Check and warn on overwriting existing files 
    :type check_existing: boolean, (optional)
    :param filter_blender: Filter .blend files 
    :type filter_blender: boolean, (optional)
    :param filter_backup: Filter .blend files 
    :type filter_backup: boolean, (optional)
    :param filter_image: Filter image files 
    :type filter_image: boolean, (optional)
    :param filter_movie: Filter movie files 
    :type filter_movie: boolean, (optional)
    :param filter_python: Filter python files 
    :type filter_python: boolean, (optional)
    :param filter_font: Filter font files 
    :type filter_font: boolean, (optional)
    :param filter_sound: Filter sound files 
    :type filter_sound: boolean, (optional)
    :param filter_text: Filter text files 
    :type filter_text: boolean, (optional)
    :param filter_btx: Filter btx files 
    :type filter_btx: boolean, (optional)
    :param filter_collada: Filter COLLADA files 
    :type filter_collada: boolean, (optional)
    :param filter_alembic: Filter Alembic files 
    :type filter_alembic: boolean, (optional)
    :param filter_folder: Filter folders 
    :type filter_folder: boolean, (optional)
    :param filter_blenlib: Filter Blender IDs 
    :type filter_blenlib: boolean, (optional)
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file 
    :type filemode: int in [1, 9], (optional)
    :param relative_path: Relative Path, Select the file relative to the blend file 
    :type relative_path: boolean, (optional)
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_SHORT Short List, Display files as short list.LIST_LONG Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: enum in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
    :param sort_method: File sorting modeFILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.FILE_SORT_TIME Sort by time, Sort files by modification time.FILE_SORT_SIZE Sort by size, Sort files by size. 
    :type sort_method: enum in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
    :param modifier: Modifier, Name of the modifier to edit 
    :type modifier: string, (optional, never None)
    '''

    pass


def multires_higher_levels_delete(modifier=""):
    '''Deletes the higher resolution mesh, potential loss of detail 

    :param modifier: Modifier, Name of the modifier to edit 
    :type modifier: string, (optional, never None)
    '''

    pass


def multires_reshape(modifier=""):
    '''Copy vertex coordinates from other object 

    :param modifier: Modifier, Name of the modifier to edit 
    :type modifier: string, (optional, never None)
    '''

    pass


def multires_subdivide(modifier=""):
    '''Add a new level of subdivision 

    :param modifier: Modifier, Name of the modifier to edit 
    :type modifier: string, (optional, never None)
    '''

    pass


def ocean_bake(modifier="", free=False):
    '''Bake an image sequence of ocean data 

    :param modifier: Modifier, Name of the modifier to edit 
    :type modifier: string, (optional, never None)
    :param free: Free, Free the bake, rather than generating it 
    :type free: boolean, (optional)
    '''

    pass


def origin_clear():
    '''Clear the object’s origin 

    '''

    pass


def origin_set(type='GEOMETRY_ORIGIN', center='MEDIAN'):
    '''Set the object’s origin, by either moving the data, or set to center of data, or use 3D cursor 

    :param type: TypeGEOMETRY_ORIGIN Geometry to Origin, Move object geometry to object origin.ORIGIN_GEOMETRY Origin to Geometry, Calculate the center of geometry based on the current pivot point (median, otherwise bounding-box).ORIGIN_CURSOR Origin to 3D Cursor, Move object origin to position of the 3D cursor.ORIGIN_CENTER_OF_MASS Origin to Center of Mass (Surface), Calculate the center of mass from the surface area.ORIGIN_CENTER_OF_VOLUME Origin to Center of Mass (Volume), Calculate the center of mass from the volume (must be manifold geometry with consistent normals). 
    :type type: enum in ['GEOMETRY_ORIGIN', 'ORIGIN_GEOMETRY', 'ORIGIN_CURSOR', 'ORIGIN_CENTER_OF_MASS', 'ORIGIN_CENTER_OF_VOLUME'], (optional)
    :param center: Center 
    :type center: enum in ['MEDIAN', 'BOUNDS'], (optional)
    '''

    pass


def parent_clear(type='CLEAR'):
    '''Clear the object’s parenting 

    :param type: TypeCLEAR Clear Parent, Completely clear the parenting relationship, including involved modifiers if any.CLEAR_KEEP_TRANSFORM Clear and Keep Transformation, As ‘Clear Parent’, but keep the current visual transformations of the object.CLEAR_INVERSE Clear Parent Inverse, Reset the transform corrections applied to the parenting relationship, does not remove parenting itself. 
    :type type: enum in ['CLEAR', 'CLEAR_KEEP_TRANSFORM', 'CLEAR_INVERSE'], (optional)
    '''

    pass


def parent_no_inverse_set():
    '''Set the object’s parenting without setting the inverse parent correction 

    '''

    pass


def parent_set(type='OBJECT', xmirror=False, keep_transform=False):
    '''Set the object’s parenting 

    :param type: Type 
    :type type: enum in ['OBJECT', 'ARMATURE', 'ARMATURE_NAME', 'ARMATURE_AUTO', 'ARMATURE_ENVELOPE', 'BONE', 'BONE_RELATIVE', 'CURVE', 'FOLLOW', 'PATH_CONST', 'LATTICE', 'VERTEX', 'VERTEX_TRI'], (optional)
    :param xmirror: X Mirror, Apply weights symmetrically along X axis, for Envelope/Automatic vertex groups creation 
    :type xmirror: boolean, (optional)
    :param keep_transform: Keep Transform, Apply transformation before parenting 
    :type keep_transform: boolean, (optional)
    '''

    pass


def particle_system_add():
    '''Add a particle system 

    '''

    pass


def particle_system_remove():
    '''Remove the selected particle system 

    '''

    pass


def paths_calculate(start_frame=1, end_frame=250):
    '''Calculate motion paths for the selected objects 

    :param start_frame: Start, First frame to calculate object paths on 
    :type start_frame: int in [-1048574, 1048574], (optional)
    :param end_frame: End, Last frame to calculate object paths on 
    :type end_frame: int in [-1048574, 1048574], (optional)
    '''

    pass


def paths_clear(only_selected=False):
    '''Clear path caches for all objects, hold Shift key for selected objects only 

    :param only_selected: Only Selected, Only clear paths from selected objects 
    :type only_selected: boolean, (optional)
    '''

    pass


def paths_range_update():
    '''Update frame range for motion paths from the Scene’s current frame range 

    '''

    pass


def paths_update():
    '''Recalculate paths for selected objects 

    '''

    pass


def posemode_toggle():
    '''Enable or disable posing/selecting bones 

    '''

    pass


def proxy_make(object='DEFAULT'):
    '''Add empty object to become local replacement data of a library-linked object 

    :param object: Proxy Object, Name of lib-linked/collection object to make a proxy for 
    :type object: enum in ['DEFAULT'], (optional)
    '''

    pass


def quick_explode(style='EXPLODE',
                  amount=100,
                  frame_duration=50,
                  frame_start=1,
                  frame_end=10,
                  velocity=1.0,
                  fade=True):
    '''Undocumented contribute <https://developer.blender.org/T51061> 

    :param style: Explode Style 
    :type style: enum in ['EXPLODE', 'BLEND'], (optional)
    :param amount: Amount of pieces 
    :type amount: int in [2, 10000], (optional)
    :param frame_duration: Duration 
    :type frame_duration: int in [1, 300000], (optional)
    :param frame_start: Start Frame 
    :type frame_start: int in [1, 300000], (optional)
    :param frame_end: End Frame 
    :type frame_end: int in [1, 300000], (optional)
    :param velocity: Outwards Velocity 
    :type velocity: float in [0, 300000], (optional)
    :param fade: Fade, Fade the pieces over time 
    :type fade: boolean, (optional)
    '''

    pass


def quick_fluid(style='BASIC',
                initial_velocity=(0.0, 0.0, 0.0),
                show_flows=False,
                start_baking=False):
    '''Undocumented contribute <https://developer.blender.org/T51061> 

    :param style: Fluid Style 
    :type style: enum in ['INFLOW', 'BASIC'], (optional)
    :param initial_velocity: Initial Velocity, Initial velocity of the fluid 
    :type initial_velocity: float array of 3 items in [-100, 100], (optional)
    :param show_flows: Render Fluid Objects, Keep the fluid objects visible during rendering 
    :type show_flows: boolean, (optional)
    :param start_baking: Start Fluid Bake, Start baking the fluid immediately after creating the domain object 
    :type start_baking: boolean, (optional)
    '''

    pass


def quick_fur(density='MEDIUM', view_percentage=10, length=0.1):
    '''Undocumented contribute <https://developer.blender.org/T51061> 

    :param density: Fur Density 
    :type density: enum in ['LIGHT', 'MEDIUM', 'HEAVY'], (optional)
    :param view_percentage: View % 
    :type view_percentage: int in [1, 100], (optional)
    :param length: Length 
    :type length: float in [0.001, 100], (optional)
    '''

    pass


def quick_smoke(style='SMOKE', show_flows=False):
    '''Undocumented contribute <https://developer.blender.org/T51061> 

    :param style: Smoke Style 
    :type style: enum in ['SMOKE', 'FIRE', 'BOTH'], (optional)
    :param show_flows: Render Smoke Objects, Keep the smoke objects visible during rendering 
    :type show_flows: boolean, (optional)
    '''

    pass


def randomize_transform(random_seed=0,
                        use_delta=False,
                        use_loc=True,
                        loc=(0.0, 0.0, 0.0),
                        use_rot=True,
                        rot=(0.0, 0.0, 0.0),
                        use_scale=True,
                        scale_even=False,
                        scale=(1.0, 1.0, 1.0)):
    '''Randomize objects loc/rot/scale 

    :param random_seed: Random Seed, Seed value for the random generator 
    :type random_seed: int in [0, 10000], (optional)
    :param use_delta: Transform Delta, Randomize delta transform values instead of regular transform 
    :type use_delta: boolean, (optional)
    :param use_loc: Randomize Location, Randomize the location values 
    :type use_loc: boolean, (optional)
    :param loc: Location, Maximum distance the objects can spread over each axis 
    :type loc: float array of 3 items in [-100, 100], (optional)
    :param use_rot: Randomize Rotation, Randomize the rotation values 
    :type use_rot: boolean, (optional)
    :param rot: Rotation, Maximum rotation over each axis 
    :type rot: float array of 3 items in [-3.14159, 3.14159], (optional)
    :param use_scale: Randomize Scale, Randomize the scale values 
    :type use_scale: boolean, (optional)
    :param scale_even: Scale Even, Use the same scale value for all axis 
    :type scale_even: boolean, (optional)
    :param scale: Scale, Maximum scale randomization over each axis 
    :type scale: float array of 3 items in [-100, 100], (optional)
    '''

    pass


def rotation_clear(clear_delta=False):
    '''Clear the object’s rotation 

    :param clear_delta: Clear Delta, Clear delta rotation in addition to clearing the normal rotation transform 
    :type clear_delta: boolean, (optional)
    '''

    pass


def scale_clear(clear_delta=False):
    '''Clear the object’s scale 

    :param clear_delta: Clear Delta, Clear delta scale in addition to clearing the normal scale transform 
    :type clear_delta: boolean, (optional)
    '''

    pass


def select_all(action='TOGGLE'):
    '''Change selection of all visible objects in scene 

    :param action: Action, Selection action to executeTOGGLE Toggle, Toggle selection for all elements.SELECT Select, Select all elements.DESELECT Deselect, Deselect all elements.INVERT Invert, Invert selection of all elements. 
    :type action: enum in ['TOGGLE', 'SELECT', 'DESELECT', 'INVERT'], (optional)
    '''

    pass


def select_by_type(extend=False, type='MESH'):
    '''Select all visible objects that are of a type 

    :param extend: Extend, Extend selection instead of deselecting everything first 
    :type extend: boolean, (optional)
    :param type: Type 
    :type type: enum in ['MESH', 'CURVE', 'SURFACE', 'META', 'FONT', 'ARMATURE', 'LATTICE', 'EMPTY', 'GPENCIL', 'CAMERA', 'LIGHT', 'SPEAKER', 'LIGHT_PROBE'], (optional)
    '''

    pass


def select_camera(extend=False):
    '''Select the active camera 

    :param extend: Extend, Extend the selection 
    :type extend: boolean, (optional)
    '''

    pass


def select_grouped(extend=False, type='CHILDREN_RECURSIVE'):
    '''Select all visible objects grouped by various properties 

    :param extend: Extend, Extend selection instead of deselecting everything first 
    :type extend: boolean, (optional)
    :param type: TypeCHILDREN_RECURSIVE Children.CHILDREN Immediate Children.PARENT Parent.SIBLINGS Siblings, Shared Parent.TYPE Type, Shared object type.COLLECTION Collection, Shared collection.HOOK Hook.PASS Pass, Render pass Index.COLOR Color, Object Color.KEYINGSET Keying Set, Objects included in active Keying Set.LIGHT_TYPE Light Type, Matching light types. 
    :type type: enum in ['CHILDREN_RECURSIVE', 'CHILDREN', 'PARENT', 'SIBLINGS', 'TYPE', 'COLLECTION', 'HOOK', 'PASS', 'COLOR', 'KEYINGSET', 'LIGHT_TYPE'], (optional)
    '''

    pass


def select_hierarchy(direction='PARENT', extend=False):
    '''Select object relative to the active object’s position in the hierarchy 

    :param direction: Direction, Direction to select in the hierarchy 
    :type direction: enum in ['PARENT', 'CHILD'], (optional)
    :param extend: Extend, Extend the existing selection 
    :type extend: boolean, (optional)
    '''

    pass


def select_less():
    '''Deselect objects at the boundaries of parent/child relationships 

    '''

    pass


def select_linked(extend=False, type='OBDATA'):
    '''Select all visible objects that are linked 

    :param extend: Extend, Extend selection instead of deselecting everything first 
    :type extend: boolean, (optional)
    :param type: Type 
    :type type: enum in ['OBDATA', 'MATERIAL', 'DUPGROUP', 'PARTICLE', 'LIBRARY', 'LIBRARY_OBDATA'], (optional)
    '''

    pass


def select_mirror(extend=False):
    '''Select the Mirror objects of the selected object eg. L.sword -> R.sword 

    :param extend: Extend, Extend selection instead of deselecting everything first 
    :type extend: boolean, (optional)
    '''

    pass


def select_more():
    '''Select connected parent/child objects 

    '''

    pass


def select_pattern(pattern="*", case_sensitive=False, extend=True):
    '''Select objects matching a naming pattern 

    :param pattern: Pattern, Name filter using ‘*’, ‘?’ and ‘[abc]’ unix style wildcards 
    :type pattern: string, (optional, never None)
    :param case_sensitive: Case Sensitive, Do a case sensitive compare 
    :type case_sensitive: boolean, (optional)
    :param extend: Extend, Extend the existing selection 
    :type extend: boolean, (optional)
    '''

    pass


def select_random(percent=50.0, seed=0, action='SELECT'):
    '''Set select on random visible objects 

    :param percent: Percent, Percentage of objects to select randomly 
    :type percent: float in [0, 100], (optional)
    :param seed: Random Seed, Seed for the random number generator 
    :type seed: int in [0, inf], (optional)
    :param action: Action, Selection action to executeSELECT Select, Select all elements.DESELECT Deselect, Deselect all elements. 
    :type action: enum in ['SELECT', 'DESELECT'], (optional)
    '''

    pass


def select_same_collection(collection=""):
    '''Select object in the same collection 

    :param collection: Collection, Name of the collection to select 
    :type collection: string, (optional, never None)
    '''

    pass


def shade_flat():
    '''Render and display faces uniform, using Face Normals 

    '''

    pass


def shade_smooth():
    '''Render and display faces smooth, using interpolated Vertex Normals 

    '''

    pass


def shaderfx_add(type='FX_BLUR'):
    '''Add a visual effect to the active object 

    :param type: TypeFX_BLUR Blur, Apply Gaussian Blur to object.FX_COLORIZE Colorize, Apply different tint effects.FX_FLIP Flip, Flip image.FX_GLOW Glow, Create a glow effect.FX_LIGHT Light, Simulate ilumination.FX_PIXEL Pixelate, Pixelate image.FX_RIM Rim, Add a rim to the image.FX_SHADOW Shadow, Create a shadow effect.FX_SWIRL Swirl, Create a rotation distortion.FX_WAVE Wave Distortion, Apply sinusoidal deformation. 
    :type type: enum in ['FX_BLUR', 'FX_COLORIZE', 'FX_FLIP', 'FX_GLOW', 'FX_LIGHT', 'FX_PIXEL', 'FX_RIM', 'FX_SHADOW', 'FX_SWIRL', 'FX_WAVE'], (optional)
    '''

    pass


def shaderfx_move_down(shaderfx=""):
    '''Move shaderfx down in the stack 

    :param shaderfx: Shader, Name of the shaderfx to edit 
    :type shaderfx: string, (optional, never None)
    '''

    pass


def shaderfx_move_up(shaderfx=""):
    '''Move shaderfx up in the stack 

    :param shaderfx: Shader, Name of the shaderfx to edit 
    :type shaderfx: string, (optional, never None)
    '''

    pass


def shaderfx_remove(shaderfx=""):
    '''Remove a shaderfx from the active grease pencil object 

    :param shaderfx: Shader, Name of the shaderfx to edit 
    :type shaderfx: string, (optional, never None)
    '''

    pass


def shape_key_add(from_mix=True):
    '''Add shape key to the object 

    :param from_mix: From Mix, Create the new shape key from the existing mix of keys 
    :type from_mix: boolean, (optional)
    '''

    pass


def shape_key_clear():
    '''Clear weights for all shape keys 

    '''

    pass


def shape_key_mirror(use_topology=False):
    '''Mirror the current shape key along the local X axis 

    :param use_topology: Topology Mirror, Use topology based mirroring (for when both sides of mesh have matching, unique topology) 
    :type use_topology: boolean, (optional)
    '''

    pass


def shape_key_move(type='TOP'):
    '''Move the active shape key up/down in the list 

    :param type: TypeTOP Top, Top of the list.UP Up.DOWN Down.BOTTOM Bottom, Bottom of the list. 
    :type type: enum in ['TOP', 'UP', 'DOWN', 'BOTTOM'], (optional)
    '''

    pass


def shape_key_remove(all=False):
    '''Remove shape key from the object 

    :param all: All, Remove all shape keys 
    :type all: boolean, (optional)
    '''

    pass


def shape_key_retime():
    '''Resets the timing for absolute shape keys 

    '''

    pass


def shape_key_transfer(mode='OFFSET', use_clamp=False):
    '''Copy another selected objects active shape to this one by applying the relative offsets 

    :param mode: Transformation Mode, Relative shape positions to the new shape methodOFFSET Offset, Apply the relative positional offset.RELATIVE_FACE Relative Face, Calculate relative position (using faces).RELATIVE_EDGE Relative Edge, Calculate relative position (using edges). 
    :type mode: enum in ['OFFSET', 'RELATIVE_FACE', 'RELATIVE_EDGE'], (optional)
    :param use_clamp: Clamp Offset, Clamp the transformation to the distance each vertex moves in the original shape 
    :type use_clamp: boolean, (optional)
    '''

    pass


def skin_armature_create(modifier=""):
    '''Create an armature that parallels the skin layout 

    :param modifier: Modifier, Name of the modifier to edit 
    :type modifier: string, (optional, never None)
    '''

    pass


def skin_loose_mark_clear(action='MARK'):
    '''Mark/clear selected vertices as loose 

    :param action: ActionMARK Mark, Mark selected vertices as loose.CLEAR Clear, Set selected vertices as not loose. 
    :type action: enum in ['MARK', 'CLEAR'], (optional)
    '''

    pass


def skin_radii_equalize():
    '''Make skin radii of selected vertices equal on each axis 

    '''

    pass


def skin_root_mark():
    '''Mark selected vertices as roots 

    '''

    pass


def slow_parent_clear():
    '''Clear the object’s slow parent 

    '''

    pass


def slow_parent_set():
    '''Set the object’s slow parent 

    '''

    pass


def speaker_add(view_align=False,
                enter_editmode=False,
                location=(0.0, 0.0, 0.0),
                rotation=(0.0, 0.0, 0.0)):
    '''Add a speaker object to the scene 

    :param view_align: Align to View, Align the new object to the view 
    :type view_align: boolean, (optional)
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object 
    :type enter_editmode: boolean, (optional)
    :param location: Location, Location for the newly added object 
    :type location: float array of 3 items in [-inf, inf], (optional)
    :param rotation: Rotation, Rotation for the newly added object 
    :type rotation: float array of 3 items in [-inf, inf], (optional)
    '''

    pass


def subdivision_set(level=1, relative=False):
    '''Sets a Subdivision Surface Level (1-5) 

    :param level: Level 
    :type level: int in [-100, 100], (optional)
    :param relative: Relative, Apply the subsurf level as an offset relative to the current level 
    :type relative: boolean, (optional)
    '''

    pass


def surfacedeform_bind(modifier=""):
    '''Bind mesh to target in surface deform modifier 

    :param modifier: Modifier, Name of the modifier to edit 
    :type modifier: string, (optional, never None)
    '''

    pass


def text_add(radius=1.0,
             view_align=False,
             enter_editmode=False,
             location=(0.0, 0.0, 0.0),
             rotation=(0.0, 0.0, 0.0)):
    '''Add a text object to the scene 

    :param radius: Radius 
    :type radius: float in [0, inf], (optional)
    :param view_align: Align to View, Align the new object to the view 
    :type view_align: boolean, (optional)
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object 
    :type enter_editmode: boolean, (optional)
    :param location: Location, Location for the newly added object 
    :type location: float array of 3 items in [-inf, inf], (optional)
    :param rotation: Rotation, Rotation for the newly added object 
    :type rotation: float array of 3 items in [-inf, inf], (optional)
    '''

    pass


def track_clear(type='CLEAR'):
    '''Clear tracking constraint or flag from object 

    :param type: Type 
    :type type: enum in ['CLEAR', 'CLEAR_KEEP_TRANSFORM'], (optional)
    '''

    pass


def track_set(type='DAMPTRACK'):
    '''Make the object track another object, using various methods/constraints 

    :param type: Type 
    :type type: enum in ['DAMPTRACK', 'TRACKTO', 'LOCKTRACK'], (optional)
    '''

    pass


def transform_apply(location=False,
                    rotation=False,
                    scale=False,
                    properties=True):
    '''Apply the object’s transformation to its data 

    :param location: Location 
    :type location: boolean, (optional)
    :param rotation: Rotation 
    :type rotation: boolean, (optional)
    :param scale: Scale 
    :type scale: boolean, (optional)
    :param properties: Apply Properties, Modify properties such as curve vertex radius, font size and bone envelope 
    :type properties: boolean, (optional)
    '''

    pass


def transform_axis_target():
    '''Interactively point cameras and lights to a location (Ctrl translates) 

    '''

    pass


def transforms_to_deltas(mode='ALL', reset_values=True):
    '''Convert normal object transforms to delta transforms, any existing delta transforms will be included as well 

    :param mode: Mode, Which transforms to transferALL All Transforms, Transfer location, rotation, and scale transforms.LOC Location, Transfer location transforms only.ROT Rotation, Transfer rotation transforms only.SCALE Scale, Transfer scale transforms only. 
    :type mode: enum in ['ALL', 'LOC', 'ROT', 'SCALE'], (optional)
    :param reset_values: Reset Values, Clear transform values after transferring to deltas 
    :type reset_values: boolean, (optional)
    '''

    pass


def unlink_data():
    '''Undocumented contribute <https://developer.blender.org/T51061> 

    '''

    pass


def vertex_group_add():
    '''Add a new vertex group to the active object 

    '''

    pass


def vertex_group_assign():
    '''Assign the selected vertices to the active vertex group 

    '''

    pass


def vertex_group_assign_new():
    '''Assign the selected vertices to a new vertex group 

    '''

    pass


def vertex_group_clean(group_select_mode='', limit=0.0, keep_single=False):
    '''Remove vertex group assignments which are not required 

    :param group_select_mode: Subset, Define which subset of Groups shall be used 
    :type group_select_mode: enum in [], (optional)
    :param limit: Limit, Remove vertices which weight is below or equal to this limit 
    :type limit: float in [0, 1], (optional)
    :param keep_single: Keep Single, Keep verts assigned to at least one group when cleaning 
    :type keep_single: boolean, (optional)
    '''

    pass


def vertex_group_copy():
    '''Make a copy of the active vertex group 

    '''

    pass


def vertex_group_copy_to_linked():
    '''Replace vertex groups of all users of the same geometry data by vertex groups of active object 

    '''

    pass


def vertex_group_copy_to_selected():
    '''Replace vertex groups of selected objects by vertex groups of active object 

    '''

    pass


def vertex_group_deselect():
    '''Deselect all selected vertices assigned to the active vertex group 

    '''

    pass


def vertex_group_fix(dist=0.0, strength=1.0, accuracy=1.0):
    '''Modify the position of selected vertices by changing only their respective groups’ weights (this tool may be slow for many vertices) 

    :param dist: Distance, The distance to move to 
    :type dist: float in [-inf, inf], (optional)
    :param strength: Strength, The distance moved can be changed by this multiplier 
    :type strength: float in [-2, inf], (optional)
    :param accuracy: Change Sensitivity, Change the amount weights are altered with each iteration: lower values are slower 
    :type accuracy: float in [0.05, inf], (optional)
    '''

    pass


def vertex_group_invert(group_select_mode='',
                        auto_assign=True,
                        auto_remove=True):
    '''Invert active vertex group’s weights 

    :param group_select_mode: Subset, Define which subset of Groups shall be used 
    :type group_select_mode: enum in [], (optional)
    :param auto_assign: Add Weights, Add verts from groups that have zero weight before inverting 
    :type auto_assign: boolean, (optional)
    :param auto_remove: Remove Weights, Remove verts from groups that have zero weight after inverting 
    :type auto_remove: boolean, (optional)
    '''

    pass


def vertex_group_levels(group_select_mode='', offset=0.0, gain=1.0):
    '''Add some offset and multiply with some gain the weights of the active vertex group 

    :param group_select_mode: Subset, Define which subset of Groups shall be used 
    :type group_select_mode: enum in [], (optional)
    :param offset: Offset, Value to add to weights 
    :type offset: float in [-1, 1], (optional)
    :param gain: Gain, Value to multiply weights by 
    :type gain: float in [0, inf], (optional)
    '''

    pass


def vertex_group_limit_total(group_select_mode='', limit=4):
    '''Limit deform weights associated with a vertex to a specified number by removing lowest weights 

    :param group_select_mode: Subset, Define which subset of Groups shall be used 
    :type group_select_mode: enum in [], (optional)
    :param limit: Limit, Maximum number of deform weights 
    :type limit: int in [1, 32], (optional)
    '''

    pass


def vertex_group_lock(action='TOGGLE'):
    '''Change the lock state of all vertex groups of active object 

    :param action: Action, Lock action to execute on vertex groupsTOGGLE Toggle, Unlock all vertex groups if there is at least one locked group, lock all in other case.LOCK Lock, Lock all vertex groups.UNLOCK Unlock, Unlock all vertex groups.INVERT Invert, Invert the lock state of all vertex groups. 
    :type action: enum in ['TOGGLE', 'LOCK', 'UNLOCK', 'INVERT'], (optional)
    '''

    pass


def vertex_group_mirror(mirror_weights=True,
                        flip_group_names=True,
                        all_groups=False,
                        use_topology=False):
    '''Mirror vertex group, flip weights and/or names, editing only selected vertices, flipping when both sides are selected otherwise copy from unselected 

    :param mirror_weights: Mirror Weights, Mirror weights 
    :type mirror_weights: boolean, (optional)
    :param flip_group_names: Flip Group Names, Flip vertex group names 
    :type flip_group_names: boolean, (optional)
    :param all_groups: All Groups, Mirror all vertex groups weights 
    :type all_groups: boolean, (optional)
    :param use_topology: Topology Mirror, Use topology based mirroring (for when both sides of mesh have matching, unique topology) 
    :type use_topology: boolean, (optional)
    '''

    pass


def vertex_group_move(direction='UP'):
    '''Move the active vertex group up/down in the list 

    :param direction: Direction, Direction to move the active vertex group towards 
    :type direction: enum in ['UP', 'DOWN'], (optional)
    '''

    pass


def vertex_group_normalize():
    '''Normalize weights of the active vertex group, so that the highest ones are now 1.0 

    '''

    pass


def vertex_group_normalize_all(group_select_mode='', lock_active=True):
    '''Normalize all weights of all vertex groups, so that for each vertex, the sum of all weights is 1.0 

    :param group_select_mode: Subset, Define which subset of Groups shall be used 
    :type group_select_mode: enum in [], (optional)
    :param lock_active: Lock Active, Keep the values of the active group while normalizing others 
    :type lock_active: boolean, (optional)
    '''

    pass


def vertex_group_quantize(group_select_mode='', steps=4):
    '''Set weights to a fixed number of steps 

    :param group_select_mode: Subset, Define which subset of Groups shall be used 
    :type group_select_mode: enum in [], (optional)
    :param steps: Steps, Number of steps between 0 and 1 
    :type steps: int in [1, 1000], (optional)
    '''

    pass


def vertex_group_remove(all=False, all_unlocked=False):
    '''Delete the active or all vertex groups from the active object 

    :param all: All, Remove all vertex groups 
    :type all: boolean, (optional)
    :param all_unlocked: All Unlocked, Remove all unlocked vertex groups 
    :type all_unlocked: boolean, (optional)
    '''

    pass


def vertex_group_remove_from(use_all_groups=False, use_all_verts=False):
    '''Remove the selected vertices from active or all vertex group(s) 

    :param use_all_groups: All Groups, Remove from all groups 
    :type use_all_groups: boolean, (optional)
    :param use_all_verts: All Verts, Clear the active group 
    :type use_all_verts: boolean, (optional)
    '''

    pass


def vertex_group_select():
    '''Select all the vertices assigned to the active vertex group 

    '''

    pass


def vertex_group_set_active(group=''):
    '''Set the active vertex group 

    :param group: Group, Vertex group to set as active 
    :type group: enum in [], (optional)
    '''

    pass


def vertex_group_smooth(group_select_mode='', factor=0.5, repeat=1,
                        expand=0.0):
    '''Smooth weights for selected vertices 

    :param group_select_mode: Subset, Define which subset of Groups shall be used 
    :type group_select_mode: enum in [], (optional)
    :param factor: Factor 
    :type factor: float in [0, 1], (optional)
    :param repeat: Iterations 
    :type repeat: int in [1, 10000], (optional)
    :param expand: Expand/Contract, Expand/contract weights 
    :type expand: float in [-1, 1], (optional)
    '''

    pass


def vertex_group_sort(sort_type='NAME'):
    '''Sort vertex groups 

    :param sort_type: Sort type, Sort type 
    :type sort_type: enum in ['NAME', 'BONE_HIERARCHY'], (optional)
    '''

    pass


def vertex_parent_set():
    '''Parent selected objects to the selected vertices 

    '''

    pass


def vertex_weight_copy():
    '''Copy weights from active to selected 

    '''

    pass


def vertex_weight_delete(weight_group=-1):
    '''Delete this weight from the vertex (disabled if vertex group is locked) 

    :param weight_group: Weight Index, Index of source weight in active vertex group 
    :type weight_group: int in [-1, inf], (optional)
    '''

    pass


def vertex_weight_normalize_active_vertex():
    '''Normalize active vertex’s weights 

    '''

    pass


def vertex_weight_paste(weight_group=-1):
    '''Copy this group’s weight to other selected verts (disabled if vertex group is locked) 

    :param weight_group: Weight Index, Index of source weight in active vertex group 
    :type weight_group: int in [-1, inf], (optional)
    '''

    pass


def vertex_weight_set_active(weight_group=-1):
    '''Set as active vertex group 

    :param weight_group: Weight Index, Index of source weight in active vertex group 
    :type weight_group: int in [-1, inf], (optional)
    '''

    pass


def visual_transform_apply():
    '''Apply the object’s visual transformation to its data 

    '''

    pass
