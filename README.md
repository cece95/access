# Controllable Sentence Simplification

The repository [ACCESS](https://github.com/facebookresearch/access) contains the original implementation of the ACCESS model (**A**udien**C**e-**CE**ntric **S**entence **S**implification)  presented in [Controllable Sentence Simplification](https://arxiv.org/abs/1910.02677).

The version that was used at submission time is on branch [submission](https://github.com/facebookresearch/access/tree/submission).

This fork contains the modified code to run the pretrained model on the **Headlines** Dataset and to perform transfer learning on it aswell.
This fork also includes as default `sacrebleu 1.4.5` as dependency instead of the default `sacrebleu 1.4.10` to fix a compatibility issue with easse

## Getting Started

### Dependencies

* Python 3.6

### Installing

```
git clone git@github.com:facebookresearch/access.git
cd access
pip install -e .
pip install --force-reinstall easse@git+git://github.com/cece95/easse.git
pip install --force-reinstall fairseq@git+https://github.com/louismartin/fairseq.git@controllable-sentence-simplification
```

### How to use

Evaluate the pretrained model on WikiLarge:
```
python scripts/evaluate.py
```

Simplify text with the pretrained model
```
python scripts/generate.py < my_file.complex
```

Train a model
```
python scripts/train.py
```

## Pretrained model

The fairseq checkpoint of our model with the best scores can be found [here](http://dl.fbaipublicfiles.com/access/best_model.tar.gz).
The model's output simplifications can be viewed on the [EASSE HTML report](http://htmlpreview.github.io/?https://github.com/facebookresearch/access/blob/master/system_output/easse_report.html).

## References

If you use this code, please cite:  
L. Martin, B. Sagot, E. De la Clergerie, A. Bordes, [*Controllable Sentence Simplification*](https://arxiv.org/abs/1910.02677)

## Author

If you have any question, please contact the author:
**Louis Martin** ([louismartincs@gmail.com](mailto:louismartincs@gmail.com))

## License

See the [LICENSE](LICENSE) file for more details.
