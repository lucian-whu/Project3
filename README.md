# 20170626

* 爬取mesh中的每个词的“Year introduced”

 * * meshes.txt: mesh词列表
* * * 从meshInformation.csv中得到meshes.txt


* * 编写request爬虫从网站上爬取 crawlMesh.py
* * * 发现利用mesh词检索的话，可能出现多个选项，没有直接到达页面；
* * * 换用mesh编号后，还是有这样的情况，因此标记为checkAgainLater