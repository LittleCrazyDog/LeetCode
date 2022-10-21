<h2><a href="https://leetcode.com/problems/find-cutoff-score-for-each-school/">1988. Find Cutoff Score for Each School</a></h2><h3>Medium</h3><hr><div class="sql-schema-wrapper__3VBi"><a class="sql-schema-link__3cEg">SQL Schema<svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__1Md2"><path fill-rule="evenodd" d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"></path></svg></a></div><div><p>Table: <code>Schools</code></p>

<pre>+-------------+------+
| Column Name | Type |
+-------------+------+
| school_id   | int  |
| capacity    | int  |
+-------------+------+
school_id is the primary key for this table.
This table contains information about the capacity of some schools. The capacity is the maximum number of students the school can accept.
</pre>

<p>&nbsp;</p>

<p>Table: <code>Exam</code></p>

<pre>+---------------+------+
| Column Name   | Type |
+---------------+------+
| score         | int  |
| student_count | int  |
+---------------+------+
score is the primary key for this table.
Each row in this table indicates that there are student_count students that got at least score points in the exam.
The data in this table will be logically correct, meaning a row recording a higher score will have the same or smaller student_count compared to a row recording a lower score. More formally, for every two rows i and j in the table, if score<sub>i</sub> &gt; score<sub>j</sub> then student_count<sub>i</sub> &lt;= student_count<sub>j</sub>.
</pre>

<p>&nbsp;</p>

<p>Every year, each school announces a <strong>minimum score requirement</strong> that a student needs to apply to it. The school chooses the minimum score requirement based on the exam results of all the students:</p>

<ol>
	<li>They want to ensure that even if <strong>every</strong> student meeting the requirement applies, the school can accept everyone.</li>
	<li>They also want to <strong>maximize</strong> the possible number of students that can apply.</li>
	<li>They <strong>must</strong> use a score that is in the <code>Exam</code> table.</li>
</ol>

<p>Write an SQL query to report the <strong>minimum score requirement</strong> for each school. If there are multiple score values satisfying the above conditions, choose the <strong>smallest</strong> one. If the input data is not enough to determine the score, report <code>-1</code>.</p>

<p>Return the result table in <strong>any order</strong>.</p>

<p>The query result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong>
Schools table:
+-----------+----------+
| school_id | capacity |
+-----------+----------+
| 11        | 151      |
| 5         | 48       |
| 9         | 9        |
| 10        | 99       |
+-----------+----------+
Exam table:
+-------+---------------+
| score | student_count |
+-------+---------------+
| 975   | 10            |
| 966   | 60            |
| 844   | 76            |
| 749   | 76            |
| 744   | 100           |
+-------+---------------+
<strong>Output:</strong>
+-----------+-------+
| school_id | score |
+-----------+-------+
| 5         | 975   |
| 9         | -1    |
| 10        | 749   |
| 11        | 744   |
+-----------+-------+
<strong>Explanation:</strong> 
- School 5: The school's capacity is 48. Choosing 975 as the min score requirement, the school will get at most 10 applications, which is within capacity.
- School 10: The school's capacity is 99. Choosing 844 or 749 as the min score requirement, the school will get at most 76 applications, which is within capacity. We choose the smallest of them, which is 749.
- School 11: The school's capacity is 151. Choosing 744 as the min score requirement, the school will get at most 100 applications, which is within capacity.
- School 9: The data given is not enough to determine the min score requirement. Choosing 975 as the min score, the school may get 10 requests while its capacity is 9. We do not have information about higher scores, hence we report -1.
</pre>
</div>