def bend(
        value=(0.0),
        mirror=False,
        proportional='DISABLED',
        proportional_edit_falloff='SMOOTH',
        proportional_size=1.0,
        snap=False,
        snap_target='CLOSEST',
        snap_point=(0.0, 0.0, 0.0),
        snap_align=False,
        snap_normal=(0.0, 0.0, 0.0),
        gpencil_strokes=False,
        center_override=(0.0, 0.0, 0.0),
        release_confirm=False,
        use_accurate=False):
    '''Bend selected items between the 3D cursor and the mouse 

    :param value: Angle 
    :type value: float array of 1 items in [-inf, inf], (optional)
    :param mirror: Mirror Editing 
    :type mirror: boolean, (optional)
    :param proportional: Proportional EditingDISABLED Disable, Proportional Editing disabled.ENABLED Enable, Proportional Editing enabled.PROJECTED Projected (2D), Proportional Editing using screen space locations.CONNECTED Connected, Proportional Editing using connected geometry only. 
    :type proportional: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing modeSMOOTH Smooth, Smooth falloff.SPHERE Sphere, Spherical falloff.ROOT Root, Root falloff.INVERSE_SQUARE Inverse Square, Inverse Square falloff.SHARP Sharp, Sharp falloff.LINEAR Linear, Linear falloff.CONSTANT Constant, Constant falloff.RANDOM Random, Random falloff. 
    :type proportional_edit_falloff: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
    :param proportional_size: Proportional Size 
    :type proportional_size: float in [1e-06, inf], (optional)
    :param snap: Use Snapping Options 
    :type snap: boolean, (optional)
    :param snap_target: TargetCLOSEST Closest, Snap closest point onto target.CENTER Center, Snap transormation center onto target.MEDIAN Median, Snap median onto target.ACTIVE Active, Snap active onto target. 
    :type snap_target: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
    :param snap_point: Point 
    :type snap_point: float array of 3 items in [-inf, inf], (optional)
    :param snap_align: Align with Point Normal 
    :type snap_align: boolean, (optional)
    :param snap_normal: Normal 
    :type snap_normal: float array of 3 items in [-inf, inf], (optional)
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes 
    :type gpencil_strokes: boolean, (optional)
    :param center_override: Center Override, Force using this center value (when set) 
    :type center_override: float array of 3 items in [-inf, inf], (optional)
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button 
    :type release_confirm: boolean, (optional)
    :param use_accurate: Accurate, Use accurate transformation 
    :type use_accurate: boolean, (optional)
    '''

    pass


def create_orientation(name="", use_view=False, use=False, overwrite=False):
    '''Create transformation orientation from selection 

    :param name: Name, Name of the new custom orientation 
    :type name: string, (optional, never None)
    :param use_view: Use View, Use the current view instead of the active object to create the new orientation 
    :type use_view: boolean, (optional)
    :param use: Use after creation, Select orientation after its creation 
    :type use: boolean, (optional)
    :param overwrite: Overwrite previous, Overwrite previously created orientation with same name 
    :type overwrite: boolean, (optional)
    '''

    pass


def delete_orientation():
    '''Delete transformation orientation 

    '''

    pass


def edge_bevelweight(value=0.0,
                     snap=False,
                     snap_target='CLOSEST',
                     snap_point=(0.0, 0.0, 0.0),
                     snap_align=False,
                     snap_normal=(0.0, 0.0, 0.0),
                     release_confirm=False,
                     use_accurate=False):
    '''Change the bevel weight of edges 

    :param value: Factor 
    :type value: float in [-1, 1], (optional)
    :param snap: Use Snapping Options 
    :type snap: boolean, (optional)
    :param snap_target: TargetCLOSEST Closest, Snap closest point onto target.CENTER Center, Snap transormation center onto target.MEDIAN Median, Snap median onto target.ACTIVE Active, Snap active onto target. 
    :type snap_target: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
    :param snap_point: Point 
    :type snap_point: float array of 3 items in [-inf, inf], (optional)
    :param snap_align: Align with Point Normal 
    :type snap_align: boolean, (optional)
    :param snap_normal: Normal 
    :type snap_normal: float array of 3 items in [-inf, inf], (optional)
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button 
    :type release_confirm: boolean, (optional)
    :param use_accurate: Accurate, Use accurate transformation 
    :type use_accurate: boolean, (optional)
    '''

    pass


def edge_crease(value=0.0,
                snap=False,
                snap_target='CLOSEST',
                snap_point=(0.0, 0.0, 0.0),
                snap_align=False,
                snap_normal=(0.0, 0.0, 0.0),
                release_confirm=False,
                use_accurate=False):
    '''Change the crease of edges 

    :param value: Factor 
    :type value: float in [-1, 1], (optional)
    :param snap: Use Snapping Options 
    :type snap: boolean, (optional)
    :param snap_target: TargetCLOSEST Closest, Snap closest point onto target.CENTER Center, Snap transormation center onto target.MEDIAN Median, Snap median onto target.ACTIVE Active, Snap active onto target. 
    :type snap_target: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
    :param snap_point: Point 
    :type snap_point: float array of 3 items in [-inf, inf], (optional)
    :param snap_align: Align with Point Normal 
    :type snap_align: boolean, (optional)
    :param snap_normal: Normal 
    :type snap_normal: float array of 3 items in [-inf, inf], (optional)
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button 
    :type release_confirm: boolean, (optional)
    :param use_accurate: Accurate, Use accurate transformation 
    :type use_accurate: boolean, (optional)
    '''

    pass


