"""You are given an integer `side`, representing the edge length of a square with corners at `(0, 0)`, `(0, side)`, `(side, 0)`, and `(side, side)` on a Cartesian plane.
You are also given a positive integer `k` and a 2D integer array `points`, where `points[i] = [xi, yi]` represents the coordinate of a point lying on the boundary of the square.
You need to select `k` elements among `points` such that the minimum Manhattan distance between any two points is maximized.
Return the maximum possible minimum Manhattan distance between the selected `k` points.
The Manhattan Distance between two cells `(xi, yi)` and `(xj, yj)` is `|xi - xj| + |yi - yj|`.
 
Example 1:
Input: side = 2, points = [[0,2],[2,0],[2,2],[0,0]], k = 4
Output: 2
Explanation:

Select all four points.
Example 2:
Input: side = 2, points = [[0,0],[1,2],[2,0],[2,2],[2,1]], k = 4
Output: 1
Explanation:

Select the points `(0, 0)`, `(2, 0)`, `(2, 2)`, and `(2, 1)`.
Example 3:
Input: side = 2, points = [[0,0],[0,1],[0,2],[1,2],[2,0],[2,2],[2,1]], k = 5
Output: 1
Explanation:

Select the points `(0, 0)`, `(0, 1)`, `(0, 2)`, `(1, 2)`, and `(2, 2)`.
 
Constraints:

* `1 <= side <= 109`
* `4 <= points.length <= min(4 * side, 15 * 103)`
* `points[i] == [xi, yi]`
* The input is generated such that:
   * `points[i]` lies on the boundary of the square.
   * All `points[i]` are unique.
* `4 <= k <= min(25, points.length)`"""

def minimumDistance(side: int, points: list[list[int]], k: int) -> int:
    
    def to_1d(x, y):
        if y == 0:      return x
        elif x == side: return side + y
        elif y == side: return 2 * side + (side - x)
        else:           return 3 * side + (side - y)
    
    perimeter = 4 * side
    pos = sorted(to_1d(x, y) for x, y in points)
    n = len(pos)
    
    def find_next(lo, target):
        """First index in pos[lo..n) where pos[idx] >= target"""
        left, right = lo, n
        while left < right:
            mid = left + (right - left) // 2
            if pos[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left  # n if not found
    
    def condition(d) -> bool:
        for start in range(n):
            count = 1
            curr = pos[start]
            i = start
            while count < k:
                idx = find_next(i + 1, curr + d)
                if idx < n:
                    curr = pos[idx]
                    i = idx
                    count += 1
                else:
                    break
            if count == k and perimeter - (curr - pos[start]) >= d:
                return True
        return False

    left, right = 1, perimeter // k
    while left < right:
        mid = left + (right - left + 1) // 2
        if condition(mid):
            left = mid
        else:
            right = mid - 1
    return left
