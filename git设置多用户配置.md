# 一、背景  
**作为一名出色的开发工程师，目前互联网代码托管平台众多同时有些平台已不支持账号和密码的直接gitbash操作。在我们托管平台多项目多，比如公司用的gitlab、而同时也参加一些开源项目在github、gitee等代码托管平台上；那么如何利用手中的一台开发机，同时支持多个代码托管平台的代码免密进行代码提交拉取等操作呢？这篇文章告诉你答案**

# 二、步骤  
### 清除全局的帐号

    
    
    git config --global --unset user.name
    git config --global --unset user.email

  
### 在用户目录下的.ssh目录下生成ssh免密登录公钥和私钥  
.ssh/目录（C:\Users\自己的用户名\\.ssh）下，右键Git Bash Here，打开git-bash窗口

    
    
    ssh-keygen -t rsa -C "gitee邮箱地址"
    
    如果gitee和gitlab配置的账户名不一样 则需要生成不同的rsa公钥 

<img src='https://img-blog.csdnimg.cn/img_convert/a486560b451c31ee30fe1dabec4cb864.png' />  
生成不同的ssh 则路径后的文件名也不一致  
# 三、创建config文件  
### 在.ssh目录下创建config 文件，git通过这个文件才知道哪个私钥去对应哪个公钥。

    
    
    Host gitee.com
    HostName gitee.com
    User "填写邮箱"
    IdentityFile C:\Users\xxx\.ssh/id_rsa_gitee
    
    Host gitlab.com
    HostName gitlab.com
    User "填写邮箱"
    IdentityFile C:\Users\xxx\.ssh/id_rsa_gitlab
    

  
>config文件部分参数含义，仅做记录  
Host：可以看作是一个你要识别的模式，对识别的模式，配置对应的主机名和ssh文件。（不重复即可）  
User：自定义的用户名，默认为git，可不配置  
HostName：真正连接的服务器地址  
IdentityFile：指定本次连接使用的密钥文件

# 四、测试ssh-key是否连通  
<img src='https://img-blog.csdnimg.cn/img_convert/dc4d779a8f3bd667231d931f2c249e3e.png' />

# gitlab配置多用户  
也是需要生成一个ssh 私钥，并把ssh放入gitlab  
如果push clone报错  
<img src='https://img-blog.csdnimg.cn/img_convert/c764383e91513ed714377787e1c85742.png' />

>当我们想要clone一个项目时，发现了上面的错误  
这个错误我是出现在输入密码的时候，我输入的密码是我的登录密码，它提示了我这个错误信息  
<img src='https://img-blog.csdnimg.cn/img_convert/dd5a1952d62c0a017006512bee57ce17.png' />  
··进入gitlab生成一个token  
<img src='https://img-blog.csdnimg.cn/img_convert/de8560e77c543097faa4335a74ed2eb6.png' />  
\--**用户名输入 自己gitlab的用户名 密码输入这个生成的token就可以进行拉取和提交代码了**  

