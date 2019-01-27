# Deep Learning playground
This repository compiles different challenges for deep learning enthusiasts. It was initially dedicated to Udacity scholars from the Deep Learning nanodegree.

Diving further into the different topics of the course and notebook exercises from the nanodegree [repo](https://github.com/frgfm/deep-learning-v2-pytorch), you can find the following exercises for each lesson.

### Neural Network building blocks
Create the building blocks for your own MLP in numpy by completing two challenges:
- Feed-forward MLP ([notebook](https://github.com/frgfm/udacity-dl-exercises/blob/master/nn-basics/mlp_basics.ipynb))
- Full MLP back-propagation ([notebook](https://github.com/frgfm/udacity-dl-exercises/blob/master/nn-basics/full_mlp.ipynb))

### Convolutional neural networks

Implementing convolutional layers as part of your layer portfolio with numpy by completing two challenges:

- Convolutional layers (being finalized)
- Layer activation visualization (coming soon)

### Next upcoming challenges
- Optimizers
- Regularization
- Style Transfer
- Recurrent Neural Networks
- Generative Adversarial Networks
- Deep Reinforcement Learning

## Requirements
The numpy and matplotlib packages are required to properly use the repo.
Tested on the following version:

```python
import sys
import numpy, matplotlib
print('Python %s' % '.'.join(map(str, sys.version_info[:3])))
print(f'Numpy {numpy.__version__}, Matplotlib {matplotlib.__version__}')
```
```console
Python 3.6.5
Numpy 1.15.4, Matplotlib 2.2.3
```


## How to use it
Each lesson has a folder with a folders and other modules. The notebook will contain all the instructions.
Fork this repo to complete the exercises, and please notify the author of potential bugs/issues

### Completing an exercise
Run your jupyter notebook server in the same environment you installed the previously mentioned requirements.
If you are using Anaconda distribution, open your terminal (Linux/MacOS) or Anaconda prompt (Windows) and run:
```bash
jupyter notebook
```
Now navigate to the corresponding folder and follow the instructions of the notebook.


### Submitting a request / Reporting an issue
If you wish to submit a request or report an issue, go to the [Issues section](https://github.com/frgfm/udacity-dl-exercises/issues), and create a "New issue".

Regarding issues, use the following format for the title:
```
[Lesson #] Your Issue name
```
Example: [Lesson 2] Adding more instructions for the layer exercise
and these guidelines for the comment:
- Ensure you already have restart your kernel before reporting an issue
- Specify your setup (OS, OS version, Python version, requirements' versions)
- Format and specify the part of the code that is an issue
- Format and specify the error/issue that you encounter
- If relevant, explain what you have already tried to resolve the issue


Regarding requests, use the following title format:
```
[Request] Your request name
```
Example: [Request] Creating an exercise illustrating dropout


## TODO
- [x] NN Basics
- [ ] CNN
- [ ] Optimizers
- [ ] Regularization
- [ ] Reinforcement Learning
- [ ] GANs
