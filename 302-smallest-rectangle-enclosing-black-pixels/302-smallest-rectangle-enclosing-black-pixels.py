class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        m, n = len(image), len(image[0])
        has_pixel_in_row = lambda i : any(image[i][j] == '1' for j in range(n))
        has_pixel_in_col = lambda j : any(image[i][j] == '1' for i in range(m))
        
        def bsearch(left, right, condition):
            while left < right:
                mid = (left + right) // 2
                if condition(mid):
                    right = mid
                else:
                    left = mid + 1
            return left
        
        low_x = bsearch(0, x+1, lambda r : has_pixel_in_row(r))
        high_x = bsearch(x, m, lambda r: not has_pixel_in_row(r))
        low_y = bsearch(0, y+1, lambda c : has_pixel_in_col(c))
        high_y = bsearch(y, n, lambda c: not has_pixel_in_col(c))
        
        return (high_y-low_y)*(high_x-low_x)