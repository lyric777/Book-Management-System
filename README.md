# Book-Management-System
Flask + LayUI + SQLite，图书管理Web系统

使用说明+功能演示：

下载整个程序包，确保系统有python3环境，打开cmd，输入命令（替换成本机的工程目录地址）：
python F:\book_management_sys\book_management_sys.py runserver

浏览器输入  http://127.0.0.1:5000/  进入系统

系统分两类用户：普通读者用户，管理员用户。

普通读者用户可以查看图书信息和查看借阅记录，在登录页顶端导航栏切换功能，不用输入用户名、密码。

管理员用户可使用一切功能，账号、密码登陆后，进行日常业务操作。

测试数据： 图书信息书名可填写“学习”“机器”，类别可填写“计算机”等；学生借阅卡可填写：16000001,16000002,16000003（该卡无借阅记录）；

# 管理员功能使用说明
登录页面:  账号：201801  密码：123456，后续页面增加路由保护功能，以下为登录页面演示：
![image](https://github.com/lyric777/Book-Management-System/blob/master/gif/login.gif)

在主菜单栏点击查询图书信息，选择查询方式（书名，ISBN，作者，类别），并且输入查询内容，进行模糊搜索，渲染表格显示搜索结果；若无查询结果，则提示无结果：
![image](https://github.com/lyric777/Book-Management-System/blob/master/gif/searchbook.gif)

在主菜单栏点击查询学生信息，输入学生借阅卡号码，进行查询，显示学生基本信息，并且渲染表格显示该学生的借阅记录：
![image](https://github.com/lyric777/Book-Management-System/blob/master/gif/searchstudent.gif)

在主菜单栏点击图书管理，展开二级菜单，点击新书入库，新书入库功能又分为两个子功能，如果采购的书之前图书馆没有，则先点击“新书登记”填写新书的信息，在对该书进行编号，在库存补充子功能里填写图书编号、位置等信息：
![image](https://github.com/lyric777/Book-Management-System/blob/master/gif/newbook.gif)

点击图书管理下的“学生借书”，输入要借书的学生借阅卡号码，提供按书名查找、显示可借的图书列表，点击搜索，渲染表格，选中某一行进行借出操作，确认后，表格进行重载，可连续进行借出操作（如果该借阅卡欠费、到期或者已挂失，会给出相应提示信息）：
![image](https://github.com/lyric777/Book-Management-System/blob/master/gif/borrow.gif)

点击图书管理下的“学生还书”，输入要还书的学生借阅卡号码，点击，显示该学生未还的图书列表，选中某一行进行归还操作，确认后，表格重载，可连续进行归还操作：
![image](https://github.com/lyric777/Book-Management-System/blob/master/gif/return.gif)

在侧边主菜单点击信息设置，可修改现在登录的管理员的信息，在顶端导航栏，光标移到管理员姓名或头像上，选择查看个人信息或者修改密码：
![image](https://github.com/lyric777/Book-Management-System/blob/master/gif/changepw.gif)

# 普通用户功能使用说明
在登录页面顶端导航栏上选择，查询图书信息或者查询学生信息，页面及使用与管理员功能说明一致：
![image](https://github.com/lyric777/Book-Management-System/blob/master/gif/common.gif)

