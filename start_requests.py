def start_requests(**kwargs):
    # TODO: 根据网站栏目数量, 复制要传递的列表页参数定义部分
    # TODO: 请复制粘贴网站名
    web_site = "请替换此处为网站名"

    # TODO: 请复制粘贴栏目的链接
    web_site_url = "请替换此处为栏目的链接"
    hub_fields = {"web_site": web_site, "web_site_url": web_site_url}

    # 根据需要选择下面的模板代码块
    # 只有一条列表页
    # TODO: 请仔细核对配置页面编号, 修改None值
    yield {"url": web_site_url, "page_rule_id": None, "hub_fields": hub_fields}

    # 列表页分页为GET请求
    # TODO: 请仔细核对配置分页总页数, 修改None值
    for page in range(None):
        # TODO: 计算页码
        page = f"_{page}" if page else ""
        # TODO: 请复制粘贴列表页链接, 并修改变化部分为page参数
        url = f"请替换此处为列表页链接然后修改为格式化字符串"
        # TODO: 请仔细核对配置页面编号, 修改None值
        yield {"url": url, "page_rule_id": None, "hub_fields": hub_fields}

    # 列表页分页为POST请求: 请先尝试转换为GET方式是否可行
    # TODO: 请仔细核对配置页面编号, 修改None值
    url = ""
    for page in range(None):
        page = f"_{page}" if page else ""
        data = f""
        yield {
            "url": url,
            "page_rule_id": None,
            "data": data,
            "method": "POST",
            "hub_fields": hub_fields,
        }

    # 栏目链接相似度较高的列表页
    cates = [
        {"cate": "请替换此处为栏目链接的差异部分", "pages": None},
        {"cate": "请替换此处为栏目链接的差异部分", "pages": None},
    ]
    for each in cates:
        cate = each["cate"]
        pages = each["pages"]
        web_site_url = f"请替换此处为栏目的链接格式化"
        hub_fields = {"web_site": web_site, "web_site_url": web_site_url}
        for page in range(pages):
            page = f"_{page}" if page else ""
            url = f""
            yield {"url": url, "page_rule_id": None, "hub_fields": hub_fields}


if __name__ == "__main__":
    for each in start_requests():
        print(each)
