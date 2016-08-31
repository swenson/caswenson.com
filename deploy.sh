#!/bin/bash

aws s3 sync docs/ s3://caswenson.com/ --exclude '20*' --exclude about --exclude archive --exclude contact --exclude feed --exclude mc --exclude rss --exclude speaking --region us-west-2 --acl public-read --content-disposition inline
aws s3 sync docs s3://caswenson.com/ --exclude '*' --include '20*' --include about --include archive --include contact --include feed --include mc --include rss --include speaking --region us-west-2 --acl public-read --content-type text/html
