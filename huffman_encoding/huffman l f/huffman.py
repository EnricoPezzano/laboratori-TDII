import math
import os
class node:
	def __init__(self, frequenza, symbol, left=None, right=None):
		self.frequenza = frequenza

		self.symbol = symbol

		self.left = left

		self.right = right

		self.huff = ''


# calcola l’entropia di Shannon H(X)
def Entropy(x):
	entr = 0
	for y in range(len(x)):
		entr = entr+ ((x[y])/100000)*((math.log((1/(x[y]/100000)),2)))
	return entr

def findCod(node, ch, w, val=''):		# cerco la codifica del carattere e la stampo
	newVal = val + str(node.cod)		# ogni volta che scendo di un livello alla codifica viene aggiunto uno 0 o un 1
	if(node.left):
		findCod(node.left, ch, w, newVal)
	if(node.right):
		findCod(node.right, ch, w, newVal)
	# ho raggiunto una foglia dell'albero (solo le foglie ontengono delle codifiche)
	if(node.left==None and node.right==None and node.car == ch):		# se è la codifica del carattere che stavo cercando
		w.write(newVal)		# la stampo nel file destinazione
		codifica[node.car] = len(newVal)		# aggiungo al dizionario per ogni carattere la lunghezza della sua codifica



cod={}
cod2={}

def printNodes(node, val=''):
	newVal = val + str(node.huff)
	if(node.left):
		printNodes(node.left, newVal)
	if(node.right):
		printNodes(node.right, newVal)

	if(not node.left and not node.right):
		cod[node.symbol]=newVal


def lunghezzacaratteri():
	for item in cod:
		cod2[item]=len(cod[item])
	return cod2


def lunghezzaAttesa():
	l=0
	for item in dizcf:
		l=l+(dizcf[item]/100)*cod2[item]
	return l

def compressionefile(fileName, cod):

	fIn = open(fileName, "r")
	fOut = open("file.txt", "w")
	valcomp = 0;
	while 1:
		s = fIn.read(1)
		if not s:
			break
		valcomp = valcomp + len(cod[s])
		fOut.write(cod[s]);
	fIn.close();
	fOut.close();
	return valcomp
caratteri=[]
frequenza=[]
occorrenze=[]
ausiliario=[]
dizcf={}
fileName="text.txt" ---
with open(fileName, "r") as f: #salvo tutto il file in una lista
  for line in f.readlines():
      for x in range(0,len(line)):
        caratteri.append((line[x]))
f.close() #chiusura file
tot=0
empty
for x in range(0,len(ausiliario)):
	dizcf[ausiliario[x]]=frequenza[x]
	tot=tot + frequenza[x]
for x in range(len(frequenza)):
	print('Il carattere', ausiliario[x], "    volte:  ", occorrenze[x],' con una probabilita\' del:', frequenza[x], '%')
nodes = []
resultantListchar = []

for element in caratteri:
    if element not in resultantListchar:
        resultantListchar.append(element)
for x in range(0,len(resultantListchar)):
	nodes.append(node(frequenza[x], resultantListchar[x]))

while len(nodes) > 1:
	nodes = sorted(nodes, key=lambda x: x.frequenza)
	left = nodes[0]
	right = nodes[1]
	left.huff = 0
	right.huff = 1
	newNode = node(left.frequenza+right.frequenza, left.symbol+right.symbol, left, right)
	nodes.remove(left)
	nodes.remove(right)
	nodes.append(newNode)
printNodes(nodes[0])
entropia=Entropy(occorrenze)
print("l'entropia vale : ",entropia)
cod2=lunghezzacaratteri()
print('La lunghezza attesa della codifica e\':', round(lunghezzaAttesa(), 2))
compressione=compressionefile(fileName, cod)
print('La compressione è\':', compressione)
