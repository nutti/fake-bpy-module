frame_change_post = None
'''on frame change for playback and rendering (after) '''

frame_change_pre = None
'''on frame change for playback and rendering (before) '''

game_post = None
'''on ending the game engine '''

game_pre = None
'''on starting the game engine '''

load_post = None
'''on loading a new blend file (after) '''

load_pre = None
'''on loading a new blend file (before) '''

render_cancel = None
'''on canceling a render job '''

render_complete = None
'''on completion of render job '''

render_init = None
'''on initialization of a render job '''

render_post = None
'''on render (after) '''

render_pre = None
'''on render (before) '''

render_stats = None
'''on printing render statistics '''

render_write = None
'''on writing a render frame (directly after the frame is written) '''

save_post = None
'''on saving a blend file (after) '''

save_pre = None
'''on saving a blend file (before) '''

scene_update_post = None
'''on every scene data update. Does not imply that anything changed in the scene, just that the dependency graph was reevaluated, and the scene was possibly updated by Blenders animation system. '''

scene_update_pre = None
'''on every scene data update. Does not imply that anything changed in the scene, just that the dependency graph is about to be reevaluated, and the scene is about to be updated by Blenders animation system. '''

version_update = None
'''on ending the versioning code '''

persistent = None
'''Function decorator for callback functions not to be removed when loading new files '''
