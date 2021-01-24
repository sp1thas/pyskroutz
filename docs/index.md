# Welcome to pyskroutz documentation

A Python client for Skroutz API.

![Main photo](https://i.imgur.com/98Ddr0h.jpg)
*Ermoupoli, Syros, Greece 2020*

This a python client that let's you interact with Skroutz API. Every response is validated and is a pydantic object.

!!! info
    Make sure that you have a pair of client id and client secret.

## Installation

```shell
pip install pyskroutz
```

## Usage

```python
from pyskroutz.client import SkroutzClient
client = SkroutzClient('<client-id>', '<client-secret>')
first_category = client.categories.list(per=1)
```
