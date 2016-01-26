#!/usr/bin/python
# coding=utf-8
#
# 179770346@qq.com / binfeix.li@intel.com
# 2016/1/26 v0.1
#   merge multiply snapshot into one

import Image, ImageChops

#--------------------------------------------------------------------------------------------------
def diff_image(img1, img2):
  return ImageChops.lighter(img1, img2)

#--------------------------------------------------------------------------------------------------
def main():
  img1 = Image.open("test/1.png")
  for index in range(1, 100):
    index += 1
    img2 = Image.open("test/%d.png" % index)
    img1 = diff_image(img1, img2)
  img1.save("test.png")

if __name__ == '__main__':
  main()