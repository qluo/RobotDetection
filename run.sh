#!/bin/bash

python ~/PycharmProjects/RobotDetection/DataReader.py train.csv bids.csv bid

python ~/PycharmProjects/RobotDetection/DataReader.py train.csv bids.csv train

python ~/PycharmProjects/RobotDetection/DataReader.py train.csv bids.csv test