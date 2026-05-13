# # 1

# def matrix_to_dict(matrix):
#     answer_dict = {}

#     for i in range(0, len(matrix)):
#         row = {}
#         for j in range(0, len(matrix[i])):
#             row[j] = matrix[i][j]
        
#         answer_dict[i] = row
    
#     return answer_dict

# # 2

# def dict_to_matrix(d):
#     matrix = []

#     for i in range(len(d)):
#         row = []
#         for j in range(len(d[i])):
#             row += [d[i][j]]
        
#         matrix += [row]
    
#     return matrix


# # 3

# def transpose_matrix(matrix):
#     matrix_dict = matrix_to_dict(matrix)
#     trans_dict = {i: {} for i in range(0, len(matrix[0]))}
    
#     for i in range(0, len(matrix)):
#         for j in range(0, len(matrix[0])):
#             trans_dict[j][i] = matrix_dict[i][j]
    
#     return dict_to_matrix(trans_dict)

# # 4

# from collections import defaultdict

# def frequency_dict(matrix):
#     counter_el = defaultdict(int)
#     for i in matrix:
#         for j in i:
#             counter_el[j] += 1
    
#     return dict(counter_el)


# # 5

# def row_sums(matrix):
#     sums_row_dict = {}

#     for index, i in enumerate(matrix):
#         sums_row_dict[index] = sum(i)
    
#     return sums_row_dict


# # 6

# def adjacency_matrix_to_dict(matrix):
#     graph = {}

#     for i in range(len(matrix)):
#         graph[i] = []

#         for j in range(len(matrix[i])):
#             if matrix[i][j] == 1:
#                 graph[i] += [j]

#     return graph

# # 7

# def dict_to_adjacency_matrix(d, n):
#     matrix = [[0] * n for _ in range(n)]

#     for i in d:
#         for j in d[i]:
#             matrix[i][j] = 1

#     return matrix

# # 8

# def path_in_matrix(matrix, path):
#     answer_dict = {}
#     for i in path:
#         try:
#             answer_dict[i] = matrix[i[0]][i[1]]
#         except:
#             pass
    
#     return answer_dict

# # 9

# def rotate_matrix(matrix):
#     matrix_dict = matrix_to_dict(matrix)
#     trans_dict = {i: {} for i in range(0, len(matrix[0]))}
    
#     for i in range(0, len(matrix)):
#         for j in range(0, len(matrix[0])):
#             trans_dict[j][i] = matrix_dict[i][j]
    
#     return [i[::-1] for i in dict_to_matrix(trans_dict)]

# # 11

# def saddle_points(matrix):
#     saddle_dict = {}
#     trans = [list(i) for i in zip(*matrix)]
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if matrix[i][j] == min(matrix[i]) and matrix[i][j] == max(trans[j]):
#                 saddle_dict[(i, j)] = matrix[i][j]
    
#     return saddle_dict

# # 12

# def count_neighbourhood(matrix, x, y):
#     count = 0
#     for i in range(x - 1, x + 2):
#         for j in range(y - 1, y + 2):
#             if i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[i]):
#                 count += matrix[i][j]
#     return count - matrix[x][y]


# def game_of_life_step(matrix):
#     next_step = {}

#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if (matrix[i][j] == 1 and count_neighbourhood(matrix, i, j) in [2, 3]) or (matrix[i][j] == 0 and count_neighbourhood(matrix, i, j) == 3):
#                 next_step[(i, j)] = 1
            
#             else:
#                 next_step[(i, j)] = 0

#     return [[next_step[(i, j)] for j in range(len(matrix[i]))] for i in range(len(matrix))]
