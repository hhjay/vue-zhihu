# 使用vue组件化 zhihu

---------

使用py爬虫、使用vue组件化前端、(使用webpack等 | 暂时还不知道用来干嘛)、使用sass

### 1. 首页
- [ ] 显示主内容
	- [1] 提问、回答、写文章 =>暂不支持
	- [2] 最新动态
		- [2.1] 列表显示 =>加载更多
		- [2.2] 列表内容 =>
			- [2.2.1] 有图片
			- [2.2.2] 无图片
			- [2.2.3] 内容过多
			- [2.2.4] 内容不多
- [ ] 侧栏消息
	- [1] 我的收藏 =>n多个收藏
	- [2] 我关注的问题
	- [3] 邀请我回答的问题
- [ ] 知乎专栏、知乎圆桌、知乎书店 暂不支持

### 2. 话题
- [ ] 已关注的话题动态
	- [1] n多标签 =>默认显示第一个(优化：默认选择全部，然后全部择优显示)
	- [2] 热门排序|时间排序 =>默认热门排序、这样更突出该用户喜欢的内容
	- [3] 排序的列表 =>(首页-显示主内容-[2]最新动态-[2.2])
	- [4] 显示更多   =>(首页-显示主内容-[2]最新动态-[2.1])
- [ ] 其他人关注的话题 
	- [1] 热门的5个话题

### 3. 发现
- [ ] 内容推荐
	- [1] 排序的列表 =>(首页-显示主内容-[2]最新动态-[2.2])
	- [2] 显示更多   =>(首页-显示主内容-[2]最新动态-[2.1])
- [ ] 热门话题
	- [1] 更多话题 just a link
	- [2] 头像 + 关注人数 + 话题链接
- [ ] 热门收藏
	- [1] 换一批 ->点击发送ajax
	- [2] 话题链接 + 收藏人数 + 回复条数

### 4. 消息
- [ ] 关于我的消息
- [ ] 关注我的人
- [ ] 你回答问题的回复

### 5. 头部
- [ ] 搜索内容
	- [1] 搜索结果展示(内容)
		- [1.1]: 排序的列表 =>(首页-显示主内容- [2]最新动态- [2.2])
		- [1.2] 显示更多   =>(首页-显示主内容- [2]最新动态- [2.1])
	- [2] 搜索结果展示(用户)
		- [2.1] 用户列表
	- [3] 搜索结果展示(话题)
		- [3.1] 话题列表
- [ ] 导航栏
	- [1] logo 
	- [2] 主导航栏
	- [3] 提问(99+的消息提示)
	- [4] 用户名
		- [4.1] 注册 =>现在是爬取的信息，那么暂不支持这个
		- [4.2] 登录

### 6. 个人主页
- [ ] 暂时不做 

### 7. 私信
- [ ] 暂时不做

### 8. 设置
- [ ] 暂时不做

### 9. 文件排列
``` javascript
|___
	zh-crawl-app (py爬虫)
		|___
			venv (爬虫包)
				|___
					home.py (home的抓取)
					etc     (其他都是引入的包)

	zh-front-app (vue前端代码)
		|___
			src
				|___
					app
						|___
						|	components (公用组件)
						|		|___
						|			header (头部)
						|				|___
						|					nav (导航栏)
						|			|___footer (尾部声明)
						|___
							home  (主页)
							pages (头部以下主要内容)
							topic (话题)

```

### 10. 项目进度
- [ ] zh-front-app
	- [x] 由于在install vue-cli之前没有install webpack
	- [x] 好像是npm版本太低 update -g可以
- [ ] zh-crawl-app
	- [x] pip install virtualenv (Python1.7.11+ 目前发现是这样子)
	- [x] virtualenv venv
	- [x] venv: pip install requests beautifulsoup4
	- [x] chardet: pip install chardet 判断文本编码的(eg utf-8/gb2312...)
	- [x] pip更新: python ...忘了Q_Q
	- [x] 引入urllib2模板,然后使用urlopen即可：打算使用.html暂存,然后每多少请求一次,推翻之前的那些模板吧,不然不同机子运行会有问题
	- [x] 判断网络连接 没有从文件读 然后定时器
	- [ ] 判断定时器a、使用os.system('netstat') b、os.systm('ping baidu.com')然后遍历 c、使用urlopen打开，失败即网络连接失败
	- [ ] 判断拉取下来的编码

