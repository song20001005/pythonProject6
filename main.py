import requests
import json
import pandas as pd
import threading
n = 0
lis = [3, 1, 2]
x = 16804
id = []
goodComments = []
title_three = []
title_one = '个人护理'
title_two = '口腔护理'
title_third = ['牙膏', '牙刷', '牙线/牙线棒', '漱口水', '口腔护理套装']
df_all = pd.DataFrame(index=['title_one', 'title_two', 'title_three', 'id', 'goodComments'])
cookies = {
    '__jdu': '1662558366980405616591',
    'areaId': '18',
    'ipLoc-djd': '18-1482-0-0',
    'unpl': 'JF8EAKlnNSttXkoDB08KTkdET1xTW1oLHB9RODIMXV9RG1MAHQUfEhR7XlVdXhRKHx9vZRRUWFNKUA4ZASsSEXtfVVdcDkgWA25XNVNdUQYVV1YyGBIgS1xkXloPSBMHZmUCU1VRSlEEHwUbFRRDXWRuWghCJzNfYgVVXFxIUgMYCisTIElcVVtVCkMUCm5XTjpcFUtTAhgGHxsSTFpcV1wNShMEb2ABXF1oSmQG',
    '__jdv': '122270672|t.zoukankan.com|t_308072010_|tuiguang|70f3e9dde506462f9cfd8838a6476515|1663049133820',
    'pinId': '1AraDNxXQYmzDIyxbeiGwuX_gsAoUmvs',
    'unick': 'jd_Q8Yj82NWYIh8tgY',
    '_tp': 'GOjjwmEeKMlb2WYfirATKS2UR3XP0YKwwSua6tt5SuY%3D',
    '_pst': 'jd_Q8Yj82NWYIh8tgY',
    'login': 'true',
    '3AB9D23F7A4B3C9B': '7HYU4RPTCTHCRFNKFA26MFVM6W4JUUNONU6UW5YWYYG4IUOL4TYIU6QAXWRSNUP54SFOAFU5Y6UXD3NLLE3LHGBKYM',
    'TrackID': '1iuqwQsTAuKWnn7WLL4N693ZiXsLEhqDhddWFzYxY8o-0Cs9KQiVCJf3A9LsTFnTGiECwJNWu-s2lYQz-DUlGjnA9cTOun5rqQCIcMmmfiC1Ba1MlLbskDZtcEdcjLq-tqdwSqHh8jY49xOVhP6Vdig',
    'pin': 'jd_Q8Yj82NWYIh8tgY',
    'ceshi3.com': '000',
    '__jda': '209449046.1662558366980405616591.1662558366.1663152177.1663154994.6',
    '__jdc': '209449046',
    'MMsgIdjd_Q8Yj82NWYIh8tgY': '7551649',
    'MNoticeIdjd_Q8Yj82NWYIh8tgY': '529',
    'ssid': '"BYXfM45LSaqDTJU7bXR41A=="',
    'sidebarStatus': '0',
    'thor': '29F7824425E099A8DC44A3DE57DF58C2C91D66A231D37830E8BF99B3D1157F98E2DD5AD78894C1BDB6BF091F83CC60C5F6405ECC5256209D8E2DB4B8B026A945A4503CF847D8E2E8A8612A7469410AB40478F38AC588B823BDC2394DC8436071204D786F932B52FA46944A14AC6B60F3FEF6855E1E345440193E4361080DBD6EE80FDFD7DEC6016BDE2E10E0ABF3FA84F2F027239D366C23C3BCE2AB94E9CF77',
    '__jdb': '209449046.70.1662558366980405616591|6.1663154994',
    'RT': '"z=1&dm=jd.com&si=ylni5378ppj&ss=l81jjhzw&sl=1q&tt=3hie&ld=3mnnk&nu=5f816c624352b16dbea9ecffde5a1db6&cl=367lw"',
}

