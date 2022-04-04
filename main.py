import math
import random

class Node:
    def __init__(self, value):
        self.value = value # wartość
        self.left = None # lewy syn
        self.right = None # prawy syn
        self.treeheight = 0 # wysokość drzewa

def AVLpolowienie(tab):                     
    if len(tab) == 1:           
        node = Node(tab[0])                 # tworzymy nowy węzeł dla jedynego elementu w pozostałej tablicy
        node.treeheight = 0                     # który jest na najniższym poziomie
    else:
        pol = math.floor(len(tab) / 2)          # wybieramy środkowy indeks
        node = Node(tab[pol])                   # tworzymy nowy węzeł dla elementu na środkowym indeksie
        node.left = AVLpolowienie(tab[:pol])    # rekurencyjnie wywołujemy funkcję przypisania dla lewego dziecka 
        if len(tab) > 2:                                # jeśli istnieją przynajmniej 2 elementy (bo [pol] to element prawy w 2 el tablicy)
            node.right = AVLpolowienie(tab[pol + 1:])   # rekurencyjnie wywołujemy funkcję przypisania dla prawego dziecka 
        node.treeheight = 1 + max(node.left.treeheight, node.right.treeheight)
    return node                                    # zwracamy korzeń do przypisania

def BSTstworz(tab, node):
    for el in tab:
        BSTwstaw(el, node)
    return node

def BSTwstaw(val, node):
    if not node.value:      # jeśli węzeł nie ma nadanej wartości (pierwszy)
        node.value = val    # value = val

    elif val < node.value:          # jak jest mniejsze to sprawdzamy lewe dziecko
        if node.left:                       # jeśli już istnieje
            BSTwstaw(val, node.left)    # idziemy rekurencyjnie w dół w lewo
        else:                               # jeśli nie
            node.left = Node(val)       # tworzymy nowy węzeł
                                    # jak jest większe to sprawdzamy prawe dziecko
    elif node.right:                        # jeśli już istnieje 
        BSTwstaw(val, node.right)       # idziemy rekurencyjnie w dół w prawo
    else:                                   # jeśli nie
        node.right = Node(val)          # tworzymy nowy węzeł

def getHeight(node):
    if node:
        return node.height
    else:
        return 0


def getMin(node):             # idziemy do najbardziej lewego elementu
    print(node.value)
    while (node.left):
        node = node.left
        print(node.value)

    return node

def getMax(node):               # idziemy do najbardziej prawego elementu
    print(node.value)
    while (node.right):
        node = node.right
        print(node.value)

    return node

def deleteNode(root, val, AVL):
    if val < root.value:            # do usunięcia mniejsza niż aktualna 
        root.left = deleteNode(root.left, val, AVL) # zchodzimy rekurencyjnie w dół
    elif val > root.value:          # do usunięcia większa niż aktualna 
        root.right = deleteNode(root.right, val, AVL) # zchodzimy rekurencyjnie w prawo
    else:                           # do usunięcia właśnie ta
        if not root.left and not root.right:    # jeśli nie ma dzieci
            return None                             # usuwany
        
        elif not root.left:                     # jeśli nie ma lewego dziecka 
            rightofroot = root.right                # to prawe jest nowym korzeniem
            root = None                             # stary korzeń usuwamy
            return rightofroot                      # zwracamy do przypisania nowy
 
        elif not root.right:                    # jeśli nie ma prawego dziecka
            leftofroot = root.left                  # to lewe jest nowym korzeniem
            root = None                             # stary korzeń usuwamy
            return leftofroot                       # zwracamy do przypisania nowy

        else:                                   # jeśli ma dwoje dzieci
            smallestinrightsub = root.right         
            while smallestinrightsub.left:
                smallestinrightsub = smallestinrightsub.left                   # bierzemy najmniejsze dziecko w prawym poddrzewie

            root.value = smallestinrightsub.value                              # przypisujemy /\ wartość do korzenia 

            root.right = deleteNode(root.right, smallestinrightsub.value, AVL) # i usuwamy podwojoną wartość w prawym poddrzewie
        
    return root

