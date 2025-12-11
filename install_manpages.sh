#!/usr/bin/env bash
# install_man.sh
set -e
mkdir -p /usr/local/share/man/man1/
cp hg_license_cli.1 /usr/local/share/man/man1/
mandb || true
echo "man page installed. Try: man hg_license_cli"
