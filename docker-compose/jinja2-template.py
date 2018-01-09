#!/usr/bin/env python3
import os
import sys
import jinja2
from jinja2 import Environment, FileSystemLoader

image_dir = 'images'
image_filename = 'image_full_tag.txt'
docker_tags = {}
filenames = {}

def parse_cmdline():
    filenames["inputfile"] = sys.argv[1]
    filenames["outputfile"] = sys.argv[1].rsplit(".", 1 )[0]
    return filenames

def load_tags():
    for dirname in os.listdir(image_dir):
        if os.path.isdir(image_dir + "/" + dirname):
            with open(image_dir + "/" + dirname + "/" + image_filename, 'r') as file:
                docker_tags[dirname] = file.read().strip()
                file.close()
    return docker_tags

def write_template(filenames, docker_tags):
    print ("Using", image_dir + " to template",filenames["inputfile"] + " to",filenames["outputfile"])
    # Create the jinja2 environment.
    template = Environment(loader=FileSystemLoader('.'))
    with open(filenames["outputfile"], 'w') as file:
        print (template.get_template(filenames["inputfile"]).render(env=os.environ,images=docker_tags), file=file)
        file.close()

if __name__ == '__main__':
    write_template(parse_cmdline(),load_tags())
