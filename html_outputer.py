# 输出器，输出获得的数据内容
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        # 输出到一共html文件中
        fout = open('output.html', 'w', encoding='utf-8')
        # 以html的形式写入文件
        fout.write("<!DOCTYPE html>\n")
        fout.write("<html>\n")
        fout.write("<head>\n")
        fout.write("<title></title>\n")
        fout.write("<meta http-equiv=\"content-type\" content=\"text/html\" charset=utf-8\">\n")
        fout.write("</head>\n")
        fout.write("<body>\n")
        fout.write("<table>\n")

        for data in self.datas:
            fout.write("<tr>\n")

            fout.write("<td>%s</td>\n" % data['url'])
            fout.write("<td>%s</td>\n" % data['title'])
            fout.write("<td>%s</td>\n" % data['summary'])

            fout.write("</tr>\n")

        fout.write("</table>\n")
        fout.write("</body>\n")
        fout.write("</html>\n")

        fout.close()