import heapq
from puzzle.base_search import BaseSearch
from puzzle.state import State, GOAL_STATE
from puzzle.result import SearchResult


class AStar(BaseSearch):

    def heuristic(self, state: State) -> int:
        total = 0
        for i, tile in enumerate(state.tiles):
            if tile == 0:
                continue
            goal_index = GOAL_STATE.index(tile)
            total += abs(i // 3 - goal_index // 3) + abs(i % 3 - goal_index % 3)
        return total

    def search(self, initial: State) -> SearchResult:
        result = SearchResult(solution=None, nodes_generated=1, max_frontier_size=1)
        frontier = [(self.heuristic(initial), initial)]
        explored = set()

        while frontier:
            _, state = heapq.heappop(frontier)
            if state in explored:
                continue
            if state.is_goal:
                result.solution = state
                result.depth = state.cost
                return result

            explored.add(state)
            result.nodes_expanded += 1
            for child in state.neighbors():
                if child not in explored:
                    result.nodes_generated += 1
                    heapq.heappush(frontier, (child.cost + self.heuristic(child), child))
            result.max_frontier_size = max(result.max_frontier_size, len(frontier))

        return result
