<h2><a href="https://leetcode.com/problems/all-the-pairs-with-the-maximum-number-of-common-followers/">1951. All the Pairs With the Maximum Number of Common Followers</a></h2><h3>Medium</h3><hr><div class="sql-schema-wrapper__3VBi"><a class="sql-schema-link__3cEg">SQL Schema<svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__1Md2"><path fill-rule="evenodd" d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"></path></svg></a></div><div><p>Table: <code>Relations</code></p>

<pre>+-------------+------+
| Column Name | Type |
+-------------+------+
| user_id     | int  |
| follower_id | int  |
+-------------+------+
(user_id, follower_id) is the primary key for this table.
Each row of this table indicates that the user with ID follower_id is following the user with ID user_id.
</pre>

<p>&nbsp;</p>

<p>Write an SQL query to find all the pairs of users with the maximum number of common followers. In other words, if the maximum number of common followers between any two users is <code>maxCommon</code>, then you have to return all pairs of users that have <code>maxCommon</code> common followers.</p>

<p>The result table should contain the pairs <code>user1_id</code> and <code>user2_id</code> where <code>user1_id &lt; user2_id</code>.</p>

<p>Return the result table in <strong>any order</strong>.</p>

<p>The query result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> 
Relations table:
+---------+-------------+
| user_id | follower_id |
+---------+-------------+
| 1       | 3           |
| 2       | 3           |
| 7       | 3           |
| 1       | 4           |
| 2       | 4           |
| 7       | 4           |
| 1       | 5           |
| 2       | 6           |
| 7       | 5           |
+---------+-------------+
<strong>Output:</strong> 
+----------+----------+
| user1_id | user2_id |
+----------+----------+
| 1        | 7        |
+----------+----------+
<strong>Explanation:</strong> 
Users 1 and 2 have two common followers (3 and 4).
Users 1 and 7 have three common followers (3, 4, and 5).
Users 2 and 7 have two common followers (3 and 4).
Since the maximum number of common followers between any two users is 3, we return all pairs of users with three common followers, which is only the pair (1, 7). We return the pair as (1, 7), not as (7, 1).
Note that we do not have any information about the users that follow users 3, 4, and 5, so we consider them to have 0 followers.
</pre>
</div>