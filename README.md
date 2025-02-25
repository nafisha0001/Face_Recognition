# Face Recognition using AWS Rekognition

## Overview

This project performs face recognition using AWS Rekognition. The goal is to check whether a person in an input image has any previous record in a database of stored images on Amazon S3. The compare_faces method is used to compare the input face with stored images.

## Features

* Uses AWS Rekognition for face comparison
* Fetches stored images from an S3 bucket
* Compares input images against stored records
* Runs efficiently using AWS Lambda

## How It Works

1. The input image is uploaded to an S3 bucket.
2. It compares the input image with each stored image using AWS Rekognition's compare_faces method.
3. If a match is found, it returns the matched image name along with a confidence score.
4. If no match is found, it returns "no result found".

## Prerequisites

AWS account with Rekognition, S3 and Lambda services enabled.
