first-contributions

## Fork（复制）本代码仓库



点击图示中的按钮去 Fork 这个代码仓库。 这个操作会将代码仓库复制到你的账户名下。

## Clone（克隆）代码仓库



[![克隆此仓库代码](https://camo.githubusercontent.com/d4bafe4b6b8db07be80cb5d74070c2fb8ec18559711ad85ab3ae2bc576e1e9bc/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f526561646d652f636c6f6e652e706e67)](https://camo.githubusercontent.com/d4bafe4b6b8db07be80cb5d74070c2fb8ec18559711ad85ab3ae2bc576e1e9bc/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f526561646d652f636c6f6e652e706e67)

接下来将复制的代码仓库克隆到你的电脑上。点击图示中的绿色按钮，接着点击复制到剪切板按钮（将代码仓库地址复制下来）。

随后打开命令行窗口，敲入如下 Git 命令：

```
git clone "刚才复制的 URL 链接"
```

"刚才复制的 URL 链接"（去掉双引号）就是复制到你账户名下的代码仓库地址。获取该链接的方法详见上一步。

[![将 URL 链接复制到剪贴板](https://camo.githubusercontent.com/fe81d0584418cc04c31a477538ec11825bceb285d865f5c34dff84180fb5adeb/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f526561646d652f636f70792d746f2d636c6970626f6172642e706e67)](https://camo.githubusercontent.com/fe81d0584418cc04c31a477538ec11825bceb285d865f5c34dff84180fb5adeb/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f526561646d652f636f70792d746f2d636c6970626f6172642e706e67)

譬如：

```
git clone git@github.com:<GitHub用户名>/first-contributions.git
```

'GitHub 用户名' 指的是你的 GitHub 用户名。这一步，这个操作将会克隆你账户名下 first-contributions 这个代码仓库到本地电脑上。

## 新建一个代码分支



在命令行窗口中把目录切换到 first-contributions。

```
cd first-contributions
```

接下来使用 `git switch` 命令新建一个代码分支：

```
git switch -c <新分支的名称>
```

譬如：

```
git switch -c add-myname
```

<details style="box-sizing: border-box; display: block; margin-top: 0px; margin-bottom: 16px; color: rgb(31, 35, 40); font-family: &quot;Mona Sans VF&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, &quot;Noto Sans Backtick Fix&quot;, &quot;Noto Sans&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><summary style="box-sizing: border-box; display: list-item; cursor: pointer;"><strong style="box-sizing: border-box; font-weight: 600;">如果在运行 git switch 时报错，请点击这里：</strong></summary><p dir="auto" style="box-sizing: border-box; margin-top: 0px; margin-bottom: 16px;">如果出现错误信息 “Git: <code style="box-sizing: border-box; font-family: ui-monospace, SFMono-Regular, &quot;SF Mono&quot;, Menlo, Consolas, &quot;Liberation Mono&quot;, monospace; font-size: 13.6px; white-space: break-spaces; background-color: rgba(129, 139, 152, 0.12); border-radius: 6px; margin: 0px; padding: 0.2em 0.4em;">switch</code> is not a git command. See <code style="box-sizing: border-box; font-family: ui-monospace, SFMono-Regular, &quot;SF Mono&quot;, Menlo, Consolas, &quot;Liberation Mono&quot;, monospace; font-size: 13.6px; white-space: break-spaces; background-color: rgba(129, 139, 152, 0.12); border-radius: 6px; margin: 0px; padding: 0.2em 0.4em;">git --help</code>”（即提示 switch 不是 git 命令），可能是因为你使用的是旧版本的 Git。</p><p dir="auto" style="box-sizing: border-box; margin-top: 0px; margin-bottom: 16px;">在这种情况下，请尝试改用 <code style="box-sizing: border-box; font-family: ui-monospace, SFMono-Regular, &quot;SF Mono&quot;, Menlo, Consolas, &quot;Liberation Mono&quot;, monospace; font-size: 13.6px; white-space: break-spaces; background-color: rgba(129, 139, 152, 0.12); border-radius: 6px; margin: 0px; padding: 0.2em 0.4em;">git checkout</code> 命令：</p><div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" style="box-sizing: border-box; overflow: auto !important; position: relative !important; margin-bottom: 16px; background-color: rgb(246, 248, 250); justify-content: space-between; display: flex;"><pre style="box-sizing: border-box; font-family: ui-monospace, SFMono-Regular, &quot;SF Mono&quot;, Menlo, Consolas, &quot;Liberation Mono&quot;, monospace; font-size: 13.6px; margin-top: 0px; margin-bottom: 0px; overflow-wrap: normal; padding: 16px; color: rgb(31, 35, 40); background-color: rgb(246, 248, 250); border-radius: 6px; line-height: 1.45; overflow: auto; word-break: normal;">git checkout -b <span class="pl-k" style="box-sizing: border-box; color: rgb(207, 34, 46);">&lt;</span>新分支的名称<span class="pl-k" style="box-sizing: border-box; color: rgb(207, 34, 46);">&gt;</span></pre><div style="box-sizing: border-box;"></div></div></details>

(新分支的名称不一定需要有 *add*。然而，在新分支的名称加入 *add* 是一件合理的事情，因为这个分支的目的是将你的名字添加到列表中。)

## 对代码进行修改并提交修改



现在，在文本编辑器中打开 `Contributors.md` 文件，将你的名字添加到文件中。不要把名字加在文件的开头或结尾，请加在它们之间的任意位置。然后保存文件。

[![修改`Contributors.md`后的git状态](https://camo.githubusercontent.com/f4e28238c2321744c1488e34da1b0a439e91d12a9ce67f5d0fc425baead200c4/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f526561646d652f6769742d7374617475732e706e67)](https://camo.githubusercontent.com/f4e28238c2321744c1488e34da1b0a439e91d12a9ce67f5d0fc425baead200c4/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f526561646d652f6769742d7374617475732e706e67)

如果在项目目录下运行 `git status` 命令，你会看到有文件被修改了。

使用 `git add` 命令，将这些修改添加到刚才创建的分支中：

```
git add Contributors.md
```

现在就可以使用 `git commit` 命令提交你的修改了：

```
git commit -m "Add <你的名字> to Contributors list"
```

将 `<你的名字>` 替换成你的名字。

## 将改动 Push（推送）到 GitHub



使用 `git push` 命令推送代码：

```
git push -u origin <新分支的名称>
```

将 `<新分支的名称>` 替换为之前新建的分支名称。

<details style="box-sizing: border-box; display: block; margin-top: 0px; margin-bottom: 16px; color: rgb(31, 35, 40); font-family: &quot;Mona Sans VF&quot;, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, &quot;Noto Sans Backtick Fix&quot;, &quot;Noto Sans&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><summary style="box-sizing: border-box; display: list-item; cursor: pointer;"><strong style="box-sizing: border-box; font-weight: 600;">如果在推送（push）过程中出现错误（error），点击这里：</strong></summary><ul dir="auto" style="box-sizing: border-box; margin-top: 0px; margin-bottom: 16px; padding-left: 2em;"><li style="box-sizing: border-box;"><div class="markdown-heading" dir="auto" style="box-sizing: border-box; position: relative;"><h3 tabindex="-1" class="heading-element" dir="auto" style="box-sizing: border-box; margin-top: 24px; margin-bottom: 16px; font-size: 1.25em; font-weight: 600; line-height: 1.25;">Authentication Error</h3><a id="user-content-authentication-error" class="anchor" aria-label="Permalink: Authentication Error" href="https://github.com/firstcontributions/first-contributions/blob/main/docs/translations/README.zh-cn.md#authentication-error" style="box-sizing: border-box; background-color: rgba(0, 0, 0, 0); color: rgb(9, 105, 218); text-decoration: none; float: left; padding-right: 4px; margin: auto; line-height: 1; text-underline-offset: 0.2rem; border-radius: 6px; opacity: 0; justify-content: center; align-items: center; width: 28px; height: 28px; display: flex; position: absolute; top: 12.5px; left: -28px; transform: translateY(-50%);"><svg data-component="Octicon" class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div><pre style="box-sizing: border-box; font-family: ui-monospace, SFMono-Regular, &quot;SF Mono&quot;, Menlo, Consolas, &quot;Liberation Mono&quot;, monospace; font-size: 13.6px; margin-top: 0px; margin-bottom: 16px; overflow-wrap: normal; padding: 16px; color: rgb(31, 35, 40); background-color: rgb(246, 248, 250); border-radius: 6px; line-height: 1.45; overflow: auto;">remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
fatal: Authentication failed for 'https://github.com/&lt;your-username&gt;/first-contributions.git/'</pre><p dir="auto" style="box-sizing: border-box; margin-top: 16px; margin-bottom: 16px;">去 <a href="https://docs.github.com/cn/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account" style="box-sizing: border-box; background-color: rgba(0, 0, 0, 0); color: rgb(9, 105, 218); text-decoration: underline; text-underline-offset: 0.2rem;">GitHub 教程</a> 学习如何生成新的 SSH 密钥并进行配置。</p><p dir="auto" style="box-sizing: border-box; margin-top: 16px; margin-bottom: 16px;">另外，你可能需要运行 <code style="box-sizing: border-box; font-family: ui-monospace, SFMono-Regular, &quot;SF Mono&quot;, Menlo, Consolas, &quot;Liberation Mono&quot;, monospace; font-size: 13.6px; white-space: break-spaces; background-color: rgba(129, 139, 152, 0.12); border-radius: 6px; margin: 0px; padding: 0.2em 0.4em;">git remote -v</code> 来检查你的远程仓库地址。</p><p dir="auto" style="box-sizing: border-box; margin-top: 16px; margin-bottom: 16px;">如果它看起来像这样：</p><pre style="box-sizing: border-box; font-family: ui-monospace, SFMono-Regular, &quot;SF Mono&quot;, Menlo, Consolas, &quot;Liberation Mono&quot;, monospace; font-size: 13.6px; margin-top: 0px; margin-bottom: 16px; overflow-wrap: normal; padding: 16px; color: rgb(31, 35, 40); background-color: rgb(246, 248, 250); border-radius: 6px; line-height: 1.45; overflow: auto;">origin	https://github.com/your-username/first-contributions.git (fetch)
origin	https://github.com/your-username/first-contributions.git (push)</pre><p dir="auto" style="box-sizing: border-box; margin-top: 16px; margin-bottom: 16px;">请使用以下命令进行修改：</p><div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto" style="box-sizing: border-box; overflow: auto !important; position: relative !important; margin-bottom: 16px; background-color: rgb(246, 248, 250); justify-content: space-between; display: flex;"><pre style="box-sizing: border-box; font-family: ui-monospace, SFMono-Regular, &quot;SF Mono&quot;, Menlo, Consolas, &quot;Liberation Mono&quot;, monospace; font-size: 13.6px; margin-top: 0px; margin-bottom: 0px; overflow-wrap: normal; padding: 16px; color: rgb(31, 35, 40); background-color: rgb(246, 248, 250); border-radius: 6px; line-height: 1.45; overflow: auto; word-break: normal;">git remote set-url origin git@github.com:your-username/first-contributions.git</pre><div style="box-sizing: border-box;"></div></div><p dir="auto" style="box-sizing: border-box; margin-top: 16px; margin-bottom: 16px;">否则你仍会被要求输入用户名和密码，从而导致认证错误。</p></li></ul></details>

## 提出 Pull Request 将你的修改供他人审阅



前往你的 GitHub 代码仓库，你会看到一个 `Compare & pull request` 的按钮。点击该按钮。

[![创建 pull request](https://camo.githubusercontent.com/af350925874cc9d92469b7800b819295f2b8da906486a169b54a874a30d75ded/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f526561646d652f636f6d706172652d616e642d70756c6c2e706e67)](https://camo.githubusercontent.com/af350925874cc9d92469b7800b819295f2b8da906486a169b54a874a30d75ded/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f526561646d652f636f6d706172652d616e642d70756c6c2e706e67)

接着再点击 `Create pull request` 按钮，正式提交 pull request。

[![提交 pull request](https://camo.githubusercontent.com/87bc1d6af5a0c15e6ed798ff80fe57efe8a145c47e98ba16245350ebdfd13007/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f526561646d652f7375626d69742d70756c6c2d726571756573742e706e67)](https://camo.githubusercontent.com/87bc1d6af5a0c15e6ed798ff80fe57efe8a145c47e98ba16245350ebdfd13007/68747470733a2f2f6669727374636f6e747269627574696f6e732e6769746875622e696f2f6173736574732f526561646d652f7375626d69742d70756c6c2d726571756573742e706e67)

我们就会把你所有的修改合并到这个项目的 main 分支。更改合并后，你会收到一封电子邮件通知。