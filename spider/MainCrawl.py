import csv
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import json


class crawl(object):
    def __init__(self, type, page):
        self.type = type  # 岗位关键字
        self.page = page  # 页码数
        self.url = "https://www.zhipin.com/web/geek/job?query=%s&city=100010000&page=%s"

    def startBroswer(self):
        service = Service('./chromedriver')
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ['enable-automation'])
        return webdriver.Chrome(service=service, options=options)

    def init(self):
        if not os.path.exists('./temp.csv'):
            with open('./temp.csv', 'a', encoding='utf-8', newline='') as wf:
                writer = csv.writer(wf)
                writer.writerow([
                    'title',  # 岗位名字
                    'address',  # 地址
                    'type',  # 岗位
                    'education',  # 学历
                    'workExperience',  # 工作经验
                    'workTag',  # 工作标签
                    'salary',  # 薪资
                    'salaryMonth',  # 年底多薪
                    'companyTags',  # 公司福利
                    'hrWork',  # HR职位
                    'hrName',  # HR姓名
                    'practice',  # 实习生
                    'companyTitle',  # 公司名字
                    'companyAvatar',  # 公司头像
                    'companyType',  # 公司性质
                    'companyStatus',  # 公司状态
                    'companyScale',  # 规模
                    'detailUrl',  # 岗位详情页
                    'companyUrl',  # 公司详情页
                    'dist',  # 行政区
                ])

    def main(self, page):
        # if self.page > page: return
        browser = self.startBroswer()
        print("正在爬取路径：" + self.url % (self.type, self.page))
        browser.get(self.url % (self.type, self.page))
        time.sleep(30)
        job_list = browser.find_elements(By.XPATH, '//ul[@class="job-list-box"]/li')
        for index, job in enumerate(job_list):
            print("正在爬取第%d条数据" % (index + 1))
            title = job.find_element(By.XPATH,
                                     './/a[@class="job-card-left"]/div[contains(@class, "job-title")]/span['
                                     '@class="job-name"]').text
            addresses = job.find_element(By.XPATH,
                                         './/a[@class="job-card-left"]/div[contains(@class, "job-title")]/span['
                                         '@class="job-area-wrapper"]/span').text.split(
                '·')
            address = addresses[0]
            if len(addresses) != 1:
                dist = addresses[1]
            else:
                dist = ''
            type = self.type
            tag_list = job.find_elements(By.XPATH,
                                         './/a[@class="job-card-left"]/div[contains(@class, "job-info")]/ul['
                                         '@class="tag-list"]/li')
            if len(tag_list) == 2:
                education = tag_list[1].text
                workExperience = tag_list[0].text
            else:
                education = tag_list[2].text
                workExperience = tag_list[1].text
            workTags = job.find_elements(By.XPATH,
                                         './div[contains(@class, "job-card-footer")]/ul[@class="tag-list"]/li')
            wordTags = json.dumps(list(map(lambda x: x.text, workTags)))
            practice = 0
            salaries = job.find_element(By.XPATH,
                                        './/a[@class="job-card-left"]/div[contains(@class, "job-info")]/span['
                                        '@class="salary"]').text
            if salaries.find("K"):
                salaries = salaries.split("·")
                if len(salaries) == 1:
                    salary = list(map(lambda x:
                                      int(x) * 1000,
                                      salaries[0].replace("K", "").split("-")))
                    salaryMonth = '12薪'
                else:
                    salary = list(map(lambda x:
                                      int(x) * 1000,
                                      salaries[0].replace("K", "").split("-")))
                    salaryMonth = salaries[1]
            else:
                salary = list(map(lambda x:
                                  int(x),
                                  salaries[0].replace("元/天", "").split("-")))
                salaryMonth = '12薪'
                practice = 1

            companyTags = job.find_elements(By.XPATH,
                                            './div[contains(@class, "job-card-footer")]/div[@class, "info-desc"]').text
            if not companyTags:
                companyTags = '无'
            else:
                companyTags = json.dumps(companyTags.split('，'))
            hrWork = job.find_element(By.XPATH,
                                      './/a[@class="job-card-left"]/div[contains(@class, "job-info")]/div['
                                      '@class="info-public"]').text
            hrName = job.find_element(By.XPATH,
                                      './/a[@class="job-card-left"]/div[contains(@class, "job-info")]/div['
                                      '@class="info-public"]/em').text

            companyTitle = job.find_element(By.XPATH,
                                            './/a[@class="job-card-right"]/div[@class, "company-info"]/h3/a').text
            companyAvatar = job.find_element(By.XPATH,
                                             './/a[@class="job-card-right"]/div[@class, "company-logo"]/a/img').get_attribute(
                'src')
            companyInfos = job.find_element(By.XPATH,
                                            './/a[@class="job-card-right"]/div[@class, "company-info"]/ul[@class, '
                                            '"company-tag-list"]/li')
            if len(companyInfos) == 3:
                companyType = companyInfos[0].text
                companyStatus = companyInfos[1].text
                companyScale = companyInfos[2].text
                if companyScale != '10000人以上':
                    list(map(lambda x: int(x), companyInfos[2].text.replace('人', '').split('-')))
                else:
                    companyScale = [0, 10000]
            else:
                companyType = companyInfos[0].text
                companyStatus = '未融资'
                companyScale = companyInfos[1].text
                if companyScale != '10000人以上':
                    list(map(lambda x: int(x), companyInfos[2].text.replace('人', '').split('-')))
                else:
                    companyScale = [0, 10000]
            detailUrl = job.find_element(By.XPATH, './/a[@class="job-card-left"]').get_attribute('href')
            companyUrl = job.find_element(By.XPATH,
                                            './/a[@class="job-card-right"]/div[@class, "company-info"]/h3/a').get_attribute('href')
            print(title, address, dist, type, education, workExperience, hrWork, hrName)
            print(wordTags, practice, salary, salaryMonth)
            print(companyTags, companyTitle, companyAvatar, companyType, companyStatus, companyScale)
            print(detailUrl, companyUrl)

            break

        # self.page += 1


if __name__ == '__main__':
    crawlObj = crawl('Web前端', 1)
    crawlObj.init()
    crawlObj.main(10)
