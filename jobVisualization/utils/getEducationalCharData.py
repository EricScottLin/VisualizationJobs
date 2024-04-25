import json

from jobVisualization.models import JobInfo
from .getPublicData import *


def getPageData():
    return list(educations.keys())


def getAverged(list):
    result = 0
    for i in list:
        result += i
    return round(result / len(list), 2)


def getExpirenceData(educational):
    hasEmpty = False
    if educational == '不限':
        jobs = JobInfo.objects.all()
    else:
        jobs = JobInfo.objects.filter(educational=educational)
    workExperiences = {}
    workPeople = {}
    for i in workExperience:
        workExperiences[i] = []
        workPeople[i] = 0
    for job in jobs:
        for k, v in workExperiences.items():
            if job.workExperience == k:
                if job.pratice == 0:
                    workExperiences[k].append(json.loads(job.salary)[1])
                    workPeople[k] += 1
    for k, v in workExperiences.items():
        try:
            workExperiences[k] = getAverged(v)
        except:
            workExperiences[k] = 0

    if len(jobs) == 0:
        hasEmpty = True

    return workExperience, list(workExperiences.values()), list(workPeople.values()), hasEmpty


def getPeopleData():
    jobs = getAllJobs()
    educationData = {}
    for i in jobs:
        if educationData.get(i.educational, -1) == -1:
            educationData[i.educational] = 1
        else:
            educationData[i.educational] += 1
    return list(educationData.keys()), list(educationData.values())

