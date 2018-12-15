# Advanced exercises for Udacity Deep Learning scholars
This repository compiles different exercises for scholars of the Deep Learning nanodegree from Udacity that want to go the extra mile.

Diving further into the different topics of the course and notebook exercises from the nanodegree [repo](https://github.com/frgfm/deep-learning-v2-pytorch), you can find the following exercises for each lesson:

### Lesson 2 (Neural networks)
Create the building blocks for your own MLP in numpy by completing two challenges:
- Feed-forward MLP ([notebook](https://github.com/frgfm/udacity-dl-exercises/blob/master/2-nn/mlp_basics.ipynb))
- Full MLP backpropagation ([notebook](https://github.com/frgfm/udacity-dl-exercises/blob/master/2-nn/full_mlp.ipynb))

### Other lessons (coming soon)
- Lesson 4 (PyTorch)
- Lesson 5 (Convolutional Neural Network)
- Lesson 6 (Style Transfer)
- Lesson 7 (Recurrent Neural Network)
- Lesson 8 (Sentiment Analysis)

## Requirements
The numpy, matplotlib, torch and torchvision packages are required to properly use the repo.
Tested on the following version:
```python
import sys
import numpy, matplotlib, torch, torchvision
print('Python %s' % '.'.join(map(str, sys.version_info[:3])))
print(f'Numpy {numpy.__version__}, Matplotlib {matplotlib.__version__}, PyTorch {torch.__version__}, Torchvision {torchvision.__version__}')
```
```console
Python 3.6.5
Numpy 1.15.4, Matplotlib 2.2.3, PyTorch 1.0.0, Torchvision 0.2.1
```

Please refer to PyTorch/Torchvision installation [instructions](https://pytorch.org/get-started/locally/) if you haven't installed them yet.


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
- [x] Lesson 2
- [ ] Lesson 4
- [ ] Lesson 5
- [ ] Lesson 6
- [ ] Lesson 7
- [ ] Lesson 8
