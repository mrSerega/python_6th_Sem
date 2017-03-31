import good_kruskal as gk
import bad_kruskal as bk

def main():
	n = 7 #input here
	arcs = [(3,0,1),(1,0,2),(2,0,4),(7,0,5),(9,1,2),(2,2,3),(8,2,4),(4,3,4),(5,3,6),(5,4,5),(7,4,6),(4,5,6)] #input here
	parents = []
	res = gk.good_kruskal(arcs,7, parents)

	bk.bad_kruskal(arcs, 7)

if __name__ == '__main__':
	main()
