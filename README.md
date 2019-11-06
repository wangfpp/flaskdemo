### Flask Jinja2学习项目

## 依赖项
- flask

## 功能
- 1. 列表判断循环
- 2. HTML post提交数据Flask接收请求数据处理后render_template

```javascript
    {% name %} // 变量
    {% for item in list%}
         {% set outer_loop = loop %} // 设置一个可用变量
         {% if item["childrens"] | count > 0 %}　// 过滤器 count/length
            <div class="list_item {{'selected' if item.name == curr}}"></div>　// DOM节点中进行动态绑定
        {% endif %}
    {% endfor %}
```

### 后续继续学习