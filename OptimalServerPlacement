def findSeq(array, NX, X):
    X[-1][0] = array[-1]
    X[-2][0] = array[-2] + X[-1][0]
    X[-2][1] = "x"
    NX[-2][0] = 1 + array[-1]
    NX[-2][1] = "x"
    NX[-2][2] = 1

    i = len(array) - 3
    while i >= 0:
        x = array[i] + X[i+1][0]
        nx = array[i] + NX[i+1][0]
        X[i][0] = min(x, nx)
        if x < nx:
            X[i][1] = "x"
        else:
            X[i][1] = "nx"
        nx2 = NX[i+1][0] + NX[i+1][2]+1
        x2 = X[i+1][0] + 1
        NX[i][0] = min(x2, nx2)
        if x2 < nx2:
            NX[i][1] = "x"
            NX[i][2] = 1
        else:
            NX[i][1] = "nx"
            NX[i][2] = NX[i+1][2] + 1
        i -= 1

    val = 0
    result = ""
    if X[0][0] < NX[0][0]:
        result += "Place, "
        val = X[0][1]
    else:
        result += "Don't Place, "
        val = NX[0][1]


    for i in range(1, len(array)): //Generates a Place/Not Place string based off the nx or x values
        if val == "x":
            result += "Place, "
            if X[i][1] == "x":
                val = X[i][1]
            else:
                val = NX[i][1]
        else:
            result += "Don't Place, "
            if NX[i][1] == "x":
                val = NX[i][1]
            else:
                val = X[i][1]
    print(result)


array = [4,2,15,13,80]
#array = [1000, 1000,1000, 4,1000,1000,10]
NX = [([0,"",0]) for i in range( len(array))]
X = [[0,"",0] for i in range(len(array))]
#print (len(array))
#print(X)
#print(NX)
findSeq(array, NX, X)

--------------------------------------------------------------------------------
Explanation:
	The algorithm above starts on the far right side and assigns a tuple with the parameters: (current value in sequence,  Place or not to place (N or NX),  Value to be added if not placed).
	As a result the algorithm calculates the costs of placing versus the cost of adding the cost to move to the next node. From there it then takes the minimum for each of the possibilities for placing or accessing the next node. This then iterates and ends up with the final minimum value of placement on in the array NX[0][0] or in X[0][0] with the minimum of the two holding the final value. Therefore, we then retrace back through the two arrays based on the transition from nx - x values, so that the optimal sequence is deduced.

****this code is runnable python code and give the optimal values for all test cases****
*****It also returns whether or not to place****


Runtime:

	The runtime of this algorithm is O(n) as to populate both of the lists with be O(n), and to retrace back through an array of n size O(n) resulting in O(2n) or O(n)

Proof:
	Basecase: n = 1:
		We place at S[0] and we have the most optimal solution. This is evident.
	Else:
		Pi = the total opt cost by placing at i
		Ni = The total opt cost with no placement at i
		Ai = Access Cost
		Ci = Placement Cost
		OPT(i) = min(Ci + min(Pi+1, Ni+1), ai + min(Pi+1, Ni+1))

		Cases that OPT(i) considers:
1.	Place from a previous placement
2.	Place from a previous access
3.	Access from a previous placement
4.	Access from a previous access
^See below for explanation
	Because of the recursive nature of OPT(i), we always result in having an optimal value of i returned, as we check for all of the combinations for the most optimal case these cases being the previous two optimal cases, each being permuted with both placement and access costs, resulting in 4 cases, of which we choose the two minimum ones, for both a placement and an access. Therefore, we maintain OPT(i) for all I, as we check for all possible optimal combinations for producing a minimum cost.
	
	
	
