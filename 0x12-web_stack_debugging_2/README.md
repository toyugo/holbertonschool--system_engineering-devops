#!/usr/bin/env bash
# create a new shell with the user given in param and do the command whoami
su "$1" -s /bin/bash -c 'whoami'
