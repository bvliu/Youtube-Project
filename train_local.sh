#!/bin/bash

MODEL_DIR=/Users/Brandon/development/youtube/models
python youtube-8m/train.py \
--train_data_pattern='features/video_level_train/train*.tfrecord' \
--model=LogisticModel \
--train_dir=$MODEL_DIR/video_level_logistic_model
