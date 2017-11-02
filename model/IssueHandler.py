import xml.sax
import html

import re

SAMPLE = '<?xml version="1.0" encoding="UTF-8"?>\
<feed xmlns="http://www.w3.org/2005/Atom">\
  <title/>\
  <link rel="self" href="http://10.0.1.3/redmine/issues/144811.atom?key=16e31f4e41ffaa1b29dd8a7f5c11fb21c1dd00c0"/>\
  <link rel="alternate" href="http://10.0.1.3/redmine/"/>\
  <id>http://10.0.1.3/redmine/</id>\
  <icon>http://10.0.1.3/redmine/redmine/favicon.ico?1420968012</icon>\
  <updated>2017-10-31T09:59:19Z</updated>\
  <author>\
    <name>framgia Redmine</name>\
  </author>\
  <entry>\
    <title>Memvo Lab - Task #144811: [BUY POINT][UI] Implement VISA/Master payment UI</title>\
    <link rel="alternate" href="http://10.0.1.3/redmine/issues/144811"/>\
    <id>http://10.0.1.3/redmine/issues/144811?journal_id=676862</id>\
    <updated>2017-10-31T09:59:19Z</updated>\
    <author>\
      <name>Chuong Vu Duy</name>\
      <email>vu.duy.chuong@framgia.com</email>\
    </author>\
    <content type="html">\
&lt;ul&gt;&lt;li&gt;&lt;strong&gt;Story point&lt;/strong&gt; set to &lt;i&gt;5&lt;/i&gt;&lt;/li&gt;&lt;/ul&gt;    </content>\
  </entry>\
  <entry>\
    <title>Memvo Lab - Task #144811: [BUY POINT][UI] Implement VISA/Master payment UI</title>\
    <link rel="alternate" href="http://10.0.1.3/redmine/issues/144811"/>\
    <id>http://10.0.1.3/redmine/issues/144811?journal_id=677134</id>\
    <updated>2017-11-01T01:21:12Z</updated>\
    <author>\
      <name>Nguyen Ba Long</name>\
      <email>nguyen.ba.long@framgia.com</email>\
    </author>\
    <content type="html">\
&lt;ul&gt;&lt;li&gt;&lt;strong&gt;Status&lt;/strong&gt; changed from &lt;i&gt;New&lt;/i&gt; to &lt;i&gt;In Progress&lt;/i&gt;&lt;/li&gt;&lt;/ul&gt;    </content>\
  </entry>\
  <entry>\
    <title>Memvo Lab - Task #144811: [BUY POINT][UI] Implement VISA/Master payment UI</title>\
    <link rel="alternate" href="http://10.0.1.3/redmine/issues/144811"/>\
    <id>http://10.0.1.3/redmine/issues/144811?journal_id=677886</id>\
    <updated>2017-11-01T09:59:30Z</updated>\
    <author>\
      <name>Chuong Vu Duy</name>\
      <email>vu.duy.chuong@framgia.com</email>\
    </author>\
    <content type="html">\
&lt;ul&gt;&lt;li&gt;&lt;strong&gt;Due date&lt;/strong&gt; changed from &lt;i&gt;11/01/2017&lt;/i&gt; to &lt;i&gt;11/02/2017&lt;/i&gt;&lt;/li&gt;&lt;li&gt;&lt;strong&gt;Estimated time&lt;/strong&gt; changed from &lt;i&gt;10.00&lt;/i&gt; to &lt;i&gt;16.00&lt;/i&gt;&lt;/li&gt;&lt;/ul&gt;    </content>\
  </entry>\
  <entry>\
    <title>Memvo Lab - Task #144811: [BUY POINT][UI] Implement VISA/Master payment UI</title>\
    <link rel="alternate" href="http://10.0.1.3/redmine/issues/144811"/>\
    <id>http://10.0.1.3/redmine/issues/144811?journal_id=678431</id>\
    <updated>2017-11-02T09:37:41Z</updated>\
    <author>\
      <name>Chuong Vu Duy</name>\
      <email>vu.duy.chuong@framgia.com</email>\
    </author>\
    <content type="html">\
&lt;ul&gt;&lt;li&gt;&lt;strong&gt;Status&lt;/strong&gt; changed from &lt;i&gt;In Progress&lt;/i&gt; to &lt;i&gt;Resolved&lt;/i&gt;&lt;/li&gt;&lt;li&gt;&lt;strong&gt;Assignee&lt;/strong&gt; changed from &lt;i&gt;Chuong Vu Duy&lt;/i&gt; to &lt;i&gt;Cuong Hoang Van&lt;/i&gt;&lt;/li&gt;&lt;li&gt;&lt;strong&gt;% Done&lt;/strong&gt; changed from &lt;i&gt;80&lt;/i&gt; to &lt;i&gt;100&lt;/i&gt;&lt;/li&gt;&lt;/ul&gt;    </content>\
  </entry>\
</feed>'


class IssueHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.title = ""
        self.link = ""
        self.id = ""
        self.updated = ""
        self.author = ""
        self.content = ""

    # Call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "link":
            self.link = attributes['href']

    # Call when an elements ends
    def endElement(self, tag):
        if self.CurrentData == "title":
            print("title:", self.title)
        elif self.CurrentData == "link":
            print("link:", self.link)
        elif self.CurrentData == "id":
            print("id:", self.id)
        elif self.CurrentData == "updated":
            print("updated:", self.updated)
        elif self.CurrentData == "author":
            print("author:", self.author)
        elif self.CurrentData == "content":
            print("content:", self.content)
        self.CurrentData = ""

    # Call when a character is read
    def characters(self, ct):
        if self.CurrentData == "title":
            self.title = ct
        elif self.CurrentData == "id":
            self.id = ct
        elif self.CurrentData == "updated":
            self.updated = ct
        elif self.CurrentData == "author":
            self.author = ct
        elif self.CurrentData == "content":
            self.content += ct

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

if (__name__ == "__main__"):
    # create an XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # override the default ContextHandler
    Handler = IssueHandler()
    parser.setContentHandler(Handler)

    # parser.parseString(SAMPLE)
    xml.sax.parseString(SAMPLE, Handler)
    print(Handler.content)