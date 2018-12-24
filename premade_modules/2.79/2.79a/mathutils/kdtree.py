class KDTree:
    '''KdTree(size) -> new kd-tree initialized to hold size items. '''

    def balance(self):
        '''Balance the tree. 

        '''
        pass

    def find(self, co, filter=None):
        '''Find nearest point to co. 

        :param co: 3d coordinates. 
        :type co: float triplet
        :param filter: function which takes an index and returns True for indices to include in the search. 
        :type filter: callable
        :rtype: tuple 
        :return:  Returns (Vector, index, distance). 
        '''
        pass

    def find_n(self, co, n):
        '''Find nearest n points to co. 

        :param co: 3d coordinates. 
        :type co: float triplet
        :param n: Number of points to find. 
        :type n: int
        :rtype: list 
        :return:  Returns a list of tuples (Vector, index, distance). 
        '''
        pass

    def find_range(self, co, radius):
        '''Find all points within radius of co. 

        :param co: 3d coordinates. 
        :type co: float triplet
        :param radius: Distance to search for points. 
        :type radius: float
        :rtype: list 
        :return:  Returns a list of tuples (Vector, index, distance). 
        '''
        pass

    def insert(self, co, index):
        '''Insert a point into the KDTree. 

        :param co: Point 3d position. 
        :type co: float triplet
        :param index: The index of the point. 
        :type index: int
        '''
        pass

    def __init__(self, size):
        '''

        '''
        pass
