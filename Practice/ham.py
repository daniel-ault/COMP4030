
import graph

G = graph.UUG()
G.add(1,2); G.add(1,5); G.add(2,3); G.add(3,4); 
G.add(2,7); G.add(2,8); G.add(3,8); G.add(4,9);
G.add(5,6); G.add(5,10); G.add(6,7); G.add(6,11);
G.add(7,8); G.add(8,9); G.add(10,11); G.add(11,12);
G.add(9,12);

G.add(1,12)

#G = graph.UUG()
#G.add(1,2); G.add(2,3); G.add(3,4); G.add(4,1)

N = len(G.vertices)
solution = [-1]*N

# generate all Ham circuits from the current config solutions[0..i]
def Ham(i):
	if promising(i):
		if i==N-1:
			print(solution)
		else:
			for j in range(N):
				if j not in solution[0:i+1]:
					solution[i+1] = j
					Ham(i+1)


def promising(i):
	if i>0 and G[solution[i-1]+1, solution[i]+1] == False:
		return False
	if i==N-1 and G[solution[N-1]+1, solution[0]+1] == False:
		return False
	return True


Ham(-1)




# generate all permutations from current config solutions [0..i]
def Perm(i):
	if i==N-1:
		print(solution)
	else:
		for j in range(N):
			if j not in solution[0:i+1]:
				solution[i+1] = j
				Perm(i+1)

#Perm(-1)
