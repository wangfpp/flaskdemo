> 本文简单阐述一下MVC然后会写一个基于Python Flask的DEMO

### 什么是MVC

> MVC模式（Model–view–controller）是软件工程中的一种软件架构模式，把软件系统分为三个基本部分：模型（Model）、视图（View）和控制器（Controller）。

先放一张图片
![MVC](https://graph.baidu.com/resource/111bfb00e2c224d739a2901573177862.jpg)
### 模型Model
Model是Controller处理DataBase后得到的能够被View_Template解析的一个数据结构
- 1. Model只受Controller的控制做出变更继而影响View
### 视图View
   视图和用户的距离最近,使用户可以操作数据的窗口,也就是HTML或者其他的展示形式,其实就是展示和提供操作Model的能力
- 1. 视图接收Controller传递过来的Model利用模板插值来解析这些数据填充View
- 2. 用户通过外射操作View把操作指令传递给Controller　也就是HTTP或者其他的Interface请求

### 控制器 Controller
Controller在View和Model中间做为一个数据处理中转的地方,隔离数据和视图并提供修改功能
- 1. Controller从DataBase中拿到数据　经过处理成View_Template能够解析的Model结构
- 2. View经过用户的操作对Data做更改指令　Controller接收指令后操作DB来改变Model从而又影响View的变更

### 实战MVC(基于Python Flask)
具体如何使用看github的说明,这里只阐述逻辑[github](https://github.com/wangfpp/flaskdemo)
https://github.com/wangfpp/flaskdemo
### 一个变量的例子
Controller上定义一个路由、Madel、需要render的HTML Template
```python
## 首页路由
@app.route('/')
def index():
    name= {"name": "wangfpp"}
    title={"title": "首页"}
    hobby={"hobby": ['Study', "Game", "Girl"]}
    info = {**name, **title, **hobby}　#这里相当于处理DataBase
    # info=info就是Model
    return render_template('index.html', info=info)
```
View接收Model并渲染
```html
<title>{{info.title}}</title>　// 这里可以直接取值
<body>
    {% set name = info.name%} //这里可以设置变量
    <p name="{{name}}">我的名字是: {{name}}</p>　
    //模板插值也可以动态绑定属性
    <p>我的爱好: {{info.hobby | list2str("&&")}}</p>　
　　//list2str是我自定义的一个过滤器 Vue里面也有类似的过滤器
</body>
```
效果
![效果](https://graph.baidu.com/resource/1110d434e60d1ae75ff9501573181261.jpg "flask mvc")

### 一个列表渲染和条件渲染的例子
数据结构为多级列表用if条件控制渲染
控制当前选中的列表和其他列表颜色不同 有子列表的要渲染子列表　还能修改当前选中的列表项
```python

## 列表页路由　
@app.route('/list', methods=['GET', 'POST'])　# 定义C和Ｖ之间的Interface
def list_name():
    method = request.method
    selectitem = 'app'
    lista= [ #两层列表
      {"title": 'app', "name": 'app', "desc": 'peoject', 
         "childrens": []},
      {"title": 'Vue', "name": 'Vue', "desc": '前端项目框架', 
         "childrens": ['route', 'vuex']},
      {"title": 'ReactNative', "name": 'ReactNative', "desc": '媲美原生应用的App框架', 
         "childrens": ['JSBridge', 'Route', 'Storage']}
    ]
    if method == 'GET': #如果是get直接render_template
        return render_template('list.html', title="列表循环", list=lista, curr=selectitem)

    elif method == 'POST': # POST则修改当前选中的列表项
        req_dict = request.form.to_dict()
        return render_template('list.html', title="列表循环", list=lista, curr=req_dict["name"])
```
HTML View渲染
```html
<body>
    <h3>列表循环</h3>
   <div class="lietcontainer">
    {% for item in list %} // 循环列表
        {% set outer_loop = loop %} //这里是获取循环的下标index
        {% set children = item["childrens"] %}　// 设置变量
        <div class="list_item {{'selected' if item.name == curr}}" // 动态绑定属性是不是选中的列表项
　　　　　　　index={{outer_loop.index}} 
　　　　　　　name={{item.name}}>
　　　　　　　　这是第 {{ outer_loop.index }}个span {{item.name}}
            {% if children | count > 0 %}
                <div class="children">
                  {% for child in children %}
                     <p class="child_item {{'selected' if item.name == curr}}" >{{child}}</p>
                  {% endfor %}
                </div>
            {% endif %}
        </div>
    {% endfor %}
   </div>
   <div class="select_container">
    {{curr}}
   </div>
</body>
```
Javascript部分　修改当前选择项
```javascript
document.onload = function() {
    let listNode = document.querySelectorAll('.list_item');
    listNode.forEach(node => {
        node.onclick = function() {
            $(this).children('.children').css({display: 'block'});
            let name = $(this).attr('name'),
            index = $(this).attr('index');
            $.ajax({
                method: 'POST',
                url:'/list',
                data: {name, index},
                success: (res) => {
                    document.body.innerHTML = "";
                    document.write(res);
                },
                error: err => {
                    console.log(err);
                }
            })
        }
    })
}()
```
效果图　初始渲染第一个为选择项
![初始渲染](https://graph.baidu.com/resource/1114619322e32401e5f2f01573182154.jpg)
用户操作点击第二个通过AJAX　POST修改选择项
![修改选择项](https://graph.baidu.com/resource/11152169c10eb33a3c33301573182205.jpg)

### 还有一个文件上传的功能这里就不做展示了代码会放到Github上

### 模板语法说明部分
```javascript
{{变量名称}} 
{% 控制语句 %} {% end控制语句%}
{% for item in lista %}....{% endfor %}
{% if a > b % } {% endif %}
{% set a = item.info %}
// 总结双大括号{{}}是用于Model显示的
// 单大括号加百分号{% %}用于控制渲染流程的
```
### 写在最后
具体的模板语法学习可以查阅Jinja2的文档　http://docs.jinkan.org/docs/jinja2/
不过这个东西的名字挺恶心人的Jinja(神社)