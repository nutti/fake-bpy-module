class BVHTree:
    def find_nearest(self, origin, distance=1.84467e+19):
        '''Find the nearest element to a point. 

        :param co: Find nearest element to this point. 
        :type co: Vector
        :param distance: Maximum distance threshold. 
        :type distance: float
        :rtype: tuple 
        :return:  Returns a tuple (Vector location, Vector normal, int index, float distance), Values will all be None if no hit is found. 
        '''
        pass

    def find_nearest_range(self, origin, distance=1.84467e+19):
        '''Find the nearest elements to a point in the distance range. 

        :param co: Find nearest elements to this point. 
        :type co: Vector
        :param distance: Maximum distance threshold. 
        :type distance: float
        :rtype: list 
        :return:  Returns a list of tuples (Vector location, Vector normal, int index, float distance), 
        '''
        pass

    def overlap(self, other_tree):
        '''Find overlapping indices between 2 trees. 

        :param other_tree: Other tree to preform overlap test on. 
        :type other_tree: BVHTree
        :rtype: list 
        :return:  Returns a list of unique index pairs, the first index referencing this tree, the second referencing the other_tree. 
        '''
        pass

    def ray_cast(self, origin, direction, distance=sys.float_info.max):
        '''Cast a ray onto the mesh. 

        :param co: Start location of the ray in object space. 
        :type co: Vector
        :param direction: Direction of the ray in object space. 
        :type direction: Vector
        :param distance: Maximum distance threshold. 
        :type distance: float
        :rtype: tuple 
        :return:  Returns a tuple (Vector location, Vector normal, int index, float distance), Values will all be None if no hit is found. 
        '''
        pass
