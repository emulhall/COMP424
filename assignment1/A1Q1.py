from collections import deque
import copy
import heapq
class Node:
	def __init__(self, parent, value):
		self.parent=parent
		self.value=value
		self.children=[]

#state = [l_t, c_t, r_t, l_b, c_b, r_b]
#part A
#transitions have unit cost
#ensure that states that have been explored are not added to the search queue
#algorithm should prefer the state that involves moving a lower numbered piece
#initial_state = State(1, 4, 2, 5, 3, None)
i_state= [1, 4, 2, 5, 3, None]
g_state = [None, 1, 2, 5, 4, 3]

'''
possible moves:
[None, ....]
-swap none and [1] or swap none and [3]

[a,None,...]
-swap none and [0] or swap none and [2] or swap none and [4]

[a, b, None,...]
-swap none and [1] or swap none and [5]

[a, b, c, None...]
-swap none and [0] or swap none and [4]

[a, b, c, d, None...]
-swap none and [1] or swap none and [3] or swap none and [5]

[a, b, c, d, e, None]
-swap none and [2] or swap none and [4]
'''

def place_of_none(s):
	i=0
	for element in s:
		if element == None:
			return i
		else:
			i=i+1

def swap(i, g, state):
	output=copy.copy(state)
	output[i]=state[g]
	output[g]=state[i]
	return output
#a part 1
def bfs_dfs(initial, goal, key):
	visited=[]
	start=Node(None, initial)
	visited.append(start)
	visit=[start]
	to_visit=deque(visit)
	to_visit_values=[]
	options={0 : [1, 3], 1 : [0, 2, 4] , 2 : [1, 5], 3 : [0, 4], 4 : [1, 3, 5], 5: [2, 4]}
	while len(to_visit)>0:
		if key=='dfs':
			current=to_visit.pop()
		else:
			current=to_visit.popleft()
		if goal==current.value:
			return path(current, initial)
		location=place_of_none(current.value)
		switches=options[location]
		for element in switches:
			temp=current.value
			new=swap(location, element, temp)
			current.children.append(Node(current, new))
		for child in current.children:
			if child in visited:
				continue
			if child.value not in to_visit_values:
				to_visit.append(child)
				to_visit_values.append(child.value)
		visited.append(current)

def uniform_cost_search(initial, goal):
	visited=[]
	start=Node(None, initial)
	visited.append(start.value)
	to_visit=[]
	to_visit_values=[]
	heapq.heappush(to_visit, (0, 0, start))
	options={0 : [1, 3], 1 : [0, 2, 4] , 2 : [1, 5], 3 : [0, 4], 4 : [1, 3, 5], 5: [2, 4]}
	while len(to_visit)>0:
		point=heapq.heappop(to_visit)
		previous_priority=point[0]
		current=point[2]
		if goal==current.value:
			return path(current, initial)
		location=place_of_none(current.value)
		switches=options[location]
		for element in switches:
			temp=current.value
			new=swap(location, element, temp)
			current.children.append(Node(current, new))
		for child in current.children:
			if child.value in visited:
				continue
			if child.value not in to_visit_values:
				none=place_of_none(child.value)
				switches_possible=options[none]
				moves=[]
				for switch in switches_possible:
					moves.append(child.value[switch])
				lowest_move=sorted(moves)[0]
				heapq.heappush(to_visit, (previous_priority+1, lowest_move, child))
				to_visit_values.append(child.value)
		visited.append(current)


def path(n, start):
	solution=[]
	current=n
	while current.value != start:
		solution.append(current.value)
		parent=current.parent
		current=parent
	solution.append(start)
	return solution[::-1]

#iterative deepening
def dls(initial, goal, depth):
	visited=[]
	start=Node(None, initial)
	visited.append(start.value)
	visit=[start]
	to_visit=deque(visit)
	to_visit_values=[]
	options={0 : [1, 3], 1 : [0, 2, 4] , 2 : [1, 5], 3 : [0, 4], 4 : [1, 3, 5], 5: [2, 4]}
	while len(to_visit)>0:
		current=to_visit.pop()
		if goal==current.value:
			return path(current, initial)
		location=place_of_none(current.value)
		switches=options[location]
		for element in switches:
			temp=current.value
			new=swap(location, element, temp)
			current.children.append(Node(current, new))
		if (depth)>0:
			for child in current.children:
				if child.value in visited:
					continue
				if child.value not in to_visit_values:
					to_visit.append(child)
					to_visit_values.append(child.value)
			depth-=1
		elif depth==0:
			depth+=1
		else:
			continue
		visited.append(current)
	return None

def iterative_deepening(initial, goal):
	depth=0
	result = None
	while result == None :
		result=dls(initial, goal, depth)
		depth+=1
	return result, depth

#uncomment below to test
#print uniform_cost_search(i_state, g_state)
#print bfs_dfs(heuristic_state, g_state, 'bfs')
#print bfs_dfs(i_state, g_state, 'dfs')
#print iterative_deepening(i_state, g_state)