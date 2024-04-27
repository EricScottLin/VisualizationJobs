## 爬取数据

- [ ]  1. 打开Chrome调试控制台

  ```bash
  google\ chrome --remote-debugging-port=9222 
  ```

- [ ] 2. 运行`MainCrawl.py`爬虫程序

- [ ] 3. 检查`temp.csv`文件

- [ ] 4. 检查mysql数据库



## 运行服务

- [ ] 1. 安装依赖

	```bash
	pip install -r requirements.txt
	```

- [ ] 2. 修改MySQL连接配置

  修改`ml/settings.py`

  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'bossinfo',	# 数据库
          'USER': 'root',	# 用户名
          'PASSWORD': '123456',	# 密码
          'HOST': 'localhost',	# IP地址
          'PORT': '3306',	# 端口号
      }
  }
  ```

  修改`myApp/wordCloud.py`

  ```python
  # 连接数据库
  con = connect(host="localhost",	# IP地址
                user="root",	# 用户名
                password="123456",	# 密码
                database="bossinfo",	# 数据库
                port=3306,	# 端口号
                charset="utf8mb4")	# 数据库字符集
  ```

- [ ] 3. 生成数据库迁移文件

  ```bash
  python manage.py makemigrations
  ```

- [ ] 4. 迁移数据库

  ```bash
  python manage.py migrate
  ```

- [ ] 5. 运行服务

  ```bash
  python3 manage.py runserver 8000
  ```

- [ ] 6. 打开服务器查看页面

  ```http
  localhost:8000/jobVisualization/main/
  ```

  
