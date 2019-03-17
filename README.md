# SplunkHecDataGen

## Introduction
This is a small project to get data into your splunk http event collector for testing and learning purposes with docker. At this point the container sends telemetry data with the sourcetype "_json" like:
```
{
  "Value":-0.428985120998
}
```
The generated values look like a sinus curve. Other types of data: TBD.

## Preparations
Set up your splunk server and create a token for your http event collector.
Install docker: https://docs.docker.com/install/

## On Windows
Edit the dockerBuildRunAndLog.bat file. 
Change  "<url>"  to the url of your splunk http event collector url.
Also change  "<token>" with your splunk token.
### Optional:
There are optional environment variable that you can add to the docker run command in the dockerBuildRunAndLog.bat file.
#### Key 
KEY: This changes "Value" to the value of your key.
Example:
docker run --name splunk-hec-datagen --network host -e URL=<url> -e TOKEN=<token>  -e KEY="Temperature" splunk-hec-datagen
In this case the resulting message will look like this:
```
{
  "Temperature":-0.428985120998
}
```
#### TBD

## On Arm
TBD