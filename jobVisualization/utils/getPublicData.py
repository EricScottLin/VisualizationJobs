from jobVisualization.models import *

monthList = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
weekList = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]


def getAllJobs():
    return JobInfo.objects.all()