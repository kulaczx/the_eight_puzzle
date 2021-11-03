class puzzle:
    def __init__(self, slist, puzzle_number=9, topRight=2):
        self.state = []
        for item in slist:
            self.state.append(item)
        self.move = "NONE"
        self.max_num = puzzle_number
        self.top_right = topRight
        self.rowSize = self.top_right + 1
        self.goal_state = []
        self.move_cost = 1
        for i in range(1, self.max_num):
            self.goal_state.append(i)
        self.goal_state.append(0)

    def cpy_puzzle(self):
        temp = []
        new_pzle = puzzle(self.state)
        return new_pzle

    def move_blank_up(self):  # index 0, 1, 2 can't do up
        resultBool = False
        for i in range(self.max_num):
            if self.state[i] == 0:
                if i > self.top_right:
                    blank = i
                    resultBool = True
                    break
        if not resultBool:
            return False

        self.state[blank] = self.state[blank - self.rowSize]
        self.state[blank - self.rowSize] = 0
        self.move = "UP"
        self.move_cost = 1
        return True

    def move_blank_down(self):
        resultBool = False
        for i in range(self.max_num):
            if self.state[i] == 0:
                if i < self.rowSize * (self.rowSize - 1):
                    blank = i
                    resultBool = True
                    break
        if not resultBool:
            return False
        self.state[blank] = self.state[blank + self.rowSize]
        self.state[blank + self.rowSize] = 0
        self.move = "DOWN"
        self.move_cost = 1
        return True

    def move_blank_right(self):
        resultBool = False
        for i in range(self.max_num):
            if self.state[i] == 0:
                if abs(i - self.top_right) % 3 != 0 and i > 0:
                    blank = i
                    resultBool = True
                    break
        if not resultBool:
            return False
        self.state[blank] = self.state[blank + 1]
        self.state[blank + 1] = 0
        self.move = "RIGHT"
        self.move_cost = 1
        return True

    def move_blank_left(self):
        resultBool = False
        for i in range(self.max_num):
            if self.state[i] == 0:
                if (i % self.rowSize) != 0 and i > 0:
                    blank = i
                    resultBool = True
                    break
        if not resultBool:
            return False
        self.state[blank] = self.state[blank - 1]
        self.state[blank - 1] = 0
        self.move = "LEFT"
        self.move_cost = 1
        return True

    def compare_state(self):
        missCount = 0
        for i in range(self.max_num):
            if self.state[i] != self.goal_state[i] and self.state[i] != 0:
                missCount += 1
        return missCount

    def show_puzzle(self):
        row_count = 1
        row = ''
        print("current state")
        for i in range(len(self.state)):
            if row_count == self.rowSize:
                row += str(self.state[i])
                print(row)
                row_count = 1
                row = ''
            else:
                row += str(self.state[i])
                row_count += 1
        print(row)
        row = ''
        row_count = 1
        print("goal state")
        for i in range(len(self.goal_state)):
            if row_count == self.rowSize:
                row += str(self.goal_state[i])
                print(row)
                row_count = 1
                row = ''
            else:
                row += str(self.goal_state[i])
                row_count += 1
        print(row)

    def get_move(self):
        return self.move

    def get_move_cost(self):
        return self.move_cost

    def distance_to_goal(self):
        total_distance = 0
        goal_state_row = 0
        current_state_row = 0
        for i in range(self.max_num):
            if self.state[i] != self.goal_state[i] and self.state[i] != 0:
                for row in range(self.rowSize, 0, -1):
                    if i < row * self.rowSize:  # find current tile's row number
                        current_state_row = row
                    if self.state[i] - 1 < row * self.rowSize:  # find goal tile's row number
                        goal_state_row = row

                    move_to_rows = abs(
                        goal_state_row - current_state_row)  # get row difference between goal and current
                    if current_state_row < goal_state_row:  # get index of current tile after doing row moves
                        index_near_goal = i + move_to_rows * self.rowSize
                    else:
                        index_near_goal = i - move_to_rows * self.rowSize

                    move_in_row = abs(self.state[i] - 1 - index_near_goal)
                total_distance += move_in_row + move_to_rows

        return total_distance
