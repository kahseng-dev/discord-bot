#!/usr/bin/env bash
# exit on error
set -o errexit

STORAGE_DIR=/opt/render/project/.render
FILE_NAME=./google-chrome-stable_current_amd64.deb

if [[ ! -d $STORAGE_DIR/chrome ]]; then
  echo "[BUILD] Downloading Chrome..."
  mkdir -p $STORAGE_DIR/chrome
  cd $STORAGE_DIR/chrome
  wget -P ./ https://dl.google.com/linux/direct/$FILE_NAME
  dpkg -x $FILE_NAME $STORAGE_DIR/chrome
  rm $FILE_NAME
  cd $HOME/project/src
else
  echo "[BUILD] Using Chrome from cache..."
fi

echo "[BUILD] Running pip install requirements..."
pip install -r requirements.txt