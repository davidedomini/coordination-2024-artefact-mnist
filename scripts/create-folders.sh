#!/bin/sh
for folder in 'charts' 'data'; do
  mkdir -p "/experiment/$folder"
  chmod 777 "/experiment/$folder"
done
