# coding: utf-8
"""
递归获取对象中的数据 输出一个字典列表
仅适用于输出单一key-value对 对输出复杂的数据结构无效
ps1:
    obj = ['cs', {'data': {'attachments': [{'title': '平安财富-84天成长3号（净值型）人民币理财产品的公告.pdf','url': 'https://bank-static.pingan.com.cn/aum/ifms_pms/01/3/114/DK7LK180007/ea1c6b2b790447b18a1babed47e8d29320200707090741.pdf'}],'totalSize': 14552}}]
    entry_params = {'url':'url','title':'title'}
    custom_tools(obj=obj,entry_params=entry_params)
    输出：
        [
            {'title': '平安财富-28天成长2号（净值型）人民币理财产品的公告.pdf', 'url': 'https://bank-static.pingan.com.cn/aum/ifms_pms/01/3/114/DK1LK180002/27700465c6f94812b37edf423434136920200707090729.pdf'}
        ]
ps2:
    obj = ['','cs1',{'cs2':'','title': '平安财富-28天成长2号（净值型）人民币理财产品的公告.pdf1'},['','',{'title': '平安财富-28天成长2号（净值型）人民币理财产品的公告.pdf','url': 'https://bank-static.pingan.com.cn/aum/ifms_pms/01/3/114/DK1LK180002/27700465c6f94812b37edf423434136920200707090729.pdf'}]]
    entry_params = {'url': '自定义url', 'title': '自定义title'}
    custom_tools(obj=obj,entry_params=entry_params)
    输出：
        [
            {'title': '平安财富-28天成长2号（净值型）人民币理财产品的公告.pdf1'},
            {'title': '平安财富-28天成长2号（净值型）人民币理财产品的公告.pdf', 'url': 'https://bank-static.pingan.com.cn/aum/ifms_pms/01/3/114/DK1LK180002/27700465c6f94812b37edf423434136920200707090729.pdf'}
        ]
ps3:
   obj = {'success': True, 'result': {'total': 12339, 'data': [
    {'supplierId': 10005575632, 'bizRstCode': '', 'status': 'OFFICIAL', 'name': '武陵区蓝华蓝华办公用品店', 'englishName': '',
     'usedName': '', 'abbreviation': '', 'logoPath': '', 'supplierType': '', 'supplierTypeCode': '',
     'auditStatus': 'WAIT_CHANGE_AUDIT', 'registerDate': '2020-04-20 11:48:31', 'enterDate': '2020-04-28 11:00:41',
     'source': '', 'supplierSettleType': '个体工商户', 'hangupStatus': 0}], 'empty': False}, 'error': ''}
    entry_params = {'name': 'name', 'supplierSettleType': 'supplierSettleType','enterDate':'enterDate','bizRstCode':'bizRstCode'}
    custom_tools(obj=obj,entry_params=entry_params)
    输出：
        [
            {
                'bizRstCode': '', 'name': '武陵区蓝华蓝华办公用品店', 'enterDate': '2020-04-28 11:00:41', 'supplierSettleType': '个体工商户'
            }
        ]
"""
import sys

PY_VERSION = sys.version_info[0]
if PY_VERSION == 2:
    str_ = (int, float, str, unicode)
if PY_VERSION == 3:
    str_ = (int, float, str)


def recursion_get(original_datas, meta_datas, output_datas=None, custom_handle_fields=[], callback=None):
    """
    :param original_datas: 传入的源数据->obj
    :param meta_datas: 需要输出的数据字段格式->{'自定义key':'key'}
    :param output_datas: 默认返回数据格式
    :param custom_handle_fields: 需要处理的字段
    :param callback: 回调函数对需要的字段进行自定义处理
    :return: [{}] 字典列表
    """
    global each_data
    each_data = {}
    if output_datas is None:
        output_datas = []
    if isinstance(original_datas, list):
        for v in original_datas:
            if isinstance(v, (dict, list)):
                recursion_get(v, meta_datas, output_datas, custom_handle_fields, callback)
    if isinstance(original_datas, dict):
        for k, v in original_datas.items():
            if isinstance(v, str_) or not v:
                for custom_k, original_k in meta_datas.items():  # 遍历需要输出的字段进行比对存储
                    if set(meta_datas.values()).issubset(set(original_datas.keys())):  # 判断字段是否完全
                        if original_k == k:
                            if all((callback, original_k in custom_handle_fields)):  # 回调函数对需要处理的字段进行处理
                                v = callback(v)
                            each_data.update({custom_k: v})
                            if len(each_data.keys()) == len(meta_datas.keys()):  # 递归分开每一条数据 单独存在
                                output_datas.append(each_data)
                                each_data = {}
                    else:
                        if original_k == k:
                            each_data.update({custom_k: v})
                            output_datas.append(each_data)
                            each_data = {}
            elif isinstance(v, (dict, list)):
                recursion_get(v, meta_datas, output_datas, custom_handle_fields, callback)
    return output_datas

