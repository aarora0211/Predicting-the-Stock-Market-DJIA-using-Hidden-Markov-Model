'''
Akshit Arora, Sheershak Agarwal
HMM.py
Implements the forward and viterbi algorithm
Prints the Trellis diagram on the shell

function FORWARD(observations of len T, state-graph of len N) returns forward-prob
	
	create a probability matrix forward[N,T]
	for each state s from 1 to N do ; initialization step
		forward[s,1] ← π_s ∗ b_s(o_1)
	for each time step t from 2 to T do ; recursion step
		for each state s from 1 to N do
			forward[s,t]← ∑(from s'= 1 to N) of forward[s',t −1] ∗ a_s',s ∗ b_s(o_t)
	forwardprob ←  ∑(from s = 1 to N) of forward[s,T] ; termination step
return forwardprob
'''
def forward(obs, states, start_p, trans_p, emit_p):
        F = [{}]
        # Initialize base cases (t == 0)
        for y in states:
                F[0][y] = start_p[y] * emit_p[y][obs[0]]
                # Run Forward algorithm for t > 0
        for t in range(1, len(obs)):
                F.append({})
                for y in states:
                        F[t][y] = sum((F[t-1][y0] * trans_p[y0][y] * emit_p[y][obs[t]]) for y0 in states)
        forwardprob = sum((F[len(obs) - 1][s]) for s in states)
        return forwardprob

'''
function VITERBI(observations of len T,state-graph of len N) returns best-path, path-prob
	create a path probability matrix viterbi[N,T]
	for each state s from 1 to N do ; initialization step
		viterbi[s,1] ← π_s ∗ b_s(o_1)
		backpointer[s,1] ← 0
	for each time step t from 2 to T do ; recursion step
		for each state s from 1 to N do
			viterbi[s,t] ← max(from s'= 1 to N) of viterbi[s',t −1] ∗ a_s',s ∗ b_s(o_t)
			backpointer[s,t] ← argmax(from s'= 1 to N) of viterbi[s',t −1] ∗ a_s',s ∗ b_s(o_t)

	bestpathprob ← max(from s = 1 to N) of viterbi[s,T] ; termination step
	bestpathpointer ← argmax(from s = 1 to N) of viterbi[s,T] ; termination step
	bespath ← the path starting at statbe bestpathpointer, that follows backpointer[] to states back in time
return bestpath, bestpathprob
'''
def viterbi(obs, states, start_p, trans_p, emit_p):
        V = [{}]
        path = {}
        # Initialize base cases (t == 0)
        for y in states:
                V[0][y] = start_p[y] * emit_p[y][obs[0]]
                path[y] = [y]
        # Run Viterbi for t > 0
        for t in range(1,len(obs)):
                V.append({})
                newpath = {}
                for y in states:
                        (prob, state) = max([(V[t-1][y0] * trans_p[y0][y] * emit_p[y][obs[t]], y0) for y0 in states])
                        V[t][y] = prob
                        newpath[y] = path[state] + [y]
                # Don't need to remember the old paths
                path = newpath
        print_brief_fns(obs, V)
        (prob, state) = max([(V[len(obs) - 1][y], y) for y in states])
        return (prob, path[state])

# Prints sequence of belief functions in a sort of vertical format using print statements
def print_brief_fns(obs, V):
        s = "             "
        space = []
        temp_space = ""
        space.append(temp_space)
        for i in obs:
                s = s + i + "   "
                for j in range(1, len(i) - 6):
                        temp_space += " ";
                space.append(temp_space)
        s = s + '\n'
        for y in V[0]:
                s += y
                for i in range(len(y), 14):
                        s = s + " ";
                for index in range(0,len(obs)):
                        s = s + space[index] + str(round(V[index][y], 3)) + "      "
                s += "\n"
        print("\n Trellis diagram for the Dataset is: \n")
        print(s)
        print("\n")

