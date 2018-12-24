depsgraph_update_post = None
'''on depsgraph update (post) '''

depsgraph_update_pre = None
'''on depsgraph update (pre) '''

frame_change_post = None
'''on frame change for playback and rendering (after) '''

frame_change_pre = None
'''on frame change for playback and rendering (before) '''

load_factory_startup_post = None
'''on loading factory startup (after) '''

load_post = None
'''on loading a new blend file (after) '''

load_pre = None
'''on loading a new blend file (before) '''

redo_post = None
'''on loading a redo step (after) '''

redo_pre = None
'''on loading a redo step (before) '''

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

undo_post = None
'''on loading an undo step (after) '''

undo_pre = None
'''on loading an undo step (before) '''

version_update = None
'''on ending the versioning code '''

persistent = None
'''Function decorator for callback functions not to be removed when loading new files '''
