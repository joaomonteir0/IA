from tree_search import *
from cidades import *
from blocksworld import *

def func_branching(connections,coordinates):
    #IMPLEMENT HERE
    #print(connections)
    cities = []
    for city in coordinates:
        cities.append(city)

    count = 0
    for city in cities:
        for con in connections:
            if city == con[0]:
                #print(f"{city} tem conexão em {con[1]}")
                count+=1
            if city == con[1]:
                #print(f"{city} tem conexão em {con[2]}")
                count+=1
    
    #print(f"Number of neighboors: {n_neighboor}")
    #print(f"Number of cities: {len(coordinates)}")
    
    return count/len(coordinates) - 1

class MyCities(Cidades):
    def __init__(self,connections,coordinates):
        super().__init__(connections,coordinates)
        # ADD CODE HERE IF NEEDED

class MySTRIPS(STRIPS):
    def __init__(self,optimize=False):
        super().__init__(optimize)

    def simulate_plan(self,state,plan):
        #IMPLEMENT HERE
        pass

 
class MyNode(SearchNode):
    def __init__(self,state,parent,arg3=None,arg4=None,arg5=None):
        super().__init__(state,parent)
        #ADD HERE ANY CODE YOU NEED
        self.cost = 0
        self.heuristic = 0
        self.depth = 0

class MyTree(SearchTree):

    def __init__(self,problem, strategy='breadth',optimize=0,keep=0.25): 
        super().__init__(problem,strategy)
        #ADD HERE ANY CODE YOU NEED

    def astar_add_to_open(self,lnewnodes):
        #IMPLEMENT HERE
        pass

    # remove a fraction of open (terminal) nodes
    # with lowest evaluation function
    # (used in Incrementally Bounded A*)
    def forget_worst_terminals(self):
        #IMPLEMENT HERE
        pass

    # procurar a solucao
    def search2(self):
        #IMPLEMENT HERE
        while self.open_nodes != []:
            node = self.open_nodes.pop(0)
            if self.problem.goal_test(node.state):
                self.solution = node
                self.terminals = len(self.open_nodes)+1
                return self.get_path(node)
            lnewnodes = []
            self.non_terminals += 1
            for a in self.problem.domain.actions(node.state):
                newstate = self.problem.domain.result(node.state,a)
                cost_node = self.problem.domain.cost(node.state, a)
                newnode = SearchNode(newstate,node, node.depth+1, node.cost + cost_node,self.problem.domain.heuristic(newstate, self.problem.goal), a)
                if not node.in_parent(newstate):
                   lnewnodes.append(newnode)
            self.add_to_open(lnewnodes)

        pass

# If needed, auxiliary functions can be added




