import pdb
# 在可能出错的地方增加断点调试语句
s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会暂停
print(10 / n)