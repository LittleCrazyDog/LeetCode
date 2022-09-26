<h2><a href="https://leetcode.com/problems/lonely-pixel-ii/">533. Lonely Pixel II</a></h2><h3>Medium</h3><hr><div><p>Given an <code>m x n</code> <code>picture</code> consisting of black <code>'B'</code> and white <code>'W'</code> pixels and an integer target, return <em>the number of <b>black</b> lonely pixels</em>.</p>

<p>A black lonely pixel is a character <code>'B'</code> that located at a specific position <code>(r, c)</code> where:</p>

<ul>
	<li>Row <code>r</code> and column <code>c</code> both contain exactly <code>target</code> black pixels.</li>
	<li>For all rows that have a black pixel at column <code>c</code>, they should be exactly the same as row <code>r</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/24/pixel2-1-grid.jpg" style="width: 493px; height: 333px;">
<pre><strong>Input:</strong> picture = [["W","B","W","B","B","W"],["W","B","W","B","B","W"],["W","B","W","B","B","W"],["W","W","B","W","B","W"]], target = 3
<strong>Output:</strong> 6
<strong>Explanation:</strong> All the green 'B' are the black pixels we need (all 'B's at column 1 and 3).
Take 'B' at row r = 0 and column c = 1 as an example:
 - Rule 1, row r = 0 and column c = 1 both have exactly target = 3 black pixels. 
 - Rule 2, the rows have black pixel at column c = 1 are row 0, row 1 and row 2. They are exactly the same as row r = 0.
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/24/pixel2-2-grid.jpg" style="width: 253px; height: 253px;">
<pre><strong>Input:</strong> picture = [["W","W","B"],["W","W","B"],["W","W","B"]], target = 1
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m ==&nbsp;picture.length</code></li>
	<li><code>n ==&nbsp;picture[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 200</code></li>
	<li><code>picture[i][j]</code> is <code>'W'</code> or <code>'B'</code>.</li>
	<li><code>1 &lt;= target &lt;= min(m, n)</code></li>
</ul>
</div>