# Google Contact Photo Upload

The standard Google contact export flow does not include the contact photo.

These scripts support uploading of contact photos. Photos can be fetched via Google Takeout.

This can be useful if moving contacts across Google accounts.

## Setup

* `virtualenv venv`
* `./venv/bin/pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`
    * As described in the [People API Python Quickstart](https://developers.google.com/people/quickstart/python)
* Export source contacts from [Google Takeout](https://takeout.google.com/settings/takeout)
* Upload vcf to destination account
* Move images from Takeout bundle to "contacts" subfolder here
* Configure a GCP project with access to the People API and scope `https://www.googleapis.com/auth/contacts`
    * Store Desktop credentials in this folder as `credentials.json`
* Run `./loop.sh`
    * Adjust the sleep setting as desired to circumvent rate limiting on your account

Enjoy!
