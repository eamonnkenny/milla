#!/usr/bin/env bash

# Copyright 2013 Eamonn Kenny 

workingDir=`dirname $0`
# Set the paths to the binaries and scripts needed
KALDI_ROOT=${workingDir}/../build/kaldi_trunk
export PATH=$KALDI_ROOT/src/onlinebin:$KALDI_ROOT/src/bin:$PATH
export LD_LIBRARY_PATH=${workingDir}/../build/kaldi_trunk/src/lib

data_file=${workingDir}/voxforge-for-kaldi

# Change this to "tri2a" if you like to test using a ML-trained model
ac_model_type=tri3b_fmmi_b
#ac_model_type=tri2a

# Alignments and decoding results are saved in this directory(simulated decoding only)
decode_dir="./work"

ac_model=${data_file}/models/$ac_model_type

/opt/kaldi/bin/online-gmm-decode-faster $ac_model/model $ac_model/HCLG.fst $ac_model/words.txt '1:2:3:4:5' $ac_model/matrix
#./online-gmm-decode-faster $ac_model/model $ac_model/HCLG.fst $ac_model/words.txt '1:2:3:4:5'
