#!/usr/bin/env python
# coding=utf-8

import os
import argparse

def batch_name(work_dir, old_ext, new_ext):
    for filename in os.listdir(work_dir):
        splite_file = os.path.splitext(filename)
        file_ext = splite_file[1]
        if old_ext == file_ext:
            newfile = splite_file[0] + new_ext
            os.rename(
                os.path.join(work_dir, filename),
                os.path.join(work_dir, newfile)
            )


old_ext = '.c'
new_ext = '.py'
work_dir = './'

batch_name(work_dir, old_ext, new_ext)
