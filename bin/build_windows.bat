@echo off

rd /s /q build

mkdir build
cd build

SET CPPZMQ_INCLUDE=C:/packages/pg/prod/cppzmq/4.6.1/include
SET LIBZMQ_INCLUDE_DIR=C:/packages/pg/prod/libzmq/4.3.2/include
SET LIBZMQ_LIB_DIR=C:/packages/pg/prod/libzmq/4.3.2/vs14_2015_x64/libzmq-v140-mt-4_3_2.lib

cmake -DZeroMQ_LIBRARY:STRING=%LIBZMQ_LIB_DIR% -DPC_LIBZMQ_INCLUDE_DIRS:STRING=%LIBZMQ_INCLUDE_DIR% -DCPPZMQ_INCLUDE:STRING=%CPPZMQ_INCLUDE% -DCMAKE_INSTALL_PREFIX="C:/packages/pg/prod/turret_lib/1.1.17" -G "Visual Studio 14 2015 Win64" ..
cmake --build . --config Release --target install -- /M:16

cd ..
