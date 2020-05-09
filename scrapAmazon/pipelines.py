# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class ScrapamazonPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("scrapedbooks.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS amazonbooks_tb""")
        self.curr.execute("""create table amazonbooks_tb(
            book_title text,
            book_author text,
            book_price text,
            book_imagelink text
        )
        """)


    def process_item(self, item, spider):
        self.table_data(item)
        return item

    def table_data(self,item):
        for data in range(len(item['product_name'])):
                
            self.curr.execute(""" insert into amazonbooks_tb values (?,?,?,?)""",
            (
                item['product_name'][data],
                item['product_author'][data],
                item['product_price'][data],
                item['product_imagelink'][data],
            ))

            self.conn.commit()