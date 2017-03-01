# lj-parspace

[![Build Status](https://travis-ci.org/mohebifar/lj-parspace.svg?branch=master)](https://travis-ci.org/mohebifar/lj-parspace)
[![codecov.io](https://codecov.io/github/hbetts/orbitalpy/coverage.svg?branch=master)](https://codecov.io/github/mohebifar/lj-parspace?branch=master)

Work in progress...

## Installation

Clone the repository and cd to the created directory. Install the dependencies using pip:

```
sudo pip install -r requirements.txt
```

You need to create a configuration file in `~/.ljparspace.cfg` with the following format:

```cfg
[DEFAULT]
postg_path = /path/to/postg

```

## Usage

### Validation
You can use the `bin/validate.py` script to validate the LJ parameters by giving a wave function and its Gromacs topology file.

[Check out the examples](https://github.com/mohebifar/lj-parspace/tree/master/examples).
## Contributing

Read [CONTRIBUTING](CONTRIBUTING.md).
