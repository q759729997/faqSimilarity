# 相似度匹配结果-tfidf

## 2Gram

~~~wiki
text:朱日和站
words:['朱日', '日和', '和站']
search_result:[('朱日和基', 0.81649655), ('温都尔站', 0.0)]
text:温都尔站
words:['温都', '都尔', '尔站']
search_result:[('温都尔站', 0.99999994), ('东乌广厦', 0.0)]
text:国电站
words:['国电', '电站']
search_result:[('国电四郎', 0.57735026), ('温都尔站', 0.0)]
~~~

## 1Gram

~~~wiki
text:朱日和站
words:['朱', '日', '和', '站']
search_result:[('朱日和基', 0.8227205), ('温都尔站', 0.109244354)]
text:温都尔站
words:['温', '都', '尔', '站']
search_result:[('温都尔站', 0.99999994), ('阿尔善站', 0.24478666)]
text:国电站
words:['国', '电', '站']
search_result:[('国电四郎', 0.6559487), ('温都尔站', 0.13064952)]
~~~

## 结巴

- 非精确匹配：

~~~wiki
text:朱日和站
words:['朱日', '和', '站']
search_result:[('朱日和基', 0.7574243), ('温都尔站', 0.18476632)]
text:温都尔站
words:['温都尔', '站']
search_result:[('温都尔站', 1.0), ('阿尔善站', 0.24478666)]
text:国电站
words:['国', '电站']
search_result:[('温都尔站', 0.0), ('东乌广厦', 0.0)]
~~~

- 精确匹配：

~~~wiki
text:朱日和站
words:['朱', '日', '和', '站']
search_result:[('朱日和基', 0.8227205), ('温都尔站', 0.15449485)]
text:温都尔站
words:['温都尔', '站']
search_result:[('温都尔站', 1.0), ('阿尔善站', 0.15449485)]
text:国电站
words:['国电', '电站']
search_result:[('国电四郎', 0.57735026), ('温都尔站', 0.0)]
~~~