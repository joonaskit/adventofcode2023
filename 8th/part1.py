class Node:
    def __init__(self, name: str, left = None, right = None) -> None:
        self.name = name
        self.right = right
        self.left = left

    def set_left(self, left: "Node"):
        self.left = left
    
    def set_right(self, right: "Node"):
        self.right = right
    
    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
    
    def get_name(self):
        return self.name
    
    def __str__(self) -> str:
        return f"Node: {self.name}; left {self.get_left()} - right {self.get_right()}"
    
    def __eq__(self, other: "Node"):
        if isinstance(other, self.__class__):
            return self.get_name() == other.get_name()
        else:
            return False
    
    def __repr__(self) -> str:
        return f"{self.get_name()}"

def read_file(filename: str):
    with open(filename, 'r') as file:
        return file.readlines()

def parse_line(line: str):
    tmp = line.split(" = ")
    name = tmp[0].strip()
    childs = tmp[1].split(", ")
    left = childs[0][1:]
    right = childs[1].strip()[0:-1]
    return name, left, right

def parse_lines(lines: list):
    nodes = []
    for line in lines: 
        if line == '' or line == '\n':
            continue
        else:
            name, left, right = parse_line(line)
            node = Node(name, Node(left), Node(right))
            if node not in nodes:
                nodes.append(node)
    return nodes

def loop(nodes: list, directions: list):
    node = ""
    for test in nodes:
        if test.get_name() == "AAA":
            node = test
            break
    not_found = True
    end = Node("ZZZ", None, None)
    steps = 0
    while not_found:
        for direction in directions:
            if node != end:
                if direction == "L":
                    node = nodes[nodes.index(node.get_left())]
                elif direction == "R":
                    node = nodes[nodes.index(node.get_right())]
                steps += 1
            else:
                not_found = False
                break
    return steps

    
def main():
    lines = read_file("8th/input.txt")
    directions = list(lines.pop(0).strip())
    lines.pop(0)
    nodes = parse_lines(lines)
    for node in nodes:
        print(node)
    print(directions)
    print(lines)
    print(f"Steps: {loop(nodes, directions)}")
    

main()