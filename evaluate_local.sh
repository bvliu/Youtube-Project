#!/bin/bash

MODEL_DIR=/Users/Brandon/development/youtube/models
python youtube-8m/eval.py \
--eval_data_pattern='features/video_level_validate/validate*.tfrecord' \
--model=LogisticModel \
--train_dir=$MODEL_DIR/video_level_logistic_model \
--run_once=True
