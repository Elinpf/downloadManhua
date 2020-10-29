function(p, a, c, k, e, d) {
    // p 是最后要替换成的HTML格式
    // a = 62  c=84 都在后面的值中
    // k = 网页给出的Array
    // e 函数
    // d = 算出的 键值对
    e = function(c) {
        return (c < a ? '' : e(parseInt(c / a))) + ((c = c % a) > 35 ? String.fromCharCode(c + 29) : c.toString(36))
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
    while (c--) {
        if (k[c]) {
            p = p.replace(new RegExp('\\b' + e(c) + '\\b', 'g'), k[c])
        }
    }
    return p;

    eval(function(p, a, c, k, e, d) {
        e = function(c) { return (c < a ? '' : e(parseInt(c / a))) + ((c = c % a) > 35 ? String.fromCharCode(c + 29) : c.toString(36)) };
        if (!''.replace(/^/, String)) {
            while (c--) { d[e(c)] = k[c] || e(c) }
            k = [function(e) { return d[e] }];
            e = function() { return '\\w+' };
            c = 1
        };
        while (c--) { if (k[c]) { p = p.replace(new RegExp('\\b' + e(c) + '\\b', 'g'), k[c]) } }
        return p
    }('b N=\'//17.15.14/13?A=12&11=1\';b H="t://10.v.q";b E="t://7.v.q";j 9(c){G(c.F(/^(\\/r\\/?)/i)){x H+c}W G(c.F(/^(\\/|u?)/i)){x E+c}x c}j B(){b k=T S();k.8=9("/r/I-D/1");k.R=j(){l.s=\'<0><a h="/g/f/d-3.e"><0 4="6:5;"><7 4="o-m: 5;6:n;"  8="\'+9("/r/C/1")+\'"></0></a><a h="/g/f/d-3.e"><0><7 4="o-m: 5;6:n;M: 16%;" 8="\'+9("/r/I-D/1")+\'" /><p 4="y-J: z;">2/1h</p></0></a><a h="/g/f/d-3.e"><0 4="6:5;"><7 4="o-m: 5;6:n;"  8="\'+9("/r/C/1")+\'"></0></a><7 4="o-m: 5;6:5;"  8="\'+9("/r/K-L/2")+\'"></0>\'};k.1d=j(){l.s=\'<a h="/g/f/d-3.e" 4="1l-19: 1k; 1j: 1g;y-J: z;"><0 1a="P"  4="6:n;" ><7 4="6:5;" 8="\'+9("/r/K-L/2")+\'" O=""><7 8="t://1i.v.q/u/18/1f.1e" O="" 4="1c-M: 1b;"> <p>图片加载失败，点击刷新页面试试</p><p>刷新几次都无法加载就翻下一页吧</p></0></a>\';b 0=w.Y(\'0\');0.s=\'<0 4="6: 5;"><7 8="\'+N+\'"></0>\';w.U.V(0)}}Q.X();b l=w.Z(\'u\');l.A="";B();', 62, 84, 'div||||style|none|display|img|src|getImageUrl||var|image|367213|html|zhoushuhuizhan|manhua|href||function|v82405|vfdbbf|events|block|pointer||com||innerHTML|https|images|duoduomh|document|return|text|center|id|loadImage|7DBJqJo7MuLOEvUHyGW2I4YmZkNTETzGpzLxzeSB6MRz6x2gsAMonWjQ9Gr3kGbGJbX|tP6heC_H8zpmoaURZ1RQUjQJ4d8dNFf2Wu1Xp9YZj80yBP2e4cjtVWx2gsAMonWjQ9Gr3kGbGJbX|cih|match|if|cirh|7m7DBJqJo7MuLOEvUHyGW2I4YmZkNTE0ZGJlZGJkYzVjZGUwMzc4NTNkYTBkNWIzM2IxZTcyN2IyOGQwZjZlN2VjYjllY2E3YmJhNWIxYWTguFu6pYifOveOTqNzNymRVuKoRnJFLCIC93K2n5jxeJC4itcyrTzBcro_yyv0ybDYleJmnIk|align|uPht9K80qlgRjVRhfgCG4zg1MjNlYTVkNmFlYzRhNmFiOTY5OWMzYjUxNjVmYzRmOWFhOWNlNDI3MGFhODAxYTJiNzkxNTVhMzA1MzVmOTSGPytmfCXxXNAZK7_Z3kmJPfIwIFoO51olC7i2BZhTEDMjw89b2CJ1thMB44Y0d8_bCZnkRJ3EufIJHejSGJzjnSwZV754fjEFHB4HibDuFN0CJIBkjyacqUV6qQt1b8w|FMkPp3aBBqgfW544MGr2|width|esi|alt|fail|sinChapter|onload|Image|new|body|append|else|initBan|createElement|getElementById|res0826|pvFlag|4187563|go1|la|51|100|ia|default|size|class|15em|max|onerror|png|error|red|52|img1|color|16px|font'.split('|'), 0, {}))


    var esi = '//ia.51.la/go1?id=4187563&pvFlag=1';
    var cirh = "https://res0826.duoduomh.com";
    var cih = "https://img.duoduomh.com";

    function getImageUrl(image) {
        if (image.match(/^(\/r\/?)/i)) {
            return cirh + image
        } else if (image.match(/^(\/|images?)/i)) {
            return cih + image
        }
        return image
    }

    function loadImage() {
        var v82405 = new Image();
        v82405.src = getImageUrl("/r/7m7DBJqJo7MuLOEvUHyGW2I4YmZkNTE0ZGJlZGJkYzVjZGUwMzc4NTNkYTBkNWIzM2IxZTcyN2IyOGQwZjZlN2VjYjllY2E3YmJhNWIxYWTguFu6pYifOveOTqNzNymRVuKoRnJFLCIC93K2n5jxeJC4itcyrTzBcro_yyv0ybDYleJmnIk-tP6heC_H8zpmoaURZ1RQUjQJ4d8dNFf2Wu1Xp9YZj80yBP2e4cjtVWx2gsAMonWjQ9Gr3kGbGJbX/1");
        v82405.onload = function() {
            vfdbbf.innerHTML = '<div><a href="/manhua/zhoushuhuizhan/367213-3.html"><div style="display:none;"><img style="pointer-events: none;display:block;"  src="' + getImageUrl("/r/7DBJqJo7MuLOEvUHyGW2I4YmZkNTETzGpzLxzeSB6MRz6x2gsAMonWjQ9Gr3kGbGJbX/1") + '"></div></a><a href="/manhua/zhoushuhuizhan/367213-3.html"><div><img style="pointer-events: none;display:block;width: 100%;" src="' + getImageUrl("/r/7m7DBJqJo7MuLOEvUHyGW2I4YmZkNTE0ZGJlZGJkYzVjZGUwMzc4NTNkYTBkNWIzM2IxZTcyN2IyOGQwZjZlN2VjYjllY2E3YmJhNWIxYWTguFu6pYifOveOTqNzNymRVuKoRnJFLCIC93K2n5jxeJC4itcyrTzBcro_yyv0ybDYleJmnIk-tP6heC_H8zpmoaURZ1RQUjQJ4d8dNFf2Wu1Xp9YZj80yBP2e4cjtVWx2gsAMonWjQ9Gr3kGbGJbX/1") + '" /><p style="text-align: center;">2/52</p></div></a><a href="/manhua/zhoushuhuizhan/367213-3.html"><div style="display:none;"><img style="pointer-events: none;display:block;"  src="' + getImageUrl("/r/7DBJqJo7MuLOEvUHyGW2I4YmZkNTETzGpzLxzeSB6MRz6x2gsAMonWjQ9Gr3kGbGJbX/1") + '"></div></a><img style="pointer-events: none;display:none;"  src="' + getImageUrl("/r/uPht9K80qlgRjVRhfgCG4zg1MjNlYTVkNmFlYzRhNmFiOTY5OWMzYjUxNjVmYzRmOWFhOWNlNDI3MGFhODAxYTJiNzkxNTVhMzA1MzVmOTSGPytmfCXxXNAZK7_Z3kmJPfIwIFoO51olC7i2BZhTEDMjw89b2CJ1thMB44Y0d8_bCZnkRJ3EufIJHejSGJzjnSwZV754fjEFHB4HibDuFN0CJIBkjyacqUV6qQt1b8w-FMkPp3aBBqgfW544MGr2/2") + '"></div>'
        };
        v82405.onerror = function() {
            vfdbbf.innerHTML = '<a href="/manhua/zhoushuhuizhan/367213-3.html" style="font-size: 16px; color: red;text-align: center;"><div class="fail"  style="display:block;" ><img style="display:none;" src="' + getImageUrl("/r/uPht9K80qlgRjVRhfgCG4zg1MjNlYTVkNmFlYzRhNmFiOTY5OWMzYjUxNjVmYzRmOWFhOWNlNDI3MGFhODAxYTJiNzkxNTVhMzA1MzVmOTSGPytmfCXxXNAZK7_Z3kmJPfIwIFoO51olC7i2BZhTEDMjw89b2CJ1thMB44Y0d8_bCZnkRJ3EufIJHejSGJzjnSwZV754fjEFHB4HibDuFN0CJIBkjyacqUV6qQt1b8w-FMkPp3aBBqgfW544MGr2/2") + '" alt=""><img src="https://img1.duoduomh.com/images/default/error.png" alt="" style="max-width: 15em;"> <p>图片加载失败，点击刷新页面试试</p><p>刷新几次都无法加载就翻下一页吧</p></div></a>';
            var div = document.createElement('div');
            div.innerHTML = '<div style="display: none;"><img src="' + esi + '"></div>';
            document.body.append(div)
        }
    }
    sinChapter.initBan();
    var vfdbbf = document.getElementById('images');
    vfdbbf.id = "";
    loadImage();