#! /usr/bin/env python3.4
# -*- coding: utf-8 -*-
# config.py - configration for crysadm web and redis server
__author__ = 'powergx'

# Redis����������
class RedisConfig():
    def __init__(self, host, port, db, password=None):
        self.host = host
        self.port = port
        self.db = db
        self.password = password

# Crysadm ����
class Config(object):
    DEBUG = False  #����ģʽ
    TESTING = False  #����ģʽ
    DATABASE_URI = ''  #���ݿ�����
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}  #����ĺ�׺��
    SESSION_TYPE = 'memcached'  #��������
    SECRET_KEY = '7e30485a-dd01-11e4-8abd-10ddb199c373'  #��ȫ��Կ
    REDIS_CONF = RedisConfig(host='127.0.0.1', port=6379, db=0)  #Redis����������
    PASSWORD_PREFIX = "08b3db21-d120-11e4-9ttd-10ddb199c373"  #����ǰ׺
    ENCRYPT_PWD_URL = None  #ģʽ
    SERVER_IP = '0.0.0.0'  #������IP
    SERVER_PORT = 5000  #�˿�

# ��������ʱ����
class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

# ����������ģʽ
class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False

# ����ģʽ
class TestingConfig(Config):
    DEBUG = True
    TESTING = True