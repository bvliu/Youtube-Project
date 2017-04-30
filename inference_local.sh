#!/bin/bash

MODEL_DIR=/tmp/yt8m

python youtube-8m/inference.py \
--output_file=$MODEL_DIR/video_level_logistic_model/predictions.csv \
--input_data_pattern='features/video_level_test/test2S.tfrecord' \
--train_dir=$MODEL_DIR/video_level_logistic_model
