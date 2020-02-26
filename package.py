# -*- coding: utf-8 -*-

name = 'turret_lib'

version = '1.1.17'

authors = ['ben.skinner',
           'daniel.flood'
           ]

requires = ['libzmq-4',
            'boost']

build_requires = [
    'cmake-3.2',
]

variants = []


def commands():
    env.LIBTURRET_ROOT.set("{this.root}")
    env.LD_LIBRARY_PATH.append('{root}/lib')
    env.PATH.append('{root}/lib')
    env.TURRET_RETRIES.set("1")
