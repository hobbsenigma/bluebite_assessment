Andrew notes:

Time spent:
I spent a lot of time trying to get Docker and Pipenv working, and finally gave up on that approach.  I spent around 2 hours on the actual assignment (without effective debugging) before changing my approach.  After changing my approach, and installing postgres, I was able to finish the assignment in about 4 additional hours.

Additional work:
1. Make saving data to the database asynchronous to avoid database writes becoming a bottleneck.
2. Consider streaming responses for retrieval endpoints, in case of large result sets.
3. Remove database credentials from settings file.

# Blue Bite Assessment

## Introduction

This repo includes a stub Django project. We would like you to extend this project by adding three
routes and related validation logic. Included are example files and schema for the expected JSON
request structure.

We use this test to gain insight into your approach when solving a general problem, and to
gauge your familiarity with Django and its related dependencies. So if you are unable to complete
all the requirements due to time constraints or other issues with the local environment, please
submit your partial work.

While we are a test-driven engineering team, we understand take-home assessments can be
time-consuming and do not expect unit tests for this project, though if you'd like to write some
by all means feel free!

## Data Constraints

There is a JSON Schema that describes the format of incoming API request bodies.
[It can be found  here](files/schema.json). You may use it to validate the requests.
**Alternative validation methods, such as serialization, are allowed**.

Each object record will be part of an array and will look something like this:
```json
{
  "batch_id": "71a8a97591894dda9ea1a372c89b7987",
  "objects": [
    {
      "object_id": "d6f983a8905e48f29ad480d3f5969b52",
      "data": [
        {
          "key": "type",
          "value": "shoe"
        },
        {
          "key": "color",
          "value": "purple"
        }
      ]
    },
    {
      "object_id": "1125528d300d4538a33069a9456df4e8",
      "data": [
        {
          "key": "fizz",
          "value": "buzz"
        }
      ]
    }
  ]
}
```

Object records will contain a `data` array consisting of a random assortment of `key` and `value`
pairs. The values in both `key` and `value` are not normalized, but will always be strings.

`object_id` fields should be treated as unique.

The `batch_id` value for a submitted Object should be associated to the created Object in some way.

Example request bodies can be found in [files directory](files)

## Requirements

You are welcome to use whatever amount of time you see fit on this assessment, but we do not expect
developers to spend more than two hours implementing both parts. **If you used more or less than the
two-hour allotment, please indicate how much time you used in your repo's README.**

### Part 1

* The application should accept JSON requests via a route.
    * When the application receives a new request it must be validated, parsed and (if the data is correct) stored in the database.
    * The application must be able to handle validation errors. The format of the errors is your choice so long as it is consistent and adheres to HTTP protocol standards.

### Part 2
* Add two routes for Object retrieval
  * One retrieval endpoint that returns an object for a given `object_id`.
  * One list endpoint that can be filtered based on `data` keys and/or values.

## Submission

After finishing the requirements, or reaching your time constraints, **please document any unfinished
work you would have completed if given more time**.

Feel free to add any additional information you'd like us to know about your assessment as well
(code documentation, decision process for a specific design choice etc).

Once completed, please zip your assignment and email it to your point of contact at Blue Bite. You
may alternatively send us a link to your published GitHub Repo.

**If you choose to publish your solution, please do not fork the assessment repository.**


## Local Setup

This repo includes support for spinning up Django and a local Postgres server using Docker and
Pipenv.

**You are welcome to utilize other package managers, or a simple `requirements.txt` file if
preferred.**

If you choose to utilize the included Docker+Pipenv implementation, use the following steps to
set up the local environment.

Your system needs to be able to:
 - Run `docker-compose` (you will need an up-to-date version of `docker` installed).
 - Run a `bash` script.

Everything is dockerized so as long as you are running an up-to-date version of docker
then everything will work. The automated spin up maps the app port to `8000` for
convenience.

### Basic Spin-up

Run `./scripts/run-local`

This will spin up a `postgres` container and an `app` container that is running a bare
Django app on a hot-loaded debug server. After spin-up, the command will run the database
migrations. This does **not** seed any users or super users.

### Adding Additional Dependencies

When adding a dependency to the `pipfile`, make sure to rerun `./scripts/run-local`, or run
`docker-compose build`, or Docker will not properly pull in the new dep.
