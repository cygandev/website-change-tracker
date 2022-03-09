# website-change-tracker
Website tracker sending out alerts by email when the website content has changed.  
For detailed project walk through and instructions please see my [blog](https://datastack.ch/posts/website-change-monitor/).

## run instructions

Clone repository and cd into the newly created directory.
```bash
git clone <this-repo>
cd website-change-tracker
```

The application expects some environment variables to be present.
They can be defined in env_file and are then set in the docker container during container start up.  
If you want to use a proxy for your requests to the tracked website set _USE_PROXY=1_. 

```bash
touch env_file
```

Replace the variables in env_file with your values.
```cmd
EMAIL="<GmailAccountAddress>@gmail.com"
PW_GMAIL="<MySuperSecretPassword>"
EMAIL_RECEIVER="email1@gm.com, email2@gmail.com"
URL="<UrlToMonitor>"
USE_PROXY=0
AWS_ACCESS_KEY_ID="<KeyId>"
AWS_SECRET_ACCESS_KEY="<Secret>"
```

Build a Docker image based on the instructions in the Dockerfile and start a container with the image.
Make sure to have the working directory set to where the Dockerfile is located in order for the __docker build__ command to work.
Assign the name __website-monitoring__ to the image and set the tag __latest__ .

Start the container with __docker run__ and pass it the list of environment variables defined in __env_file__ to be set in the container.

```bash
docker build --no-cache -t website-monitoring:latest .
docker run --env-file=env_file -d website-monitoring:latest
```

## Maintenance

Once the container is running, it writes its standard output and errors to a logfile.
The logs can be inspected in the running container.

```bash
# get name of container where IMAGE=website-monitoring:latest
docker ps -a
# open cli in running container
docker exec -it <container-name> /bin/sh
# inspect logfile
cat logfile
```

## Stop

To stop the running container, simply execute the following command

```bash
docker stop <container-name> 
```
