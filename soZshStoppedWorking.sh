#!/bin/bash

omz update;

chsh -s $(which zsh);

echo "now log off and log back in so that the userprofile changes apply. Restarting the shell won't do it. Actually log out.";