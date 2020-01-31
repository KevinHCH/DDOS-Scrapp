#!/usr/bin/bash
#Instala dependencias por PIP para que funcione
#Update de los repos de Centos
yum install centos-release-scl
yum install https://centos7.iuscommunity.org/ius-release.rpm
yum update
#Ultima version estable de los repos de Centos + PIP
yum install -y python36u python36u-libs python36u-devel python36u-pip

pip3 install cloudscraper
pip3 install beautifulsoup4
