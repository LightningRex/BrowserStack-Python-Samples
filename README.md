# BrowserStack Interactive Debugging (Python)

This repository contains minimal Python examples to start an interactive debugging session on BrowserStack using the BrowserStack SDK.

## Project Structure

```
.
├── android/
│   ├── Minimal Android example
│   └── browserstack.yml
├── ios/
│   ├── Minimal iOS example
│   └── browserstack.yml
└── README.md
```

## Prerequisites

- Python 3.x
- BrowserStack account
- BrowserStack SDK

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Update the `browserstack.yml` file with your BrowserStack credentials and desired device/app configuration.

## Run

### Android

```bash
cd android
browserstack-sdk python android_sample.py
```

### iOS

```bash
cd ios
browserstack-sdk python ios_sample.py
```

## Purpose

These examples are intended as a minimal starting point for:
- Launching interactive App Automate sessions
- Reproducing issues on BrowserStack
- Debugging Appium tests with the BrowserStack SDK

Feel free to modify the scripts to suit your testing requirements.