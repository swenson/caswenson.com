#!/bin/bash

aws s3 sync public/ s3://caswenson.com/ --region us-west-2 --acl public-read