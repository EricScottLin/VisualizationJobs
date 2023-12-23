import time

from .getPublicData import *


def getCurrentTime():
    timeFormatter = time.localtime()
    year = timeFormatter.tm_year
    mon = timeFormatter.tm_mon
    date = timeFormatter.tm_mday
    weekday = timeFormatter.tm_wday
    hour = timeFormatter.tm_hour
    min = timeFormatter.tm_min
    sec = timeFormatter.tm_sec
    return year, monthList[mon - 1], date, weekList[weekday - 1], hour, min, sec


def getMapData(type):
    if type == 'all':
        jobs = JobInfo.objects.all()
    else:
        jobs = JobInfo.objects.filter(type=type)
    addressData = {}
    for i in jobs:
        if i.address in ['唐山', '秦皇岛', '邯郸', '邢台', '保定', '张家口', '承德', '沧州', '廊坊', '衡水', '石家庄']:
            if addressData.get('河北', -1) == -1:
                addressData['河北'] = 1
            else:
                addressData['河北'] += 1
        elif i.address in ['太原', '大同', '阳泉', '长治', '晋城', '朔州', '忻州', '吕梁', '晋中', '临汾', '运城']:
            if addressData.get('山西', -1) == -1:
                addressData['山西'] = 1
            else:
                addressData['山西'] += 1
        elif i.address in ['呼和浩特', '包头', '乌海', '赤峰', '呼伦贝尔', '兴安盟', '通辽', '锡林郭勒盟', '乌兰察布盟', '伊克昭盟（鄂尔多斯旧称）', '巴彦淖尔盟',
                           '阿拉善盟']:
            if addressData.get('内蒙古', -1) == -1:
                addressData['内蒙古'] = 1
            else:
                addressData['内蒙古'] += 1
        elif i.address in ['沈阳', '大连', '鞍山', '抚顺', '本溪', '丹东', '锦州', '营口', '阜新', '辽阳', '盘锦', '铁岭', '朝阳', '葫芦岛']:
            if addressData.get('辽宁', -1) == -1:
                addressData['辽宁'] = 1
            else:
                addressData['辽宁'] += 1
        elif i.address in ['长春', '吉林', '四平', '辽源', '通化', '白山', '松原', '白城', '延边朝鲜族自治州']:
            if addressData.get('吉林', -1) == -1:
                addressData['吉林'] = 1
            else:
                addressData['吉林'] += 1
        elif i.address in ['哈尔滨', '齐齐哈尔', '鸡西', '鹤岗', '双鸭山', '大庆', '伊春', '七台河', '牡丹江', '黑河', '绥化', '大兴安岭']:
            if addressData.get('黑龙江', -1) == -1:
                addressData['黑龙江'] = 1
            else:
                addressData['黑龙江'] += 1
        elif i.address in ['南京', '无锡', '徐州', '常州', '苏州', '南通', '连云港', '淮安(原淮阴）', '盐城', '扬州', '镇江', '泰州', '宿迁']:
            if addressData.get('江苏', -1) == -1:
                addressData['江苏'] = 1
            else:
                addressData['江苏'] += 1
        elif i.address in ['杭州', '宁波', '温州', '嘉兴', '湖州', '绍兴', '金华', '衢州', '舟山', '台州', '丽水']:
            if addressData.get('浙江', -1) == -1:
                addressData['浙江'] = 1
            else:
                addressData['浙江'] += 1
        elif i.address in ['合肥', '芜湖', '蚌埠', '淮南', '马鞍山', '淮北', '铜陵', '安庆', '黄山', '滁州', '阜阳', '宿州', '六安', '宣城', '巢湖',
                           '池州']:
            if addressData.get('安徽', -1) == -1:
                addressData['安徽'] = 1
            else:
                addressData['安徽'] += 1
        elif i.address in ['福州', '厦门', '宁德', '莆田', '泉州', '漳州', '龙岩', '三明', '南平']:
            if addressData.get('福建', -1) == -1:
                addressData['福建'] = 1
            else:
                addressData['福建'] += 1
        elif i.address in ['南昌', '景德镇', '萍乡', '九江', '新余', '鹰潭', '赣州', '宜春', '上饶', '吉安', '抚州']:
            if addressData.get('江西', -1) == -1:
                addressData['江西'] = 1
            else:
                addressData['江西'] += 1
        elif i.address in ['济南', '青岛', '淄博', '枣庄', '东营', '烟台', '潍坊', '济宁', '泰安', '威海', '日照', '莱芜', '临沂', '德州', '聊城',
                           '滨州', '菏泽']:
            if addressData.get('山东', -1) == -1:
                addressData['山东'] = 1
            else:
                addressData['山东'] += 1
        elif i.address in ['郑州', '开封', '洛阳', '平顶山', '安阳', '鹤壁', '新乡', '焦作', '濮阳', '许昌', '漯河', '三门峡', '南阳', '商丘', '信阳',
                           '周口', '驻马店']:
            if addressData.get('河南', -1) == -1:
                addressData['河南'] = 1
            else:
                addressData['河南'] += 1
        elif i.address in ['武汉', '黄石', '十堰', '宜昌', '襄樊', '襄阳', '鄂州', '荆门', '孝感', '荆州', '黄冈', '咸宁', '随州', '恩施土家族苗族自治州']:
            if addressData.get('湖北', -1) == -1:
                addressData['湖北'] = 1
            else:
                addressData['湖北'] += 1
        elif i.address in ['长沙', '株洲', '湘潭', '衡阳', '邵阳', '岳阳', '常德', '张家界', '益阳', '郴州', '永州', '怀化', '娄底', '湘西土家族苗族自治州']:
            if addressData.get('湖南', -1) == -1:
                addressData['湖南'] = 1
            else:
                addressData['湖南'] += 1
        elif i.address in ['广州', '韶关', '深圳', '珠海', '汕头', '佛山', '江门', '湛江', '茂名', '肇庆', '惠州', '梅州', '汕尾', '河源', '阳江',
                           '清远', '东莞', '中山', '潮州', '揭阳', '云浮']:
            if addressData.get('广东', -1) == -1:
                addressData['广东'] = 1
            else:
                addressData['广东'] += 1
        elif i.address in ['南宁', '柳州', '桂林', '梧州', '北海', '防城港', '钦州', '贵港', '玉林', '崇左', '来宾', '贺州', '百色', '河池']:
            if addressData.get('广西', -1) == -1:
                addressData['广西'] = 1
            else:
                addressData['广西'] += 1
        elif i.address in ['海口', '三亚']:
            if addressData.get('海南', -1) == -1:
                addressData['海南'] = 1
            else:
                addressData['海南'] += 1
        elif i.address in ['成都', '自贡', '攀枝花', '泸州', '德阳', '绵阳', '广元', '遂宁', '内江', '乐山', '南充', '宜宾', '广安', '达川', '雅安',
                           '阿坝藏族羌族自治州', '甘孜藏族自治州', '凉山彝族自治州', '巴中', '眉山', '资阳', ]:
            if addressData.get('四川', -1) == -1:
                addressData['四川'] = 1
            else:
                addressData['四川'] += 1
        elif i.address in ['贵阳', '六盘水', '遵义', '铜仁', '黔西南布依族苗族自治州', '毕节', '安顺', '黔东南苗族侗族自治州', '黔南布依族苗族自治州']:
            if addressData.get('贵州', -1) == -1:
                addressData['贵州'] = 1
            else:
                addressData['贵州'] += 1
        elif i.address in ['昆明', '曲靖', '玉溪', '昭通', '楚雄彝族自治州', '红河哈尼族彝族自治州', '文山壮族苗族自治州', '思茅', '西双版纳傣族自治州', '大理白族自治州',
                           '保山', '德宏傣族景颇族自治州', '丽江', '怒江傈僳族自治州', '迪庆藏族自治州', '临沧']:
            if addressData.get('云南', -1) == -1:
                addressData['云南'] = 1
            else:
                addressData['云南'] += 1
        elif i.address in ['拉萨', '昌都', '山南', '日喀则', '那曲', '阿里', '林芝']:
            if addressData.get('西藏', -1) == -1:
                addressData['西藏'] = 1
            else:
                addressData['西藏'] += 1
        elif i.address in ['兰州','嘉峪关','金昌','白银','天水','酒泉','张掖','武威','定西','陇南','平凉','庆阳','临夏回族自治州','甘南藏族自治州']:
            if addressData.get('甘肃', -1) == -1:
                addressData['甘肃'] = 1
            else:
                addressData['甘肃'] += 1
        elif i.address in ['西宁','海东','海北藏族自治州','黄南藏族自治州','海南藏族自治州','果洛藏族自治州','玉树藏族自治州','海西蒙古族藏族自治州']:
            if addressData.get('青海', -1) == -1:
                addressData['青海'] = 1
            else:
                addressData['青海'] += 1
        elif i.address in ['银川','石嘴山','吴忠','固原','中卫']:
            if addressData.get('宁夏', -1) == -1:
                addressData['宁夏'] = 1
            else:
                addressData['宁夏'] += 1
        elif i.address in ['乌鲁木齐','克拉玛依','吐鲁番','哈密','昌吉回族自治州','博尔塔拉蒙古自治州','巴音郭楞蒙古自治州','阿克苏','克孜勒苏柯尔克孜自治州','喀什','和田','伊犁哈萨克自治州','塔城','阿勒泰']:
            if addressData.get('新疆', -1) == -1:
                addressData['新疆'] = 1
            else:
                addressData['新疆'] += 1
        elif i.address in ['西安','铜川','宝鸡','咸阳','渭南','延安','汉中','安康','商洛','榆林']:
            if addressData.get('陕西', -1) == -1:
                addressData['陕西'] = 1
            else:
                addressData['陕西'] += 1
        else:
            if addressData.get(i.address, -1) == -1:
                addressData[i.address] = 1
            else:
                addressData[i.address] += 1

    result = []
    for k, v in addressData.items():
        result.append({
            'name': k,
            'value': v
        })
    return result

