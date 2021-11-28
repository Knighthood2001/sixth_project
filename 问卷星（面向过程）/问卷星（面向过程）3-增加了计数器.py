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
count = 0
def sum():
    global count
    count += 1
    w = print("第{}次运行".format(count))
    return w

def run():
    # 电竞问卷
    url = 'https://www.wjx.cn/vm/wrKZIRP.aspx'
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
    while i <= 20:
        base_xpath1 = '//*[@id="div{}"]'.format(i)
        base_xpath2 = base_xpath1 + '/div[2]/div'
        a = driver.find_elements_by_xpath(base_xpath2)
        # print(len(a))
        # 在选项个数范围内，随机生成一个数字 如有四个选项，随机生成数字3
        b = random.randint(1, len(a))
        # print(b)
        # 通过随机数字，点击该数字的选项
        time.sleep(0.1)


        if i == 7 or i == 11 or i == 12 or i == 14:
            q = int_random(1, len(a), b)
            q.sort()
            # print(q)
            for r in q:
                driver.find_element_by_css_selector('#div{} > div.ui-controlgroup > div:nth-child({})'.format(i, r)).click()
                time.sleep(0.1)
        # elif (i == 8 and b == 6) or (i == 9 and b == 5):
        #     driver.find_element_by_css_selector('#div{} > div.ui-controlgroup > div:nth-child({})'.format(i, b)).click()
        # elif (i == 8 and b != 6) or (i == 9 and b != 5):
        #     q = int_random(1, b-1, b)
        #     q.sort()
        #     for r in q:
        #         driver.find_element_by_css_selector('#div{} > div.ui-controlgroup > div:nth-child({})'.format(i, r)).click()
        #         time.sleep(0.5)
        elif (i == 8 and b == 6):
            driver.find_element_by_css_selector('#div{} > div.ui-controlgroup > div:nth-child({})'.format(i, b)).click()
        elif (i == 8 and b != 6):
            q = int_random(1, 5, b)
            q.sort()
            for r in q:
                driver.find_element_by_css_selector('#div{} > div.ui-controlgroup > div:nth-child({})'.format(i, r)).click()
                time.sleep(0.1)
        elif (i == 9 and b == 5):
            driver.find_element_by_css_selector('#div{} > div.ui-controlgroup > div:nth-child({})'.format(i, b)).click()
        elif (i == 9 and b != 5):
            q = int_random(1, 4, b)
            q.sort()
            for r in q:
                driver.find_element_by_css_selector('#div{} > div.ui-controlgroup > div:nth-child({})'.format(i, r)).click()
                time.sleep(0.1)
        else:
            driver.find_element_by_css_selector('#div{} > div.ui-controlgroup > div:nth-child({})'.format(i, b)).click()
        # 判断i答案1跳到第8题，答案2跳到第9题，答案3跳到第7题，如果i不是第六题则
        if i == 6 and b == 1:
            i = 8
        elif i == 6 and b == 2:
            i = 9
        elif i == 6 and b == 3:
            i = 7
        elif i == 10 and b == 2:
            i = 15
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
    time.sleep(0.5)
    # 刷新页面（可能不需要）
    driver.refresh()
    # 关闭当前页面，如果只有一个页面，则也关闭浏览器
    driver.close()
    # 计数器
    sum()

schedule.every(2).seconds.do(run)

while True:
    schedule.run_pending()




