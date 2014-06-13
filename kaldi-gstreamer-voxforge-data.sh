#!/usr/bin/env bash

# Copyright 2013 Eamonn Kenny 

workingDir=../MILLA-eNTERFACE2014
# Set the paths to the binaries and scripts needed
KALDI_ROOT=${workingDir}/build/kaldi_trunk
export PATH=$KALDI_ROOT/src/onlinebin:$KALDI_ROOT/src/bin:$PATH
export LD_LIBRARY_PATH=${workingDir}/../build/kaldi_trunk/src/lib

data_file=./voxforge-for-kaldi

# Change this to "tri2a" if you like to test using a ML-trained model
ac_model_type=tri3b_fmmi_b
#ac_model_type=tri2a

# Alignments and decoding results are saved in this directory(simulated decoding only)
decode_dir="./work"

ac_model=${data_file}/models/$ac_model_type

GST_PLUGIN_PATH=$KALDI_ROOT/src/gst-plugin gst-launch-1.0 -q pulsesrc ! audioconvert ! audioresample ! onlinegmmdecodefaster model=$ac_model/model fst=$ac_model/HCLG.fst word-syms=$ac_model/words.txt silence-phones="1:2:3:4:5" lda-mat=$ac_model/matrix ! filesink location=/dev/stdout buffer-mode=2
