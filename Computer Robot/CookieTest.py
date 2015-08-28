__author__ = 'lulizhou'
import urllib
import urllib2
import cookielib
filename='cookie.txt'
cookie=cookielib.MozillaCookieJar(filename)
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata=urllib.urlencode({
            'number':'3120403020',
            'passwd':'121224llz'
        })
loginUrl="http://nitopac.nit.net.cn/reader/redr_verify.php"
result=opener.open(loginUrl,postdata)
cookie.save(ignore_discard=True,ignore_expires=True)
booklistUrl="http://nitopac.nit.net.cn/reader/book_hist.php"
result=opener.open(booklistUrl)
print result.read()