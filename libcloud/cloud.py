#!/usr/bin/env python3

from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
import os
import json

with open(os.path.expanduser('~/.profitbricks.json'), encoding='utf-8') as data_file:
    data = json.loads(data_file.read())

cls = get_driver(Provider.PROFIT_BRICKS)
driver = cls(
    data.get('username', ''),
    data.get('password', ''),
    region='pb-test',
)

for size in driver.list_sizes():
    print('size={}'.format(size))

for image in driver.list_images():
    print('image={}'.format(image))
