def new():
    '''

    :return:  a new preview collection. 
    '''

    pass


def remove(pcoll):
    '''Remove the specified previews collection. 

    :param pcoll: Preview collection to close. 
    :type pcoll: ImagePreviewCollection
    '''

    pass


class ImagePreviewCollection:
    '''This is a subclass of Python’s built-in dict type, used to store multiple image previews. '''

    def clear(self):
        '''Clear all previews. 

        '''
        pass

    def close(self):
        '''Close the collection and clear all previews. 

        '''
        pass

    def load(self, name, filepath, filetype, force_reload=False):
        '''Generate a new preview from given file path, or return existing one matching name. 

        :param name: The name (unique id) identifying the preview. 
        :type name: string
        :param filepath: The file path to generate the preview from. 
        :type filepath: string
        :param filetype: The type of file, needed to generate the preview in [‘IMAGE’, ‘MOVIE’, ‘BLEND’, ‘FONT’]. 
        :type filetype: string
        :param force_reload: If True, force running thumbnail manager even if preview already exists in cache. 
        :type force_reload: bool
        :rtype: bpy.types.ImagePreview 
        :return:  The Preview matching given name, or a new empty one. 
        '''
        pass

    def new(self, name):
        '''Generate a new empty preview, or return existing one matching name. 

        :param name: The name (unique id) identifying the preview. 
        :type name: string
        :rtype: bpy.types.ImagePreview 
        :return:  The Preview matching given name, or a new empty one. 
        '''
        pass
