from js2py.evaljs import eval_js
import re


# raw_data = """eval(function(p,a,c,k,e,d){e=function(c){return(c<a?'':e(parseInt(c/a)))+((c=c%a)>35?String.fromCharCode(c+29):c.toString(36))};if(!''.replace(/^/,String)){while(c--){d[e(c)]=k[c]||e(c)}k=[function(e){return d[e]}];e=function(){return'\\w+'};c=1};while(c--){if(k[c]){p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c])}}return p}('d I=\'//1k.P.Q/O?D=S&Y=1\';d M="9://W.8.7";d J="9://6.8.7";n b(c){N(c.x(/^(\\/r\\/?)/i)){t M+c}U N(c.x(/^(\\/|u?)/i)){t J+c}t c}n H(){d e=V T();e.5=b("/r/C-B=/19");e.R=n(){q.w=\'<0><a l="9://m.8.7/k/j/h.s"><0 2="3:4;"><6 2="o-g: 4;3:f;"  5="\'+b("/r/L-z=/19")+\'"></0></a><a l="9://m.8.7/k/j/h.s"><0><6 2="o-g: 4;3:f;K: X%;" 5="\'+b("/r/C-B=/19")+\'" /><p 2="G-F: y;">A/A</p></0></a><a l="9://m.8.7/k/j/h.s"><0 2="3:4;"><6 2="o-g: 4;3:f;"  5="\'+b("/r/L-z=/19")+\'"></0></a><6 2="o-g: 4;3:4;"  5="\'+b("")+\'"></0>\'};e.10=n(){q.w=\'<a l="9://m.8.7/k/j/h.s" 2="1j-1i: 1h; Z: 1g;G-F: y;"><0 1f="1e"  2="3:f;" ><6 2="3:4;" 5="\'+b("")+\'" E=""><6 5="9://1d.8.7/u/11/1b.1c" E="" 2="1a-K: 18;"> <p>图片加载失败，点击刷新页面试试</p><p>刷新几次都无法加载就翻下一页吧</p></0></a>\';d 0=v.17(\'0\');0.w=\'<0 2="3: 4;"><6 5="\'+I+\'"></0>\';v.16.15(0)}}14.13();d q=v.12(\'u\');q.D="";H();',62,83,'div||style|display|none|src|img|com|duoduomh|https||getImageUrl|image|var|vebd9b|block|events|1106286||zhoushuhuizhan|manhua|href||function|pointer||v3b87d||html|return|images|document|innerHTML|match|center|kAEzLFxx5ZOi632kTWQwYjlTzGpzLxzeSB6MRz62d0cYRfw|20|kAEzLFxx5ZOi632kTWQwYjlhNGJhZGM0NmNhMTg1MDExZGI5Nzc2MGE5MGU1MDEwY2M5OGQ2ZjgzZTg1NjFiNmY0YjJmNzg0Y2Y2MGWDjBu86jJa4kNCUkrzGxiY9aXdkyoYfwUOW7162KtFDpMtRjVWAJcJjK4LfmkRXbaoUtUiwi7KB3FcAZmamCV7e6kbL5BI_PBzm6dLY2ok9nX_7lP94E4PIp72d0cYRfw|EXL|id|alt|align|text|loadImage|esi|cih|width||cirh|if|go1|51|la|onload|4187563|Image|else|new|res0826|100|pvFlag|color|onerror|default|getElementById|initBan|sinChapter|append|body|createElement|15em||max|error|png|img1|fail|class|red|16px|size|font|ia'.split('|'),0,{}))"""


def duoduo_get_image_url(raw_data):

    func_raw = eval_js("""
    function(p, a, c, k, e, d) {
        e = function(c) {
            return (c < a ? '': e(parseInt(c / a))) + ((c = c % a) > 35 ? String.fromCharCode(c + 29) : c.toString(36))
        };
        if (!''.replace(/^/, String)) {
            while (c--) {
                d[e(c)] = k[c] || e(c)
            }
            k = [function(e) {
                return d[e]
            }];
            e = function() {
                return '\\w+'
            };
            c = 1
        };
        return d;
    }
    """)

    res = re.search(
        r'}\(\'(.*?\(\);)\',(\d+),(\d+),\'(.*?)\'\.split', raw_data)

    p = res.group(1)
    a = res.group(2)
    c = res.group(3)
    k = res.group(4).split('|')

    k: dict = func_raw(p, a, c, k, 0, {})

    for key in k:
        p = re.sub(r'\b' + key + r'\b', k[key], p)

    # print(p)

    # 还原出整个XHR后，再找其中的图像加载地
    uri = re.search(r'src=getImageUrl\("(.*?)"\);', p).group(1)
    resouce_url = re.search(r'var cirh="(.*?)"', p).group(1)
    return resouce_url + uri
