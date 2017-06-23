# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
import MySQLdb.cursors

class CwbPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(host='127.0.0.1',
                                    user='demouser',
                                    passwd='demo1234',
                                    db='demo',
                                    charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        self.cursor.execute("""INSERT INTO a136 (sid, name, t_10m, t_1h, t_3h, t_6h, t_12h, t_24h, t_today, t_yday, t_2d) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",(
            item['sid'],
            item['name'],
            item['t_10m'],
            item['t_1h'],
            item['t_3h'],
            item['t_6h'],
            item['t_12h'],
            item['t_24h'],
            item['t_today'],
            item['t_yday'],
            item['t_2d']
        ))  
        self.conn.commit()
        #self.conn.close()

        return item

    
