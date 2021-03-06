# zcan
A protocol adapter for Zehnder ComfoAir Q series devices with CAN bus interface. It reads and interprets CAN messages from a USBtin CAN adapter (https://amzn.to/2KiAR2U) and sends metrics to an Influxdb instance.

## Installation

### Preparation

Have python 3 installed and run the following to install pybuilder (build tool)
  
    pip3 install pybuilder
  
### build the project

Go to the project root dir and execute

    pyb install_dependencies
    pyb
  
### Install locally

    pyb install
  

## Execution

### normal operation

Start the application as a daemon writing known metrics to influxdb.

    zcan run
  
To run the app in the backround

    nohup zcan run &
  
### print out CAN messages

    zcan show --all --debug
