from django.db import models


# Create your models here.
class JobInfo(models.Model):
    id = models.AutoField("id", primary_key=True)
    title = models.CharField('岗位名字', max_length=255, default='')
    address = models.CharField('省份', max_length=255, default='')
    type = models.CharField('职位', max_length=255, default='')
    education = models.CharField('学历', max_length=255, default='')
    workExperience = models.CharField('工作经验', max_length=255, default='')
    workTags = models.CharField('工作标签', max_length=255, default='')
    salary = models.CharField('薪资', max_length=255, default='')
    salaryMonth = models.CharField('年终奖', max_length=255, default='')
    companyTags = models.CharField('公司福利', max_length=499, default='')
    hrWork = models.CharField('人事职位ְλ', max_length=255, default='')
    hrName = models.CharField('人事名字', max_length=255, default='')
    practice = models.BooleanField('是否为实习单位', max_length=255, default='')
    companyTitle = models.CharField('公司名称', max_length=255, default='')
    companyAvatar = models.CharField('公司头像', max_length=499, default='')
    companyType = models.CharField('公司性质', max_length=255, default='')
    companyStatus = models.CharField('公司状态', max_length=255, default='')
    companyScale = models.CharField('公司人数', max_length=255, default='')
    detailUrl = models.CharField('详情地址', max_length=499, default='')
    companyUrl = models.CharField('公司详情地址', max_length=499, default='')
    createTime = models.DateField('创建时间',auto_now_add=True)
    dist = models.CharField('行政区', max_length=255, default='')

    class Meta:
        db_table = 'jobInfo'

