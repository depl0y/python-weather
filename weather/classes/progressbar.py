from math import *        

class Progressbar:
    @staticmethod
    def loadingBar(i, N, size):
        import sys
        
        percent = float(i) / float(N)
        sys.stdout.write("\r"
                     + str(int(i)).rjust(3, '0')
                     +"/"
                     +str(int(N)).rjust(3, '0')
                     + ' ['
                     + '='*ceil(percent*size)
                     + ' '*floor((1-percent)*size)
                     + ']')