import csv
import os
import time
import json

import pandas as pd
import django
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VisualizationJobs.settings')
django.setup()

from jobVisualization.models import JobInfo

jobs = ['前端', '后端', 'Python', 'Java', 'JavaScript', '人工智能', '数据分析师', '全栈', '软件测试', '机器学习', '数据库', '大数据', '云计算',
        '软件', '图像', '自然语言处理', '人工智能', '学习', '前端', '后端', '数据', '算法', '测试', '网络安全', '运维', 'UI', '区块链', '网络', '全栈',
        '硬件', 'Java', 'C++', 'PHP', 'C#', '.NET', 'Hadoop', 'Python', 'Perl', 'Ruby', 'Nodejs', 'Go', 'Javascript',
        'Delphi', 'jsp', 'sql', '软件工程师', '网络工程师', '数据分析师', '系统管理员', 'Java工程师', '前端工程师', 'Python开发',
        '人工智能工程师', '数据库管理员', '项目经理', '算法工程师', '测试工程师', '运维工程师', 'DevOps工程师', '产品经理',
        'UI/UX设计师', '信息安全分析师', '全栈开发', '软件架构师', '数据工程师', '云计算工程师', '人工智能研究员', '嵌入式软件工程师', 'Web工程师',
        '大数据工程师', '区块链工程师', '机器学习工程师', '物联网工程师', '信息技术经理', '网络安全工程师', '游戏开发'
                                                                      '区块链工程师', '网络安全工程师', '物联网工程师', '嵌入式软件工程师', 'vue',
        '游戏开发', '运维', 'Hadoop', 'Nodejs']


def startBrowser():
    service = Service('./chromedriver')
    options = webdriver.ChromeOptions()
    # options.add_experimental_option("excludeSwitches", ['enable-automation'])
    options.add_experimental_option("debuggerAddress", "localhost:9222")
    return webdriver.Chrome(service=service, options=options)


def save_to_csv(rowData):
    with open('temp0.csv', 'a', newline='', encoding='utf-8') as wf:
        writer = csv.writer(wf)
        writer.writerow(rowData)


def clean_data():
    df = pd.read_csv('temp0.csv')
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    df['salaryMonth'] = df['salaryMonth'].map(lambda x: x.replace('薪', ''))
    df['companyTags'] = df['companyTags'].apply(lambda x: x.encode('utf-8').decode('unicode_escape'))
    df['workTags'] = df['workTags'].apply(lambda x: x.encode('utf-8').decode('unicode_escape'))
    print("总数据量为%d" % df.shape[0])
    return df.values


def save_to_mysql():
    data = clean_data()
    for job in data:
        JobInfo.objects.create(
            title=job[0],
            address=job[1],
            type=job[2],
            education=job[3],
            workExperience=job[4],
            workTags=job[5],
            salary=job[6],
            salaryMonth=job[7],
            companyTags=job[8],
            hrWork=job[9],
            hrName=job[10],
            practice=job[11],
            companyTitle=job[12],
            companyAvatar=job[13],
            companyType=job[14],
            companyStatus=job[15],
            companyScale=job[16],
            detailUrl=job[17],
            companyUrl=job[18],
            dist=job[19],
        )


def init():
    if not os.path.exists('temp0.csv'):
        with open('temp0.csv', 'a', encoding='utf-8', newline='') as wf:
            writer = csv.writer(wf)
            writer.writerow([
                'title',  # 岗位名字
                'address',  # 地址
                'type',  # 岗位
                'education',  # 学历
                'workExperience',  # 工作经验
                'workTags',  # 工作标签
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


class crawl(object):
    def __init__(self, type, page):
        self.type = type  # 岗位关键字
        self.page = page  # 页码数
        self.url = "https://www.zhipin.com/web/geek/job?query=%s&city=100010000&page=%s"

    def main(self, page):
        # if self.page > page: return
        browser = startBrowser()
        print("正在爬取路径：" + self.url % (self.type, self.page))
        browser.get(self.url % (self.type, self.page))
        time.sleep(15)
        job_list = browser.find_elements(By.XPATH, '//ul[@class="job-list-box"]/li')
        for index, job in enumerate(job_list):
            try:
                jobData = []
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
                workTags = json.dumps(list(map(lambda x: x.text, workTags)))
                practice = 0
                salaries = job.find_element(By.XPATH,
                                            './/a[@class="job-card-left"]/div[contains(@class, "job-info")]/span['
                                            '@class="salary"]').text
                if salaries.find("K") != -1:
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
                                      salaries.replace("元/天", "").split("-")))
                    salaryMonth = '12薪'
                    practice = 1

                companyTags = job.find_element(By.XPATH,
                                               './div[contains(@class, "job-card-footer")]/div[@class="info-desc"]').text
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
                                                './/div[@class="job-card-right"]/div[@class="company-info"]/h3/a') \
                    .text
                companyAvatar = job.find_element(By.XPATH,
                                                 './/div[@class="job-card-right"]/div[@class="company-logo"]/a/img') \
                    .get_attribute('src')
                companyInfos = job.find_elements(By.XPATH,
                                                 './/div[@class="job-card-right"]/div[@class="company-info"]/ul['
                                                 '@class="company-tag-list"]/li')
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
                        list(map(lambda x: int(x), companyInfos[1].text.replace('人', '').split('-')))
                    else:
                        companyScale = [0, 10000]
                detailUrl = job.find_element(By.XPATH, './/a[@class="job-card-left"]').get_attribute('href')
                companyUrl = job.find_element(By.XPATH,
                                              './/div[@class="job-card-right"]/div[@class="company-info"]/h3/a') \
                    .get_attribute('href')
                jobData.append(title)
                jobData.append(address)
                jobData.append(type)
                jobData.append(education)
                jobData.append(workExperience)
                jobData.append(workTags)
                jobData.append(salary)
                jobData.append(salaryMonth)
                jobData.append(companyTags)
                jobData.append(hrWork)
                jobData.append(hrName)
                jobData.append(practice)
                jobData.append(companyTitle)
                jobData.append(companyAvatar)
                jobData.append(companyType)
                jobData.append(companyStatus)
                jobData.append(companyScale)
                jobData.append(detailUrl)
                jobData.append(companyUrl)
                jobData.append(dist)
                save_to_csv(jobData)
            except:
                pass

        if self.page != 1:
            self.page += 1
            self.main(page)


if __name__ == '__main__':
    for j in jobs:
        print(f"爬取关键字为'{j}'的岗位信息")
        crawlObj = crawl(j, 1)
        init()
        crawlObj.main(30)
    JobInfo.objects.all()
    save_to_mysql()
