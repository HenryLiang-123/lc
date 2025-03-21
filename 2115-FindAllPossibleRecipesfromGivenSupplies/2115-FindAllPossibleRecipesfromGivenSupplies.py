// Last updated: 3/21/2025, 2:35:40 PM
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # go through list of ingredients, form the adj_list by adding the food as a node if all ingredients are in supplies
        adj_list = defaultdict(list)
        n = len(recipes)
        supplies = set(supplies)

        for i in range(n):
            food = recipes[i]
            need = ingredients[i]
            adj_list[food] = need
        
        seen = set()
        memo = {}

        def dfs(node, path):
            if node in memo:
                return memo[node]

            if node in supplies:
                return True

            if node in path or node not in adj_list:
                return False

            path.add(node)
            memo[node] = False
            for nei in adj_list[node]:
                if not dfs(nei, path):
                    return False

            supplies.add(node)
            path.remove(node)
            memo[node] = True
            return True
        
        return [r for r in recipes if dfs(r, set())]

        # print(topo)

                    


