from matplotlib import pylab as plt
from wordcloud import WordCloud
from PIL import Image
from pymysql import connect

import numpy as np
import json
import jieba


def get_img(field, targetImageSrc, resImageSrc):
    # 连接数据库
    con = connect(host="localhost", user="root", password="20021117", database="jobinfo", port=3306, charset="utf8mb4")
    cursor = con.cursor()
    # 从表里取出指定的字段
    sql = f"SELECT {field} FROM jobinfo"
    cursor.execute(sql)
    data = cursor.fetchall()
    # 将所有字符连在一起
    text = ''
    # 如果是companyTags要进一步分词
    if field == 'companyTags':
        for i in data:
            if i[0] != 'æ\x97\xa0':  # 数据为无
                tagsArr = json.loads(i[0])[0].split('，')
                for j in tagsArr:
                    text += j
    else:
        for i in data:
            text += i[0]
    # 关闭数据库连接
    cursor.close()
    con.close()
    # 分词
    data_cut = jieba.cut(text, cut_all=False)
    stop_words = []
    with open('./stopwords.txt', 'r', encoding='utf-8') as rf:
        for line in rf:
            if len(line) > 0:
                stop_words.append(line.strip())
    data_result = [x for x in data_cut if x not in stop_words]
    string = ' '.join(data_result)

    # 词云图配
    img = Image.open(targetImageSrc)
    img_arr = np.array(img)
    wc = WordCloud(
        background_color='#100c2a',
        mask=img_arr,
        font_path='/System/Library/Fonts/PingFang.ttc',
    )
    wc.generate_from_text(string)

    # 绘制图片
    plt.figure(1)
    plt.imshow(wc)
    plt.axis('off')
    plt.savefig(resImageSrc, dpi=600)


# get_img('title', '../static/jobs.png', '../static/title_wordcloud.png')
# get_img('address', '../static/map.png', '../static/address_wordcloud.png')
# get_img('education', '../static/edu.jpg', '../static/education_wordcloud.png')
# get_img('workTags', '../static/tech.png', '../static/workTags_wordcloud.png')
get_img('companyTags', '../static/welfare.png', '../static/companyTags_wordcloud.png')
