#!/usr/bin/env python
# -*- coding: utf-8 -*-


def format_cat_id(cat_id):
    return cat_id.replace("-",",")

if __name__ == "__main__":
    print(format_cat_id("1000,1222,333"))