import re,sys


t = sys.stdin.read()
text = t[2:]

# text = '''<div class="portal" role="navigation" id='p-lang'>
# <h3>Languages</h3>
# <div class="body">
# <ul>
# <li class="interwiki-simple"><a href="//simple.wikipedia.org/wiki/" title="" lang="simple" hreflang="simple">Simple English</a></li>
# <li class="interwiki-ar"><a href="//ar.wikipedia.org/wiki/" title="" lang="ar" hreflang="ar"></a></li>
# <li class="interwiki-id"><a href="//id.wikipedia.org/wiki/" title="" lang="id" hreflang="id">Bahasa Indonesia</a></li>
# <li class="interwiki-ms"><a href="//ms.wikipedia.org/wiki/" title="" lang="ms" hreflang="ms">Bahasa Melayu</a></li>
# <li class="interwiki-bg"><a href="//bg.wikipedia.org/wiki/" title="" lang="bg" hreflang="bg"></a></li>
# <li class="interwiki-ca"><a href="//ca.wikipedia.org/wiki/" title="" lang="ca" hreflang="ca">Catal</a></li>
# <li class="interwiki-cs"><a href="//cs.wikipedia.org/wiki/" title="" lang="cs" hreflang="cs">esky</a></li>
# <li class="interwiki-da"><a href="//da.wikipedia.org/wiki/" title="" lang="da" hreflang="da"><b>Dansk</b></a></li>
# <li class="interwiki-de{-truncated-}'''


def find_attr(text):
    tag_d = {}
    attr_pattern = r' ([a-z]+)=(?:"|\').*?(?:"|\')' #href='blabla.bla'
    tag_pattern = r'<([a-z0-9]+)([ ]?.*?)>' # <div (optional)>
    tags = re.findall(tag_pattern,text)
    for i in tags: # tags is a list of object like (tag,rest of it part before its closing >)
        if i[0] in tag_d: # if there is a existing tag in tag-d then merge this two..
            tmp = tag_d[i[0]]
            attr = re.findall(attr_pattern,i[1])
            lst = []
            for j in attr:
                lst.append(j)
            tag_d[i[0]] = sorted(list(set(lst+tmp)))
        else:
            attr = re.findall(attr_pattern,i[1])
            lst = []
            for j in attr:
                lst.append(j)
            tag_d[i[0]] = sorted(lst)
    return tag_d
def write(dic):
    for i in sorted(dic):
        text = ''
        for j in dic[i]:
            text += j+','
        print(i,":",text[:len(text)-1],sep='')

list = find_attr(text)
write(list)
