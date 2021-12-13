import requests
import urllib.request as urlrequest
from lxml import etree
import pandas as pd
import matplotlib.pyplot as plt

def example():
    """
    报错的,沿着它这个改一下
    :return:
    """
    # 获取html
    url = r'https://www.tiobe.com/tiobe-index/'
    page = urlrequest.urlopen(url).read()
    # 创建lxml对象
    html = etree.HTML(page)
    # 解析HTML，筛选数据
    df = html.xpath('//table[contains(@class, "table-top20")]/tbody/tr//text()')
    # 数据写入数据库
    tmp = []
    for i in range(0, len(df), 5):
        tmp.append(df[i: i+5])
    df = pd.DataFrame(tmp)
    # 查看数据
    df.head(2)

    # 数据处理
    df.columns = ['Aug 2019', 'Aug 2018', 'Name', 'Rating', 'Change']
    # 处理最后两列数据
    df['Rating'] = [float(istr.replace('%', '')) for istr in df['Rating']]
    df['Change'] = [float(istr.replace('%', '')) for istr in df['Change']]
    # 再次查看数据
    df.head()

    # 绘制图像
    plt.pie(df['Rating'], labels=df['Name'])
    plt.show()

def get_index():
    url = "https://www.tiobe.com/tiobe-index/"
    page = requests.get(url)
    # print("page: ", page.text)
    # page = urlrequest.urlopen(url).read()
    html = etree.HTML(page.text)
    df = html.xpath('//table[contains(@class, "table-top20")]/tbody/tr//text()')

    return df

def filter_data(df):
    tmp = []
    for i in range(0, len(df), 5):
        tmp.append(df[i:i+5])
    df = pd.DataFrame(tmp)
    # 查看数据
    df.head(2)
    # 数据处理
    df.columns = ['Dec 2021', 'Dec 2020', 'Name', 'Rating', 'Change']

    # 处理最后两列数据
    df['Rating'] = [float(istr.replace('%', '')) for istr in df['Rating']]
    df['Change'] = [float(istr.replace('%', '')) for istr in df['Change']]

    # 再次查看数据
    df.head()
    print(df)
    print(df["Rating"])
    print(type(df["Rating"]))
    print(df["Name"])
    print(type(df["Name"]))
    return df

def draw_image(df):
    plt.pie(df["Rating"], labels=df["Name"])
    # 保存图表，plt.savefig( )
    plt.savefig("饼图01.png")
    plt.show()

def main():
    df = get_index()
    # 返回值df再赋值，要不报错
    # TypeError: list indices must be integers or slices, not str
    df = filter_data(df)
    draw_image(df)


if __name__ == '__main__':
    main()