headers = {
    'authority': 'union.jd.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '";Not A Brand";v="99", "Chromium";v="94"',
    'accept': 'application/json, text/plain, */*',
    'content-type': 'application/json;charset=UTF-8',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.175.400 QQBrowser/11.1.5155.400',
    'sec-ch-ua-platform': '"Windows"',
    'origin': 'https://union.jd.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://union.jd.com/proManager/index?categories=16750,16755,16806&pageNo=1',
    'accept-language': 'zh-CN,zh;q=0.9',
    # Requests sorts cookies= alphabetically
    # 'cookie': '__jdu=1662558366980405616591; areaId=18; ipLoc-djd=18-1482-0-0; unpl=JF8EAKlnNSttXkoDB08KTkdET1xTW1oLHB9RODIMXV9RG1MAHQUfEhR7XlVdXhRKHx9vZRRUWFNKUA4ZASsSEXtfVVdcDkgWA25XNVNdUQYVV1YyGBIgS1xkXloPSBMHZmUCU1VRSlEEHwUbFRRDXWRuWghCJzNfYgVVXFxIUgMYCisTIElcVVtVCkMUCm5XTjpcFUtTAhgGHxsSTFpcV1wNShMEb2ABXF1oSmQG; __jdv=122270672|t.zoukankan.com|t_308072010_|tuiguang|70f3e9dde506462f9cfd8838a6476515|1663049133820; pinId=1AraDNxXQYmzDIyxbeiGwuX_gsAoUmvs; unick=jd_Q8Yj82NWYIh8tgY; _tp=GOjjwmEeKMlb2WYfirATKS2UR3XP0YKwwSua6tt5SuY%3D; _pst=jd_Q8Yj82NWYIh8tgY; login=true; 3AB9D23F7A4B3C9B=7HYU4RPTCTHCRFNKFA26MFVM6W4JUUNONU6UW5YWYYG4IUOL4TYIU6QAXWRSNUP54SFOAFU5Y6UXD3NLLE3LHGBKYM; TrackID=1iuqwQsTAuKWnn7WLL4N693ZiXsLEhqDhddWFzYxY8o-0Cs9KQiVCJf3A9LsTFnTGiECwJNWu-s2lYQz-DUlGjnA9cTOun5rqQCIcMmmfiC1Ba1MlLbskDZtcEdcjLq-tqdwSqHh8jY49xOVhP6Vdig; pin=jd_Q8Yj82NWYIh8tgY; ceshi3.com=000; __jda=209449046.1662558366980405616591.1662558366.1663152177.1663154994.6; __jdc=209449046; MMsgIdjd_Q8Yj82NWYIh8tgY=7551649; MNoticeIdjd_Q8Yj82NWYIh8tgY=529; ssid="BYXfM45LSaqDTJU7bXR41A=="; sidebarStatus=0; thor=29F7824425E099A8DC44A3DE57DF58C2C91D66A231D37830E8BF99B3D1157F98E2DD5AD78894C1BDB6BF091F83CC60C5F6405ECC5256209D8E2DB4B8B026A945A4503CF847D8E2E8A8612A7469410AB40478F38AC588B823BDC2394DC8436071204D786F932B52FA46944A14AC6B60F3FEF6855E1E345440193E4361080DBD6EE80FDFD7DEC6016BDE2E10E0ABF3FA84F2F027239D366C23C3BCE2AB94E9CF77; __jdb=209449046.70.1662558366980405616591|6.1663154994; RT="z=1&dm=jd.com&si=ylni5378ppj&ss=l81jjhzw&sl=1q&tt=3hie&ld=3mnnk&nu=5f816c624352b16dbea9ecffde5a1db6&cl=367lw"',
}
for i in range(2, 7):
    x = x + lis[i % 3]
    for n in range(0, 100):
        json_data = {
            'pageNo': 1 + n,
            'pageSize': 60,
            'searchUUID': '75b8fd61e052402b8de28198393868f7',
            'data': {
                'bonusIds': None,
                'categoryId': 16750,
                'cat2Id': 16755,
                'cat3Id': x,
                'deliveryType': 0,
                'fromCommissionRatio': None,
                'toCommissionRatio': None,
                'fromPrice': None,
                'toPrice': None,
                'hasCoupon': 0,
                'isHot': None,
                'preSale': 0,
                'isPinGou': 0,
                'jxFlag': 0,
                'isZY': 0,
                'isCare': 0,
                'lock': 0,
                'orientationFlag': 0,
                'sort': None,
                'sortName': None,
                'searchType': 'st3',
                'keywordType': 'kt0',
            },
        }

        response = requests.post('https://union.jd.com/api/goods/search', cookies=cookies, headers=headers,
                                 json=json_data)
        response = response.text
        data = json.loads(response)
        for m in range(0, 60):
            try:
                id.append(data['data']['unionGoods'][m][0]['skuId'])
                goodComments.append(data['data']['unionGoods'][m][0]['goodComments'])
                title_three.append(title_third[i-2])
            except:
                continue
df = pd.DataFrame({'title_one': title_one, 'title_two': title_two, 'title_three': title_three, 'id': id,
                   'goodComments': goodComments})
df.to_csv('店铺数据01.csv',index=False,encoding='gbk')

# 需求：爬取上图圈出的5个3级分类（牙膏，牙刷，牙线/牙线棒，漱口水，口腔护理套装）下的所有商品（超过6000）。输出csv文件，一共5列：一级分类，二级分类，三级分类，商品id,好评数。
# https://union.jd.com/proManager/index?categories=16750,16755&pageNo=1