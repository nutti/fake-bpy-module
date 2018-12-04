def bake_animation():
    '''Update the audio animation cache 

    '''

    pass


def mixdown(filepath="",
            check_existing=True,
            filter_blender=False,
            filter_backup=False,
            filter_image=False,
            filter_movie=False,
            filter_python=False,
            filter_font=False,
            filter_sound=True,
            filter_text=False,
            filter_btx=False,
            filter_collada=False,
            filter_alembic=False,
            filter_folder=True,
            filter_blenlib=False,
            filemode=9,
            relative_path=True,
            display_type='DEFAULT',
            sort_method='FILE_SORT_ALPHA',
            accuracy=1024,
            container='FLAC',
            codec='FLAC',
            format='S16',
            bitrate=192,
            split_channels=False):
    '''Mix the scene’s audio to a sound file 

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
    :param accuracy: Accuracy, Sample accuracy, important for animation data (the lower the value, the more accurate) 
    :type accuracy: int in [1, inf], (optional)
    :param container: Container, File formatAC3 ac3, Dolby Digital ATRAC 3.FLAC flac, Free Lossless Audio Codec.MATROSKA mkv, Matroska.MP2 mp2, MPEG-1 Audio Layer II.MP3 mp3, MPEG-2 Audio Layer III.OGG ogg, Xiph.Org Ogg Container.WAV wav, Waveform Audio File Format. 
    :type container: enum in ['AC3', 'FLAC', 'MATROSKA', 'MP2', 'MP3', 'OGG', 'WAV'], (optional)
    :param codec: Codec, Audio CodecAAC AAC, Advanced Audio Coding.AC3 AC3, Dolby Digital ATRAC 3.FLAC FLAC, Free Lossless Audio Codec.MP2 MP2, MPEG-1 Audio Layer II.MP3 MP3, MPEG-2 Audio Layer III.PCM PCM, Pulse Code Modulation (RAW).VORBIS Vorbis, Xiph.Org Vorbis Codec. 
    :type codec: enum in ['AAC', 'AC3', 'FLAC', 'MP2', 'MP3', 'PCM', 'VORBIS'], (optional)
    :param format: Format, Sample formatU8 U8, 8 bit unsigned.S16 S16, 16 bit signed.S24 S24, 24 bit signed.S32 S32, 32 bit signed.F32 F32, 32 bit floating point.F64 F64, 64 bit floating point. 
    :type format: enum in ['U8', 'S16', 'S24', 'S32', 'F32', 'F64'], (optional)
    :param bitrate: Bitrate, Bitrate in kbit/s 
    :type bitrate: int in [32, 512], (optional)
    :param split_channels: Split channels, Each channel will be rendered into a mono file 
    :type split_channels: boolean, (optional)
    '''

    pass


def open(filepath="",
         filter_blender=False,
         filter_backup=False,
         filter_image=False,
         filter_movie=True,
         filter_python=False,
         filter_font=False,
         filter_sound=True,
         filter_text=False,
         filter_btx=False,
         filter_collada=False,
         filter_alembic=False,
         filter_folder=True,
         filter_blenlib=False,
         filemode=9,
         relative_path=True,
         show_multiview=False,
         use_multiview=False,
         display_type='DEFAULT',
         sort_method='FILE_SORT_ALPHA',
         cache=False,
         mono=False):
    '''Load a sound file 

    :param filepath: File Path, Path to file 
    :type filepath: string, (optional, never None)
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
    :param show_multiview: Enable Multi-View 
    :type show_multiview: boolean, (optional)
    :param use_multiview: Use Multi-View 
    :type use_multiview: boolean, (optional)
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_SHORT Short List, Display files as short list.LIST_LONG Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: enum in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
    :param sort_method: File sorting modeFILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.FILE_SORT_TIME Sort by time, Sort files by modification time.FILE_SORT_SIZE Sort by size, Sort files by size. 
    :type sort_method: enum in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
    :param cache: Cache, Cache the sound in memory 
    :type cache: boolean, (optional)
    :param mono: Mono, Merge all the sound’s channels into one 
    :type mono: boolean, (optional)
    '''

    pass


def open_mono(filepath="",
              filter_blender=False,
              filter_backup=False,
              filter_image=False,
              filter_movie=True,
              filter_python=False,
              filter_font=False,
              filter_sound=True,
              filter_text=False,
              filter_btx=False,
              filter_collada=False,
              filter_alembic=False,
              filter_folder=True,
              filter_blenlib=False,
              filemode=9,
              relative_path=True,
              show_multiview=False,
              use_multiview=False,
              display_type='DEFAULT',
              sort_method='FILE_SORT_ALPHA',
              cache=False,
              mono=True):
    '''Load a sound file as mono 

    :param filepath: File Path, Path to file 
    :type filepath: string, (optional, never None)
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
    :param show_multiview: Enable Multi-View 
    :type show_multiview: boolean, (optional)
    :param use_multiview: Use Multi-View 
    :type use_multiview: boolean, (optional)
    :param display_type: Display TypeDEFAULT Default, Automatically determine display type for files.LIST_SHORT Short List, Display files as short list.LIST_LONG Long List, Display files as a detailed list.THUMBNAIL Thumbnails, Display files as thumbnails. 
    :type display_type: enum in ['DEFAULT', 'LIST_SHORT', 'LIST_LONG', 'THUMBNAIL'], (optional)
    :param sort_method: File sorting modeFILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.FILE_SORT_TIME Sort by time, Sort files by modification time.FILE_SORT_SIZE Sort by size, Sort files by size. 
    :type sort_method: enum in ['FILE_SORT_ALPHA', 'FILE_SORT_EXTENSION', 'FILE_SORT_TIME', 'FILE_SORT_SIZE'], (optional)
    :param cache: Cache, Cache the sound in memory 
    :type cache: boolean, (optional)
    :param mono: Mono, Mixdown the sound to mono 
    :type mono: boolean, (optional)
    '''

    pass


def pack():
    '''Pack the sound into the current blend file 

    '''

    pass


def unpack(method='USE_LOCAL', id=""):
    '''Unpack the sound to the samples filename 

    :param method: Method, How to unpack 
    :type method: enum in ['USE_LOCAL', 'WRITE_LOCAL', 'USE_ORIGINAL', 'WRITE_ORIGINAL'], (optional)
    :param id: Sound Name, Sound data-block name to unpack 
    :type id: string, (optional, never None)
    '''

    pass


def update_animation_flags():
    '''Update animation flags 

    '''

    pass
