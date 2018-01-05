
# 操作文件和目录
# 如果我们要操作文件、目录，可以在命令行下面输入操作系统提供的各种命令来完成。比如dir、cp等命令。

# 如果要在Python程序中执行这些目录和文件的操作怎么办？其实操作系统提供的命令只是简单地调用了操作系统提供的接口函数，Python内置的os模块也可以直接调用操作系统提供的接口函数。

# 打开Python交互式命令行，我们来看看如何使用os模块的基本功能
import os
# 获取所有的文件夹
print([x for x in os.listdir('.') if os.path.isdir(x)])

# 获取.md文件
l = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.md']
print(l)