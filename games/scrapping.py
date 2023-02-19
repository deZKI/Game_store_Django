"""Специальный файл для логики парсинга сайта steambuy и добавления информации в бд"""
import bs4
import requests
from fake_useragent import UserAgent


def scrapping(genres:list):

    cookies = {
        'PHPSESSID': '56e89338f28b97314440d763d7159cdc',
        'SL_G_WPT_TO': 'ru',
        'SL_GWPT_Show_Hide_tmp': '1',
        'SL_wptGlobTipTmp': '1',
        'WhiteCallback_updateMainPage': 'kCpPJ',
        '__sbn_uhs': 'a%3A3%3A%7Bi%3A1338013%3Bi%3A1%3Bi%3A2679639%3Bi%3A1%3Bi%3A2471968%3Bi%3A1%3B%7D',
        '__s3_huid': '11752942',
        '__s3_hses': 'ebddec4e4d269f31d1b2ade0346abf46fc975ce1',
        '__f_sub': '0.1.0.0.1676651493',
        'WhiteCallback_visitorId': '10555660694',
        'WhiteCallback_visit': '20379892670',
        'WhiteSaas_uniqueLead': 'no',
        '__cf_bm': 'M9uRlaqqRX2pUnm1zTbWGCqWgm4UC7JhDhUgnfaoSuM-1676693046-0-ARbRjeP2HQUjt7dds+jIsLxpxwCNr1yoPztyB4mH3AHflE35hKYjio3ey1pru45iDpi6I2DGo54Uxwb5CSabZ6Ihefc+0SDHQTvrcxfwcy+33lWHNIQH8eysUUr00Mp8lj4oJ9OyduaEPgYfZ9RD/To=',
        'WhiteCallback_openedPages': 'kCpPJ.ArGaK.CfJAF.EXyXQ',
        'WhiteCallback_mainPage': 'EXyXQ',
        '__sb3_c': 'a16fe59e622c33a925290428086c6bca',
        'WhiteCallback_timeAll': '7790',
        'WhiteCallback_timePage': '7804',
    }

    headers = {
        'authority': 'steambuy.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'cookie': 'PHPSESSID=56e89338f28b97314440d763d7159cdc; SL_G_WPT_TO=ru; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; WhiteCallback_updateMainPage=kCpPJ; __sbn_uhs=a%3A3%3A%7Bi%3A1338013%3Bi%3A1%3Bi%3A2679639%3Bi%3A1%3Bi%3A2471968%3Bi%3A1%3B%7D; __s3_huid=11752942; __s3_hses=ebddec4e4d269f31d1b2ade0346abf46fc975ce1; __f_sub=0.1.0.0.1676651493; WhiteCallback_visitorId=10555660694; WhiteCallback_visit=20379892670; WhiteSaas_uniqueLead=no; __cf_bm=M9uRlaqqRX2pUnm1zTbWGCqWgm4UC7JhDhUgnfaoSuM-1676693046-0-ARbRjeP2HQUjt7dds+jIsLxpxwCNr1yoPztyB4mH3AHflE35hKYjio3ey1pru45iDpi6I2DGo54Uxwb5CSabZ6Ihefc+0SDHQTvrcxfwcy+33lWHNIQH8eysUUr00Mp8lj4oJ9OyduaEPgYfZ9RD/To=; WhiteCallback_openedPages=kCpPJ.ArGaK.CfJAF.EXyXQ; WhiteCallback_mainPage=EXyXQ; __sb3_c=a16fe59e622c33a925290428086c6bca; WhiteCallback_timeAll=7790; WhiteCallback_timePage=7804',
        'referer': 'https://steambuy.com/catalog/?genres=indi,action,shuter',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {

        'offset': '0',
        'region_free': '0',
        'sort': 'cnt_sell',
        'sortMode': 'descendant',
        'view': 'extended',
        'a': 'getcat',
        'q': '',
        'series': '',
        'publisher': '',
        'izdatel': '',
        'currency': 'wmr',
        'curr': '',
        'currMaxSumm[wmr]': '3000',
        'currMaxSumm[wmz]': '100',
        'currMaxSumm[wme]': '70',
        'currMaxSumm[wmu]': '1000',
        'letter': '',
        'limit': '0',
        'page': '1',
        'minPrice': '0',
        'maxPrice': '9999',
        'minDate': '0',
        'maxDate': '0',
        'genres[]': [
        'indi',
        'action',
        'shuter',
        ],
        'deleted': '0',
        'no_price_range': '0',
        'records': '20',
    }

    response = requests.get('https://steambuy.com/ajax/_get.php', params=params, cookies=cookies, headers=headers)
    a = open('games/1.html','w')
    a.write(response.text)
    a.close()
