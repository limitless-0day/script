### 项目名称
脚本存储网页

### 项目简介
本项目旨在创建一个网页，用于存储和展示各种命令，用户可以通过粘贴复制命令到服务器来完成nginx、MySQL等软件的安装任务。项目还包含各种异常处理机制，确保用户在执行命令时能够避免潜在的问题。

### 发起时间
2024/5/7

### 技术选型
后端 python3.6 ，fastapi
前端 Vue

### 接口设计
1. 获取脚本列表
   请求方法：GET

请求路径：/v1/scripts
请求参数：无
响应示例：
```
{
"data": [
{
"id": 1,
"name": "安装nginx",
"command": "sudo apt-get install nginx"
},
{
"id": 2,
"name": "安装MySQL",
"command": "sudo apt-get install mysql-server"
}
]
}
```
2. 创建脚本
   请求方法：POST

请求路径：/v1/scripts

请求参数：

参数名 | 类型	 | 必填 | 描述
---- | ----- | -----|-
name | string | 是 | 脚本名称
command | string | 是 | 脚本命令

请求示例：
```
{
"name": "安装nginx",
"command": "sudo apt-get install nginx"
}
响应示例：

{
"data": {
"id": 1,
"name": "安装nginx",
"command": "sudo apt-get install nginx"
}
}
```
3. 更新脚本
   请求方法：PUT

请求路径：/v1/scripts/{id}

请求参数：

参数名 | 类型	 | 必填 | 描述
---- | ----- | -----|-
id	 | int	 | 是	 | 脚本ID
name	 | string	 | 否	 | 脚本名称
command | 	string | 	否	 | 脚本命令
请求示例：
```
{
"name": "更新nginx",
"command": "sudo apt-get update && sudo apt-get install nginx"
}
响应示例：

{
"data": {
"id": 1,
"name": "更新nginx",
"command": "sudo apt-get update && sudo apt-get install nginx"
}
}
```
4. 删除脚本
   请求方法：DELETE

请求路径：/v1/scripts/{id}

请求参数：

参数名 | 类型	 | 必填 | 描述
---- | ----- | -----|-
id | int | 是 | 脚本ID
响应示例：
```
{
"data": {
"id": 1,
"name": "更新nginx",
"command": "sudo apt-get update && sudo apt-get install nginx"
}
}
```
5. 获取脚本详情
   请求方法：GET

请求路径：/v1/scripts/{id}

请求参数：

参数名 | 类型	 | 必填 | 描述
---- | ----- | -----|-
id	 | int	 | 是	 | 脚本ID
响应示例：
```
{
"data": {
"id": 1,
"name": "更新nginx",
"command": "sudo apt-get update && sudo apt-get install nginx"
}
}
```
6. 搜索脚本
   请求方法：GET

请求路径：/v1/scripts/search?q={query}

请求参数：

参数名 | 类型	 | 必填 | 描述
---- | ----- | -----|-
query	 | string	 | 是	 | 搜索关键词
响应示例：
```
{
"data": [
{
"id": 1,
"name": "安装nginx",
"command": "sudo apt-get install nginx"
},
{
"id": 2,
"name": "安装MySQL",
"command": "sudo apt-get install mysql-server"
}
]
}
```

### 前端代码
前端代码主要负责展示用户界面和与后端进行通信

组件（Components）：Vue.js组件用于构建用户界面。组件可以是简单的HTML元素，也可以是复杂的用户界面部分。在本项目中，我们可能会有以下组件：
ScriptList.vue：用于显示脚本列表。
ScriptForm.vue：用于创建和更新脚本。
ScriptDetail.vue：用于显示脚本详情。
路由（Routes）：Vue Router用于管理应用程序的路由。在本项目中，我们可能会有以下路由：
/scripts：显示脚本列表。
/scripts/create：创建新脚本。
/scripts/:id：显示脚本详情。
/scripts/:id/edit：更新脚本。
状态管理（State Management）：Vuex用于管理应用程序的状态。在本项目中，我们可能会有一个Vuex store来存储脚本列表、当前选中的脚本等状态。
API请求（API Requests）：使用axios或fetch等HTTP客户端与后端进行通信。在本项目中，我们需要实现以下API请求：
GET /v1/scripts：获取脚本列表。
POST /v1/scripts：创建新脚本。
PUT /v1/scripts/:id：更新脚本。
DELETE /v1/scripts/:id：删除脚本。
GET /v1/scripts/:id：获取脚本详情。
GET /v1/scripts/search?q={query}：搜索脚本。
### 后端代码
后端代码主要负责处理API请求和与数据库进行通信。以下是后端代码的主要部分：

路由（Routes）：FastAPI使用路由来处理API请求。在本项目中，我们需要实现以下路由：
GET /v1/scripts：获取脚本列表。
POST /v1/scripts：创建新脚本。
PUT /v1/scripts/{id}：更新脚本。
DELETE /v1/scripts/{id}：删除脚本。
GET /v1/scripts/{id}：获取脚本详情。
GET /v1/scripts/search?q={query}：搜索脚本。
数据模型（Data Models）：使用Pydantic或SQLAlchemy等库定义数据模型。在本项目中，我们需要定义一个Script模型，包含id、name和command等字段。
数据库（Database）：使用SQLite、PostgreSQL等数据库存储脚本数据。在本项目中，我们可能会使用SQLite作为数据库。
异常处理（Error Handling）：在后端代码中，我们需要处理各种异常，例如数据库错误、验证错误等。我们可以使用FastAPI的异常处理机制来实现这一点。
中间件（Middleware）：FastAPI支持中间件，可以用于实现诸如身份验证、日志记录等功能。在本项目中，我们可能会使用中间件来处理跨域资源共享（CORS）问题。