# encoding:utf-8
import execjs
import re

# resp = """<script>var x="@@DOMContentLoaded@Wed@@@while@toString@@@yEBDZuOKYo@a@fh@@@length@e@cookie@@GR@match@return@0xFF@chars@@@@Expires@19@09@8@@@7@May@fromCharCode@new@x@@0xEDB88320@setTimeout@pathname@rOm9XFMtA3QKV7nYsPGT4lifyWwkq5vcjH2IdxUoCbhERLaz81DNB6@catch@function@@Array@window@D@@https@1500@@1@@@charCodeAt@Path@innerHTML@for@@d@substr@@toLowerCase@@RegExp@div@eval@@@captcha@@charAt@href@onreadystatechange@3@else@search@17@JgSe0upZ@try@@document@@@createElement@514@@parseInt@@__jsl_clearance@J3nxVU@@@@@split@1559118017@reverse@if@@location@@attachEvent@@var@GMT@@20@addEventListener@replace@@36@@@false@g@join@String@@f@firstChild@29@0@@challenge@".replace(/@*$/,"").split("@"),y="29 1l=J(){F('25.1q=25.G+25.1u.2e(/[\\?|&]1n-2t/,\\'\\')',13);1z.i='1H=21.1D|2r|'+(J(){29 2f=[J(1l){m 1l},J(2f){m 2f},(J(){29 1l=1z.1C('1j');1l.1a='<c 1q=\\'/\\'>1y</c>';1l=1l.2p.1q;29 2f=1l.l(/12?:\\/\\//)[2r];1l=1l.1e(2f.g).1g();m J(2f){1b(29 1y=2r;1y<2f.g;1y++){2f[1y]=1l.1p(2f[1y])};m 2f.2l('')}})()],1y=[[-~!{}-~!{}-~(+!{})-~[]+(-~{}<<-~{})],((-~[]+[(-~!{}-~!{})*[-~!{}-~!{}]]>>-~[])+[]),[-~[]]+[~~{}],(-~!{}-~!{}+[]),[~~{}],[(+!+[])+(-~(+!{})+[-~!{}-~!{}]>>-~!{}-~!{})-~[]+(-~-~[])*[-~-~[]]],[v],[1s],[-~[]],(-~(+!{})-~[]+(-~{}<<-~{})+[[]][2r]),((-~!{}+[(+[])])/[-~-~[]]+[[]][2r])];1b(29 1l=2r;1l<1y.g;1l++){1y[1l]=2f[[15,2r,15,2r,15,2r,15,2r,15,2r,15][1l]](['d','1I%',(-~!{}-~!{}+[])+[+{}+[]][2r].1p(~~[]),([-~-~[]]/~~[]+[]).1p(y),[1s],'10','k',([][{}]+[[]][2r]).1p(-~(+!{})-~[]+(-~{}<<-~{}))+[(+!+[])/~~{}+[]+[]][2r].1p(([-~!{}-~!{}]+~~''>>-~!{}-~!{})),'C',([[]][15]+[]+[[]][2r]).1p(v),'b'][1y[1l]])};m 1y.2l('')})()+';s=4, 2q-z-t u:2c:1v 2a;19=/;'};23((J(){1x{m !!M.2d;}I(h){m 2j;}})()){1z.2d('3',1l,2j)}1t{1z.27('1r',1l)}",f=function(x,y){var a=0,b=0,c=0;x=x.split("");y=y||99;while((a=x.shift())&&(b=a.charCodeAt(0)-77.5))c=(Math.abs(b)<13?(b+48.5):parseInt(a,36))+y*c;return c},z=f(y.match(/\w/g).sort(function(x,y){return f(x)-f(y)}).pop());while(z++)try{eval(y.replace(/\b\w+\b/g, function(y){return x[f(y,z)-1]||("_"+y)}));break}catch(_){}</script>"""
# resp = """<script>var x="@@@window@@hantom@chars@@firstChild@0xEDB88320@507@setTimeout@GMT@@join@addEventListener@@for@@callP@attachEvent@toLowerCase@0@captcha@@@@fromCharCode@false@parseInt@https@@Path@@a@__jsl_clearance@@if@JgSe0upZ@@replace@QP@e@try@D@1543978118@d@@Wed@search@return@eval@@else@String@length@@toString@innerHTML@@@18@DOMContentLoaded@05@8@2@ES@@@split@EKx@@document@charAt@38@4@RegExp@6@Expires@@Dec@@36@rOm9XFMtA3QKV7nYsPGT4lifyWwkq5vcjH2IdxUoCbhERLaz81DNB6@href@while@z@onreadystatechange@function@g@@@@Array@challenge@@@div@cookie@@48@@new@@substr@03@@Bmv@location@createElement@var@@@0xFF@1500@@@f@match@@catch@charCodeAt@pathname@1@@reverse@@".replace(/@*$/,"").split("@"),y="1T 1d=1x(){c('1R.1t=1R.2b+1R.O.F(/[\\?|&]o-1D/,\\'\\')',23);1h.1H='A=K.b|n|'+(1x(){1T 1d=[(-~[]-~[]+[]),[-~~~[]]+((+![])+[]+[]),[-~{}+[~~'']-(-~{})],[-~~~[]],(-~~~[]-~-~!{}-~~~[]-~-~!{}+[[]][n]),((-~[]+[(-~[]<<-~[])]>>(-~[]<<-~[]))+[]+[]),((-~!{}+[(-~-~!{}<<-~{})]>>-~!{})+[]+[[]][n]),(-~[(-~!{}+[(-~-~!{}<<-~{})]>>-~!{})]+[]),[-~~~[]]+((-~[]+[(-~[]<<-~[])]>>(-~[]<<-~[]))+[]+[]),[-~~~[]]+(-~[]-~[]+[]),((-~!{}<<1a)+[[]][n]),(([(-~[]<<-~[])]+~~{}>>(-~[]<<-~[]))+[]+[]),[-~~~[]]+[-~~~[]],((+![])+[]+[])],B=1C(1d.10);i(1T 21=n;21<1d.10;21++){B[1d[21]]=[[(-~[-~-~!{}])/~~{}+[]+[]][n].1i(1m),[+[~~[], ~~[]]+[]][n].1i(-~[])+[!![][[]]+[]][n].1i(1k)+[+[~~[], ~~[]]+[]][n].1i(-~[])+[!{}+[]][n].1i((+[]))+((-~!{}<<1a)+[[]][n]),'G','1b',({}+[]).1i(-~~~[]),'1v','1Q',[4['k'+'6']+[]][n].1i(-~~~[])+({}+[]+[]).1i((+!-[])+1k)+[!![][[]]+[]][n].1i(1k)+(-~{}/(+![])+[]).1i(~~{}),'J',((-~[]+[(-~[]<<-~[])]>>(-~[]<<-~[]))+[]+[]),(-~~~[]-~-~!{}-~~~[]-~-~!{}+[[]][n])+[-~{}+[~~'']-(-~{})]+((-~!{}<<1a)+[[]][n]),'1f','%',[!{}+[]][n].1i(-~[]-~[])+[{}+[]+[]][n].1i((+!-[])+(-~!{}<<(-~[]|-~[]-~[])))][21]};P B.f('')})()+';1n=N, 18-1p-16 1O:1J:1j d;x=/;'};C((1x(){I{P !!4.g;}29(H){P t;}})()){1h.g('17',1d,t)}S{1h.l('1w',1d)}",f=function(x,y){var a=0,b=0,c=0;x=x.split("");y=y||99;while((a=x.shift())&&(b=a.charCodeAt(0)-77.5))c=(Math.abs(b)<13?(b+48.5):parseInt(a,36))+y*c;return c},z=f(y.match(/\w/g).sort(function(x,y){return f(x)-f(y)}).pop());while(z++)try{eval(y.replace(/\b\w+\b/g, function(y){return x[f(y,z)-1]||("_"+y)}));break}catch(_){}</scrip>"""

