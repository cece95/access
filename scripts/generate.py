# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#

import sys

from access.preprocessors import get_preprocessors
from access.resources.prepare import prepare_models
from access.simplifiers import get_fairseq_simplifier, get_preprocessed_simplifier
from access.text import word_tokenize
from access.utils.helpers import yield_lines, write_lines, get_temp_filepath, mute

import os

config_sets = {1: {
		'LengthRatioPreprocessor': {'target_ratio': 0.95},
		'LevenshteinPreprocessor': {'target_ratio': 0.75},
		'WordRankRatioPreprocessor': {'target_ratio': 0.75},
		'SentencePiecePreprocessor': {'vocab_size': 10000},
	}, 2: {
		'LengthRatioPreprocessor': {'target_ratio': 0.95},
		'LevenshteinPreprocessor': {'target_ratio': 0.75},
		'WordRankRatioPreprocessor': {'target_ratio': 0.85},
		'SentencePiecePreprocessor': {'vocab_size': 10000},
	}, 3: {
		'LengthRatioPreprocessor': {'target_ratio': 0.95},
		'LevenshteinPreprocessor': {'target_ratio': 0.75},
		'WordRankRatioPreprocessor': {'target_ratio': 0.95},
		'SentencePiecePreprocessor': {'vocab_size': 10000},
	}, 4: {
		'LengthRatioPreprocessor': {'target_ratio': 0.95},
		'LevenshteinPreprocessor': {'target_ratio': 0.85},
		'WordRankRatioPreprocessor': {'target_ratio': 0.95},
		'SentencePiecePreprocessor': {'vocab_size': 10000},
	}, 5: {
		'LengthRatioPreprocessor': {'target_ratio': 0.95},
		'LevenshteinPreprocessor': {'target_ratio': 0.95},
		'WordRankRatioPreprocessor': {'target_ratio': 0.95},
		'SentencePiecePreprocessor': {'vocab_size': 10000},
	}, 6: {
		'LengthRatioPreprocessor': {'target_ratio': 0.95},
		'LevenshteinPreprocessor': {'target_ratio': 0.6},
		'WordRankRatioPreprocessor': {'target_ratio': 0.6},
		'SentencePiecePreprocessor': {'vocab_size': 10000},
	}, 7: {
		'LengthRatioPreprocessor': {'target_ratio': 0.95},
		'LevenshteinPreprocessor': {'target_ratio': 0.4},
		'WordRankRatioPreprocessor': {'target_ratio': 0.4},
		'SentencePiecePreprocessor': {'vocab_size': 10000},
	}} 


if __name__ == '__main__':
	# Usage: python generate.py < my_file.complex
	# Read from stdin
	filename = sys.argv[1]
	# Load best model
	if not os.path.exists('headlines_simplified'):
	    os.mkdir('headlines_simplified')
	#print(len(sys.argv))    
	if len(sys.argv) > 3:
	    c = int(sys.argv[3])
	    config_range = [c]
	else:
	    config_range = range(1,len(config_sets) + 1,1)
	for config in config_range:
		best_model_dir = prepare_models(sys.argv[2])
		print("BEST MODEL: {}".format(best_model_dir))
		recommended_preprocessors_kwargs = config_sets[config]
		preprocessors = get_preprocessors(recommended_preprocessors_kwargs)
		simplifier = get_fairseq_simplifier(best_model_dir, train=False, beam=8)
		simplifier = get_preprocessed_simplifier(simplifier, preprocessors=preprocessors)
		print(simplifier)
		with open(filename, 'r', encoding='utf-8') as i_f, open('headlines_simplified/{}_config_{}.txt'.format(filename.split('/')[-1], config), 'w', encoding='utf-8') as o_f:
			for line in i_f:
				#remove journal name from headline
				#line = ' '.join(line.split('-')[:-1])
				print(line)
				source_filepath = get_temp_filepath()
				write_lines([word_tokenize(line)], source_filepath)
				print(1)
				# Simplify
				pred_filepath = get_temp_filepath()
				print(1.8)
				with mute():
				    print(1.999)
				    simplifier(source_filepath, pred_filepath)
				    print(2)
				print(3)
				for o_line in yield_lines(pred_filepath):
					print(o_line)
					o_f.write(o_line+"\n")
				print(4)
			
