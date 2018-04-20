# import os
#
# base = os.path.join(os.path.abspath(os.curdir), 'data')
# print(base)
from hashlib import md5, sha1, sha224, sha256, sha384, sha512
from pprint import pprint

# hash_funcs = [md5, sha1, sha224, sha256, sha384, sha512]
#
#
# def hash_show(s):
#     result = []
#     for func in hash_funcs:
#         s_hash_obj = func(s)
#         s_hash_hex = s_hash_obj.hexdigest()
#         result.append((s_hash_obj.name, s_hash_hex,  len(s_hash_hex)))
#     return result
#
#
# if __name__ == '__main__':
#     s = 'hello python'
#     rs = hash_show(s)
#     pprint(rs)

# import tensorflow as tf
#
#
# img = tf.constant(value=[[[[1],[2],[3],[4]],[[1],[2],[3],[4]],[[1],[2],[3],[4]],[[1],[2],[3],[4]]]],dtype=tf.float32)
# img = tf.concat(values=[img,img],axis=3)
# filter = tf.constant(value=1, shape=[3,3,2,5], dtype=tf.float32)
# out_img1 = tf.nn.atrous_conv2d(value=img, filters=filter, rate=1, padding='SAME')
# out_img2 = tf.nn.atrous_conv2d(value=img, filters=filter, rate=1, padding='VALID')
# out_img3 = tf.nn.atrous_conv2d(value=img, filters=filter, rate=2, padding='SAME')
#
# #error
# #out_img4 = tf.nn.atrous_conv2d(value=img, filters=filter, rate=2, padding='VALID')
#
# with tf.Session() as sess:
#     print(img)
#
#     print('rate=1, SAME mode result:')
#     print(sess.run(out_img1))
#
#     print('rate=1, VALID mode result:')
#     print(sess.run(out_img2))
#
#     print( 'rate=2, SAME mode result:')
#     print(sess.run(out_img3))
#
#     # error
#     #print 'rate=2, VALID mode result:'
#     #print(sess.run(out_img4))
import tensorflow as tf