import requests


def execJS(resp):
    '''<script>var x="onreadystatechange@@uL@@@String@O@@pathname@var
    @window@@parseInt@charAt@@@@@56@@@Expires@1@3@@@document@Path@@for
    @while@0@@@headless@n@@div@@Feb@match@JgSe0upZ@@@BO7@36@createElement
    @href@1500@@@chars@@19@split@firstChild@@@@challenge@r2Xf@DOMContentLoaded
    @@@search@toLowerCase@function@cookie@Array@2@@replace@d@catch@eval
    @addEventListener@@@@RegExp@fromCharCode@return@
    rOm9XFMtA3QKV7nYsPGT4lifyWwkq5vcjH2IdxUoCbhERLaz81DNB6@51@length@03@if
    @@@@@charCodeAt@@a@@@1550026611@else@@ws@13@15@0xEDB88320
    @@captcha@false@g@setTimeout@@attachEvent@toString@@Wed@@reverse@try@innerHTML
    @join@GMT@0xFF@__jsl_clearance@substr@f@location@https@8@new
    @e".replace(/@*$/,"").split("@"),y="a 1v=23(){3c('3s.1g=3s.9+3s.21.28(/[\\?|&]39-1s/,\\'\\')',1h);r.24='3p=31.36|10|'+(23(){a 2p=[23(1v){2i 1v},23(2p){2i 2p},23(1v){2i 2b('6.2h('+1v+')')},23(1v){u(a 2p=10;2p<1v.2l;2p++){1v[2p]=d(1v[2p]).3f(1e)};2i 1v.3m('')}],1v=[(-~(+[])-~(+[])+o+[[]][10]),'3',[[-~{}]+[-~{}]],'29',[[(-~![]+[(-~(+[])-~(+[])<<-~![])]>>-~![])]+(-~(+[])-~(+[])+o+[[]][10]),(-~![]-~(+[])-~(+[])+[[]][10])+[(-~![]+[(-~(+[])-~(+[])<<-~![])]>>-~![])]],(26+[]),'1d',[(26+[])+[-~{}]],[[(-~{}<<(-~![]+[-~(+!'')]>>-~(+!'')))]+[~~''],(-~![]-~(+[])-~(+[])+[[]][10])+[(-~![]+[(-~(+[])-~(+[])<<-~![])]>>-~![])]],(26+[]),[[(-~![]+[(-~(+[])-~(+[])<<-~![])]>>-~![])]+[~~'']],'7',(+{}+[]+[]).e((+!!b.13)),'14',[(-~![]-~(+[])-~(+[])+[[]][10])+[26+26]],'10',[[(-~{}<<(-~![]+[-~(+!'')]>>-~(+!'')))]+(26+[]),[-~[([-~(+!'')]+~~{}>>-~(+!''))]]+[-~[([-~(+!'')]+~~{}>>-~(+!''))]]],'1t',[[(-~![]+[(-~(+[])-~(+[])<<-~![])]>>-~![])]+(26+[])],[(26+[])+[~~'']],'34',[(-~![]-~(+[])-~(+[])+[[]][10])+[(-~![]+[(-~(+[])-~(+[])<<-~![])]>>-~![])]],(-~![]-~(+[])-~(+[])+[[]][10]),[[-~[([-~(+!'')]+~~{}>>-~(+!''))]]+[(-~{}<<(-~![]+[-~(+!'')]>>-~(+!'')))]]];u(a h=10;h<1v.2l;h++){1v[h]=2p[[10,n,o,n,26,10,n,o,26,10,26,n,10,n,o,n,26,n,26,o,n,26,10,26][h]](1v[h])};2i 1v.3m('')})()+';m=3h, 35-18-1m 2m:j:2k 3n;s=/;'};2n((23(){3k{2i !!b.2c;}2a(40){2i 3a;}})()){r.2c('1u',1v,3a)}32{r.3e('1',1v)}",f=function(x,y){var a=0,b=0,c=0;x=x.split("");y=y||99;while((a=x.shift())&&(b=a.charCodeAt(0)-77.5))c=(Math.abs(b)<13?(b+48.5):parseInt(a,36))+y*c;return c},z=f(y.match(/\w/g).sort(function(x,y){return f(x)-f(y)}).pop());while(z++)try
    {eval(y.replace(/\b\w+\b/g, function(y){return x[f(y,z)-1]||("_"+y)}));break}catch(_){}</script>'''
    cookies = {}
    # 获取和替换动态js，生成cookie在此访问
    js_match = re.findall(r'<script>(.*?)</script>', resp)
    if js_match:
        js = js_match[0]
        key_js = re.findall(r'eval\((.*?)\);', js)[0]
        replace = 'var cookie_js={};'.format(key_js)
        js = re.sub(r'eval\(.*?\);', replace, js)
        js = js.replace(
            'break',
            'if(cookie_js.indexOf("document.cookie=\'__jsl_clearance=")!=-1){cookie_js = cookie_js.match(/document.cookie=(.*?)\+\';Expires/i)[1];break}')
        js = 'var cookie_js, window={};' + js + 'function get_cookie(){return eval(cookie_js);}'
        js = js.replace('', '')

        ctx = execjs.compile(js)
        cookie_value = ctx.call("get_cookie")
        cookies = {
            cookie_value.split('=')[0]: cookie_value.split('=')[1]
        }
    return cookies


# print execJS(resp)
url = "http://www.gsxt.gov.cn/index.html"
headers = {
    # "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3610.2 Safari/537.36",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0",
}

resp = requests.get(url=url, headers=headers)
print(resp.cookies)
cookies = execJS(resp.text)
cookies["__jsluid"] = resp.cookies.get("__jsluid")
resp = requests.get(url=url, headers=headers, cookies=cookies, allow_redirects=False)
print(resp.text)

print(execJS(resp))
