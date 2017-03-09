I = [] #
J = [] #
H = [] #heads
L = [] #links

count = 0

def set_num_of_nodes(num):
    for i in range(num):
         H.append(-1)

def add_edge(left, right):
    global count #cause python
    I.append(left)
    J.append(right)
    L.append(-1)
    it = H[left]
    if it!=-1:
        while(L[it]!=-1):
            it = L[it]
        L[it]=count
        count+=1
    else:
        H[left] = count
        count+=1

def print_lists():
    print(I)
    print(J)

def make_norm_graph(G):
    G.clear()
    for i in range(len(H)):
        G.add_node(i)
        it = H[i]
        while(it!=-1):
            G.add_edge(I[it],J[it])
            it = L[it]
