<h2><a href="https://leetcode.com/problems/maximum-transaction-each-day/">1831. Maximum Transaction Each Day</a></h2><h3>Medium</h3><hr><div class="sql-schema-wrapper__3VBi"><a class="sql-schema-link__3cEg">SQL Schema<svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__1Md2"><path fill-rule="evenodd" d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"></path></svg></a></div><div><p>Table: <code>Transactions</code></p>

<pre>+----------------+----------+
| Column Name    | Type     |
+----------------+----------+
| transaction_id | int      |
| day            | datetime |
| amount         | int      |
+----------------+----------+
transaction_id is the primary key for this table.
Each row contains information about one transaction.
</pre>

<p>&nbsp;</p>

<p>Write an SQL query to report the IDs of the transactions with the <strong>maximum</strong> <code>amount</code> on their respective day. If in one day there are multiple such transactions, return all of them.</p>

<p>Return the result table <strong>ordered by</strong> <code>transaction_id</code> <strong> in ascending order</strong>.</p>

<p>The query result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> 
Transactions table:
+----------------+--------------------+--------+
| transaction_id | day                | amount |
+----------------+--------------------+--------+
| 8              | 2021-4-3 15:57:28  | 57     |
| 9              | 2021-4-28 08:47:25 | 21     |
| 1              | 2021-4-29 13:28:30 | 58     |
| 5              | 2021-4-28 16:39:59 | 40     |
| 6              | 2021-4-29 23:39:28 | 58     |
+----------------+--------------------+--------+
<strong>Output:</strong> 
+----------------+
| transaction_id |
+----------------+
| 1              |
| 5              |
| 6              |
| 8              |
+----------------+
<strong>Explanation:</strong> 
"2021-4-3"  --&gt; We have one transaction with ID 8, so we add 8 to the result table.
"2021-4-28" --&gt; We have two transactions with IDs 5 and 9. The transaction with ID 5 has an amount of 40, while the transaction with ID 9 has an amount of 21. We only include the transaction with ID 5 as it has the maximum amount this day.
"2021-4-29" --&gt; We have two transactions with IDs 1 and 6. Both transactions have the same amount of 58, so we include both in the result table.
We order the result table by transaction_id after collecting these IDs.
</pre>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you solve it without using the <code>MAX()</code> function?</p>
</div>