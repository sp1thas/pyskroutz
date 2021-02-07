# Welcome to pyskroutz documentation

A Python client for [Skroutz API](https://developer.skroutz.gr/api/v3/).

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
import pyskroutz
client = pyskroutz.client('<client-id>', '<client-secret>')
first_category = pyskroutz.categories(client).get(per=1).execute()
```
