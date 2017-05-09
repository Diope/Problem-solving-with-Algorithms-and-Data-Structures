def search_from(maze, start_row, start_column):
	maze.update_position(start_row, start_column)
	# Checks base cases:
	# If you run into an obstacle, return false
	if maze[start_row][start_column] == OBSTACLE:
		return False
	# Found a square that has already been explored
	if maze[start_row][start_column] == TRIED:
		return False
	# An outside edge NOT occupied by an obstacle
	if maze.is_exit(start_row, start_column):
		maze.update_position(start_row, start_column, PART_OF_PATH)
		return True
	maze.update_position(start_row, start_row, TRIED)

	found = search_from(maze, start_row - 1, start_column) or search_from(maze, start_row + 1, start_column) or 
			search_from(maze, start_row, start_column - 1) or search_from(maze, start_row - 1, start_column + 1)
	if found:
		maze.update_position(start_row, start_column, PART_OF_PATH)
	else:
		maze.update_position(start_row, start_column, DEAD_END)
	return found