# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 13:23:32 2018

@author: 15862
"""

import json
import re
from pyecharts import Bar
from pyecharts import Grid
from pyecharts import WordCloud
from pyecharts import Pie
from pyecharts import Map
from collections import Counter
import jieba.analyse
import PIL.Image as Image
import os
import math
import codecs

def get_pie(item_name,item_name_list,item_num_list):
    total = item_num_list[0]+item_num_list[1]+item_num_list[2]
    subtitle = "共有：%d个好友"%total
    
    pie = Pie(item_name_list,page_title = item_name,title_text_size=30,title_pos='center',\
              subtitle=subtitle,subtitle_text_size=25,width=800,height= 800)
    pie.add("",item_name_list,item_num_list,is_label_show=True,center=[50, 45],radius=[0,50],\
        legend_pos ='left',legend_orient='vertical',label_text_size=20)
    
    out_file_name = './analyse/'+item_name+'.html'
    pie.render(out_file_name)
    
def get_bar(item_name,item_name_list,item_num_list):
    subtitle="lbio_wechat"
    bar = Bar(item_name,page_title=item_name,title_text_size=30,title_pos='center',\
        subtitle = subtitle,subtitle_text_size = 25)
    bar.add("",item_name_list, item_num_list,title_pos='center', xaxis_interval=0,xaxis_rotate=27,\
        xaxis_label_textsize = 20,yaxis_label_textsize = 20,yaxis_name_pos='end',yaxis_pos = "%50")
    bar.show_config()
    grid = Grid(width=1300,height= 800)
    grid.add(bar,grid_top = "13%",grid_bottom = "23%",grid_left = "15%",grid_right = "15%")
    
    out_file_name = './analyse/'+item_name+'.html'
    bar.render(out_file_name)
    
def get_map(item_name,item_name_list,item_num_list):
    subtitle = 'lbio_wechat'
    _map = Map(item_name,width=1300,height= 800,title_pos='center',title_text_size=30,\
               subtitle = subtitle,subtitle_text_size = 25)
    _map.add("", item_name_list, item_num_list, maptype='china', is_visualmap=True, visual_text_color='#000')

    out_file_name = './analyse/'+item_name+'.html'
    _map.render(out_file_name)

def word_cloud(item_name,item_name_list,item_num_list):
    wordcloud = WordCloud(width=1400,height= 900)
    
    wordcloud.add("", item_name_list, item_num_list,word_size_range=word_size_range,shape='pentagon')
    out_file_name = './analyse/'+item_name+'.html'
    wordcloud.render(out_file_name)

    

def get_tag(text,cnt):
    text = re.sub(r"<span*span>","",text)
    print('正在分析句子：',text)
    tag_list = jieba.analyse.extract_tags(text)
    for tag in tag_list:
        cnt[tag] += 1
    
def dict2list(_dict):
    name_list = []
    num_list = []
    
    for key,value in _dict.items():
        name_list.append(key)
        num_list.append(value)
    
    return name_list,num_list

def counter2list(_counter):
    name_list = []
    num_list = []
    
    for item in _counter:
        name_list.append(item[0])
        num_list.append(item[1])
    return name_list,num_list

def mergeImage()
    
    

if __name__ == '__main__':
    
    in_file_name = './data/friends.json'
    with codecs.open(in_file_name,encoding='utf-8') as f:
        friends = json.load(f)
    
    sex_counter =  Counter()#性别
    Province_counter = Counter()#省份
    NickName_list = [] #昵称
    Signature_counter = Counter()#个性签名关键词
    
    for friend in friends:
        sex_counter[friend['Sex']] += 1
        if friend['Province'] != '':
            Province_counter[friend['Province']] += 1
        NickName_list.append(friend['NickName'])
        get_tag(friend['Signature'],Signature_counter)
        
    name_list,num_list = dict2list(sex_counter)
    get_pie('性别统计',name_list,num_list)
    
    name_list,num_list = counter2list(Province_counter.most_common(15))
    get_bar('地区统计',name_list,num_list)
    
    get_map('微信好友地图可视化',name_list,num_list)
    
    name_list,num_list = counter2list(Signature_counter.most_common(200))
    wordCloud('个性签名词云'，name_list,num_list)
    
    mergeImage()