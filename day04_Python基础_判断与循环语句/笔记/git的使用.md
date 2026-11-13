# git的使用

#### git定义

git：**Content Management System**

Git 不仅仅是个版本控制系统，它也是个内容管理系统(CMS)

特点：**Git 是分布式的**：**分布式就是把任务拆到多台机器上，通过网络协作完成，换来更强的扩展性和容错性，但也要处理网络延迟、			数据一致性和故障等复杂问题。**

​			**按元数据方式存储**：**只存这些描述信息，而不存原始数据内容**

#### git指南

```
首先创建一个文件夹
创建按新仓库：git inint
创建一个本地clone的版本：git clone <源仓库位置> [目标目录名]; clone 后面的第一个参数：源仓库地址/路径
如果是远端服务器上的仓库，你的命令会是这个样子：git clone username@host:/path/to/repository
添加到Index（暂缓区）git add filenam（文件名的意思）
实际提交改动：git commmit -m "描述"：这个就是提交到HEAd，但是还没到远端仓库
提交到远端仓库　git push origin master(远端仓库意思)
欲将你的仓库连接到某个远程服务器：gie remote add origin <server>

```

#### git工作流

本地仓库由 git 维护的三棵“树”组成（工作目录，暂缓区（index),HEAD)

#### git分支

分支是用来将特性开发绝缘开来的。在你创建仓库的时候，*master* 是“默认的”分支。在其他分支上进行开发，完成后再将它们合并到主分支上。

```
创建一个feature_x的分支并且切换过去
git checkout -b feature_x
切换回去主分支
git checkout master
在把新建的分支删除掉 
git branch -d feature_x
除非你将分支推送到远端仓库，不然该分支就是 不为他人所见的
git push origin<branch>

```

#### git更新与合并

```
更新本地仓库的新的改动
git pull
以在你的工作目录中 获取（fetch） 并 合并（merge） 远端的改动。
要合并其他分支到你的当前分支（例如 master），执行
git merge <branch>
合并完成后记得标记成功
git add <filename>
或者合并前看差异
git diff <源分支> <目标分支》
```

#### git标签

```
标签创建一个叫1.0.0标签
git tag 1.0.0 1b2e1d63ff
1b2e1d63ff 是你想要标记的提交 ID 的前 10 位字符
获取id
git log

```

#### git替换本地改动

```
替换本地改动
git checkout --filename
会使HEAD的最新内容替换掉文件目录的文件
如果想丢弃本地所有改动和提交，到服务器上获取最新版本历史本地主分支指向它
git fech origion
get reset --hard origin/master
```

#### git小知识

```
内建的图形化 git：
gitk
彩色的 git 输出：
git config color.ui true
显示历史记录时，每个提交的信息只显示一行：
git config format.pretty oneline
交互式添加文件到暂存区：
git add -i
```

git配置

```
git config 的命令，用来配置或读取相应的工作环境变量
配置个人的用户名称和电子邮件地址，这是为了在每次提交代码时记录提交者的信息：
git config --global user.name"名称"
git config --global user.email 邮箱地址
设置 Git 默认使用的文本编辑器,一般可能会是 Vi 或者 Vim，如果你有其他偏好，比如 VS Code 的话，可以重新设置：
git config --global core.editor "具体的完整地址精确到exe
差异分析工具
还有一个比较常用的是，在解决合并冲突时使用哪种差异分析工具。比如要改用 vimdiff 的话：
git congig --global merge.tool vimdiff
查看配置信息
要检查已有的配置信息，可以使用 git config --list 命令：
生成 SSH 密钥（可选）
如果你需要通过 SSH 进行 Git 操作，可以生成 SSH 密钥并添加到你的 Git 托管服务（如 GitHub、GitLab 等）上。
ssh-keygen -t rsa -b 4096 -C "your.email@example.com"
验证安装
在终端或命令行中运行以下命令，确保 Git 已正确安装并配置
git --version
git config --list

```

