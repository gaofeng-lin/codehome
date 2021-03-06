[TOC]
# 1.config相关命令
## 1.1 查看配置信息
 1. 查看系统config

```
 git config --system --list
```

 2. 查看当前用户（global）配置


```
git config --global  --list
```

 3. 查看当前仓库配置信息



```
git config -- local    --list
```

## 1.2 设置/修改配置信息
设置用户名：

```
git config --global user.name "github用户名"
```

设置邮箱

```
git config --global user.email "github注册邮箱"
```
# 2 查看提交记录
## 2.1 查看指定文件的历史提交记录
```
git log -- <file>
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/b1dc02f3dc8d4c888f7d98443524a64f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6IiU54uXMeWPtw==,size_20,color_FFFFFF,t_70,g_se,x_16)

## 2.2 查看每次提交的内容差异

```
git log -p -2 -- <file>
```

> 参数：-p 表示每次提交的内容差异，-2 则表示显示最近的两次更新。
> 
> 说明：该选项除了显示基本信息之外，还在附带了每次 commit 的变化。

![在这里插入图片描述](https://img-blog.csdnimg.cn/381402cab6344a00b05b3a42fe128a60.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6IiU54uXMeWPtw==,size_20,color_FFFFFF,t_70,g_se,x_16)
## 2.3 根据哈希值查看修改代码细节

```
git show 哈希值
```

```
git show 哈希值 文件名 //具体某个文件的变化
```

## 2.4 单词层面上的对比

```
git log --word-diff -- <file>
```

> 参数：--word-diff 表示获取单词层面上的对比。

> 说明：进行单词层面的对比常常是没什么用的。不过当你需要在书籍、论文这种很大的文本文件上进行对比的时候，这个功能就显出用武之地了。

![在这里插入图片描述](https://img-blog.csdnimg.cn/dbf8557886aa4e16905b75a0fc368c29.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6IiU54uXMeWPtw==,size_20,color_FFFFFF,t_70,g_se,x_16)
**提示：新增加的单词被 {+ +} 括起来，被删除的单词被 [- -] 括起来。**

## 2.5 图形化查看提交历史

```
gitk -- <file>
```

> 说明：随 Git 一同发布的 gitk 就是这样一种工具。它是用 Tcl/Tk 写成的，基本上相当于 git log 命令的可视化版本，凡是
> git log 可以用的选项也都能用在 gitk 上。

![在这里插入图片描述](https://img-blog.csdnimg.cn/b981ba602f044894b93bf19d74116145.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6IiU54uXMeWPtw==,size_20,color_FFFFFF,t_70,g_se,x_16)
**

> gitk中文乱码问题

**
解决办法：
打开git的配置文件(根据自己安装的git目录，此处为安装在D盘)：D:\Program Files\Git\etc\gitconfig

在文件内追加以下内容：

```
[gui]
  encoding = utf-8
```

## 2.6 提取git中某个文件的所有版本并按顺序命名

```
git log --follow --pretty=format:%H 文件名 | xargs -I{} sh -c 'git show {}:文件名 > 文件名.{}'
```

**文件名需要进行替换，不可直接输入 文件名 三个字**

<br/>

**如果出现** 

> Did you menan '哈希值：路径' aka '哈希值：路径'

字眼的错误

给第二个文件名添加 `./`

## 2.7 git将远程分支按分支名在本地建立文件夹

```
git branch -r | xargs -d/ -n1 | grep -v 'origin' | xargs -I{} sh -c 'mkdir "C:\Users\76585\Desktop\try\{}" '
```

命令分线见 **博客--Linux Shell命令总结**

# 3 git 基本使用流程

## 3.1 git pull 与 git push 详解
1.git remote
```
git remote add origin url  //这里面的origin 是给远程仓库起名字，不是给本地仓库！
```

2.git pull
```
git pull 其实就是 git fetch 和 git merge FETCH_HEAD 的简写。 命令格式如下：

git pull <远程主机名> <远程分支名>:<本地分支名>
```

```
将远程主机 origin 的 master 分支拉取过来，与本地的 brantest 分支合并。

git pull origin master:brantest

如果远程分支是与当前分支合并，则冒号后面的部分可以省略。

git pull origin master
```


3.git push 
```
git push <远程主机名> <本地分支名>:<远程分支名>

如果本地分支名与远程分支名相同，则可以省略冒号：

git push <远程主机名> <本地分支名>

```

实例：
以下命令将本地的 master 分支推送到 origin 主机的 master 分支。

```
git push origin master

相等于：

git push origin master:master

如果本地版本与远程版本有差异，但又要强制推送可以使用 --force 参数：

git push --force origin master

删除主机的分支可以使用 --delete 参数，以下命令表示删除 origin 主机的 master 分支：

git push origin --delete master

