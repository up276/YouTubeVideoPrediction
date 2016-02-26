
class VideoAnalysisException(Exception):
    '''
    User defined exception for the region class
    '''
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)