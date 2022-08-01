class Tree:
    """A rooted binary tree"""
    def __init__(self):
        self.root = None
        self.left = None
        self.right = None

def is_empty(tree: Tree) -> bool:
        """Return True if and only if tree is empty."""
        return tree.root == tree.left == tree.right == None

def join(item: object, left: Tree, right: Tree) -> Tree:
    """Return a tree with the given root and subtrees."""
    tree = Tree()
    tree.root = item
    tree.left = left
    tree.right = right
    return tree
	
"""Construction of Morse binary tree"""	
EMPTY = Tree()
H = join('H',EMPTY,EMPTY)
V = join('V',EMPTY,EMPTY)
F = join('F',EMPTY,EMPTY)
L = join('L',EMPTY,EMPTY)
P = join('P',EMPTY,EMPTY)
J = join('J',EMPTY,EMPTY)
B = join('B',EMPTY,EMPTY)
X = join('X',EMPTY,EMPTY)
C = join('C',EMPTY,EMPTY)
Y = join('Y',EMPTY,EMPTY)
Z = join('Z',EMPTY,EMPTY)
Q = join('Q',EMPTY,EMPTY)
S = join('S',H,V)
U = join('U',F,EMPTY)
R = join('R',L,EMPTY)
W = join('W',P,J)
D = join('D',B,X)
K = join('K',C,Y)
G = join('G',Z,Q)
O = join('O',EMPTY,EMPTY)
I = join('I',S,U)
A = join('A',R,W)
N = join('N',D,K)
M = join('M',G,O)
E = join('E',I,A)
T = join('T',N,M)
MORSE = join('START',E,T)

def encode_letter(tree: Tree,letter: str) -> str:
    "encode a given letter into a string of dots and dashes, the Morse code equivalent of the given letter"
    dotsdashes = []
    getMorseCode(tree, letter,dotsdashes)
    code = "".join(dotsdashes)
    print(code)

def getMorseCode(tree: Tree, letter: str,dotsdashes: list):
     
    if is_empty(tree) == True:
        return False
    elif tree.root==letter:
        return True
    else:
        if getMorseCode(tree.left, letter,dotsdashes)==True:
            dotsdashes.insert(0,".")
            return True
        elif getMorseCode(tree.right, letter,dotsdashes)==True:
            dotsdashes.insert(0,"-")
            return True
			
def encode(text) -> list:
    "encode a given non-empty string, text, into a list of Morse code letters"
    for letter in text:
        encode_letter(MORSE,letter)
    
	
preString = input("Enter String to wish to be converted to morse code:")
encode(preString)
