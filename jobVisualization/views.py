from django.shortcuts import render
from .utils import error
from .utils import getHomeData
from .utils import getSalaryCharData, getCompanyCharData, getEducationalCharData, \
    getCompanyStatusCharData, getMainData

# Create your views here.
def salary(request):
    educations, workExperiences = getSalaryCharData.getPageData()
    defaultEducation = '不限'
    defaultWorkExperience = '不限'
    if request.GET.get('educational'): defaultEducation = request.GET.get('educational')
    if request.GET.get('workExperience'): defaultWorkExperience = request.GET.get('workExperience')
    salaryList, barData, legends = getSalaryCharData.getBarData(defaultEducation, defaultWorkExperience)
    pieData = getSalaryCharData.pieData()
    louDouData = getSalaryCharData.getLouDouData()
    return render(request, 'salaryChar.html', {
        'educations': educations,
        'workExperiences': workExperiences,
        'defaultEducation': defaultEducation,
        'defaultWorkExperience': defaultWorkExperience,
        'salaryList': salaryList,
        'barData': barData,
        'legends': legends,
        'pieData': pieData,
        'louDouData': louDouData,
    })


def company(request):
    typeList = getCompanyCharData.getPageData()
    type = 'all'
    if request.GET.get('type'): type = request.GET.get('type')
    rowBarData, columnBarData = getCompanyCharData.getCompanyBar(type)
    pieData = getCompanyCharData.getCompanyPie(type)
    companyPeople, lineData = getCompanyCharData.getCompanyPeople(type)
    return render(request, 'companyChar.html', {
        'typeList': typeList,
        'type': type,
        'rowBarData': rowBarData,
        'columnBarData': columnBarData,
        'pieData': pieData,
        'companyPeople': companyPeople,
        'lineData': lineData,
    })


def educational(request):
    defaultEducation = '不限'
    if request.GET.get('educational'): defaultEducation = request.GET.get('educational')
    educations = getEducationalCharData.getPageData()
    workExperiences, charDataColumnOne, charDataColumnTwo, hasEmpty = getEducationalCharData.getExpirenceData(
        defaultEducation)
    barDataRow, barDataColumn = getEducationalCharData.getPeopleData()
    return render(request, 'educationalChar.html', {
        'educations': educations,
        'defaultEducation': defaultEducation,
        'workExperiences': workExperiences,
        'charDataColumnOne': charDataColumnOne,
        'charDataColumnTwo': charDataColumnTwo,
        'hasEmpty': hasEmpty,
        'barDataRow': barDataRow,
        'barDataColumn': barDataColumn,
    })


def companyStatus(request):
    defaultType = '不限'
    if request.GET.get('type'): defaultType = request.GET.get('type')
    typeList = getCompanyStatusCharData.getPageData()
    teachnologyRow, teachnologyColumn = getCompanyStatusCharData.getTechnologyData(defaultType)
    companyStatusData = getCompanyStatusCharData.gerCompanyStatusData()
    return render(request, 'companyStatusChar.html', {
        'typeList': typeList,
        'defaultType': defaultType,
        'teachnologyRow': teachnologyRow,
        'teachnologyColumn': teachnologyColumn,
        'companyStatusData': companyStatusData
    })


def main(request):
    year, mon, date, weekday, hour, min, sec = getMainData.getCurrentTime()
    data = getMainData.getMapData('all')
    dataCounts = getMainData.getDataCounts()
    maxSalary = getMainData.getMaxSalary()
    educationList, educationalSalary, educationPeople, hasEmpty = getMainData.getEducationalSalary()
    companyPeople, lineData = getCompanyCharData.getCompanyPeople('all')
    companyStatusData = getMainData.gerCompanyStatusData()
    return render(request, 'main.html', {
        'dateInfo': {
            'year': year,
            'mon': mon,
            'date': date,
            'weekday': weekday,
            'hour': hour,
            'min': min,
            'sec': sec,
        },
        'mapData': {
            'data': data,
        },
        'dataCount': dataCounts,
        'maxSalary': maxSalary,
        'educationList': educationList,
        'educationalSalary': educationalSalary,
        'educationPeople': educationPeople,
        'hasEmpty': hasEmpty,
        'companyPeople': companyPeople,
        'lineData': lineData,
        'companyStatusData': companyStatusData
    })