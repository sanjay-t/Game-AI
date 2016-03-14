import sys
import copy

post_to_name = dict()
post_to_name["root"] = "root"
loglist = list()
parent_pos_index = -1
log_minmax = list()
final_minmax_pos = 0
alpha = float('-inf')
beta = float('inf')
log_alpha_beta = list()
final_alpha_beta_move = 0


class war:
    def __init__(self, current_player, opponent_player, board, board_pos, cutoff_depth, cost):
        self.board = board
        self.board_pos = board_pos
        self.current_player = current_player
        self.opponent_player = opponent_player
        self.cutoff_depth = cutoff_depth
        self.cost = cost

    def get_current_player(self):
        return self.current_player

    def get_opponent_player(self):
        return self.opponent_player

    def get_board(self):
        return self.board

    def get_board_pos(self):
        return self.board_pos

    def get_cut_off_depth(self):
        return self.cutoff_depth

    def get_current_player_value(self):
        current_player_pos = [int(i) for i, x in enumerate(self.board_pos) if x == self.current_player]
        current_player_val = 0
        for i in current_player_pos:
            current_player_val += self.board[i]
        return current_player_val

    def get_current_player_pos(self):
        return [int(i) for i, x in enumerate(self.board_pos) if x == self.current_player]

    def get_opponent_player_value(self):
        opponent_player_pos = [int(i) for i, x in enumerate(self.board_pos) if x == self.opponent_player]
        opponent_player_val = 0
        for i in opponent_player_pos:
            opponent_player_val += self.board[i]
        return opponent_player_val

    def get_opponent_player_pos(self):
        return [int(i) for i, x in enumerate(self.board_pos) if x == self.opponent_player]

    def get_current_position(self):
        return [int(i) for i, x in enumerate(self.board_pos) if x == self.current_player]

    def get_opponent_positions(self):
        return [int(i) for i, x in enumerate(self.board_pos) if x == self.opponent_player]

    def get_empty_positions(self):
        return [int(i) for i, x in enumerate(self.board_pos) if x == '*']

    def get_temp_sum(self):
        return self.get_current_player_value() - self.get_opponent_player_value()

    def is_gameover(self):
        if not self.get_empty_positions():
            return True
        else:
            return False

    def switch_player(self, cplayer):
        cplayer = self.current_player
        self.current_player = self.opponent_player
        self.opponent_player = cplayer

    def minmax_calci(self, move, c_player):
        root_copy = copy.deepcopy(self)
        if c_player:
            root_copy.current_player = 'X'
            root_copy.opponent_player = 'O'
        else:
            root_copy.current_player = 'O'
            root_copy.opponent_player = 'X'
        current_sum = self.minmax_update(move, c_player)
        return current_sum

    def minmax_update(self, move, c_player):
        if c_player:
            current_player = 'X'
            opponent_player = 'O'
        else:
            current_player = 'O'
            opponent_player = 'X'
        self.board_pos[move] = current_player
        north = [0, 1, 2, 3, 4]
        south = [20, 21, 22, 23, 24]
        east = [4, 9, 14, 19, 24]
        west = [0, 5, 10, 15, 20]
        current_sum = 0
        if move in north and move in west:
            if self.board_pos[
                        move + 1] == current_player or self.board_pos[
                        move + 5] == current_player:
                if self.board_pos[move + 1] == opponent_player:
                    self.board_pos[move + 1] = current_player
                if self.board_pos[move + 5] == opponent_player:
                    self.board_pos[move + 5] = current_player
            current_sum = self.get_current_player_value() - self.get_opponent_player_value()
        elif move in north and move in east:
            if self.board_pos[move - 1] == current_player or self.board_pos[
                        move + 5] == current_player:
                if self.board_pos[move - 1] == opponent_player:
                    self.board_pos[move - 1] = current_player
                if self.board_pos[move + 5] == opponent_player:
                    self.board_pos[move + 5] = current_player
            current_sum = self.get_current_player_value() - self.get_opponent_player_value()
        elif move in south and move in west:
            if self.board_pos[
                        move + 1] == current_player or self.board_pos[
                        move - 5] == current_player:
                if self.board_pos[move + 1] == opponent_player:
                    self.board_pos[move + 1] = current_player
                if self.board_pos[move - 5] == opponent_player:
                    self.board_pos[move - 5] = current_player
            current_sum = self.get_current_player_value() - self.get_opponent_player_value()
        elif move in south and move in east:
            if self.board_pos[move - 1] == current_player or self.board_pos[
                        move - 5] == current_player:
                if self.board_pos[move - 1] == opponent_player:
                    self.board_pos[move - 1] = current_player
                if self.board_pos[move - 5] == opponent_player:
                    self.board_pos[move - 5] = current_player
            current_sum = self.get_current_player_value() - self.get_opponent_player_value()
        elif move in north:
            if self.board_pos[move - 1] == current_player or self.board_pos[
                        move + 1] == current_player or self.board_pos[
                        move + 5] == current_player:
                if self.board_pos[move - 1] == opponent_player:
                    self.board_pos[move - 1] = current_player
                if self.board_pos[move + 1] == opponent_player:
                    self.board_pos[move + 1] = current_player
                if self.board_pos[move + 5] == opponent_player:
                    self.board_pos[move + 5] = current_player
            current_sum = self.get_current_player_value() - self.get_opponent_player_value()
        elif move in south:
            if self.board_pos[move - 1] == current_player or self.board_pos[
                        move + 1] == current_player or self.board_pos[
                        move - 5] == current_player:
                if self.board_pos[move - 1] == opponent_player:
                    self.board_pos[move - 1] = current_player
                if self.board_pos[move + 1] == opponent_player:
                    self.board_pos[move + 1] = current_player
                if self.board_pos[move - 5] == opponent_player:
                    self.board_pos[move - 5] = current_player
            current_sum = self.get_current_player_value() - self.get_opponent_player_value()
        elif move in east:
            if self.board_pos[move - 1] == current_player or self.board_pos[
                        move + 5] == current_player or self.board_pos[
                        move - 5] == current_player:
                if self.board_pos[move - 1] == opponent_player:
                    self.board_pos[move - 1] = current_player
                if self.board_pos[move + 5] == opponent_player:
                    self.board_pos[move + 5] = current_player
                if self.board_pos[move - 5] == opponent_player:
                    self.board_pos[move - 5] = current_player
            current_sum = self.get_current_player_value() - self.get_opponent_player_value()
        elif move in west:
            if self.board_pos[
                        move + 1] == current_player or self.board_pos[
                        move + 5] == current_player or self.board_pos[
                        move - 5] == current_player:
                if self.board_pos[move + 1] == opponent_player:
                    self.board_pos[move + 1] = current_player
                if self.board_pos[move + 5] == opponent_player:
                    self.board_pos[move + 5] = current_player
                if self.board_pos[move - 5] == opponent_player:
                    self.board_pos[move - 5] = current_player
            current_sum = self.get_current_player_value() - self.get_opponent_player_value()
        else:
            if self.board_pos[move - 1] == current_player or self.board_pos[
                        move + 1] == current_player or self.board_pos[
                        move + 5] == current_player or self.board_pos[
                        move - 5] == current_player:
                if self.board_pos[move - 1] == opponent_player:
                    self.board_pos[move - 1] = current_player
                if self.board_pos[move + 1] == opponent_player:
                    self.board_pos[move + 1] = current_player
                if self.board_pos[move + 5] == opponent_player:
                    self.board_pos[move + 5] = current_player
                if self.board_pos[move - 5] == opponent_player:
                    self.board_pos[move - 5] = current_player
            current_sum = self.get_current_player_value() - self.get_opponent_player_value()
        return current_sum

    def special_calci(self, move, c_player):
        root_copy = copy.deepcopy(self)
        if c_player:
            current_player = 'X'
            opponent_player = 'O'
        else:
            current_player = 'O'
            opponent_player = 'X'
        root_copy.board_pos[move] = current_player
        current_sum = 0
        north = [0, 1, 2, 3, 4]
        south = [20, 21, 22, 23, 24]
        east = [4, 9, 14, 19, 24]
        west = [0, 5, 10, 15, 20]

        if move in north and move in west:
            if root_copy.board_pos[
                        move + 1] == current_player or root_copy.board_pos[
                        move + 5] == current_player:
                if root_copy.board_pos[move + 1] == opponent_player:
                    root_copy.board_pos[move + 1] = current_player
                if root_copy.board_pos[move + 5] == opponent_player:
                    root_copy.board_pos[move + 5] = current_player
            current_sum = root_copy.get_current_player_value() - root_copy.get_opponent_player_value()
        elif move in north and move in east:
            if root_copy.board_pos[move - 1] == current_player or root_copy.board_pos[
                        move + 5] == current_player:
                if root_copy.board_pos[move - 1] == opponent_player:
                    root_copy.board_pos[move - 1] = current_player
                if root_copy.board_pos[move + 5] == opponent_player:
                    root_copy.board_pos[move + 5] = current_player
            current_sum = root_copy.get_current_player_value() - root_copy.get_opponent_player_value()
        elif move in south and move in west:
            if root_copy.board_pos[
                        move + 1] == current_player or root_copy.board_pos[
                        move - 5] == current_player:
                if root_copy.board_pos[move + 1] == opponent_player:
                    root_copy.board_pos[move + 1] = current_player
                if root_copy.board_pos[move - 5] == opponent_player:
                    root_copy.board_pos[move - 5] = current_player
            current_sum = root_copy.get_current_player_value() - root_copy.get_opponent_player_value()
        elif move in south and move in east:
            if root_copy.board_pos[move - 1] == current_player or root_copy.board_pos[
                        move - 5] == current_player:
                if root_copy.board_pos[move - 1] == opponent_player:
                    root_copy.board_pos[move - 1] = current_player
                if root_copy.board_pos[move - 5] == opponent_player:
                    root_copy.board_pos[move - 5] = current_player
            current_sum = root_copy.get_current_player_value() - root_copy.get_opponent_player_value()
        elif move in north:
            if root_copy.board_pos[move - 1] == current_player or root_copy.board_pos[
                        move + 1] == current_player or root_copy.board_pos[
                        move + 5] == current_player:
                if root_copy.board_pos[move - 1] == opponent_player:
                    root_copy.board_pos[move - 1] = current_player
                if root_copy.board_pos[move + 1] == opponent_player:
                    root_copy.board_pos[move + 1] = current_player
                if root_copy.board_pos[move + 5] == opponent_player:
                    root_copy.board_pos[move + 5] = current_player
            current_sum = root_copy.get_current_player_value() - root_copy.get_opponent_player_value()
        elif move in south:
            if root_copy.board_pos[move - 1] == current_player or root_copy.board_pos[
                        move + 1] == current_player or root_copy.board_pos[
                        move - 5] == current_player:
                if root_copy.board_pos[move - 1] == opponent_player:
                    root_copy.board_pos[move - 1] = current_player
                if root_copy.board_pos[move + 1] == opponent_player:
                    root_copy.board_pos[move + 1] = current_player
                if root_copy.board_pos[move - 5] == opponent_player:
                    root_copy.board_pos[move - 5] = current_player
            current_sum = root_copy.get_current_player_value() - root_copy.get_opponent_player_value()
        elif move in east:
            if root_copy.board_pos[move - 1] == current_player or root_copy.board_pos[
                        move + 5] == current_player or root_copy.board_pos[
                        move - 5] == current_player:
                if root_copy.board_pos[move - 1] == opponent_player:
                    root_copy.board_pos[move - 1] = current_player
                if root_copy.board_pos[move + 5] == opponent_player:
                    root_copy.board_pos[move + 5] = current_player
                if root_copy.board_pos[move - 5] == opponent_player:
                    root_copy.board_pos[move - 5] = current_player
            current_sum = root_copy.get_current_player_value() - root_copy.get_opponent_player_value()
        elif move in west:
            if root_copy.board_pos[
                        move + 1] == current_player or root_copy.board_pos[
                        move + 5] == current_player or root_copy.board_pos[
                        move - 5] == current_player:
                if root_copy.board_pos[move + 1] == opponent_player:
                    root_copy.board_pos[move + 1] = current_player
                if root_copy.board_pos[move + 5] == opponent_player:
                    root_copy.board_pos[move + 5] = current_player
                if root_copy.board_pos[move - 5] == opponent_player:
                    root_copy.board_pos[move - 5] = current_player
            current_sum = root_copy.get_current_player_value() - root_copy.get_opponent_player_value()
        else:
            if root_copy.board_pos[move - 1] == current_player or root_copy.board_pos[
                        move + 1] == current_player or root_copy.board_pos[
                        move + 5] == current_player or root_copy.board_pos[
                        move - 5] == current_player:
                if root_copy.board_pos[move - 1] == opponent_player:
                    root_copy.board_pos[move - 1] = current_player
                if root_copy.board_pos[move + 1] == opponent_player:
                    root_copy.board_pos[move + 1] = current_player
                if root_copy.board_pos[move + 5] == opponent_player:
                    root_copy.board_pos[move + 5] = current_player
                if root_copy.board_pos[move - 5] == opponent_player:
                    root_copy.board_pos[move - 5] = current_player
            current_sum = root_copy.get_current_player_value() - root_copy.get_opponent_player_value()
        return current_sum

    def special_update(self, move, c_player):
        if c_player:
            current_player = 'X'
            opponent_player = 'O'
        else:
            current_player = 'O'
            opponent_player = 'X'
        self.board_pos[move] = current_player
        north = [0, 1, 2, 3, 4]
        south = [20, 21, 22, 23, 24]
        east = [4, 9, 14, 19, 24]
        west = [0, 5, 10, 15, 20]
        if move in north and move in west:
            if self.board_pos[
                        move + 1] == current_player or self.board_pos[
                        move + 5] == current_player:
                if self.board_pos[move + 1] == opponent_player:
                    self.board_pos[move + 1] = current_player
                if self.board_pos[move + 5] == opponent_player:
                    self.board_pos[move + 5] = current_player
        elif move in north and move in east:
            if self.board_pos[move - 1] == current_player or self.board_pos[
                        move + 5] == current_player:
                if self.board_pos[move - 1] == opponent_player:
                    self.board_pos[move - 1] = current_player
                if self.board_pos[move + 5] == opponent_player:
                    self.board_pos[move + 5] = current_player
        elif move in south and move in west:
            if self.board_pos[
                        move + 1] == current_player or self.board_pos[
                        move - 5] == current_player:
                if self.board_pos[move + 1] == opponent_player:
                    self.board_pos[move + 1] = current_player
                if self.board_pos[move - 5] == opponent_player:
                    self.board_pos[move - 5] = current_player
        elif move in south and move in east:
            if self.board_pos[move - 1] == current_player or self.board_pos[
                        move - 5] == current_player:
                if self.board_pos[move - 1] == opponent_player:
                    self.board_pos[move - 1] = current_player
                if self.board_pos[move - 5] == opponent_player:
                    self.board_pos[move - 5] = current_player
        elif move in north:
            if self.board_pos[move - 1] == current_player or self.board_pos[
                        move + 1] == current_player or self.board_pos[
                        move + 5] == current_player:
                if self.board_pos[move - 1] == opponent_player:
                    self.board_pos[move - 1] = current_player
                if self.board_pos[move + 1] == opponent_player:
                    self.board_pos[move + 1] = current_player
                if self.board_pos[move + 5] == opponent_player:
                    self.board_pos[move + 5] = current_player
        elif move in south:
            if self.board_pos[move - 1] == current_player or self.board_pos[
                        move + 1] == current_player or self.board_pos[
                        move - 5] == current_player:
                if self.board_pos[move - 1] == opponent_player:
                    self.board_pos[move - 1] = current_player
                if self.board_pos[move + 1] == opponent_player:
                    self.board_pos[move + 1] = current_player
                if self.board_pos[move - 5] == opponent_player:
                    self.board_pos[move - 5] = current_player
        elif move in east:
            if self.board_pos[move - 1] == current_player or self.board_pos[
                        move + 5] == current_player or self.board_pos[
                        move - 5] == current_player:
                if self.board_pos[move - 1] == opponent_player:
                    self.board_pos[move - 1] = current_player
                if self.board_pos[move + 5] == opponent_player:
                    self.board_pos[move + 5] = current_player
                if self.board_pos[move - 5] == opponent_player:
                    self.board_pos[move - 5] = current_player
        elif move in west:
            if self.board_pos[
                        move + 1] == current_player or self.board_pos[
                        move + 5] == current_player or self.board_pos[
                        move - 5] == current_player:
                if self.board_pos[move + 1] == opponent_player:
                    self.board_pos[move + 1] = current_player
                if self.board_pos[move + 5] == opponent_player:
                    self.board_pos[move + 5] = current_player
                if self.board_pos[move - 5] == opponent_player:
                    self.board_pos[move - 5] = current_player
        else:
            if self.board_pos[move - 1] == current_player or self.board_pos[
                        move + 1] == current_player or self.board_pos[
                        move + 5] == current_player or self.board_pos[
                        move - 5] == current_player:
                if self.board_pos[move - 1] == opponent_player:
                    self.board_pos[move - 1] = current_player
                if self.board_pos[move + 1] == opponent_player:
                    self.board_pos[move + 1] = current_player
                if self.board_pos[move + 5] == opponent_player:
                    self.board_pos[move + 5] = current_player
                if self.board_pos[move - 5] == opponent_player:
                    self.board_pos[move - 5] = current_player

    def greedy(self):
        empty_list = self.get_empty_positions()
        maximum = float('-inf')
        final_position = 0
        for pos in empty_list:
            node_val = self.special_calci(pos, True)
            if node_val > maximum:
                maximum = node_val
                final_position = pos
        self.special_update(final_position, True)
        write_to_file(self)

    def minmax_depth(self, depth, c_player, rc):
        if depth > rc.cutoff_depth or rc.is_gameover():
            return self.get_temp_sum()
        root_copy = copy.deepcopy(rc)
        next_copy = copy.deepcopy(self)
        parent_pos = rc.get_empty_positions()
        global parent_pos_index
        global final_minmax_pos
        if c_player:
            best_value = float('-inf')
            moves = rc.get_empty_positions()
            log_minmax.append("Node,Depth,Value\n")
            log_minmax.append("root,0,-Infinity\n")
            for move in moves:
                # print "root", depth-1, next_move
                next_copy.cost = best_value
                next_copy.free_list = moves
                for i in range(0, 25):
                    next_copy.board_pos[i] = '*'
                flist = rc.get_current_player_pos()
                for i in flist:
                    next_copy.board_pos[i] = rc.get_current_player()
                olist = rc.get_opponent_player_pos()
                for i in olist:
                    next_copy.board_pos[i] = rc.get_opponent_player()
                log_minmax.append(post_to_name[move] + "," + str(depth) + ",Infinity\n")
                next_copy.cost = next_copy.minmax_calci(move, True)
                next_move = next_copy.minmax_depth(depth + 1, False, rc)
                if next_move > best_value:
                    best_value = next_move
                    final_minmax_pos = move
                temp_depth = depth - 1
                log_minmax.append("root," + str(temp_depth) + "," + str(best_value) + "\n")
            return best_value
        else:
            parent_pos_index += 1
            next_copy_min = copy.deepcopy(next_copy)
            mv = root_copy.get_opponent_player_pos()
            cplaya = next_copy.get_current_player_pos()
            oplaya = next_copy.get_opponent_player_pos()
            moves = next_copy.get_empty_positions()
            best_value = float('inf')
            for move in moves:
                next_copy_min.cost = next_copy_min.special_calci(move, False)
                next_move = next_copy_min.minmax_depth(depth + 1, True, rc)
                if next_copy_min.cost < best_value:
                    best_value = next_copy_min.cost
                log_minmax.append(post_to_name[move] + "," + str(depth) + "," + str(next_copy_min.cost) + "\n")
                log_minmax.append(
                    post_to_name[parent_pos[parent_pos_index]] + "," + str(depth - 1) + "," + str(best_value) + "\n")
            return best_value

    def minmax_depth_rt1(self, depth, c_player, rc):
        if depth > rc.cutoff_depth or rc.is_gameover():
            return self.get_temp_sum()
        root_copy = copy.deepcopy(rc)
        next_copy = copy.deepcopy(self)
        parent_pos = rc.get_empty_positions()
        global parent_pos_index
        global final_minmax_pos
        if c_player:
            best_value = float('-inf')
            moves = rc.get_empty_positions()
            log_minmax.append("Node,Depth,Value\n")
            log_minmax.append("root,0,-Infinity\n")
            for move in moves:
                # print "root", depth-1, next_move
                next_copy.cost = best_value
                next_copy.free_list = moves
                for i in range(0, 25):
                    next_copy.board_pos[i] = '*'
                flist = rc.get_current_player_pos()
                for i in flist:
                    next_copy.board_pos[i] = rc.get_current_player()
                olist = rc.get_opponent_player_pos()
                for i in olist:
                    next_copy.board_pos[i] = rc.get_opponent_player()
                next_copy.cost = next_copy.minmax_calci(move, True)
                next_move = next_copy.minmax_depth(depth + 1, False, rc)
                log_minmax.append(post_to_name[move] + "," + str(depth) + ","+str(next_move)+"\n")
                if next_move > best_value:
                    best_value = next_move
                    final_minmax_pos = move
                temp_depth = depth - 1
                log_minmax.append("root," + str(temp_depth) + "," + str(best_value) + "\n")
            return best_value
        else:
            parent_pos_index += 1
            next_copy_min = copy.deepcopy(next_copy)
            mv = root_copy.get_opponent_player_pos()
            cplaya = next_copy.get_current_player_pos()
            oplaya = next_copy.get_opponent_player_pos()
            moves = next_copy.get_empty_positions()
            best_value = float('inf')
            for move in moves:
                next_copy_min.cost = next_copy_min.special_calci(move, False)
                next_move = next_copy_min.minmax_depth(depth + 1, True, rc)
                if next_copy_min.cost < best_value:
                    best_value = next_copy_min.cost
                log_minmax.append(post_to_name[move] + "," + str(depth) + "," + str(next_copy_min.cost) + "\n")
                log_minmax.append(
                    post_to_name[parent_pos[parent_pos_index]] + "," + str(depth - 1) + "," + str(best_value) + "\n")
            return best_value

    def minimax_caller(self):
        global final_minmax_pos
        root_copy = copy.deepcopy(self)
        # root_copy.cutoff_depth = 2
        if root_copy.cutoff_depth >1:
            best_value = root_copy.minmax_depth(1, True, root_copy)
        else:
            best_value = root_copy.minmax_depth_rt1(1, True, root_copy)
        opfile = open("traverse_log.txt", "w")
        for i in log_minmax:
            opfile.write(i)
        opfile.close()
        root_copy.special_update(final_minmax_pos, True)
        opfile2 = open("next_state.txt", "w")
        index = 0
        for i in range(0, 25):
            opfile2.write("%c" % root_copy.board_pos[i])
            if index < 4:
                index += 1
            else:
                opfile2.write("\n")
                index = 0
        opfile2.close()

    def get_text(self, val):
        if val == float('-inf'):
            return '-Infinity'
        elif val == float('inf'):
            return 'Infinity'
        else:
            return str(val)

    def alpha_beta(self, depth, player, rc):
        global alpha, beta, final_alpha_beta_move
        if depth > rc.cutoff_depth or rc.is_gameover():
            return self.get_temp_sum()
        root_copy = copy.deepcopy(rc)
        next_copy = copy.deepcopy(self)
        parent_pos = rc.get_empty_positions()
        global parent_pos_index
        global final_minmax_pos
        if player:
            moves = rc.get_empty_positions()
            best_value = float('-inf')
            log_alpha_beta.append("Node,Depth,Value,Alpha,Beta\n")
            log_alpha_beta.append("root,0,-Infinity,-Infinity,Infinity\n")
            for move in moves:
                # beta = float('inf')
                next_copy.cost = best_value
                next_copy.free_list = moves
                for i in range(0, 25):
                    next_copy.board_pos[i] = '*'
                flist = rc.get_current_player_pos()
                for i in flist:
                    next_copy.board_pos[i] = rc.get_current_player()
                olist = rc.get_opponent_player_pos()
                for i in olist:
                    next_copy.board_pos[i] = rc.get_opponent_player()
                next_copy.cost = float('inf')
                dval = self.get_text(depth)
                nval = self.get_text(next_copy.cost)
                aval = self.get_text(alpha)
                bval = self.get_text(beta)
                print post_to_name[move], depth, next_copy.cost, alpha, beta
                log_alpha_beta.append(post_to_name[move] + "," + dval + "," + nval + "," + aval + "," + bval + "\n")
                next_copy.cost = next_copy.minmax_calci(move, True)
                next_move = next_copy.alpha_beta(depth + 1, False, rc)
                best_value = max(best_value, next_move)
                if alpha < best_value:
                    final_alpha_beta_move = move
                alpha = max(alpha, best_value)
                temp_depth = depth - 1
                beta = float('inf')
                dval = self.get_text(depth - 1)
                nval = self.get_text(best_value)
                aval = self.get_text(alpha)
                bval = self.get_text(beta)
                print "root", depth - 1, best_value, alpha, beta
                log_alpha_beta.append("root" + "," + dval + "," + nval + "," + aval + "," + bval + "\n")
            return best_value
        else:
            parent_pos_index += 1
            next_copy_min = copy.deepcopy(next_copy)
            moves = next_copy.get_empty_positions()
            best_value = float('inf')
            for move in moves:
                next_copy_min.cost = next_copy_min.special_calci(move, False)
                next_move = next_copy_min.alpha_beta(depth + 1, True, rc)
                dval = self.get_text(depth)
                nval = self.get_text(next_copy_min.cost)
                aval = self.get_text(alpha)
                bval = self.get_text(beta)
                print post_to_name[move], depth, next_copy_min.cost, alpha, beta
                log_alpha_beta.append(post_to_name[move] + "," + dval + "," + nval + "," + aval + "," + bval + "\n")
                best_value = min(best_value, next_copy_min.cost)
                if best_value <= alpha:
                    beta = beta
                else:
                    beta = min(beta, best_value)
                dval = self.get_text(depth - 1)
                nval = self.get_text(best_value)
                aval = self.get_text(alpha)
                bval = self.get_text(beta)
                print post_to_name[parent_pos[parent_pos_index]], depth - 1, best_value, alpha, beta
                log_alpha_beta.append(post_to_name[parent_pos[
                    parent_pos_index]] + "," + dval + "," + nval + "," + aval + "," + bval + "\n")
                if best_value <= alpha:
                    break
            return best_value

    def alpha_beta_caller(self):
        global final_alpha_beta_move
        root_copy = copy.deepcopy(self)
        # root_copy.cutoff_depth = 2
        best_value = root_copy.alpha_beta(1, True, root_copy)
        opfile = open("traverse_log.txt", "w")
        for i in log_alpha_beta:
            opfile.write(i)
        opfile.close()
        root_copy.special_update(final_alpha_beta_move, True)
        opfile2 = open("next_state.txt", "w")
        index = 0
        for i in range(0, 25):
            opfile2.write("%c" % root_copy.board_pos[i])
            if index < 4:
                index += 1
            else:
                opfile2.write("\n")
                index = 0
        opfile2.close()


