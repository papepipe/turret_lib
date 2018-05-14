# -*- coding: utf-8 -*-

name = 'zmq_client_cpp'

version = '0.0.1'

authors = [ 'ben.skinner' ]

requires = ['libzmq',
    'boost-1.55']

build_requires = [
    'cmake-3.2',
]

variants = [['platform-linux', 'arch-x86_64']]

def commands():
    env.ZMQ_CLIENT_INCLUDE.set("{root}/include")
    env.ZMQ_CLIENT_LIB.set("{root}/lib")
    #env.ZMQ_CLIENT_LIB.set("{root}/lib/libzmq_client_cpp.a")

    env.LD_LIBRARY_PATH.append('{root}/lib')
    env.USD_CACHE_LOCATION.set("/home/13109816/zmq/usd.zmqcache")
    env.LOOK_FILES_CACHE_LOCATION.set("/home/13109816/zmq/look_files.zmqcache")

    env.ZMQ_CLIENT_LOG_LEVEL.set("1")
