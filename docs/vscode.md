## 关于环境配置

截止到今日时间2017/06/12位置，目前选择的平台是Window10，这里说一下关于环境的配置和对应编辑器的设置。（现在已经又变成Linux/Windows双开形式了，以下内容可用作Windows10 虚拟环境下的参考。

### virtualenv

1. 分别安装python3，python2，分别安装必要包（比如`virtualenv`）
2. 删除python2的path（最好装在`C:\Pathon27`）
3. 使用的时候默认python3，短期使用可用py -2调用python2
3. 长期使用用`virtualenv`的`-p C:\Pathon27\python.exe`来指定python2，默认就是python3

### vscode

1. 使用select interpreter 选择venv
2. 使用lintpath选择对于lintpath