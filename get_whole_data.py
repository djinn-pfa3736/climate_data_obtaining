
import sys
from bs4 import BeautifulSoup
import urllib.request as req
import pdb

args = sys.argv

for year in range(2011, 2020):
    for month in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]:
        url = "http://www.data.jma.go.jp/obd/stats/etrn/view/daily_s1.php?prec_no=91&block_no=47927&year=" + str(year) + "&month=" + str(month) + "&day=&view=p1"
        res = req.urlopen(url)

        soup = BeautifulSoup(res, "html.parser")

        # h1 = soup.select_one("#main h1")
        # print(h1.string)

        date_anchor = soup.select("div.a_print")

        values = soup.select("td.data_0_0")
        count = 1
        date = 1
        for td in values:
            # pdb.set_trace()
            # sys.stdout.write("COUNT({}): ".format(count))
            if((count % 16) == 1 and count != 17):
                sys.stdout.write("{}, {}, {}, {}, ".format(year, int(month), date, td.string))
            elif count == 20:
                sys.stdout.write("{}\n".format(td.string))
                count = 0
                date += 1
            elif count != 17 and count != 18:
                sys.stdout.write("{}, ".format(td.string))

            count += 1
