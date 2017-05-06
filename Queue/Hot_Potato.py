import Queue

def hot_potato(name_list, num):
	sim_queue = Queue()
	for name in name_list:
		sim_queue.enqueue(name) #User will pass a list of names that get added to the list, FIFO

	while sim_queue.size() > 1:
		for i in range(num):
			sim_queue.enqueue(sim_queue.dequeue())
		sim_queue.dequeue()
	return sim_queue.dequeue()