#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import arrow


def getdate(deltadays, currentday=None, format="%Y%m%d"):
    # 获取前beforeOfDay天的日期，beforeOfDay=1：前1天；beforeOfDay=N：前N天
    if currentday:
        today = datetime.datetime.strptime(currentday, format)
    else:
        today = datetime.datetime.now()

    re_date = (today + datetime.timedelta(days=deltadays)).strftime(format)
    return re_date


def current_time(format="%Y%m%d"):
    return getdate(0, format=format)


def get_month(deltamonth, current_month, format="%Y%m"):
    if current_month:
        today = datetime.datetime.strptime(current_month, format)
    else:
        today = datetime.datetime.now()
    result = arrow.get(today).shift(months=deltamonth).strftime(format)
    return result


if __name__ == "__main__":
    print(getdate(2,"20200823"))
    print(get_month(4, "202008"))