def edge_slide(value=0.0,
               single_side=False,
               use_even=False,
               flipped=False,
               use_clamp=True,
               mirror=False,
               snap=False,
               snap_target='CLOSEST',
               snap_point=(0.0, 0.0, 0.0),
               snap_align=False,
               snap_normal=(0.0, 0.0, 0.0),
               correct_uv=True,
               release_confirm=False,
               use_accurate=False):
    '''Slide an edge loop along a mesh 

    :param value: Factor 
    :type value: float in [-10, 10], (optional)
    :param single_side: Single Side 
    :type single_side: boolean, (optional)
    :param use_even: Even, Make the edge loop match the shape of the adjacent edge loop 
    :type use_even: boolean, (optional)
    :param flipped: Flipped, When Even mode is active, flips between the two adjacent edge loops 
    :type flipped: boolean, (optional)
    :param use_clamp: Clamp, Clamp within the edge extents 
    :type use_clamp: boolean, (optional)
    :param mirror: Mirror Editing 
    :type mirror: boolean, (optional)
    :param snap: Use Snapping Options 
    :type snap: boolean, (optional)
    :param snap_target: TargetCLOSEST Closest, Snap closest point onto target.CENTER Center, Snap transormation center onto target.MEDIAN Median, Snap median onto target.ACTIVE Active, Snap active onto target. 
    :type snap_target: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
    :param snap_point: Point 
    :type snap_point: float array of 3 items in [-inf, inf], (optional)
    :param snap_align: Align with Point Normal 
    :type snap_align: boolean, (optional)
    :param snap_normal: Normal 
    :type snap_normal: float array of 3 items in [-inf, inf], (optional)
    :param correct_uv: Correct UVs, Correct UV coordinates when transforming 
    :type correct_uv: boolean, (optional)
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button 
    :type release_confirm: boolean, (optional)
    :param use_accurate: Accurate, Use accurate transformation 
    :type use_accurate: boolean, (optional)
    '''

    pass


def from_gizmo():
    '''Transform selected items by mode type 

    '''

    pass


