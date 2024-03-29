from parcoursSeul import *
from parcoursPlusieurs import *
import time

case_dep = 1
# case_dep = random.randint(1,LONGUEUR*LARGEUR) ****Pour avoir une case random****

print("------------Non-Heuristique Seul------------\n")

chemins = []
c1 = time.process_time()
parcoursSeulNonHeuristique(case_dep, chemins, grapheSeul())
c2 = time.process_time()
cpu = c2-c1

affichageS(chemins, cpu, case_dep)


print("------------Heuristique Seul------------\n")

chemins = []
c1 = time.process_time()
parcoursSeulHeuristique(case_dep, chemins, grapheSeul())
c2 = time.process_time()
cpu = c2-c1

affichageS(chemins, cpu, case_dep)


print("------------Non-Heuristique Plusieurs------------\n")

c1 = time.process_time()
chemins = parcoursNonHeuristique(case_dep, graphe())
c2 = time.process_time()
cpu = c2-c1

affichageP(chemins, cpu, case_dep)


print("------------Heuristique Plusieurs------------\n")

c1 = time.process_time()
chemins = parcoursHeuristique(case_dep, graphe())
c2 = time.process_time()
cpu = c2-c1

affichageP(chemins, cpu, case_dep)