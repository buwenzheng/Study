# !/usr/bin/env python
# -*- coding: utf-8 -*-

# Pollow
from PIL import Image

im = Image.open('test.jpg')

w, h = im.size

print('Original image size: %s%s' % (w, h))

# 缩放到50%
im.thumbnail((w//2, h//2))

print('Original image size: %s%s' % (w//2, h//2))

# 将缩放后的图片用jpeg的格式保存
im.save('thumbnail.jpg', 'jpeg')

print('-------------------')

