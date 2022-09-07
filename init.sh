#!/bin/bash

make_link() {
    if [ -e "$PWD/$1" ]; then
        return
    fi
    ln -s "$PWD/config/$1" "$1"
}

make_link ".editorconfig"
make_link ".flake8"
make_link "pyproject.toml"