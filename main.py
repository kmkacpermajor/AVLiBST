# Klasa reprezentujaca pojedynczy wezel drzewa
import math
import random


class Node:
    def __init__(self, value):
        # Wartosc przechowywana w wezle
        self.value = value
        # Lewy syn
        self.left = None
        # Prawy syn
        self.right = None
        # Poziom danego elementu
        self.height = 0


# Rekurencyjne przeszukiwanie drzewa
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
    while(node.left):
        node = node.left
 
    return node

def getMax(node):
    while(node.right):
        node = node.right
 
    return node

def deleteWholeTree(node):
    if node.left:
        deleteWholeTree(node.left)
    if node.right:
        deleteWholeTree(node.right)
    node.left = None
    node.right = None

def AVLpolowienie(tab, prevh):
    if len(tab) != 1:
        pol = math.floor(len(tab)/2)
        root = Node(tab[pol])
        root.height = prevh + 1
        if len(tab) > 2:
            root.right = AVLpolowienie(tab[pol+1:], root.height)
        root.left = AVLpolowienie(tab[:pol], root.height)
        
    else:
        root = Node(tab[0])
        root.height = prevh + 1
    
    return root
        
        
        
wybor = "" 
while True:
    print("Jaki ma być ciąg wejściowy")
    print("1. Generowany przez program")
    print("2. Wpisywany przez użytkownika")
    wybor = input()
    if wybor in ["1","2"]:
        break

dane = []
if wybor == "1":
    for _ in range(10):
        dane.append(random.randint(0, 100))
else:
    while True:
        print("Podaj ciąg liczb (n<=10)")
        dane = input().split(" ")
        dane = [int(el) for el in dane]
        if len(dane) > 1 and len(dane)<10:
            break

print("Twoje dane to: {}".format(dane))

    

# Korzen drzewa
root = AVLpolowienie([1,2,3,4,5,6,7,8,9], 0)

# Przeszukujemy drzewo w kolejnosci in-order
inorder(root)