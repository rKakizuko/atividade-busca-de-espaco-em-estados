from collections import deque
from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult


class BFS(BaseSearch):

    def search(self, initial: State) -> SearchResult:
        result = SearchResult(solution=None, nodes_generated=1, max_frontier_size=1)
        if initial.is_goal:
            result.solution = initial
            return result

        frontier = deque([initial])
        reached = {initial}

        while frontier:
            state = frontier.popleft()
            result.nodes_expanded += 1
            for child in state.neighbors():
                if child in reached:
                    continue
                result.nodes_generated += 1
                if child.is_goal:
                    result.solution = child
                    result.depth = child.cost
                    return result
                reached.add(child)
                frontier.append(child)
            result.max_frontier_size = max(result.max_frontier_size, len(frontier))

        return result
