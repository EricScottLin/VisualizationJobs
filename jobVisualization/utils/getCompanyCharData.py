import io
import json

from .getPublicData import *
from jobVisualization.models import JobInfo

def getPageData():
    jobs = getAllJobs()
    typeData = []
    for i in jobs:typeData.append(i.type)
    return list(set(typeData))

def getCompanyBar(type):
    if type == 'all':
        jobs = JobInfo.objects.all()
    else:
        jobs = JobInfo.objects.filter(type=type)
    natureData = {}
    for i in jobs:
        if natureData.get(i.companyType,-1) == -1:
            natureData[i.companyType] = 1
        else:
            natureData[i.companyType] += 1
    natureList = list(sorted(natureData.items(), key=lambda x:x[1], reverse=True))
    rowData = []
    columnData = []
    for k,v in natureList:
        rowData.append(k)
        columnData.append(v)
    return rowData[:20], columnData[:20]

def getCompanyPie(type):
    if type == 'all':
        jobs = JobInfo.objects.all()
    else:
        jobs = JobInfo.objects.filter(type=type)
    addressData = {}
    for i in jobs:
        if addressData.get(i.address,-1) == -1:
            addressData[i.address] = 1
        else:
            addressData[i.address] += 1
    result = []
    for k,v in addressData.items():
        result.append({
            'name': k,
            'value': v
        })
    return result[:30]

def getCompanyPeople(type):
    if type == 'all':
        jobs = JobInfo.objects.all()
    else:
        jobs = JobInfo.objects.filter(type=type)

    def map_fn(item):
        item.companyScale = json.loads(item.companyScale)[1]
        return item

    jobs = list(map(map_fn, jobs))
    data = [0 for x in range(6)]

    for i in jobs:
        p = i.companyScale
        if p <= 20:
            data[0] += 1
        elif p <= 100:
            data[1] += 1
        elif p <= 500:
            data[2] += 1
        elif p <= 1000:
            data[3] += 1
        elif p < 10000:
            data[4] += 1
        else:
            data[5] += 1
    return companyPeople, data








