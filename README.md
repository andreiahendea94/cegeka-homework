# CV REST-API

I have decided to explore and learn while doing this small project. That is why I've decided to use Docker to run Flask. I know I probably made it a bit too complicated but I honestly enjoyed working on this. I have also tried to parse unformatted text in the JSON object but I ran out of time and scrapped it.

I also recommend using Linux, because it's way faster to run the project.

## Installation

* [Download](https://www.docker.com/products/docker-desktop/) and Install Docker for [Windows](https://docs.docker.com/desktop/install/windows-install/) or [Linux](https://docs.docker.com/desktop/install/linux-install/)
  - For Windows users: Install [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) and [download Ubuntu](https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-10#3-download-ubuntu) from Microsoft Store

## Run the project
* Clone the project
* In the root folder of the project run the command `docker-compose up`
* Open a new tab in your favorite browser with the URL `http://localhost:8000/`. The port `:8000` is the default one, however if it is not available the output from the `docker-compose up` command will tell you the port the server is running on.

## Available endpoints
* `/personal`\
Sample URL: [http://localhost:8000/personal/](http://localhost:8000/personal/)\
HTTP Request Type: GET\
URL GET Parameters: N/A\
Response type: `application/json`\
Response format:
```{
    "address": "Street Brooklyn 99, ap. 10, floor 2",
    "country": "United States",
    "dateOfBirth": "1980-10-12",
    "fullName": "John Williams",
    "hobbies": "Guitar, Reading, Hiking",
    "languages": "English, Spanish",
    "phone": "+401235578"
}
```

* `/education`\
Sample URL: [http://localhost:8000/education/](http://localhost:8000/education/)\
HTTP Request Type: GET\
URL GET Parameters: N/A\
Response type: `application/json`\
Response format:
```
{
  "education": {
  "01-01-2019": "Politehnica University of Bucharest",
  "01-08-2014": "National College 'Mihai Viteazu'"
  }
}
```

* `/experience`\
Sample URL: [http://localhost:8000/experience/](http://localhost:8000/experience/)\
HTTP Request Type: GET\
URL GET Parameters: N/A\
Response type: `application/json`\
Response format:
```
{
  "experience": {
  "ING Bank": [
    "Renovated complete UI to make it more modern, user-friendly, maintainable and optimised for bank use.",
    "Shared the UI structure and guidelines to be incorporated, with development team of around 50 members."
  ],
  "TrustBank-CBS": [
    "Designed and developed modern and responsive UI of entire application.",
    "Made required graphics for the project in photoshop."
  ]
  },
  "skills": [
    "Python - Less than 1 year",
    "AWS - Less than 1 year",
    "Javascript - Less than 1 year",
    "CSS3 - 6 months"
  ]
}
```

## How to run CLI commands
* Check if the Docker container is running using `docker ps`. If it is not then start it using the command `docker-compose up`
* Connect to the `web` docker using the command `docker exec -it web sh`
* Run the command `flask --help` to get the list of available commands
* Currently there are 3 custom commands implemented:
  - `get-personal-details`
  - `get-education`
  - `get-experience`
* Run one of these commands in the `web` Docker container using the command `flask custom-command`. Where `custom-command` is one of the custom commands presented earlier.

Example: `flask get-personal-details`


