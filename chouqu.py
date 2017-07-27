#  -*- coding:utf-8 -*-

import os
import codecs

##抽取中文1
def eachFile(filepath):
    pathDir = os.listdir(filepath)
    each_file = list()
    for allDir in pathDir:
        child = os.path.join('%s/%s' % (filepath, allDir))
        each_file.append(child)
    return each_file


def main(ori_road, new_file, new_chinese_file):
    if os.path.exists(new_file):
        os.remove(new_file)
    for one_path in eachFile(ori_road):  # 循环每一个原始文件
        print one_path
        temt_line = list()
        with codecs.open(new_file, "a", "utf-8") as fw, codecs.open(one_path, 'r', "utf-8") as fr:
            for line in fr:
                if line.strip()[-1] == "}":
                    if not temt_line:
                        fw.write(u"{}\r\n".format(line.strip()))
                    else:
                        temt_line.append(line.strip())
                        fw.write(u"{}\r\n".format("".join(temt_line)))
                        temt_line = list()
                else:
                    temt_line.append(line.strip())

    with codecs.open(new_file, "r", "utf-8") as fr, codecs.open(new_chinese_file, 'w', "utf-8") as fw:
        for line in fr:
            try:
                all_message = eval(line.strip()[19:])
                message_time = line.strip()[:19]
                user_id = all_message["fromUserId"]
                target_id = all_message["targetId"]

                chinese_content = ''.join(x for x in line if ord(x) >= 256)
                chinese_content = unicode(chinese_content.strip())
                if chinese_content:
                    fw.write(u"{}\t{}\t{}\t{}\r\n".format(user_id, target_id, message_time, chinese_content))
            except:
                continue


if __name__ == "__main__":
    ori_road = u"C:/负面语句判别/原始数据/2017-030506"
    new_file = u"C:/负面语句判别/抽取出来的数据/2017-030506.txt"
    new_chinese_file = u"C:/负面语句判别/抽取出来的数据/2017-030506_chinese.txt"
    main(ori_road, new_file, new_chinese_file)