```

## 3.2 将本地代码上传到远程仓库
1.（电脑里得先下载git）登录coding，新建一个仓库，点击代码浏览可以看到
![在这里插入图片描述](https://img-blog.csdnimg.cn/dfad51be62a440cd86b764c2e4f16487.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/7063830ad8194b8792977f5750a8d1d4.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6IiU54uXMeWPtw==,size_20,color_FFFFFF,t_70,g_se,x_16)
2.在本地新建一个文件夹，作为项目根目录，再此启动 Git Bash ，进入目录，并输入

```
 git init
```
3.将本地仓库和我们在coding上创建的远程仓库对接起来，输入

```
git remote add *yourname* *git_url*  //不用输这条，输下面那条
```
add 后面输入你的仓库名字，自定义。git_url代表你的git地址，这里我命名为origin

```
git remote add origin *url* //这条指令是上面的详细版，输入这个就好。
```

> （这里可能会出现叫你设置邮箱，和姓名，跟着提示设置就行了，或者可以选择以SSH公钥进行连接，不过得先去配置公钥）

回车成功后可以输入

```
git remote -v
```
4.为了我们的代码是最新的状态 和 提交时不会产生冲突，我们先执行下pull操作，将远程仓库最新代码拉到我们本地来，输入

```
git pull origin master
```

> （origin就是我们上面设置的仓库名，master代表主分支，你可以把分支理解为一块区域，我们最终编写完成的代码都要整合到master分支里面去。然后，我们还可创建一些其他分支，去保存我们正在编写中，或者尚未测试的代码。）


执行完后，你可以查看目录下的文件，这时我们本地的文件就和远程仓库里面master分支里的文件一样了。

5.接下来我们来模拟写代码并上传到远程仓库去。
我们新建一个 a.js文件，并编辑一些内容进去。首先将a文件添加到暂存区

```
git add a.js //（add后面可以带多个文件名字，用空格隔开；或者输入 . 代表全部）

//然后再提交到本地仓库中去

git commit -m "first commit"

//然后我们需要把它push到远程仓库中去。输入

git push origin master  //push到origin的master主分支里面，成功后会显示提示消息

```



## 3.3 分支的使用

**mster代表主分支，最终的代码都整合到这里面去，我们可以看下**
![在这里插入图片描述](https://img-blog.csdnimg.cn/fcc0d993653e42e7a48a10d25328f11e.png)

**这里只有一个主分支master。
有一种情况就是，一个项目多人开发，我的任务需要开发一个功能，我没办法短时间内就开发测试等等一系列完成。所以我可以新建一个分支，然后把每次完成的代码都上传到这个分支里面去，最后等到所有操作都完成后，我再把这个分支整合到master中去。下面看步骤**

1.首先查看当前分支

```
git branch -a
```

-a代表查看本地和远程的分支，此时我们看到都只有一个master分支
![在这里插入图片描述](https://img-blog.csdnimg.cn/8e219832c5df4eef8c7da9dce7cd1829.png)


2.新建分支dev

```
git checkout -b dev
```


-b代表同时切换到dev分支下面去，这时你可以再去查看分支

3.然后我们重新写一个b.js文件，再执行add，commit，最后push

```
git add b.js

git commit -m "dev"

git push origin dev
```


**注意push时要到dev分支**

成功后我们去coding看已经有了dev，并且dev下有b.js，而master没有b.js
![在这里插入图片描述](https://img-blog.csdnimg.cn/ca05925c026f48d4af3cc08ced1632da.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6IiU54uXMeWPtw==,size_12,color_FFFFFF,t_70,g_se,x_16)


master：
![在这里插入图片描述](https://img-blog.csdnimg.cn/abc1cba6a233436a8a4731ec90324646.png)


我们可以再去看看分支情况，

git branch -a
![在这里插入图片描述](https://img-blog.csdnimg.cn/5323471b84664e88b25f3f6228da4e74.png)


此时已经有了两个分支，且当前位于dev分之下
切换分支可以用 **git checkout [branch-name]**


## 3.4 整合分支
**当我们在dev下折腾完成后，最终要整合到master中去，看步骤**

1.切换本地分支到master

```
git checkout master
```


2.将远程仓库的最新代码pull下来！！因为期间其他人可能已经提交代码到远程master了，所以你首先得更新下自己本地的master代码

```
git pull origin master
```


假如有改动过，那么执行后会显示改动的信息

3.然后再把本地的dev代码整合到master，输入

```
git merge dev
```

merge整合操作，把dev整合到当前分之下（当前分支为master）。会提示增加了东西
![在这里插入图片描述](https://img-blog.csdnimg.cn/249f2d65516c483a9517f8ce5affb72f.png)


4.由于当前的东西已经在本地仓库里面了，所以最后我们再执行push，到远程仓库的master

```
git push origin master
```


成功后你可看到，master下已经有b.js文件了
![在这里插入图片描述](https://img-blog.csdnimg.cn/1f2c3d8b692b42619534a683d2c3f21a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6IiU54uXMeWPtw==,size_11,color_FFFFFF,t_70,g_se,x_16)

