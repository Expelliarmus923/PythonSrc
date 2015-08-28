# -*- coding:utf-8 -*-
import sys
import pymysql

__author__ = 'lulizhou'


class TransferMoney(object):
    def __init__(self, conn):
        self.conn = conn

    def transfermoney(self, source_acctid, transfer_acctid, money):
        try:
            self.check_acct_available(source_acctid)
            self.check_acct_available(transfer_acctid)
            self.has_enough_money(source_acctid, money)
            self.add_money(transfer_acctid, money)
            self.reduce_money(source_acctid, money)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e

    def check_acct_available(self, acctid):
        cursor = conn.cursor()
        try:
            sql = "select * from account where acctid=%s" % acctid
            print("check_acct_available %s" % sql)
            cursor.execute(sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("账号%s不存在" % acctid)
        finally:
            cursor.close()

    def has_enough_money(self, acctid, money):
        cursor = conn.cursor()
        try:
            sql = "select * from account where acctid=%s and money>%s" % (acctid, money)
            print("has_enough_money %s" % sql)
            cursor.execute(sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("账号%s余额不足" % acctid)
        finally:
            cursor.close()

    def add_money(self, acctid, money):
        cursor = conn.cursor()
        try:
            sql = "update account set money=money+%s where acctid=%s" % (money, acctid)
            print("add_money %s" % sql)
            cursor.execute(sql)
            rs = cursor.rowcount
            if rs != 1:
                raise Exception("账号%s加钱失败" % acctid)
        finally:
            cursor.close()

    def reduce_money(self, acctid, money):
        cursor = conn.cursor()
        try:
            sql = "update account set money=money-%s where acctid=%s" % (money, acctid)
            print("add_money %s" % sql)
            cursor.execute(sql)
            rs = cursor.rowcount
            if rs != 1:
                raise Exception("账号%s减钱失败" % acctid)
        finally:
            cursor.close()


if __name__ == '__main__':
    print(sys.argv)
    source_acctid = sys.argv[1]
    transfer_acctid = sys.argv[2]
    money = sys.argv[3]
    con = conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd='121224',
        db='test',
        charset='utf8'
    )
    tr_money = TransferMoney(conn)

    try:
        tr_money.transfermoney(source_acctid, transfer_acctid, money)
    except Exception as e:
        print("出现问题", str(e))
    finally:
        con.close()