def mirror(
        constraint_axis=(False, False, False),
        constraint_matrix=((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
        constraint_orientation='GLOBAL',
        proportional='DISABLED',
        proportional_edit_falloff='SMOOTH',
        proportional_size=1.0,
        gpencil_strokes=False,
        center_override=(0.0, 0.0, 0.0),
        release_confirm=False,
        use_accurate=False):
    '''Mirror selected items around one or more axes 

    :param constraint_axis: Constraint Axis 
    :type constraint_axis: boolean array of 3 items, (optional)
    :param constraint_matrix: Matrix 
    :type constraint_matrix: float multi-dimensional array of 3 * 3 items in [-inf, inf], (optional)
    :param constraint_orientation: Orientation, Transformation orientation 
    :type constraint_orientation: enum in [], (optional)
    :param proportional: Proportional EditingDISABLED Disable, Proportional Editing disabled.ENABLED Enable, Proportional Editing enabled.PROJECTED Projected (2D), Proportional Editing using screen space locations.CONNECTED Connected, Proportional Editing using connected geometry only. 
    :type proportional: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing modeSMOOTH Smooth, Smooth falloff.SPHERE Sphere, Spherical falloff.ROOT Root, Root falloff.INVERSE_SQUARE Inverse Square, Inverse Square falloff.SHARP Sharp, Sharp falloff.LINEAR Linear, Linear falloff.CONSTANT Constant, Constant falloff.RANDOM Random, Random falloff. 
    :type proportional_edit_falloff: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
    :param proportional_size: Proportional Size 
    :type proportional_size: float in [1e-06, inf], (optional)
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes 
    :type gpencil_strokes: boolean, (optional)
    :param center_override: Center Override, Force using this center value (when set) 
    :type center_override: float array of 3 items in [-inf, inf], (optional)
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button 
    :type release_confirm: boolean, (optional)
    :param use_accurate: Accurate, Use accurate transformation 
    :type use_accurate: boolean, (optional)
    '''

    pass


def push_pull(value=0.0,
              mirror=False,
              proportional='DISABLED',
              proportional_edit_falloff='SMOOTH',
              proportional_size=1.0,
              snap=False,
              snap_target='CLOSEST',
              snap_point=(0.0, 0.0, 0.0),
              snap_align=False,
              snap_normal=(0.0, 0.0, 0.0),
              center_override=(0.0, 0.0, 0.0),
              release_confirm=False,
              use_accurate=False):
    '''Push/Pull selected items 

    :param value: Distance 
    :type value: float in [-inf, inf], (optional)
    :param mirror: Mirror Editing 
    :type mirror: boolean, (optional)
    :param proportional: Proportional EditingDISABLED Disable, Proportional Editing disabled.ENABLED Enable, Proportional Editing enabled.PROJECTED Projected (2D), Proportional Editing using screen space locations.CONNECTED Connected, Proportional Editing using connected geometry only. 
    :type proportional: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing modeSMOOTH Smooth, Smooth falloff.SPHERE Sphere, Spherical falloff.ROOT Root, Root falloff.INVERSE_SQUARE Inverse Square, Inverse Square falloff.SHARP Sharp, Sharp falloff.LINEAR Linear, Linear falloff.CONSTANT Constant, Constant falloff.RANDOM Random, Random falloff. 
    :type proportional_edit_falloff: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
    :param proportional_size: Proportional Size 
    :type proportional_size: float in [1e-06, inf], (optional)
    :param snap: Use Snapping Options 
    :type snap: boolean, (optional)
    :param snap_target: TargetCLOSEST Closest, Snap closest point onto target.CENTER Center, Snap transormation center onto target.MEDIAN Median, Snap median onto target.ACTIVE Active, Snap active onto target. 
    :type snap_target: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
    :param snap_point: Point 
    :type snap_point: float array of 3 items in [-inf, inf], (optional)
    :param snap_align: Align with Point Normal 
    :type snap_align: boolean, (optional)
    :param snap_normal: Normal 
    :type snap_normal: float array of 3 items in [-inf, inf], (optional)
    :param center_override: Center Override, Force using this center value (when set) 
    :type center_override: float array of 3 items in [-inf, inf], (optional)
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button 
    :type release_confirm: boolean, (optional)
    :param use_accurate: Accurate, Use accurate transformation 
    :type use_accurate: boolean, (optional)
    '''

    pass


def resize(
        value=(1.0, 1.0, 1.0),
        constraint_axis=(False, False, False),
        constraint_matrix=((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
        constraint_orientation='GLOBAL',
        mirror=False,
        proportional='DISABLED',
        proportional_edit_falloff='SMOOTH',
        proportional_size=1.0,
        snap=False,
        snap_target='CLOSEST',
        snap_point=(0.0, 0.0, 0.0),
        snap_align=False,
        snap_normal=(0.0, 0.0, 0.0),
        gpencil_strokes=False,
        texture_space=False,
        remove_on_cancel=False,
        center_override=(0.0, 0.0, 0.0),
        release_confirm=False,
        use_accurate=False):
    '''Scale (resize) selected items 

    :param value: Scale 
    :type value: float array of 3 items in [-inf, inf], (optional)
    :param constraint_axis: Constraint Axis 
    :type constraint_axis: boolean array of 3 items, (optional)
    :param constraint_matrix: Matrix 
    :type constraint_matrix: float multi-dimensional array of 3 * 3 items in [-inf, inf], (optional)
    :param constraint_orientation: Orientation, Transformation orientation 
    :type constraint_orientation: enum in [], (optional)
    :param mirror: Mirror Editing 
    :type mirror: boolean, (optional)
    :param proportional: Proportional EditingDISABLED Disable, Proportional Editing disabled.ENABLED Enable, Proportional Editing enabled.PROJECTED Projected (2D), Proportional Editing using screen space locations.CONNECTED Connected, Proportional Editing using connected geometry only. 
    :type proportional: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing modeSMOOTH Smooth, Smooth falloff.SPHERE Sphere, Spherical falloff.ROOT Root, Root falloff.INVERSE_SQUARE Inverse Square, Inverse Square falloff.SHARP Sharp, Sharp falloff.LINEAR Linear, Linear falloff.CONSTANT Constant, Constant falloff.RANDOM Random, Random falloff. 
    :type proportional_edit_falloff: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
    :param proportional_size: Proportional Size 
    :type proportional_size: float in [1e-06, inf], (optional)
    :param snap: Use Snapping Options 
    :type snap: boolean, (optional)
    :param snap_target: TargetCLOSEST Closest, Snap closest point onto target.CENTER Center, Snap transormation center onto target.MEDIAN Median, Snap median onto target.ACTIVE Active, Snap active onto target. 
    :type snap_target: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
    :param snap_point: Point 
    :type snap_point: float array of 3 items in [-inf, inf], (optional)
    :param snap_align: Align with Point Normal 
    :type snap_align: boolean, (optional)
    :param snap_normal: Normal 
    :type snap_normal: float array of 3 items in [-inf, inf], (optional)
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes 
    :type gpencil_strokes: boolean, (optional)
    :param texture_space: Edit Texture Space, Edit Object data texture space 
    :type texture_space: boolean, (optional)
    :param remove_on_cancel: Remove on Cancel, Remove elements on cancel 
    :type remove_on_cancel: boolean, (optional)
    :param center_override: Center Override, Force using this center value (when set) 
    :type center_override: float array of 3 items in [-inf, inf], (optional)
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button 
    :type release_confirm: boolean, (optional)
    :param use_accurate: Accurate, Use accurate transformation 
    :type use_accurate: boolean, (optional)
    '''

    pass


def rotate(value=0.0,
           axis=(0.0, 0.0, 0.0),
           constraint_axis=(False, False, False),
           constraint_matrix=((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0,
                                                                 0.0)),
           constraint_orientation='GLOBAL',
           mirror=False,
           proportional='DISABLED',
           proportional_edit_falloff='SMOOTH',
           proportional_size=1.0,
           snap=False,
           snap_target='CLOSEST',
           snap_point=(0.0, 0.0, 0.0),
           snap_align=False,
           snap_normal=(0.0, 0.0, 0.0),
           gpencil_strokes=False,
           center_override=(0.0, 0.0, 0.0),
           release_confirm=False,
           use_accurate=False):
    '''Rotate selected items 

    :param value: Angle 
    :type value: float in [-inf, inf], (optional)
    :param axis: Axis, The axis around which the transformation occurs 
    :type axis: float array of 3 items in [-inf, inf], (optional)
    :param constraint_axis: Constraint Axis 
    :type constraint_axis: boolean array of 3 items, (optional)
    :param constraint_matrix: Matrix 
    :type constraint_matrix: float multi-dimensional array of 3 * 3 items in [-inf, inf], (optional)
    :param constraint_orientation: Orientation, Transformation orientation 
    :type constraint_orientation: enum in [], (optional)
    :param mirror: Mirror Editing 
    :type mirror: boolean, (optional)
    :param proportional: Proportional EditingDISABLED Disable, Proportional Editing disabled.ENABLED Enable, Proportional Editing enabled.PROJECTED Projected (2D), Proportional Editing using screen space locations.CONNECTED Connected, Proportional Editing using connected geometry only. 
    :type proportional: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing modeSMOOTH Smooth, Smooth falloff.SPHERE Sphere, Spherical falloff.ROOT Root, Root falloff.INVERSE_SQUARE Inverse Square, Inverse Square falloff.SHARP Sharp, Sharp falloff.LINEAR Linear, Linear falloff.CONSTANT Constant, Constant falloff.RANDOM Random, Random falloff. 
    :type proportional_edit_falloff: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
    :param proportional_size: Proportional Size 
    :type proportional_size: float in [1e-06, inf], (optional)
    :param snap: Use Snapping Options 
    :type snap: boolean, (optional)
    :param snap_target: TargetCLOSEST Closest, Snap closest point onto target.CENTER Center, Snap transormation center onto target.MEDIAN Median, Snap median onto target.ACTIVE Active, Snap active onto target. 
    :type snap_target: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
    :param snap_point: Point 
    :type snap_point: float array of 3 items in [-inf, inf], (optional)
    :param snap_align: Align with Point Normal 
    :type snap_align: boolean, (optional)
    :param snap_normal: Normal 
    :type snap_normal: float array of 3 items in [-inf, inf], (optional)
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes 
    :type gpencil_strokes: boolean, (optional)
    :param center_override: Center Override, Force using this center value (when set) 
    :type center_override: float array of 3 items in [-inf, inf], (optional)
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button 
    :type release_confirm: boolean, (optional)
    :param use_accurate: Accurate, Use accurate transformation 
    :type use_accurate: boolean, (optional)
    '''

    pass


def rotate_normal(value=0.0,
                  axis=(0.0, 0.0, 0.0),
                  constraint_axis=(False, False, False),
                  constraint_matrix=((0.0, 0.0, 0.0), (0.0, 0.0, 0.0),
                                     (0.0, 0.0, 0.0)),
                  constraint_orientation='GLOBAL',
                  mirror=False,
                  release_confirm=False,
                  use_accurate=False):
    '''Rotate split normal of selected items 

    :param value: Angle 
    :type value: float in [-inf, inf], (optional)
    :param axis: Axis, The axis around which the transformation occurs 
    :type axis: float array of 3 items in [-inf, inf], (optional)
    :param constraint_axis: Constraint Axis 
    :type constraint_axis: boolean array of 3 items, (optional)
    :param constraint_matrix: Matrix 
    :type constraint_matrix: float multi-dimensional array of 3 * 3 items in [-inf, inf], (optional)
    :param constraint_orientation: Orientation, Transformation orientation 
    :type constraint_orientation: enum in [], (optional)
    :param mirror: Mirror Editing 
    :type mirror: boolean, (optional)
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button 
    :type release_confirm: boolean, (optional)
    :param use_accurate: Accurate, Use accurate transformation 
    :type use_accurate: boolean, (optional)
    '''

    pass


def select_orientation(orientation='GLOBAL'):
    '''Select transformation orientation 

    :param orientation: Orientation, Transformation orientation 
    :type orientation: enum in [], (optional)
    '''

    pass


def seq_slide(
        value=(0.0, 0.0),
        snap=False,
        snap_target='CLOSEST',
        snap_point=(0.0, 0.0, 0.0),
        snap_align=False,
        snap_normal=(0.0, 0.0, 0.0),
        release_confirm=False,
        use_accurate=False):
    '''Slide a sequence strip in time 

    :param value: Offset 
    :type value: float array of 2 items in [-inf, inf], (optional)
    :param snap: Use Snapping Options 
    :type snap: boolean, (optional)
    :param snap_target: TargetCLOSEST Closest, Snap closest point onto target.CENTER Center, Snap transormation center onto target.MEDIAN Median, Snap median onto target.ACTIVE Active, Snap active onto target. 
    :type snap_target: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
    :param snap_point: Point 
    :type snap_point: float array of 3 items in [-inf, inf], (optional)
    :param snap_align: Align with Point Normal 
    :type snap_align: boolean, (optional)
    :param snap_normal: Normal 
    :type snap_normal: float array of 3 items in [-inf, inf], (optional)
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button 
    :type release_confirm: boolean, (optional)
    :param use_accurate: Accurate, Use accurate transformation 
    :type use_accurate: boolean, (optional)
    '''

    pass


def shear(value=0.0,
          shear_axis='X',
          axis=(0.0, 0.0, 0.0),
          axis_ortho=(0.0, 0.0, 0.0),
          mirror=False,
          proportional='DISABLED',
          proportional_edit_falloff='SMOOTH',
          proportional_size=1.0,
          snap=False,
          snap_target='CLOSEST',
          snap_point=(0.0, 0.0, 0.0),
          snap_align=False,
          snap_normal=(0.0, 0.0, 0.0),
          gpencil_strokes=False,
          release_confirm=False,
          use_accurate=False):
    '''Shear selected items along the horizontal screen axis 

    :param value: Offset 
    :type value: float in [-inf, inf], (optional)
    :param shear_axis: Shear Axis 
    :type shear_axis: enum in ['X', 'Y'], (optional)
    :param axis: Axis, The axis around which the transformation occurs 
    :type axis: float array of 3 items in [-inf, inf], (optional)
    :param axis_ortho: Axis, The orthogonal axis around which the transformation occurs 
    :type axis_ortho: float array of 3 items in [-inf, inf], (optional)
    :param mirror: Mirror Editing 
    :type mirror: boolean, (optional)
    :param proportional: Proportional EditingDISABLED Disable, Proportional Editing disabled.ENABLED Enable, Proportional Editing enabled.PROJECTED Projected (2D), Proportional Editing using screen space locations.CONNECTED Connected, Proportional Editing using connected geometry only. 
    :type proportional: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing modeSMOOTH Smooth, Smooth falloff.SPHERE Sphere, Spherical falloff.ROOT Root, Root falloff.INVERSE_SQUARE Inverse Square, Inverse Square falloff.SHARP Sharp, Sharp falloff.LINEAR Linear, Linear falloff.CONSTANT Constant, Constant falloff.RANDOM Random, Random falloff. 
    :type proportional_edit_falloff: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
    :param proportional_size: Proportional Size 
    :type proportional_size: float in [1e-06, inf], (optional)
    :param snap: Use Snapping Options 
    :type snap: boolean, (optional)
    :param snap_target: TargetCLOSEST Closest, Snap closest point onto target.CENTER Center, Snap transormation center onto target.MEDIAN Median, Snap median onto target.ACTIVE Active, Snap active onto target. 
    :type snap_target: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
    :param snap_point: Point 
    :type snap_point: float array of 3 items in [-inf, inf], (optional)
    :param snap_align: Align with Point Normal 
    :type snap_align: boolean, (optional)
    :param snap_normal: Normal 
    :type snap_normal: float array of 3 items in [-inf, inf], (optional)
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes 
    :type gpencil_strokes: boolean, (optional)
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button 
    :type release_confirm: boolean, (optional)
    :param use_accurate: Accurate, Use accurate transformation 
    :type use_accurate: boolean, (optional)
    '''

    pass


def shrink_fatten(value=0.0,
                  use_even_offset=True,
                  mirror=False,
                  proportional='DISABLED',
                  proportional_edit_falloff='SMOOTH',
                  proportional_size=1.0,
                  snap=False,
                  snap_target='CLOSEST',
                  snap_point=(0.0, 0.0, 0.0),
                  snap_align=False,
                  snap_normal=(0.0, 0.0, 0.0),
                  release_confirm=False,
                  use_accurate=False):
    '''Shrink/fatten selected vertices along normals 

    :param value: Offset 
    :type value: float in [-inf, inf], (optional)
    :param use_even_offset: Offset Even, Scale the offset to give more even thickness 
    :type use_even_offset: boolean, (optional)
    :param mirror: Mirror Editing 
    :type mirror: boolean, (optional)
    :param proportional: Proportional EditingDISABLED Disable, Proportional Editing disabled.ENABLED Enable, Proportional Editing enabled.PROJECTED Projected (2D), Proportional Editing using screen space locations.CONNECTED Connected, Proportional Editing using connected geometry only. 
    :type proportional: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing modeSMOOTH Smooth, Smooth falloff.SPHERE Sphere, Spherical falloff.ROOT Root, Root falloff.INVERSE_SQUARE Inverse Square, Inverse Square falloff.SHARP Sharp, Sharp falloff.LINEAR Linear, Linear falloff.CONSTANT Constant, Constant falloff.RANDOM Random, Random falloff. 
    :type proportional_edit_falloff: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
    :param proportional_size: Proportional Size 
    :type proportional_size: float in [1e-06, inf], (optional)
    :param snap: Use Snapping Options 
    :type snap: boolean, (optional)
    :param snap_target: TargetCLOSEST Closest, Snap closest point onto target.CENTER Center, Snap transormation center onto target.MEDIAN Median, Snap median onto target.ACTIVE Active, Snap active onto target. 
    :type snap_target: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
    :param snap_point: Point 
    :type snap_point: float array of 3 items in [-inf, inf], (optional)
    :param snap_align: Align with Point Normal 
    :type snap_align: boolean, (optional)
    :param snap_normal: Normal 
    :type snap_normal: float array of 3 items in [-inf, inf], (optional)
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button 
    :type release_confirm: boolean, (optional)
    :param use_accurate: Accurate, Use accurate transformation 
    :type use_accurate: boolean, (optional)
    '''

    pass


def skin_resize(
        value=(1.0, 1.0, 1.0),
        constraint_axis=(False, False, False),
        constraint_matrix=((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
        constraint_orientation='GLOBAL',
        mirror=False,
        proportional='DISABLED',
        proportional_edit_falloff='SMOOTH',
        proportional_size=1.0,
        snap=False,
        snap_target='CLOSEST',
        snap_point=(0.0, 0.0, 0.0),
        snap_align=False,
        snap_normal=(0.0, 0.0, 0.0),
        release_confirm=False,
        use_accurate=False):
    '''Scale selected vertices’ skin radii 

    :param value: Scale 
    :type value: float array of 3 items in [-inf, inf], (optional)
    :param constraint_axis: Constraint Axis 
    :type constraint_axis: boolean array of 3 items, (optional)
    :param constraint_matrix: Matrix 
    :type constraint_matrix: float multi-dimensional array of 3 * 3 items in [-inf, inf], (optional)
    :param constraint_orientation: Orientation, Transformation orientation 
    :type constraint_orientation: enum in [], (optional)
    :param mirror: Mirror Editing 
    :type mirror: boolean, (optional)
    :param proportional: Proportional EditingDISABLED Disable, Proportional Editing disabled.ENABLED Enable, Proportional Editing enabled.PROJECTED Projected (2D), Proportional Editing using screen space locations.CONNECTED Connected, Proportional Editing using connected geometry only. 
    :type proportional: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing modeSMOOTH Smooth, Smooth falloff.SPHERE Sphere, Spherical falloff.ROOT Root, Root falloff.INVERSE_SQUARE Inverse Square, Inverse Square falloff.SHARP Sharp, Sharp falloff.LINEAR Linear, Linear falloff.CONSTANT Constant, Constant falloff.RANDOM Random, Random falloff. 
    :type proportional_edit_falloff: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
    :param proportional_size: Proportional Size 
    :type proportional_size: float in [1e-06, inf], (optional)
    :param snap: Use Snapping Options 
    :type snap: boolean, (optional)
    :param snap_target: TargetCLOSEST Closest, Snap closest point onto target.CENTER Center, Snap transormation center onto target.MEDIAN Median, Snap median onto target.ACTIVE Active, Snap active onto target. 
    :type snap_target: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
    :param snap_point: Point 
    :type snap_point: float array of 3 items in [-inf, inf], (optional)
    :param snap_align: Align with Point Normal 
    :type snap_align: boolean, (optional)
    :param snap_normal: Normal 
    :type snap_normal: float array of 3 items in [-inf, inf], (optional)
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button 
    :type release_confirm: boolean, (optional)
    :param use_accurate: Accurate, Use accurate transformation 
    :type use_accurate: boolean, (optional)
    '''

    pass


def tilt(value=0.0,
         mirror=False,
         proportional='DISABLED',
         proportional_edit_falloff='SMOOTH',
         proportional_size=1.0,
         snap=False,
         snap_target='CLOSEST',
         snap_point=(0.0, 0.0, 0.0),
         snap_align=False,
         snap_normal=(0.0, 0.0, 0.0),
         release_confirm=False,
         use_accurate=False):
    '''Tilt selected control vertices of 3D curve 

    :param value: Angle 
    :type value: float in [-inf, inf], (optional)
    :param mirror: Mirror Editing 
    :type mirror: boolean, (optional)
    :param proportional: Proportional EditingDISABLED Disable, Proportional Editing disabled.ENABLED Enable, Proportional Editing enabled.PROJECTED Projected (2D), Proportional Editing using screen space locations.CONNECTED Connected, Proportional Editing using connected geometry only. 
    :type proportional: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing modeSMOOTH Smooth, Smooth falloff.SPHERE Sphere, Spherical falloff.ROOT Root, Root falloff.INVERSE_SQUARE Inverse Square, Inverse Square falloff.SHARP Sharp, Sharp falloff.LINEAR Linear, Linear falloff.CONSTANT Constant, Constant falloff.RANDOM Random, Random falloff. 
    :type proportional_edit_falloff: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
    :param proportional_size: Proportional Size 
    :type proportional_size: float in [1e-06, inf], (optional)
    :param snap: Use Snapping Options 
    :type snap: boolean, (optional)
    :param snap_target: TargetCLOSEST Closest, Snap closest point onto target.CENTER Center, Snap transormation center onto target.MEDIAN Median, Snap median onto target.ACTIVE Active, Snap active onto target. 
    :type snap_target: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
    :param snap_point: Point 
    :type snap_point: float array of 3 items in [-inf, inf], (optional)
    :param snap_align: Align with Point Normal 
    :type snap_align: boolean, (optional)
    :param snap_normal: Normal 
    :type snap_normal: float array of 3 items in [-inf, inf], (optional)
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button 
    :type release_confirm: boolean, (optional)
    :param use_accurate: Accurate, Use accurate transformation 
    :type use_accurate: boolean, (optional)
    '''

    pass


def tosphere(value=0.0,
             mirror=False,
             proportional='DISABLED',
             proportional_edit_falloff='SMOOTH',
             proportional_size=1.0,
             snap=False,
             snap_target='CLOSEST',
             snap_point=(0.0, 0.0, 0.0),
             snap_align=False,
             snap_normal=(0.0, 0.0, 0.0),
             gpencil_strokes=False,
             center_override=(0.0, 0.0, 0.0),
             release_confirm=False,
             use_accurate=False):
    '''Move selected vertices outward in a spherical shape around mesh center 

    :param value: Factor 
    :type value: float in [0, 1], (optional)
    :param mirror: Mirror Editing 
    :type mirror: boolean, (optional)
    :param proportional: Proportional EditingDISABLED Disable, Proportional Editing disabled.ENABLED Enable, Proportional Editing enabled.PROJECTED Projected (2D), Proportional Editing using screen space locations.CONNECTED Connected, Proportional Editing using connected geometry only. 
    :type proportional: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing modeSMOOTH Smooth, Smooth falloff.SPHERE Sphere, Spherical falloff.ROOT Root, Root falloff.INVERSE_SQUARE Inverse Square, Inverse Square falloff.SHARP Sharp, Sharp falloff.LINEAR Linear, Linear falloff.CONSTANT Constant, Constant falloff.RANDOM Random, Random falloff. 
    :type proportional_edit_falloff: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
    :param proportional_size: Proportional Size 
    :type proportional_size: float in [1e-06, inf], (optional)
    :param snap: Use Snapping Options 
    :type snap: boolean, (optional)
    :param snap_target: TargetCLOSEST Closest, Snap closest point onto target.CENTER Center, Snap transormation center onto target.MEDIAN Median, Snap median onto target.ACTIVE Active, Snap active onto target. 
    :type snap_target: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
    :param snap_point: Point 
    :type snap_point: float array of 3 items in [-inf, inf], (optional)
    :param snap_align: Align with Point Normal 
    :type snap_align: boolean, (optional)
    :param snap_normal: Normal 
    :type snap_normal: float array of 3 items in [-inf, inf], (optional)
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes 
    :type gpencil_strokes: boolean, (optional)
    :param center_override: Center Override, Force using this center value (when set) 
    :type center_override: float array of 3 items in [-inf, inf], (optional)
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button 
    :type release_confirm: boolean, (optional)
    :param use_accurate: Accurate, Use accurate transformation 
    :type use_accurate: boolean, (optional)
    '''

    pass


def trackball(
        value=(0.0, 0.0),
        mirror=False,
        proportional='DISABLED',
        proportional_edit_falloff='SMOOTH',
        proportional_size=1.0,
        snap=False,
        snap_target='CLOSEST',
        snap_point=(0.0, 0.0, 0.0),
        snap_align=False,
        snap_normal=(0.0, 0.0, 0.0),
        gpencil_strokes=False,
        center_override=(0.0, 0.0, 0.0),
        release_confirm=False,
        use_accurate=False):
    '''Trackball style rotation of selected items 

    :param value: Angle 
    :type value: float array of 2 items in [-inf, inf], (optional)
    :param mirror: Mirror Editing 
    :type mirror: boolean, (optional)
    :param proportional: Proportional EditingDISABLED Disable, Proportional Editing disabled.ENABLED Enable, Proportional Editing enabled.PROJECTED Projected (2D), Proportional Editing using screen space locations.CONNECTED Connected, Proportional Editing using connected geometry only. 
    :type proportional: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing modeSMOOTH Smooth, Smooth falloff.SPHERE Sphere, Spherical falloff.ROOT Root, Root falloff.INVERSE_SQUARE Inverse Square, Inverse Square falloff.SHARP Sharp, Sharp falloff.LINEAR Linear, Linear falloff.CONSTANT Constant, Constant falloff.RANDOM Random, Random falloff. 
    :type proportional_edit_falloff: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
    :param proportional_size: Proportional Size 
    :type proportional_size: float in [1e-06, inf], (optional)
    :param snap: Use Snapping Options 
    :type snap: boolean, (optional)
    :param snap_target: TargetCLOSEST Closest, Snap closest point onto target.CENTER Center, Snap transormation center onto target.MEDIAN Median, Snap median onto target.ACTIVE Active, Snap active onto target. 
    :type snap_target: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
    :param snap_point: Point 
    :type snap_point: float array of 3 items in [-inf, inf], (optional)
    :param snap_align: Align with Point Normal 
    :type snap_align: boolean, (optional)
    :param snap_normal: Normal 
    :type snap_normal: float array of 3 items in [-inf, inf], (optional)
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes 
    :type gpencil_strokes: boolean, (optional)
    :param center_override: Center Override, Force using this center value (when set) 
    :type center_override: float array of 3 items in [-inf, inf], (optional)
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button 
    :type release_confirm: boolean, (optional)
    :param use_accurate: Accurate, Use accurate transformation 
    :type use_accurate: boolean, (optional)
    '''

    pass


def transform(mode='TRANSLATION',
              value=(0.0, 0.0, 0.0, 0.0),
              axis=(0.0, 0.0, 0.0),
              constraint_axis=(False, False, False),
              constraint_matrix=((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0,
                                                                    0.0)),
              constraint_orientation='GLOBAL',
              mirror=False,
              proportional='DISABLED',
              proportional_edit_falloff='SMOOTH',
              proportional_size=1.0,
              snap=False,
              snap_target='CLOSEST',
              snap_point=(0.0, 0.0, 0.0),
              snap_align=False,
              snap_normal=(0.0, 0.0, 0.0),
              gpencil_strokes=False,
              center_override=(0.0, 0.0, 0.0),
              release_confirm=False,
              use_accurate=False):
    '''Transform selected items by mode type 

    :param mode: Mode 
    :type mode: enum in ['INIT', 'DUMMY', 'TRANSLATION', 'ROTATION', 'RESIZE', 'SKIN_RESIZE', 'TOSPHERE', 'SHEAR', 'BEND', 'SHRINKFATTEN', 'TILT', 'TRACKBALL', 'PUSHPULL', 'CREASE', 'MIRROR', 'BONE_SIZE', 'BONE_ENVELOPE', 'BONE_ENVELOPE_DIST', 'CURVE_SHRINKFATTEN', 'MASK_SHRINKFATTEN', 'GPENCIL_SHRINKFATTEN', 'BONE_ROLL', 'TIME_TRANSLATE', 'TIME_SLIDE', 'TIME_SCALE', 'TIME_EXTEND', 'BAKE_TIME', 'BWEIGHT', 'ALIGN', 'EDGESLIDE', 'SEQSLIDE'], (optional)
    :param value: Values 
    :type value: float array of 4 items in [-inf, inf], (optional)
    :param axis: Axis, The axis around which the transformation occurs 
    :type axis: float array of 3 items in [-inf, inf], (optional)
    :param constraint_axis: Constraint Axis 
    :type constraint_axis: boolean array of 3 items, (optional)
    :param constraint_matrix: Matrix 
    :type constraint_matrix: float multi-dimensional array of 3 * 3 items in [-inf, inf], (optional)
    :param constraint_orientation: Orientation, Transformation orientationGLOBAL Global, Align the transformation axes to world space.LOCAL Local, Align the transformation axes to the selected objects’ local space.NORMAL Normal, Align the transformation axes to average normal of selected elements (bone Y axis for pose mode).GIMBAL Gimbal, Align each axis to the Euler rotation axis as used for input.VIEW View, Align the transformation axes to the window.CURSOR Cursor, Align the transformation axes to the 3D cursor. 
    :type constraint_orientation: enum in ['GLOBAL', 'LOCAL', 'NORMAL', 'GIMBAL', 'VIEW', 'CURSOR'], (optional)
    :param mirror: Mirror Editing 
    :type mirror: boolean, (optional)
    :param proportional: Proportional EditingDISABLED Disable, Proportional Editing disabled.ENABLED Enable, Proportional Editing enabled.PROJECTED Projected (2D), Proportional Editing using screen space locations.CONNECTED Connected, Proportional Editing using connected geometry only. 
    :type proportional: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing modeSMOOTH Smooth, Smooth falloff.SPHERE Sphere, Spherical falloff.ROOT Root, Root falloff.INVERSE_SQUARE Inverse Square, Inverse Square falloff.SHARP Sharp, Sharp falloff.LINEAR Linear, Linear falloff.CONSTANT Constant, Constant falloff.RANDOM Random, Random falloff. 
    :type proportional_edit_falloff: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
    :param proportional_size: Proportional Size 
    :type proportional_size: float in [1e-06, inf], (optional)
    :param snap: Use Snapping Options 
    :type snap: boolean, (optional)
    :param snap_target: TargetCLOSEST Closest, Snap closest point onto target.CENTER Center, Snap transormation center onto target.MEDIAN Median, Snap median onto target.ACTIVE Active, Snap active onto target. 
    :type snap_target: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
    :param snap_point: Point 
    :type snap_point: float array of 3 items in [-inf, inf], (optional)
    :param snap_align: Align with Point Normal 
    :type snap_align: boolean, (optional)
    :param snap_normal: Normal 
    :type snap_normal: float array of 3 items in [-inf, inf], (optional)
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes 
    :type gpencil_strokes: boolean, (optional)
    :param center_override: Center Override, Force using this center value (when set) 
    :type center_override: float array of 3 items in [-inf, inf], (optional)
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button 
    :type release_confirm: boolean, (optional)
    :param use_accurate: Accurate, Use accurate transformation 
    :type use_accurate: boolean, (optional)
    '''

    pass


def translate(
        value=(0.0, 0.0, 0.0),
        constraint_axis=(False, False, False),
        constraint_matrix=((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)),
        constraint_orientation='GLOBAL',
        mirror=False,
        proportional='DISABLED',
        proportional_edit_falloff='SMOOTH',
        proportional_size=1.0,
        snap=False,
        snap_target='CLOSEST',
        snap_point=(0.0, 0.0, 0.0),
        snap_align=False,
        snap_normal=(0.0, 0.0, 0.0),
        gpencil_strokes=False,
        cursor_transform=False,
        texture_space=False,
        remove_on_cancel=False,
        release_confirm=False,
        use_accurate=False):
    '''Move selected items 

    :param value: Move 
    :type value: float array of 3 items in [-inf, inf], (optional)
    :param constraint_axis: Constraint Axis 
    :type constraint_axis: boolean array of 3 items, (optional)
    :param constraint_matrix: Matrix 
    :type constraint_matrix: float multi-dimensional array of 3 * 3 items in [-inf, inf], (optional)
    :param constraint_orientation: Orientation, Transformation orientationGLOBAL Global, Align the transformation axes to world space.LOCAL Local, Align the transformation axes to the selected objects’ local space.NORMAL Normal, Align the transformation axes to average normal of selected elements (bone Y axis for pose mode).GIMBAL Gimbal, Align each axis to the Euler rotation axis as used for input.VIEW View, Align the transformation axes to the window.CURSOR Cursor, Align the transformation axes to the 3D cursor. 
    :type constraint_orientation: enum in ['GLOBAL', 'LOCAL', 'NORMAL', 'GIMBAL', 'VIEW', 'CURSOR'], (optional)
    :param mirror: Mirror Editing 
    :type mirror: boolean, (optional)
    :param proportional: Proportional EditingDISABLED Disable, Proportional Editing disabled.ENABLED Enable, Proportional Editing enabled.PROJECTED Projected (2D), Proportional Editing using screen space locations.CONNECTED Connected, Proportional Editing using connected geometry only. 
    :type proportional: enum in ['DISABLED', 'ENABLED', 'PROJECTED', 'CONNECTED'], (optional)
    :param proportional_edit_falloff: Proportional Falloff, Falloff type for proportional editing modeSMOOTH Smooth, Smooth falloff.SPHERE Sphere, Spherical falloff.ROOT Root, Root falloff.INVERSE_SQUARE Inverse Square, Inverse Square falloff.SHARP Sharp, Sharp falloff.LINEAR Linear, Linear falloff.CONSTANT Constant, Constant falloff.RANDOM Random, Random falloff. 
    :type proportional_edit_falloff: enum in ['SMOOTH', 'SPHERE', 'ROOT', 'INVERSE_SQUARE', 'SHARP', 'LINEAR', 'CONSTANT', 'RANDOM'], (optional)
    :param proportional_size: Proportional Size 
    :type proportional_size: float in [1e-06, inf], (optional)
    :param snap: Use Snapping Options 
    :type snap: boolean, (optional)
    :param snap_target: TargetCLOSEST Closest, Snap closest point onto target.CENTER Center, Snap transormation center onto target.MEDIAN Median, Snap median onto target.ACTIVE Active, Snap active onto target. 
    :type snap_target: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
    :param snap_point: Point 
    :type snap_point: float array of 3 items in [-inf, inf], (optional)
    :param snap_align: Align with Point Normal 
    :type snap_align: boolean, (optional)
    :param snap_normal: Normal 
    :type snap_normal: float array of 3 items in [-inf, inf], (optional)
    :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes 
    :type gpencil_strokes: boolean, (optional)
    :param cursor_transform: Transform Cursor 
    :type cursor_transform: boolean, (optional)
    :param texture_space: Edit Texture Space, Edit Object data texture space 
    :type texture_space: boolean, (optional)
    :param remove_on_cancel: Remove on Cancel, Remove elements on cancel 
    :type remove_on_cancel: boolean, (optional)
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button 
    :type release_confirm: boolean, (optional)
    :param use_accurate: Accurate, Use accurate transformation 
    :type use_accurate: boolean, (optional)
    '''

    pass


def vert_slide(value=0.0,
               use_even=False,
               flipped=False,
               use_clamp=True,
               mirror=False,
               snap=False,
               snap_target='CLOSEST',
               snap_point=(0.0, 0.0, 0.0),
               snap_align=False,
               snap_normal=(0.0, 0.0, 0.0),
               correct_uv=True,
               release_confirm=False,
               use_accurate=False):
    '''Slide a vertex along a mesh 

    :param value: Factor 
    :type value: float in [-10, 10], (optional)
    :param use_even: Even, Make the edge loop match the shape of the adjacent edge loop 
    :type use_even: boolean, (optional)
    :param flipped: Flipped, When Even mode is active, flips between the two adjacent edge loops 
    :type flipped: boolean, (optional)
    :param use_clamp: Clamp, Clamp within the edge extents 
    :type use_clamp: boolean, (optional)
    :param mirror: Mirror Editing 
    :type mirror: boolean, (optional)
    :param snap: Use Snapping Options 
    :type snap: boolean, (optional)
    :param snap_target: TargetCLOSEST Closest, Snap closest point onto target.CENTER Center, Snap transormation center onto target.MEDIAN Median, Snap median onto target.ACTIVE Active, Snap active onto target. 
    :type snap_target: enum in ['CLOSEST', 'CENTER', 'MEDIAN', 'ACTIVE'], (optional)
    :param snap_point: Point 
    :type snap_point: float array of 3 items in [-inf, inf], (optional)
    :param snap_align: Align with Point Normal 
    :type snap_align: boolean, (optional)
    :param snap_normal: Normal 
    :type snap_normal: float array of 3 items in [-inf, inf], (optional)
    :param correct_uv: Correct UVs, Correct UV coordinates when transforming 
    :type correct_uv: boolean, (optional)
    :param release_confirm: Confirm on Release, Always confirm operation when releasing button 
    :type release_confirm: boolean, (optional)
    :param use_accurate: Accurate, Use accurate transformation 
    :type use_accurate: boolean, (optional)
    '''

    pass


def vertex_random(offset=0.1, uniform=0.0, normal=0.0, seed=0):
    '''Randomize vertices 

    :param offset: Amount, Distance to offset 
    :type offset: float in [-inf, inf], (optional)
    :param uniform: Uniform, Increase for uniform offset distance 
    :type uniform: float in [0, 1], (optional)
    :param normal: Normal, Align offset direction to normals 
    :type normal: float in [0, 1], (optional)
    :param seed: Random Seed, Seed for the random number generator 
    :type seed: int in [0, 10000], (optional)
    '''

    pass


def vertex_warp(warp_angle=6.28319,
                offset_angle=0.0,
                min=-1,
                max=1.0,
                viewmat=((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0),
                         (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)),
                center=(0.0, 0.0, 0.0)):
    '''Warp vertices around the cursor 

    :param warp_angle: Warp Angle, Amount to warp about the cursor 
    :type warp_angle: float in [-inf, inf], (optional)
    :param offset_angle: Offset Angle, Angle to use as the basis for warping 
    :type offset_angle: float in [-inf, inf], (optional)
    :param min: Min 
    :type min: float in [-inf, inf], (optional)
    :param max: Max 
    :type max: float in [-inf, inf], (optional)
    :param viewmat: Matrix 
    :type viewmat: float multi-dimensional array of 4 * 4 items in [-inf, inf], (optional)
    :param center: Center 
    :type center: float array of 3 items in [-inf, inf], (optional)
    '''

    pass
