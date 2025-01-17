# conference-reference-4-RIS
conference reference list in RIS format

only for ICLR2024

## todo

- [x] ICLR 2024 ` ICLR-2024-accepted.ris`
- [ ] ICLR 2023以前报错 报错
- [x] 使用python编程调用openreview的API读取会议论文的列表
- [ ] 

## about code

- `getpaperlistfromopenreview.py`: 从openreview获取对应会议论文列表，并输出RIS格式，包含摘要

- usage：

  - 新建一个`username_passwd.json`, 将其中的openreview的用户名和密码替换

    ````
    {
        "username": "<yourusername>",
        "password": "<yourpasswd>"
    }
    ````

    

  - 修改 `line111-112` 为你要获取的会议的ID，已经论文状态

  - run `getpaperListfromOpenreview.py`, 会在当前目录输出一个 `conferencename-year-status.ris`



## reference

- 第三方整理，缺点：等，看运气
- dblp数据库， 缺点：不包含abstract
- [代码 | 从 OpenReview 获取顶会接收论文集并保存至本地数据库 - 知乎](https://zhuanlan.zhihu.com/p/628467095)

- openreview api：[openreview/openreview-py: Official Python client library for the OpenReview API](https://github.com/openreview/openreview-py)

- openreview api 函数： [OpenReview Python Client Documentation — OpenReview Python Client 0.0.1 documentation](https://openreview-py.readthedocs.io/en/latest/)
- [代码 | 从 OpenReview 获取顶会接收论文集并保存至本地数据库 - 知乎](https://zhuanlan.zhihu.com/p/628467095)
- [OpenReview API | 灵活高效的学术论文筛选-CSDN博客](https://blog.csdn.net/qq_39517117/article/details/142959952)

**************************

- [How to Get All Submissions | OpenReview](https://docs.openreview.net/how-to-guides/data-retrieval-and-modification/how-to-get-all-submissions)

- [How to loop through Accepted Papers and print the Authors and their Affiliations | OpenReview](https://docs.openreview.net/how-to-guides/data-retrieval-and-modification/how-to-loop-through-accepted-papers-and-print-the-authors-and-their-affiliations)
