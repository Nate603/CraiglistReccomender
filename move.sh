#!/bin/bash
fileName=$1
mkdir "$fileName"
mv NoDuplicates.csv "$fileName"
mv initialRecommendations.csv "$fileName"
