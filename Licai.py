'理财产品收益计算'


'zanqianba'

product_name = '攒钱吧!'
#import datetime
import math
from datetime import datetime
from dateutil.relativedelta import relativedelta
from unittest import TestCase
first_date = datetime(2014,7,25,0,0)
# 一次应交金额
money_every_time = 1000

#month = timedelta(day = 30)
second_date = first_date + relativedelta(month=1)
print(second_date)

now = datetime.now()
print('今天日期:' + str(now))

lasting_days = now - first_date
# print(lasting_days.days)

# 截至目前 应交次数( )
times = math.ceil(lasting_days.days/30)
now_money_cost = times*money_every_time

test = TestCase()
test.assertTrue(now_money_cost==5000)


# 累积收益
commu_benifit = 84

# 累积收益 日均
benifit_everyday = round(commu_benifit / lasting_days.days,3)
print('产品名称为: {}\n\t\t到目前你的收益金额为: {} 元;\n\t\t每天平均收益为: {} 元'.format(product_name, commu_benifit, benifit_everyday))
