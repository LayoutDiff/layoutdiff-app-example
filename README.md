# LayoutDiff Demo project

A Flutter project to demonstrate how to use the LayoutDiff. Feel free to create Pull Requests with layout changes to see it working.

## Dashboard Credentials

You can see changes to be approved on https://app.layoutdiff.com/ using the below account:

username: layoutdiffdemo

password: Example01

## Run tests

To run the tests, you will need install flutter sdk and launch a device emulator.

[How to Install Flutter](https://flutter.dev/docs/get-started/install)

Execute below command to run flutter integration tests
`flutter drive --driver=test_driver/app_test.dart --target=test_driver/app.dart`

## Taking screenshots
You can see an example how to take screenshots on integration tests on [test_driver/app_test.dart](https://github.com/LayoutDiff/layoutdiff-app-example/blob/master/test_driver/app_test.dart)

## How to send the screenshots with layout changes to demo project

Open a bash on root of this project and execute: 

```
export GITHUB_SHA=$( git log | grep -oP 'commit \K[a-f0-9]*' | head -1)  # This line isn't necessary in a github action
sh send_screenshots.sh
```