def inorder(node):              # L K P
    if node.left:
        inorder(node.left)
    print(node.value)
    if node.right:
        inorder(node.right)

 
def preorder(node):             # K L P
    print(node.value)
    if node.left:
        preorder(node.left)
    if node.right:
        preorder(node.right)

def deleteWholeTree(node):      # przechodzimy przez drzewo od góry
    if node.left:
        deleteWholeTree(node.left)  # i rekurencyjnie schodzimy w dół 
    if node.right:
        deleteWholeTree(node.right)
    node.left = None                # jak nie ma gdzie dalej to usuwamy
    node.right = None

    return None

def rotateR(root):
    newRoot = root.left         # nowy korzeń jest lewym dzieckiem obecnego
    temp = newRoot.right        # zapisujemy prawe dziecko nowego korzenia

    newRoot.right = root        # nadpisujemy je poprzednim korzeniem
    root.left = temp            # prawe dziecko nowego korzenia staje się lewym dzieckiem prawego (starego korzenia)

    return newRoot

def rotateL(root):
    newRoot = root.right        # nowy korzeń jest prawego dzieckiem obecnego
    temp = newRoot.left         # zapisujemy lewe dziecko nowego korzenia
    
    newRoot.left = root         # nadpisujemy je poprzednim korzeniem
    root.right = temp           # lewe dziecko nowego korzenia staje się prawym dzieckiem lewego (starego korzenia)

    return newRoot

def log2(x):    # 2^log2 ( x ), pozostawiamy największy bit w liczbie
    y = 1
    x = x>>1
    while x>0:
        y = y << 1
        x = x >> 1

    return y

def DSW(root):
    newRoot = root     # kopiujemy korzeń
    n = 0           # rozpoczynami zliczanie węzłów

    while newRoot.left:             # dopóki węzeł ma lewego syna
        newRoot = rotateR(newRoot)      # to obracamy go w prawo
    root = newRoot                  # i nadpisujemy stary korzeń nowym
    n += 1                          # i zliczamy go do liczby

    temp = root                     # kopiujemy korzeń

    while temp.right:               # przechodzimy drzewo w prawo
        while temp.right.left:          # dopóki węzeł ma lewe dziecko
            temp.right = rotateR(temp.right) # obracamy go w prawo
        n += 1                      # zliczamy węzeł
        temp = temp.right           # i schodzimy dalej
    
    s = n + 1 - log2(n+1)           # wyznaczamy początkową liczbę obrotów

    for i in range(s):      # s razy
        if i == 0:              # aby nie stracić korzenia
            root = rotateL(root)    # obracamy węzeł w lewo i nadpisujemy korzeń
            temp = root             # kopiujemy korzeń
        else:
            temp.right = rotateL(temp.right)    # obracamy w prawo prawe dziecko
            temp = temp.right                   # i pomijamy jeden element

    n -= s                  # pomniejszamy liczbę obrotów o s

    temp = root             # kopiujemy korzeń

    while n > 1:    # to samo co wyżej tylko zmniejszamy n >> 1
        n >>= 1
        temp = root     # cały czas kopiujemy nowy korzeń powstały w wyniku rotacji
        for i in range(n):
            if i == 0:
                temp = rotateL(temp)
                root = temp
            else:
                temp.right = rotateL(temp.right)
                temp = temp.right

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

        if len(dane) > 1 and len(dane) <= 10:
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
            getMin(root)
            print()
            getMin(root2)
        elif w == 2:
            getMax(root)
            print()
            getMax(root2)
        elif w == 3:
            while True:
                ile = int(input("Podaj ile elementów chcesz usunąć: "))
                if ile <= len(dane):
                    break
            
            for _ in range(ile):
                val = int(input("Podaj jaki element chcesz usunąć: "))
                root = deleteNode(root, val, 1)
                root2 = deleteNode(root2, val, 1)
        elif w == 4:
            inorder(root)
            print()
            inorder(root2)
        elif w == 5:
            preorder(root)
            print()
            preorder(root2)
        elif w == 6:
            root = deleteWholeTree(root)
            root2 = deleteWholeTree(root2)
        elif w == 7:
            root = DSW(root)
            root2 = DSW(root2)