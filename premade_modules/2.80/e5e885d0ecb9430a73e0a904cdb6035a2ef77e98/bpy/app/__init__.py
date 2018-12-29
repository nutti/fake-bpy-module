from . import translations
from . import handlers
from . import timers
from . import icons

background = None
'''Boolean, True when blender is running without a user interface (started with -b) '''

factory_startup = None
'''Boolean, True when blender is running with factory-startup) '''

translations = None
'''Application and addons internationalization API '''

build_branch = None
'''The branch this blender instance was built from '''

build_cflags = None
'''C compiler flags '''

build_commit_date = None
'''The date of commit this blender instance was built '''

build_commit_time = None
'''The time of commit this blender instance was built '''

build_cxxflags = None
'''C++ compiler flags '''

build_date = None
'''The date this blender instance was built '''

build_hash = None
'''The commit hash this blender instance was built with '''

build_linkflags = None
'''Binary linking flags '''

build_platform = None
'''The platform this blender instance was built for '''

build_system = None
'''Build system used '''

build_time = None
'''The time this blender instance was built '''

build_type = None
'''The type of build (Release, Debug) '''

build_commit_timestamp = None
'''The unix timestamp of commit this blender instance was built '''

icons = None
'''Manage custom icons '''

timers = None
'''Manage timers '''

binary_path = None
'''The location of blenders executable, useful for utilities that spawn new instances '''

version_char = None
'''The Blender version character (for minor releases) '''

version_cycle = None
'''The release status of this build alpha/beta/rc/release '''

version_string = None
'''The Blender version formatted as a string '''

version = None
'''The Blender version as a tuple of 3 numbers. eg. (2, 50, 11) '''

alembic = None
'''constant value bpy.app.alembic(supported=True, version=(1, 7, 8), version_string= 1, 7, 8) '''

build_options = None
'''constant value bpy.app.build_options(bullet=True, codec_avi=True, codec_ffmpeg=True, codec_sndfile=True, compositor=True, cycles=True, cycles_osl=True, freestyle=True, image_cineon=True, image_dds=True, image_hdr=True, image_openexr=True, image_openjpeg=True, image_tiff=True, input_ndof=True, audaspace=True, international=True, openal=True, sdl=True, sdl_dynload=False, jack=False, libmv=True, mod_fluid=True, mod_oceansim=True, mod_remesh=True, mod_smoke=True, collada=True, opencolorio=True, openmp=False, …) '''

ffmpeg = None
'''constant value bpy.app.ffmpeg(supported=True, avcodec_version=(58, 18, 100), avcodec_version_string=‘58, 18, 100, avdevice_version=(58, 3, 100), avdevice_version_string=‘58, 3, 100, avformat_version=(58, 12, 100), avformat_version_string=‘58, 12, 100, avutil_version=(56, 14, 100), avutil_version_string=‘56, 14, 100, swscale_version=(5, 1, 100), swscale_version_string= 5, 1, 100) '''

handlers = None
'''constant value bpy.app.handlers(frame_change_pre=[], frame_change_post=[], render_pre=[], render_post=[], render_write=[], render_stats=[], render_init=[], render_complete=[], render_cancel=[], load_pre=[], load_post=[], save_pre=[], save_post=[], undo_pre=[], undo_post=[], redo_pre=[], redo_post=[], depsgraph_update_pre=[], depsgraph_update_post=[], version_update=[<function do_versions at 0x11cd68510>], load_factory_startup_post=[], persistent=<class ‘persistent>) '''

ocio = None
'''constant value bpy.app.ocio(supported=True, version=(1, 1, 0), version_string= 1, 1, 0) '''

oiio = None
'''constant value bpy.app.oiio(supported=True, version=(1, 8, 13), version_string= 1, 8, 13) '''

opensubdiv = None
'''constant value bpy.app.opensubdiv(supported=True, version=(0, 0, 0), version_string= 0, 0, 0) '''

openvdb = None
'''constant value bpy.app.openvdb(supported=True, version=(5, 1, 0), version_string= 5, 1, 0) '''

sdl = None
'''constant value bpy.app.sdl(supported=True, version=(2, 0, 8), version_string=‘2.0.8, available=True) '''
