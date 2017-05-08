# Brandon Liu - HackCville - 2016

import keras
from keras.models import Sequential
from keras.utils import to_categorical
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD

import tensorflow as tf
from tensorflow import gfile

import argparse
import os.path
import sys
import time

import numpy as np

frame_train_dir = 'features/frame_level_train'     
video_train_dir = 'features/video_level_train'
frame_validate_dir = 'features/frame_level_validate'     
video_validate_dir = 'features/video_level_validate'
train_file = "train*.tfrecord"
validate_file = "validate*.tfrecord"
epochs = 500
batch_size = 100

VIDEO LEVEL FEATURES:
- INPUT:

def read_and_decode(filename_queue):
	reader = tf.TFRecordReader()
	_, serialized_example = reader.read(filename_queue)
	features = tf.parse_single_example(
		serialized_example,
		features={
		'video_id': tf.FixedLenFeature([], tf.string),
		'labels': tf.VarLenFeature(tf.int64)
		})	
	video_id = tf.cast(features['video_id'], tf.string)
	labels = tf.cast(features['labels'], tf.int64)
	return video_id, labels

def inputs(train, batch_size, num_epochs):
	if not num_epochs: num_epochs = None
	filenames = gfile.Glob(video_train_dir + "/train*.tfrecord")
	print(filenames)

	filename_queue = tf.train.string_input_producer(filenames)
	video_id, label = read_and_decode(filename_queue)

	video_ids, labels = tf.train.shuffle_batch(
		[video_id, label], batch_size=batch_size, num_threads=2,
		capacity=1000 + 3 * batch_size,
		min_after_dequeue=1000)

	return video_ids, labels

def run_training():
	sess = tf.InteractiveSession()
	train_video_ids, train_labels = inputs(True, 5000, 10)
	tf.train.start_queue_runners(sess)
	train_video_ids = train_video_ids.eval()
	train_labels = train_labels.eval()
	print(len(train_video_ids))
	print(len(train_labels))
	print(train_video_ids)
	print(train_labels)

if __name__ == '__main__':
	# run_training()