import datetime

from model import FormReport
from service import ChatWorkRequest

now = datetime.datetime.now()
data = {'date': now.strftime('%d/%m/%Y'), 'plan': 'Plan', 'actually': 'Actually', 'lineOfCode': 'Line Of Code'}
r = ChatWorkRequest.addNewMessage(str(89242461), FormReport.FORM.format(**data))
print(r.text)
