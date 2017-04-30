# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import tensorflow as tf

from IPython.display import YouTubeVideo

video_lvl_record = "/Users/brandon/development/youtube/features/video_level_test/test2S.tfrecord"
frame_lvl_record = "/Users/brandon/development/youtube/features/frame_level_train/traineA.tfrecord"
# For each example in the record:
# "video_id": unique id for the video, in train set it is a Youtube video id, and in test/validation they are anonymized
# "labels": list of labels of that video
# "mean_rgb": float array of length 1024
# "mean_audio": float array of length 128

video_lvl_train = "/Users/brandon/development/youtube/features/video_level_train"
frame_lvl_train = "/Users/brandon/development/youtube/features/frame_level_train"

vid_ids = []
labels = []
mean_rgb = []
mean_audio = []

total = 0
for example in tf.python_io.tf_record_iterator(video_lvl_record):
    tf_example = tf.train.Example.FromString(example)

    vid_ids.append(tf_example.features.feature['video_id'].bytes_list.value[0].decode(encoding='UTF-8'))
    labels.append(tf_example.features.feature['labels'].int64_list.value)
    mean_rgb.append(tf_example.features.feature['mean_rgb'].float_list.value)
    mean_audio.append(tf_example.features.feature['mean_audio'].float_list.value)

print(total)

print('Number of videos in this tfrecord: ',len(mean_rgb)) # length of arbitrary list of mean_rgb, one per video
print('First video feature length',len(mean_rgb[0]))
print('First 20 features of the first youtube video (',vid_ids[0],')')
print(mean_rgb[0][:20])

print('mean_audio has length of: ')
print([len(x) for x in mean_audio][:5])
print('mean_rgb has length of: ')
print([len(x) for x in mean_rgb][:5])


def play_one_vid(record_name, video_index):
    return vid_ids[video_index]
    
# this worked on my local jupyter notebook, but doesn't show on kaggle kernels:
YouTubeVideo(play_one_vid(video_lvl_record, 7))


# feat_rgb = []
# feat_audio = []

# for example in tf.python_io.tf_record_iterator(frame_lvl_record):        
#     tf_seq_example = tf.train.SequenceExample.FromString(example)
#     n_frames = len(tf_seq_example.feature_lists.feature_list['audio'].feature)
#     sess = tf.InteractiveSession()
#     rgb_frame = []
#     audio_frame = []
#     # iterate through frames
#     for i in range(n_frames):
#         rgb_frame.append(tf.cast(tf.decode_raw(
#                 tf_seq_example.feature_lists.feature_list['rgb'].feature[i].bytes_list.value[0],tf.uint8)
#                        ,tf.float32).eval())
#         audio_frame.append(tf.cast(tf.decode_raw(
#                 tf_seq_example.feature_lists.feature_list['audio'].feature[i].bytes_list.value[0],tf.uint8)
#                        ,tf.float32).eval())
        
        
#     sess.close()
#     feat_rgb.append(rgb_frame)
#     feat_audio.append(audio_frame)
#     break

# print('The first video has %d frames' %len(feat_rgb[0]))

