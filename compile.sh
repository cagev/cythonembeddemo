#!/bin/bash

export PATH=`pwd`/../bin/python/bin:$PATH
export LD_LIBRARY_PATH=`pwd`/../bin/python/lib
export PYTHONSTARTUP=`pwd`/../bin/python/lib

echo $PATH 
python3 -V 

rm -rf *.so 
rm -rf engine.cpp 
CPPFLAGS=" -std=c++17 -I../opt/klog/include -Icore -Imods -Ipythran/pythran -Ixs/include -I../opt/asio-1.18.2/include -I../libs/buscli/include -I../libs/  -I../opt/yaml-cpp/include -I../opt/spdlog-1.8.5/include -I../libs/mdagent/include -I../opt/knet/include"
export CPPFLAGS=$CPPFLAGS" -I../opt/fmt-7.1.3/include -I.."
echo $CPPFLAGS
python3 setup.py build_ext --inplace 
