# SALONAI-FRONTEND

## Overview

This is the frontend for this project that will be used for the webApp version for now.  
A follow-up App will be soon to come which would fork this one 

*Please look at the following instrucitons bellow for those that work on the project*

## Installing Locally
```bash
npm install
npm run dev
```
* The first installs the dependencies
* The second will run the sample so you can see how it works.

## Installing NEW Dependencies

When you install a new dependency and want to save it with the exact version (to avoid the caret `^`), run:

```bash
npm install <dependency> --save --save-exact
```
### Other way of doing it
If you wish to not use the `--save --save-exact` simply run the following before you wish to install any future dependencies.
```bash
npm config set save-exact true
```
This means that you can simply stick with the `npm install...` for future, thus removing the `--save --save-exact` portion.

## Importance
In order for this to run on other machines cleanly we cannot allow for the machine once you install something to auto update the packages, hence why we need to do this

## Before Pushing to remote repo
In order to make the `package-lock.json` to function properly you need to run the following command. 
```bash
rm npm-shrinkwrap.json
npm shrinkwrap
```
shrinkwrap forces the environment to use the exact dependencies that each package needs. Thus making the same issue we have above redundant

### Note for your environment please do the following:
install npmvet
```bash
npm install npmvet -g 
```
Then run 
```bash
npmvet -r inlinetable
```
You should get a table in the `CI`
#### NOTE
*If you are getting an error please let me know and I can take a look at it and fix it*

## Files to Ignore
* node_modules
* .dist if your in vs code

# Future Updates
* Github workflows for AWS
* Updating UI
  * *(Look at React Three Fiber and Drei)*
* Implementing all of the old things I had 
  * Scribe-ocr.js
  * In-browser Whisper model `STT`
  * Look for new `TTS` model to use
  * distllBIOBERT integration & model training
  * Any other future UI improvements. 