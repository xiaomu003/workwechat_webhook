import hashlib
import base64
import requests
import json


def sendBot(url, image_path):
    '''

    :param url:   传入企业微信机器人webhoot
    :param image_path:  本地图片路径
    :return:
    '''
    with open(image_path, "br") as f:
        fcont = f.read()
        # 转化图片的base64
        ls_f = base64.b64encode(fcont)
        # 计算文件的md5
        fmd5 = hashlib.md5(fcont)
    data = {"msgtype": "image", "image": {"base64": ls_f.decode('utf8'), "md5": fmd5.hexdigest()}}
    data_json = json.dumps(data)
    print('推送的json%s' % data_json)
    prequte = requests.post(url, data=data_json)
    return prequte.text


if __name__ == '__main__':
    demo = sendBot('https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxxxxx', "2.png")
    if json.loads(demo)['errcode'] == 0:
        print('调用成功')
    else:
        print('调用失败%s' % demo)
