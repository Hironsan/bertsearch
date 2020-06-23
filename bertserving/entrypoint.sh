#!/bin/sh
bert-serving-start -num_worker=1 -max_seq_len=256 -model_dir /model
