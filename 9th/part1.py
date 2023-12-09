_EXAMPLE = [[0,3,6,9,12,15], [1,3,6,10,15,21], [10,13,16,21,30,45]]

def read_file(filename: str) -> list: 
    with open(filename, 'r') as file:
        return file.readlines()