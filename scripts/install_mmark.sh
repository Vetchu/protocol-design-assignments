#!/bin/bash

wget https://github.com/mmarkdown/mmark/releases/download/v2.2.25/mmark_2.2.25_linux_amd64.tgz
tar -xzf mmark_2.2.25_linux_amd64.tgz
mv mmark bin/mmark
rm -f mmark_2.2.25_linux_amd64.tgz