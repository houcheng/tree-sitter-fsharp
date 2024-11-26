import tree_sitter_c_sharp
import tree_sitter_fsharp
from tree_sitter_languages import get_language
cc1 = get_language('c_sharp')
print(cc1)
cc2 = tree_sitter_c_sharp.language()
print(cc2)

ff1 = get_language('fsharp')
print(ff1)
ff2 = tree_sitter_fsharp.language()
print(ff2)

import tree_sitter_c_sharp
a = tree_sitter_c_sharp.language()
print(a)

# Removed on v0.22.0
# Language(path, name) !
# Language("\\Users\\houch\\miniconda3\\envs\\tree-sitter\\Lib\\site-packages\\tree_sitter_c_sharp", "c_sharp")
#
# cc = get_language('python')
# print(cc)
#
# import tree_sitter_python
# b = tree_sitter_python.language()
# print(b)
#
