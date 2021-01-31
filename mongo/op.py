#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymongo
from multiprocess.config import default_config
from tqdm import tqdm


class DBManger(object):

    def __init__(self, mongo_addr=default_config.config["mongo_config"]["addr"]
                 , db_collection=("jicheng","tmp")):
        self.client = pymongo.MongoClient(mongo_addr)
        self.db = self.client[db_collection[0]]
        self.collection = self.client[db_collection[0]][db_collection[1]]

    def get_client(self):
        return self.client

    def create_db_collection(self, db_collection):
        self.switch_db_collection(db_collection)
        try:
            self.db.create_collection(db_collection[1])
            return True
        except pymongo.errors.CollectionInvalid as e:
            return False

    def switch_db_collection(self, db_collection):
        self.db = self.client[db_collection[0]]
        self.collection = self.client[db_collection[0]][db_collection[1]]

    def list_tables(self, dbname, filter=None):
        #filter = {"name": {"$regex": r"^(?!system\\.)"}}
        db = self.client[dbname]
        return db.list_collection_names(filter=filter)

    def get_lasted_collection(self, dbname, filter):
        # filter = {"name": {"$regex": r"^(?!system\\.)"}}
        collect_list = self.list_tables(dbname, filter)
        if collect_list:
            return sorted(collect_list)[-1]
        else:
            return None

    def close(self):
        self.client.close()

    def read_from(self, db_collect, out_field=None, pipeline=None):
        self.switch_db_collection(db_collect)
        if pipeline is None:
            if out_field is None:
                result = self.collection.find({})
                return result
            else:
                tmp = []
                for key in out_field:
                    tmp.append(1)
                filter=dict(zip(out_field,tmp))
                filter.update({"_id":0})
                result = map(lambda x: tuple([x.get(field) for field in out_field]),
                            self.collection.find({}, filter))
        else:
            if out_field:
                result = map(lambda x: tuple([x.get(field) for field in out_field]),
                             self.collection.aggregate(pipeline, allowDiskUse=True))
            else:
                result = self.collection.aggregate(pipeline, allowDiskUse=True)
        return result

    def read_from_yield(self, db_collect, out_field=None, pipeline=None, is_id_out=False, batch_size=10):
        #is_id_out must be avalid since pipeline is none
        self.switch_db_collection(db_collect)
        if pipeline is None:
            if out_field is None:
                for item in self.collection.find({}, batch_size=batch_size):
                    yield item
            else:
                tmp = []
                for key in out_field:
                    tmp.append(1)
                filter = dict(zip(out_field, tmp))
                if is_id_out:
                    filter.update({"_id": 1})
                else:
                    filter.update({"_id": 0})
                for x in self.collection.find({}, filter, batch_size=batch_size):
                    yield tuple([x.get(field) for field in out_field])
        else:
            if out_field:
                for x in self.collection.aggregate(pipeline, allowDiskUse=True, batchSize=batch_size):
                    yield tuple([x.get(field) for field in out_field])
            else:
                for x in self.collection.aggregate(pipeline, allowDiskUse=True, batchSize=batch_size):
                    yield x

    def aggregate(self, db_collect, pipeline):
        self.switch_db_collection(db_collect)
        return self.collection.aggregate(pipeline, allowDiskUse=True)

    def insert_one_dict(self, db_collect, data_dict):
        self.switch_db_collection(db_collect)
        self.collection.insert_one(data_dict)

    def count(self,db_collect, filter=None):
        self.switch_db_collection(db_collect)
        return self.collection.count(filter=filter)

    def insert_many_dict(self, db_collect, data_dict_list):
        self.switch_db_collection(db_collect)
        self.collection.insert_many(data_dict_list)

    def insert_one_tupe(self, db_collect, data_tupe, fields):
        self.switch_db_collection(db_collect)
        self.collection.insert_one(dict(zip(fields, data_tupe)))

    def insert_many_tupe(self, db_collect, data_tupe_list, fields):
        self.switch_db_collection(db_collect)
        self.collection.insert_many([dict(zip(fields, data_tupe))for data_tupe in data_tupe_list])

    def rename_collection(self, old_db_collection, new_db_collection):
        self.switch_db_collection(old_db_collection)
        self.collection.rename(new_db_collection[1])

    def drop_db_collect(self, db_collect):
        self.client[db_collect[0]].drop_collection(db_collect[1])

    def load_file_to_db(self, filename, db_collect, fields_tupe, column_index_list=None, sep="\t", buffer_size=64, attach_dict=None):
        cache = []
        if attach_dict:
            safe_attach_dict = {}
            for key in attach_dict.keys():
                if key in fields_tupe:
                    safe_attach_dict["_" + key] = attach_dict[key]
                else:
                    safe_attach_dict[key] = attach_dict[key]
        for line in open(filename):
            line = line.strip("\n").split(sep)
            if column_index_list:
                tmp_line=[]
                for item_index in column_index_list:
                    tmp_line.append(line[item_index])
                line = tmp_line
            date = dict(zip(fields_tupe, line))
            if attach_dict and safe_attach_dict:
                date.update(safe_attach_dict)
            cache.append(date)
            if len(cache) == buffer_size:
                self.insert_many_dict(db_collect, data_dict_list=cache)
                cache = []
        if cache:
            self.insert_many_dict(db_collect, data_dict_list=cache)

    def date_tuple_to_db(self, date_tuple_list, db_collect, fields_tupe, buffer_size=64,
                         attach_dict=None, show_pbar=False, pbar_name=None):
        cache = []
        if attach_dict:
            safe_attach_dict = {}
            for key in attach_dict.keys():
                if key in fields_tupe:
                    safe_attach_dict["_" + key] = attach_dict[key]
                else:
                    safe_attach_dict[key] = attach_dict[key]
        if show_pbar:
            for line_tupe in tqdm(date_tuple_list, desc=pbar_name):
                data = dict(zip(fields_tupe, line_tupe))
                if safe_attach_dict:
                    data.update(safe_attach_dict)
                cache.append(data)
                if len(cache) == buffer_size:
                    self.insert_many_dict(db_collect, data_dict_list=cache)
                    cache = []
        else:
            for line_tupe in date_tuple_list:
                data = dict(zip(fields_tupe, line_tupe))
                if safe_attach_dict:
                    data.update(safe_attach_dict)
                cache.append(data)
                if len(cache) == buffer_size:
                    self.insert_many_dict(db_collect, data_dict_list=cache)
                    cache = []
        if cache:
            self.insert_many_dict(db_collect, data_dict_list=cache)

    def __enter__(self):
        return self

    def __exit__(self, Type, value, traceback):
        self.client.close()
