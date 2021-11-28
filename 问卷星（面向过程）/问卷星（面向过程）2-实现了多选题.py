# -*- coding: utf-8-*-

import random
from selenium import webdriver
import time
import schedule as schedule
# 多选题的多个选项
def int_random(m, n, o):
    p = []
    while len(p) < o:
        new_int = random.randint(m, n)
        if (new_int not in p):
            p.append(new_int)
        else:
            pass
    return p
def run():
    url = 'https://www.wjx.cn/vm/YD3Xwc3.aspx'
    # 躲避智能检测
    option = webdriver.ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=option)
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
    })
    driver.get(url)
    # 总共有13个题目
    i = 1
    while i <= 13:
        base_xpath1 = '//*[@id="div{}"]'.format(i)
        base_xpath2 = base_xpath1 + '/div[2]/div'
        a = driver.find_elements_by_xpath(base_xpath2)
        # print(len(a))
        # 在选项个数范围内，随机生成一个数字 如有四个选项，随机生成数字3
        b = random.randint(1, len(a))
        # print(b)
        # 通过随机数字，点击该数字的选项
        # time.sleep(1)
        # 当第六个问题回答第四个选项（其他）时，需要填写
        if i == 6 and b == 4:
            driver.find_element_by_css_selector('#div{} > div.ui-controlgroup > div:nth-child({})'.format(i, b)).click()
            # time.sleep(1)
            # 这里你可以每隔一段时间更改send_keys中的内容，也可以将答案写出来，然后随机选择哪个选项
            driver.find_element_by_css_selector('#tqq6_4').send_keys('QQ群和微信群')
        elif i == 5 or i == 7 or i == 8 or i == 11:
            q = int_random(1, len(a), b)
            # sort函数表示将列表排序，如果未加参数表示从小到大排列
            q.sort()
            for r in q:
                driver.find_element_by_css_selector('#div{} > div.ui-controlgroup > div:nth-child({})'.format(i, r)).click()
                time.sleep(0.5)
        else:
            driver.find_element_by_css_selector('#div{} > div.ui-controlgroup > div:nth-child({})'.format(i, b)).click()

        # 当第三个问题答案是是时，跳到5
        if i == 3 and b == 1:
            i = 5
        else:
            i += 1
    # 点击提交按钮
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="ctlNext"]').click()
    # 出现点击验证码验证
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="alert_box"]/div[2]/div[2]/button').click()
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="rectMask"]').click()
    time.sleep(4)
    # 关闭页面
    handles = driver.window_handles
    driver.switch_to.window(handles[0])
    time.sleep(1)
    # 刷新页面（可能不需要）
    driver.refresh()
    # 关闭当前页面，如果只有一个页面，则也关闭浏览器
    driver.close()
schedule.every(2).seconds.do(run)

while True:
    schedule.run_pending()







