class Tail:
    @staticmethod
    def get(filename, lines):
        import os

        if lines == 0:
            return []

        block_counter = -1
        buffer = 4098
        result = []

        with open(filename) as file:
            while len(result) < lines:
                try:
                    file.seek(block_counter * buffer, os.SEEK_END)
                except IOError:
                    file.seek(0)
                
                    result = file.readlines()
                    break
        
                result = file.readlines()
                block_counter -= 1
    
            return result[-lines:]                
