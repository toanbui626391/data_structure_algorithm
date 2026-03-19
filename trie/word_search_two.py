"""
Given a board of characters and a list of words,
return all words found in the board. Words must be
formed by adjacent (horizontal/vertical) cells, and
no cell may be reused within a single word.

Example:
  Input:  board=[["o","a","a","n"],["e","t","a","e"],
          ["i","h","k","r"],["i","f","l","v"]],
          words=["oath","pea","eat","rain"]
  Output: ["eat","oath"]

Constraints:
  Build a trie from words; DFS avoids recomputing matches.
"""

from typing import List


class Solution:
    def findWords(
        self,
        board: List[List[str]],
        words: List[str],
    ) -> List[str]:

        def dfs(row, col, root):
            letter = board[row][col]
            curr = root[letter]
            # Remove word marker if a word ends here.
            word = curr.pop('#', False)
            if word:
                result.append(word)
            # Mark cell visited to prevent reuse.
            board[row][col] = '*'
            for dir_row, dir_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_row = row + dir_row
                next_col = col + dir_col
                if (
                    0 <= next_row < num_rows
                    and 0 <= next_col < num_cols
                    and board[next_row][next_col] in curr
                ):
                    dfs(next_row, next_col, curr)
            board[row][col] = letter
            # Prune empty trie branches for performance.
            if not curr:
                root.pop(letter)

        # Build a nested dict trie from the word list.
        trie = {}
        for word in words:
            curr = trie
            for letter in word:
                curr = curr.setdefault(letter, {})
            curr['#'] = word

        num_rows = len(board)
        num_cols = len(board[0])
        result = []

        for i in range(num_rows):
            for j in range(num_cols):
                if board[i][j] in trie:
                    dfs(i, j, trie)

        return result