def set_board_for_current_player(current_player, opponent_player, board, board_pos, cutoff_depth, cost):
    war_instance = war(current_player, opponent_player, board, board_pos, cutoff_depth, cost)
    return war_instance


def process_input_file():
    with open(sys.argv[2], "r") as f:
        lines = f.read().splitlines()
    task = int(lines[0])
    current_player = lines[1]
    opponent_player = ''
    start_player = current_player
    cut_off_depth = int(lines[2])
    board = list()
    board_pos = list()
    board_state_1 = [int(x) for x in lines[3].split(' ')]
    board_state_2 = [int(x) for x in lines[4].split(' ')]
    board_state_3 = [int(x) for x in lines[5].split(' ')]
    board_state_4 = [int(x) for x in lines[6].split(' ')]
    board_state_5 = [int(x) for x in lines[7].split(' ')]
    board_pos_val1 = lines[8]
    board_pos_val2 = lines[9]
    board_pos_val3 = lines[10]
    board_pos_val4 = lines[11]
    board_pos_val5 = lines[12]
    pos_val = board_pos_val1 + board_pos_val2 + board_pos_val3 + board_pos_val4 + board_pos_val5
    board_states = [board_state_1, board_state_2, board_state_3, board_state_4, board_state_5]
    for i in board_states:
        for val in i:
            board.append(val)
    names = ["A", "B", "C", "D", "E"]
    index = 0
    for i in pos_val:
        board_pos.append(i)
    for i in range(1, 6):
        for name in names:
            post_to_name[index] = name + str(i)
            index += 1
    if current_player == 'X':
        opponent_player = 'O'
    else:
        opponent_player = 'X'
    return task, current_player, opponent_player, cut_off_depth, board, board_pos


def write_to_file(board):
    opfile = open("next_state.txt", "w")
    index = 0
    output_board_positions = board.board_pos
    for i in range(0, 25):
        opfile.write("%c" % output_board_positions[i])
        if index < 4:
            index += 1
        else:
            opfile.write("\n")
            index = 0
    opfile.close()


def play_war():
    task, current_player, opponent_player, cutoff_depth, board, board_pos = process_input_file()
    war_instance = set_board_for_current_player(current_player, opponent_player, board, board_pos, cutoff_depth,
                                                float('-inf'))

    task_options = {1: war_instance.greedy,
                    2: war_instance.minimax_caller,
                    3: war_instance.alpha_beta_caller
                    }
    next_state = task_options[task]()


play_war()
