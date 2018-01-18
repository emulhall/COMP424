class State:
	def __init__(self, left_top, center_top, right_top, left_bottom, center_bottom, right_bottom):
		self.l_t = left_top
		self.c_t = center_top
		self.r_t = right_top
		self.l_b = left_bottom
		self.c_b = center_bottom
		self.r_b = right_bottom



#part A
#transitions have unit cost
#ensure that states that have been explored are not added to the search queue
#algorithm should prefer the state that involves moving a lower numbered piece
initial_state = State(1, 4, 2, 5, 3, None)
goal_state = State(None, 1, 2, 5, 4, 3)

#a part 1
#bfs

#a part 2
#uniform cost search

#a part 3
#depth first search

#a part 4
#iterative deepening