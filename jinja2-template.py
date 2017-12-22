#!/usr/bin/env python3
import os
import sys
import jinja2
from jinja2 import Environment, FileSystemLoader

image_dir = 'images'
image_filename = 'image_full_tag.txt'
docker_tags = {}

def load_tags():
    for dirname in os.listdir(image_dir):
        if os.path.isdir(image_dir + "/" + dirname):
            with open(image_dir + "/" + dirname + "/" + image_filename, 'r') as file:
                docker_tags[dirname] = file.read().strip()
                file.close()


def print_template():
    # Create the jinja2 environment.
    template = Environment(loader=FileSystemLoader('.'))
    print (template.get_template(sys.argv[1]).render(env=os.environ,images=docker_tags))

if __name__ == '__main__':
    load_tags()
    print_template()
