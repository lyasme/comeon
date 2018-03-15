### 美好的一天从敲代码开始

1.firstone 开始弄个github传文件，下载一个windows的github管理工具，[github  传文件](https://www.cnblogs.com/specter45/p/github.html)

2.一开始弄错了公钥的文件，调不出来。后来看了下报错，有看了另一个文件就发现问题了，英语不好，还是很抵触看英语的报错信息。多看看英语的文档吧。

3.**基本**的**命令**

  

|                 git init                 | 把这个目录变成git可以管理的仓库                        |
| :--------------------------------------: | ---------------------------------------- |
|             git add redme.md             | 文件添加到仓库                                  |
|                git add .                 | 不但可以跟单一文件，还可以跟通配符，更可以跟目录，一个点就把当前目录所有未追踪的全部add了 |
|       git commit -m 'first commit'       | 把文件提交到仓库                                 |
| git remote add origin git@github.com:lyasme/comeon | 先建仓库，关联远程仓库                              |
|        git push -u origin master         | 把本地的所有的内容推送到远程仓库上                        |

<u>注意 ：</u>

git是不能管理空文件夹的，文件里必须有文件才能add

