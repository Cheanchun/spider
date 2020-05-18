# -*- coding=utf-8 -*-
"""
@Auth:CheanCC
@Date:2020
@Desc:
@Todo
"""
import requests

"""
中信银行：
	url:https://wap.bank.ecitic.com:6443/NMBFOServer/MBIFFinancial.do?act=PEMBFIPL
	{"pkgFlag":"0","errMsg":"","dataPackage":{"business":"6t4SU4tfqHvEqk3UCezFcRyCEtteysHNOL22oQCTRjWEbm9BrfI16rlKn+BqGxuJtgrjnD9jU5YMhVY15OttUdj4HwhYf3+riCxvj7+VgjT5LxJvqZMIaMqwqwojU0XSMFxaKhBI64rZQnP1+f6ZOvUvyICY+zFmtEpEKrVP6wrtX1969anRs0VXyKXb94ih8sB/l6lECPgJA5he36ViJJKCbxM0qHtum6Ha/WBM4smyd0rTIrRmZpX/P1ZrhOsnFFebIkijIlU=","cryptFlag":"1","encryptFlag":"1","hashFlag":"0","signatureFlag":"0"},"errCode":"0"}
	{"pkgFlag":"0","errMsg":"","dataPackage":{"business":"6t4SU4tfqHtVY1FD4FzvB2zzrA4U/jTbhxFCTMFGgXArnJhu0dHSuw20A52Yc1BWHGm8/Uc8gRjpeXHHkZjCeEw64UAPe6u7LJh6d8GpfV+BxfMutjUs1fmAyoHySTp3l8sDxr/flKl+zPe7FbMxkfUvyICY+zFmE8uC1y/8QWOHYZ1y52whzW9sR0DL5/fThubFsylH0yOblpy+GJIFarK8mhsZaTPcDIVWNeTrbVFQvr0QmYRvGR+HXWf29oQcGUtMgakY2mqu4ZCnTjsmyAlyvkflo2m1Ry7PexJUznI=","cryptFlag":"1","encryptFlag":"1","hashFlag":"0","signatureFlag":"0"},"errCode":"0"}
	{"pkgFlag":"0","errMsg":"","dataPackage":{"business":"6t4SU4tfqHtVY1FD4FzvB2zzrA4U/jTbhxFCTMFGgXArnJhu0dHSuw20A52Yc1BWHGm8/Uc8gRjpeXHHkZjCeEw64UAPe6u7LJh6d8GpfV+BxfMutjUs1fmAyoHySTp31f3CPEyaEmd+zPe7FbMxkfUvyICY+zFmE8uC1y/8QWOHYZ1y52whzW9sR0DL5/fThubFsylH0yOblpy+GJIFarK8mhsZaTPcDIVWNeTrbVFQvr0QmYRvGR+HXWf29oQcGUtMgakY2mqu4ZCnTjsmyAlyvkflo2m1Ry7PexJUznI=","cryptFlag":"1","encryptFlag":"1","hashFlag":"0","signatureFlag":"0"},"errCode":"0"}
	{"pkgFlag":"0","errMsg":"","dataPackage":{"business":"6t4SU4tfqHtVY1FD4FzvB2zzrA4U/jTbhxFCTMFGgXArnJhu0dHSuw20A52Yc1BWHGm8/Uc8gRjpeXHHkZjCeEw64UAPe6u7LJh6d8GpfV+BxfMutjUs1fmAyoHySTp3dSUe0lzl/2l+zPe7FbMxkfUvyICY+zFmE8uC1y/8QWOHYZ1y52whzW9sR0DL5/fThubFsylH0yOblpy+GJIFarK8mhsZaTPcDIVWNeTrbVFQvr0QmYRvGR+HXWf29oQcGUtMgakY2mqu4ZCnTjsmyAlyvkflo2m1Ry7PexJUznI=","cryptFlag":"1","encryptFlag":"1","hashFlag":"0","signatureFlag":"0"},"errCode":"0"}
	{"pkgFlag":"0","errMsg":"","dataPackage":{"business":"6t4SU4tfqHtVY1FD4FzvB2zzrA4U/jTbhxFCTMFGgXArnJhu0dHSuw20A52Yc1BWHGm8/Uc8gRjpeXHHkZjCeEw64UAPe6u7LJh6d8GpfV+BxfMutjUs1fmAyoHySTp3UouBy1FtqV9+zPe7FbMxkfUvyICY+zFmE8uC1y/8QWOHYZ1y52whzW9sR0DL5/fThubFsylH0yOblpy+GJIFarK8mhsZaTPcDIVWNeTrbVFQvr0QmYRvGR+HXWf29oQcGUtMgakY2mqu4ZCnTjsmyAlyvkflo2m1Ry7PexJUznI=","cryptFlag":"1","encryptFlag":"1","hashFlag":"0","signatureFlag":"0"},"errCode":"0"}
	{"pkgFlag":"0","errMsg":"","dataPackage":{"business":"6t4SU4tfqHtVY1FD4FzvB2zzrA4U/jTbhxFCTMFGgXArnJhu0dHSuw20A52Yc1BWHGm8/Uc8gRjpeXHHkZjCeEw64UAPe6u7LJh6d8GpfV+BxfMutjUs1fmAyoHySTp3mzrtig3GhDl+zPe7FbMxkfUvyICY+zFmE8uC1y/8QWOHYZ1y52whzW9sR0DL5/fThubFsylH0yOblpy+GJIFarK8mhsZaTPcDIVWNeTrbVFQvr0QmYRvGR+HXWf29oQcGUtMgakY2mqu4ZCnTjsmyAlyvkflo2m1Ry7PexJUznI=","cryptFlag":"1","encryptFlag":"1","hashFlag":"0","signatureFlag":"0"},"errCode":"0"}
	{"pkgFlag":"0","errMsg":"","dataPackage":{"business":"6t4SU4tfqHtVY1FD4FzvB2zzrA4U/jTbhxFCTMFGgXArnJhu0dHSuw20A52Yc1BWHGm8/Uc8gRjpeXHHkZjCeEw64UAPe6u7LJh6d8GpfV+BxfMutjUs1fmAyoHySTp3WuD95Lasnul+zPe7FbMxkfUvyICY+zFmE8uC1y/8QWOHYZ1y52whzW9sR0DL5/fThubFsylH0yOblpy+GJIFarK8mhsZaTPcDIVWNeTrbVFQvr0QmYRvGR+HXWf29oQcGUtMgakY2mqu4ZCnTjsmyAlyvkflo2m1Ry7PexJUznI=","cryptFlag":"1","encryptFlag":"1","hashFlag":"0","signatureFlag":"0"},"errCode":"0"}
	{"pkgFlag":"0","errMsg":"","dataPackage":{"business":"6t4SU4tfqHtVY1FD4FzvB2zzrA4U/jTbhxFCTMFGgXArnJhu0dHSuw20A52Yc1BWHGm8/Uc8gRjpeXHHkZjCeEw64UAPe6u7LJh6d8GpfV+BxfMutjUs1fmAyoHySTp3z+t/rJZkt7p+zPe7FbMxkfUvyICY+zFmE8uC1y/8QWOHYZ1y52whzW9sR0DL5/fThubFsylH0yOblpy+GJIFarK8mhsZaTPcDIVWNeTrbVFQvr0QmYRvGR+HXWf29oQcGUtMgakY2mqu4ZCnTjsmyAlyvkflo2m1Ry7PexJUznI=","cryptFlag":"1","encryptFlag":"1","hashFlag":"0","signatureFlag":"0"},"errCode":"0"}
	{"pkgFlag":"0","errMsg":"","dataPackage":{"business":"6t4SU4tfqHtVY1FD4FzvB2zzrA4U/jTbhxFCTMFGgXArnJhu0dHSuw20A52Yc1BWHGm8/Uc8gRjpeXHHkZjCeEw64UAPe6u7LJh6d8GpfV+BxfMutjUs1fmAyoHySTp32nwVObpUKoJ+zPe7FbMxkfUvyICY+zFmE8uC1y/8QWOHYZ1y52whzW9sR0DL5/fThubFsylH0yOblpy+GJIFarK8mhsZaTPcDIVWNeTrbVFQvr0QmYRvGR+HXWf29oQcGUtMgakY2mqu4ZCnTjsmyAlyvkflo2m1Ry7PexJUznI=","cryptFlag":"1","encryptFlag":"1","hashFlag":"0","signatureFlag":"0"},"errCode":"0"}
	{"pkgFlag":"0","errMsg":"","dataPackage":{"business":"6t4SU4tfqHtVY1FD4FzvB2zzrA4U/jTbhxFCTMFGgXArnJhu0dHSuw20A52Yc1BWHGm8/Uc8gRjpeXHHkZjCeEw64UAPe6u7LJh6d8GpfV+BxfMutjUs1fmAyoHySTp3y2U8lVdyqd5+zPe7FbMxkfUvyICY+zFmE8uC1y/8QWOHYZ1y52whzW9sR0DL5/fThubFsylH0yOblpy+GJIFarK8mhsZaTPcDIVWNeTrbVFQvr0QmYRvGR+HXWf29oQcGUtMgakY2mqu4ZCnTjsmyAlyvkflo2m1Ry7PexJUznI=","cryptFlag":"1","encryptFlag":"1","hashFlag":"0","signatureFlag":"0"},"errCode":"0"}
	{"pkgFlag":"0","errMsg":"","dataPackage":{"business":"6t4SU4tfqHtVY1FD4FzvB2zzrA4U/jTbhxFCTMFGgXArnJhu0dHSuw20A52Yc1BWHGm8/Uc8gRjpeXHHkZjCeEw64UAPe6u7LJh6d8GpfV+BxfMutjUs1fmAyoHySTp3jgztbDh/UT6EePZpIfLlMioGH9/hfQjvhAyeFGQTGmnAK+3vHSDTRDwf9FJvwCh4lWNVhJzOdMv1L8iAmPsxZrXuspHAv1fMckMj5EcxcvkiXRWumHZBGAyFVjXk621R0MMP/Q/yfPhOLj95WtQ7oqgK2VbiGfajf/gqwX8P7ds=","cryptFlag":"1","encryptFlag":"1","hashFlag":"0","signatureFlag":"0"},"errCode":"0"}
"""
post_params = [
    {"pkgFlag": "0", "errMsg": "", "dataPackage": {
        "business": "6t4SU4tfqHvEqk3UCezFcRyCEtteysHNOL22oQCTRjWEbm9BrfI16rlKn+BqGxuJtgrjnD9jU5YMhVY15OttUdj4HwhYf3+riCxvj7+VgjT5LxJvqZMIaMqwqwojU0XSMFxaKhBI64rZQnP1+f6ZOvUvyICY+zFmtEpEKrVP6wrtX1969anRs0VXyKXb94ih8sB/l6lECPgJA5he36ViJJKCbxM0qHtum6Ha/WBM4smyd0rTIrRmZpX/P1ZrhOsnFFebIkijIlU=",
        "cryptFlag": "1", "encryptFlag": "1", "hashFlag": "0", "signatureFlag": "0"}, "errCode": "0"},
    {"pkgFlag": "0", "errMsg": "", "dataPackage": {
        "business": "6t4SU4tfqHtVY1FD4FzvB2zzrA4U/jTbhxFCTMFGgXArnJhu0dHSuw20A52Yc1BWHGm8/Uc8gRjpeXHHkZjCeEw64UAPe6u7LJh6d8GpfV+BxfMutjUs1fmAyoHySTp3l8sDxr/flKl+zPe7FbMxkfUvyICY+zFmE8uC1y/8QWOHYZ1y52whzW9sR0DL5/fThubFsylH0yOblpy+GJIFarK8mhsZaTPcDIVWNeTrbVFQvr0QmYRvGR+HXWf29oQcGUtMgakY2mqu4ZCnTjsmyAlyvkflo2m1Ry7PexJUznI=",
        "cryptFlag": "1", "encryptFlag": "1", "hashFlag": "0", "signatureFlag": "0"}, "errCode": "0"},
    {"pkgFlag": "0", "errMsg": "", "dataPackage": {
        "business": "6t4SU4tfqHtVY1FD4FzvB2zzrA4U/jTbhxFCTMFGgXArnJhu0dHSuw20A52Yc1BWHGm8/Uc8gRjpeXHHkZjCeEw64UAPe6u7LJh6d8GpfV+BxfMutjUs1fmAyoHySTp31f3CPEyaEmd+zPe7FbMxkfUvyICY+zFmE8uC1y/8QWOHYZ1y52whzW9sR0DL5/fThubFsylH0yOblpy+GJIFarK8mhsZaTPcDIVWNeTrbVFQvr0QmYRvGR+HXWf29oQcGUtMgakY2mqu4ZCnTjsmyAlyvkflo2m1Ry7PexJUznI=",
        "cryptFlag": "1", "encryptFlag": "1", "hashFlag": "0", "signatureFlag": "0"}, "errCode": "0"},
    {"pkgFlag": "0", "errMsg": "", "dataPackage": {
        "business": "6t4SU4tfqHtVY1FD4FzvB2zzrA4U/jTbhxFCTMFGgXArnJhu0dHSuw20A52Yc1BWHGm8/Uc8gRjpeXHHkZjCeEw64UAPe6u7LJh6d8GpfV+BxfMutjUs1fmAyoHySTp3dSUe0lzl/2l+zPe7FbMxkfUvyICY+zFmE8uC1y/8QWOHYZ1y52whzW9sR0DL5/fThubFsylH0yOblpy+GJIFarK8mhsZaTPcDIVWNeTrbVFQvr0QmYRvGR+HXWf29oQcGUtMgakY2mqu4ZCnTjsmyAlyvkflo2m1Ry7PexJUznI=",
        "cryptFlag": "1", "encryptFlag": "1", "hashFlag": "0", "signatureFlag": "0"}, "errCode": "0"},
    {"pkgFlag": "0", "errMsg": "", "dataPackage": {
        "business": "6t4SU4tfqHtVY1FD4FzvB2zzrA4U/jTbhxFCTMFGgXArnJhu0dHSuw20A52Yc1BWHGm8/Uc8gRjpeXHHkZjCeEw64UAPe6u7LJh6d8GpfV+BxfMutjUs1fmAyoHySTp3UouBy1FtqV9+zPe7FbMxkfUvyICY+zFmE8uC1y/8QWOHYZ1y52whzW9sR0DL5/fThubFsylH0yOblpy+GJIFarK8mhsZaTPcDIVWNeTrbVFQvr0QmYRvGR+HXWf29oQcGUtMgakY2mqu4ZCnTjsmyAlyvkflo2m1Ry7PexJUznI=",
        "cryptFlag": "1", "encryptFlag": "1", "hashFlag": "0", "signatureFlag": "0"}, "errCode": "0"},
    {"pkgFlag": "0", "errMsg": "", "dataPackage": {
        "business": "6t4SU4tfqHtVY1FD4FzvB2zzrA4U/jTbhxFCTMFGgXArnJhu0dHSuw20A52Yc1BWHGm8/Uc8gRjpeXHHkZjCeEw64UAPe6u7LJh6d8GpfV+BxfMutjUs1fmAyoHySTp3mzrtig3GhDl+zPe7FbMxkfUvyICY+zFmE8uC1y/8QWOHYZ1y52whzW9sR0DL5/fThubFsylH0yOblpy+GJIFarK8mhsZaTPcDIVWNeTrbVFQvr0QmYRvGR+HXWf29oQcGUtMgakY2mqu4ZCnTjsmyAlyvkflo2m1Ry7PexJUznI=",
        "cryptFlag": "1", "encryptFlag": "1", "hashFlag": "0", "signatureFlag": "0"}, "errCode": "0"},
    {"pkgFlag": "0", "errMsg": "", "dataPackage": {
        "business": "6t4SU4tfqHtVY1FD4FzvB2zzrA4U/jTbhxFCTMFGgXArnJhu0dHSuw20A52Yc1BWHGm8/Uc8gRjpeXHHkZjCeEw64UAPe6u7LJh6d8GpfV+BxfMutjUs1fmAyoHySTp3WuD95Lasnul+zPe7FbMxkfUvyICY+zFmE8uC1y/8QWOHYZ1y52whzW9sR0DL5/fThubFsylH0yOblpy+GJIFarK8mhsZaTPcDIVWNeTrbVFQvr0QmYRvGR+HXWf29oQcGUtMgakY2mqu4ZCnTjsmyAlyvkflo2m1Ry7PexJUznI=",
        "cryptFlag": "1", "encryptFlag": "1", "hashFlag": "0", "signatureFlag": "0"}, "errCode": "0"},
    {"pkgFlag": "0", "errMsg": "", "dataPackage": {
        "business": "6t4SU4tfqHtVY1FD4FzvB2zzrA4U/jTbhxFCTMFGgXArnJhu0dHSuw20A52Yc1BWHGm8/Uc8gRjpeXHHkZjCeEw64UAPe6u7LJh6d8GpfV+BxfMutjUs1fmAyoHySTp3z+t/rJZkt7p+zPe7FbMxkfUvyICY+zFmE8uC1y/8QWOHYZ1y52whzW9sR0DL5/fThubFsylH0yOblpy+GJIFarK8mhsZaTPcDIVWNeTrbVFQvr0QmYRvGR+HXWf29oQcGUtMgakY2mqu4ZCnTjsmyAlyvkflo2m1Ry7PexJUznI=",
        "cryptFlag": "1", "encryptFlag": "1", "hashFlag": "0", "signatureFlag": "0"}, "errCode": "0"},
    {"pkgFlag": "0", "errMsg": "", "dataPackage": {
        "business": "6t4SU4tfqHtVY1FD4FzvB2zzrA4U/jTbhxFCTMFGgXArnJhu0dHSuw20A52Yc1BWHGm8/Uc8gRjpeXHHkZjCeEw64UAPe6u7LJh6d8GpfV+BxfMutjUs1fmAyoHySTp32nwVObpUKoJ+zPe7FbMxkfUvyICY+zFmE8uC1y/8QWOHYZ1y52whzW9sR0DL5/fThubFsylH0yOblpy+GJIFarK8mhsZaTPcDIVWNeTrbVFQvr0QmYRvGR+HXWf29oQcGUtMgakY2mqu4ZCnTjsmyAlyvkflo2m1Ry7PexJUznI=",
        "cryptFlag": "1", "encryptFlag": "1", "hashFlag": "0", "signatureFlag": "0"}, "errCode": "0"},
    {"pkgFlag": "0", "errMsg": "", "dataPackage": {
        "business": "6t4SU4tfqHtVY1FD4FzvB2zzrA4U/jTbhxFCTMFGgXArnJhu0dHSuw20A52Yc1BWHGm8/Uc8gRjpeXHHkZjCeEw64UAPe6u7LJh6d8GpfV+BxfMutjUs1fmAyoHySTp3y2U8lVdyqd5+zPe7FbMxkfUvyICY+zFmE8uC1y/8QWOHYZ1y52whzW9sR0DL5/fThubFsylH0yOblpy+GJIFarK8mhsZaTPcDIVWNeTrbVFQvr0QmYRvGR+HXWf29oQcGUtMgakY2mqu4ZCnTjsmyAlyvkflo2m1Ry7PexJUznI=",
        "cryptFlag": "1", "encryptFlag": "1", "hashFlag": "0", "signatureFlag": "0"}, "errCode": "0"},
    {"pkgFlag": "0", "errMsg": "", "dataPackage": {
        "business": "6t4SU4tfqHtVY1FD4FzvB2zzrA4U/jTbhxFCTMFGgXArnJhu0dHSuw20A52Yc1BWHGm8/Uc8gRjpeXHHkZjCeEw64UAPe6u7LJh6d8GpfV+BxfMutjUs1fmAyoHySTp3jgztbDh/UT6EePZpIfLlMioGH9/hfQjvhAyeFGQTGmnAK+3vHSDTRDwf9FJvwCh4lWNVhJzOdMv1L8iAmPsxZrXuspHAv1fMckMj5EcxcvkiXRWumHZBGAyFVjXk621R0MMP/Q/yfPhOLj95WtQ7oqgK2VbiGfajf/gqwX8P7ds=",
        "cryptFlag": "1", "encryptFlag": "1", "hashFlag": "0", "signatureFlag": "0"}, "errCode": "0"},
]
post_data = 'https://wap.bank.ecitic.com:6443/NMBFOServer/MBIFFinancial.do?act=PEMBFIPL:6443'
headers = {
    "Host": "wap.bank.ecitic.com:6443",
    "Accept": "*/*",
    "Content-Type": "*/*; charset=utf-8",
    "Connection": "keep-alive",
    "Cookie": "JSESSIONID=0000i2awV5CrVJNWvgadLObVS95:1de8ljl72; citicbank_cookie=!vSDbrQmewluAbtn9uRfR4Ya0Ekd5t9DnBW37XZG0SGlq8KF6U1xGtOLZY1HHz5sR6wa/eaXYx/l2E8Y=",
    "Accept-Language": "zh-cn",
    "Content-Length": "204",
    "Accept-Encoding": "gzip,deflate",
    "User-Agent": "CiticMobileBank/2 CFNetwork/978.0.7 Darwin/18.5.0",

}
resp = requests.post(post_data, data=post_data[0], headers=headers, verify=False)
mes = {"dataPackage":{"business":"{\"RETCODE\":\"MBFO400\",\"RETMSG\":\"客户端初始化异常，请重新操作或重启客户端。\"}","signatureFlag":0,"cryptFlag":0,"hashFlag":0},"errCode":0,"errMsg":"","pkgFlag":0,"crc":0}
print(resp.content.decode('u8'))
