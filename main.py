import math
import random

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0

def inorder(node):
    if node.left:
        inorder(node.left)
    print(node.value)
    if node.right:
        inorder(node.right)


def preorder(node):
    print(node.value)
    if node.left:
        preorder(node.left)
    if node.right:
        preorder(node.right)


def getHeight(node):
    if node:
        return node.height
    else:
        return 0


def getMin(node):
    while (node.left):
        node = node.left

    return node.value


def getMax(node):
    while (node.right):
        node = node.right

    return node.value


def deleteWholeTree(node):
    if node.left:
        deleteWholeTree(node.left)
    if node.right:
        deleteWholeTree(node.right)
    node.left = None
    node.right = None


def AVLpolowienie(tab):
    if len(tab) == 1:
        node = Node(tab[0])
        node.height = 0
    else:
        pol = math.floor(len(tab) / 2)
        node = Node(tab[pol])
        node.left = AVLpolowienie(tab[:pol])
        if len(tab) > 2:
            node.right = AVLpolowienie(tab[pol + 1:])
        
        node.height = 1 + max(node.left.height,(node.right.height if node.right else 0))
        
    return node


def BSTwstaw(val, node):
    if not node.value:
        node.value = val

    elif val < node.value:
        if node.left:
            BSTwstaw(val, node.left)
        else:
            node.left = Node(val)

    elif node.right:
        BSTwstaw(val, node.right)
    else:
        node.right = Node(val)

    node.height = 1 + max((node.left.height if node.left else 0), (node.right.height if node.right else 0))


def BSTstworz(tab, node):
    for el in tab:
        BSTwstaw(el, node)
    return node

def getBalance(node):
    if node:
        return node.left.height - node.right.height 
    return 0

def rotateR(root):
    newRoot = root.left
    temp = newRoot.right

    newRoot.right = root
    root.left = temp

    root.height = 1 + max((root.left.height if root.left else 0), (root.right.height if root.right else 0))
    newRoot.height = 1 + max((root.left.height if root.left else 0), (root.right.height if root.right else 0))

    return newRoot

def rotateL(root):
    newRoot = root.right
    temp = newRoot.left
    

    newRoot.left = root
    root.right = temp

    root.height = 1 + max((root.left.height if root.left else 0), (root.right.height if root.right else 0))
    newRoot.height = 1 + max((root.left.height if root.left else 0), (root.right.height if root.right else 0))

    return newRoot

def deleteNode(root, val, AVL):
    if not root:
        return root
    
    if val < root.value:
        root.left = deleteNode(root.left, val, AVL)
    elif val > root.value:
        root.right = deleteNode(root.right, val, AVL)
    else:
        if not root.left:
            rightofroot = root.right
            root = None
            return rightofroot
 
        elif not root.right:
            leftofroot = root.left
            root = None
            return leftofroot

        smallestinrightsub = root.right
        while smallestinrightsub.left:
            smallestinrightsub = smallestinrightsub.left

        root.value = smallestinrightsub.value

        root.right = deleteNode(root.right, smallestinrightsub.value, AVL)

        if AVL:
            balance = getBalance(root)

            # jesli balance > to przechylone w lewo
            # Case 1 - Left Left
            if balance > 1 and getBalance(root.left) <= 0:
                return rotateR(root)
    
            # Case 2 - Right Right
            if balance < -1 and getBalance(root.right) >= 0:
                return rotateL(root)
    
            # Case 3 - Left Right
            if balance > 1 and getBalance(root.left) < 0:
                root.left = rotateL(root.left)
                return rotateR(root)
    
            # Case 4 - Right Left
            if balance < -1 and getBalance(root.right) > 0:
                root.right = rotateR(root.right)
                return rotateL(root)
        
    return root

def log2(x):
    y=1
    x = x>>1
    while x>0:
        y = y << 1
        x = x >> 1

    return y

def DSW(root):
    temp = root
    n = 0

    while temp.left:
        temp = rotateR(temp)
    root = temp

    while temp.right:
        while temp.right.left:
            temp.right = rotateR(temp.right)
        n += 1
        temp = temp.right
        
    s = n - log2(n+1)
    
    root = rotateL(root)
    temp = root

    for _ in range(s):
        temp.right = rotateL(temp.right)
        temp = temp.right

    n -= s

    temp = root

    preorder(root)
    print()
    

    # teraz tu nie działa \/
    while n>1:
        n >>= 1
        for _ in range(n):
            temp = rotateL(temp)
            temp = temp.right
            preorder(root)
            print()

    return root

wybor = ""
while True:
    print("Jaki ma być ciąg wejściowy")
    print("1. Generowany przez program")
    print("2. Wpisywany przez użytkownika")
    wybor = input()
    if wybor in ["1", "2"]:
        break


dane = []
if wybor == "1":
    for _ in range(10):
        while True:
            liczba = random.randint(0, 100)
            if liczba not in dane:
                dane.append(liczba)
                break
else:
    while True:
        print("Podaj ciąg różnych liczb (n<=10)")
        dane = input().split(" ")
        try:
            dane = [int(el) for el in dane]
        except:
            continue

        if len(dane) != len(set(dane)):
            continue

        if len(dane) > 1 and len(dane) < 10:
            break

print("Twoje dane to: {}".format(dane))

root = AVLpolowienie(sorted(dane))
root2 = BSTstworz(dane, Node(None))

while True:
    print("Wybierz procedure")
    print("1 - wyszukanie w drzewie elementu o najmniejszej wartości i wypisanie ścieżki poszukiwania")
    print("2 - wyszukanie w drzewie elementu o najwiekszej wartości i wypisanie ścieżki poszukiwania")
    print("3 - usunięcie elementu drzewa o wartości klucza podanej przez użytkownika")
    print("4 - wypisanie wszystkich elementów drzewa w porządku in-order")
    print("5 - wypisanie wszystkich elementów drzewa w porządku pre-order")
    print("6 - usunięcie całego drzewa element po elemencie metodą post-order")
    print("7 - równoważenie drzewa przez rotacje")
    print("0 - zakoncz program")
    w = int(input())
    if w==0:
        break
    elif w in [1,2,3,4,5,6,7]:
        if w == 1:
            print(getMin(root))
            print()
            print(getMin(root2))
        elif w == 2:
            print(getMax(root))
            print()
            print(getMax(root2))
        elif w == 3:
            val = int(input("Podaj liczbe"))
            root = deleteNode(root, val, 1)
            preorder(root)
        elif w == 4:
            inorder(root)
            print()
            inorder(root2)
        elif w == 5:
            preorder(root)
            print()
            preorder(root2)
        elif w == 6:
            deleteWholeTree(root)
            deleteWholeTree(root2)
        elif w == 7:
            preorder(root2)
            print()
            DSW(root2)