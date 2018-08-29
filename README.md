# 微信好友数据分析
#### 动机：前几天帮boss做项目，用到了echarts,趁着没忘，对，就是这样

#### get_user_info.py文件用来获取好友信息，包括头像，昵称，性别，所在省份，个性签名等
#### analyse.py文件用来生成具体的可视化图像

## 开发环境 python 3 
#### 
- PIL: pip3 install pillow
- pyecharts：pip3 install pyecharts
- pip3 install itchat
- pip3 install jieba

地图数据包：  
- pip3 install echarts-countries-pypkg
- pip3 install echarts-china-provinces-pypkg
- pip3 install echarts-china-cities-pypkg
- pip3 install echarts-china-counties-pypkg
- pip3 install echarts-china-misc-pypkg

## 以我本人的微信为例
#### 将所有好友的头像进行合成
<img height="300" align="center" src="https://github.com/lbio233/wechat/blob/master/analyse/merged.png" alt="">

#### 好友性别分布
<img align="center" src="https://github.com/lbio233/wechat/blob/master/source/pie.png" alt="">

### 好友所在省份，以及他们在地图上的展示
<img align="center" src="https://github.com/lbio233/wechat/blob/master/source/bar.png" alt="">

<img align="center" src="https://github.com/lbio233/wechat/blob/master/source/map.png" alt="">

#### 各位的个性签名词云
<img align="center" src="https://github.com/lbio233/wechat/blob/master/source/word_cloud.png" alt="">

## 喜欢的话，可以送我小星星嘛？
