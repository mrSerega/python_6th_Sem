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

def remove_edge(index):
    it_left = H[I[index]]
    it_right = H[J[index]]
    if it_left == index: 
        H[it_left] = L[H[it_left]]
    else:
        while(L[it_left]!=index):
            it_left = L[it_left]
            if it_left == -1: return
        L[it_left] = L[L[it_left]] 
    if it_right == index: 
        H[it_right] = L[H[it_right]]
    else:
        while(L[it_right]!=index):
            it_right = L[it_right]
            if it_right == -1: return
        L[it_right] = L[L[it_right]] 

def print_lists():
    print(I)
    print(J)
    print(H)
    print(L)

def make_norm_graph(G):
    G.clear()
    for i in range(len(H)):
        G.add_node(i)
        it = H[i]
        while(it!=-1):
            G.add_edge(I[it],J[it])
            it = L[it]
