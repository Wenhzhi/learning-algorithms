import requests
import re

def get_vip_music():
    # song_id = '526464293'  # 要下载歌曲的ID
    song_id = '19292998'
    file_path = "save_data/"  # 保存音乐的文件路径,最后加斜杠
    url = "https://link.hhtjim.com/163/"#外链生成地址
    play_url = "https://music.163.com/song?id=" + song_id
    mp3_url = url + song_id + ".mp3"

    print("play_url: ", play_url)
    print("mp3_url: ", mp3_url)

    # 获取歌曲16进制编码
    song = requests.get(mp3_url).content
    # 获取歌曲名称

    song_html = requests.get(play_url).text
    # 保存 网页的内容
    # with open("song.html", "w", encoding='utf-8') as fs:
    #     fs.write(song_html)

    song_name = re.findall('<em class="f-ff2">.*</em>', song_html)[0].lstrip('<em class="f-ff2">').rstrip('</em>')
    print("song_name: ", song_name)
    # 保存文件
    with open(file_path + song_name.strip() + '.mp3', 'wb') as f:
        f.write(song)
        print(mp3_url + ' 歌名：' + song_name)

def get_song_id(song_name):
    """
    回头想办法拿到song_id,就可下载VIP音乐了
    """
    url = f"https://music.163.com/#/search/m/?s={song_name}&type=1"
    pass
    
if __name__ == '__main__':
     get_vip_music()
