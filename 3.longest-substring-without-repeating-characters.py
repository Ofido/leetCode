#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#


# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0  # Início da janela deslizante
        max_length = 0  # Comprimento máximo da substring sem caracteres repetidos
        char_index_map = {}  # Dicionário para armazenar a última posição de cada caractere

        for end, char in enumerate(s):
            if char in char_index_map and char_index_map[char] >= start:
                # Atualiza o início da janela se o caractere foi visto anteriormente
                start = char_index_map[char] + 1

            # Atualiza o índice do caractere no dicionário
            char_index_map[char] = end

            # Calcula o comprimento da substring atual e atualiza o máximo
            max_length = max(max_length, end - start + 1)

        return max_length


# @lc code=end
