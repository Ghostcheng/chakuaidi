# -*- coding: utf-8 -*-
import json
import requests
def searchPackage():
    packageNum = input('请输入运单号码(只有正在途中才能看到哦):')
    url1 = 'http://www.kuaidi100.com/autonumber/autoComNum?resultv2=1&text=' + packageNum

    #  用url1查询运单号对应的快递公司，如中通，返回：中通。
    companyName = json.loads(requests.get(url1).text)['auto'][0]['comCode']

    #  在用url2查询和运单号、快递公司来查询快递详情，结果是一个json文件，用dict保存在resultdict中。
    url2 = 'http://www.kuaidi100.com/query?type=' + companyName + '&postid=' + packageNum

    print('时间↓               地点和跟踪进度↓\n')

    for item in json.loads(requests.get(url2).text)['data']:
        print(item['time'], item['context'])

searchPackage()