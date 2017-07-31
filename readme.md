# hs-events
Copy the dotenv file and add your API keys
`cp .env.sample .env`

Create and activate virtualenv, zappa complains if venv and project are the same name.
`python3 -m venv ~/.virtualenvs/hs-events-venv`

`source ~/.virtualenvs/hs-events-venv/bin/activate`

Install requirements
`pip3 install -r requirements.txt`

Create and stage databse
`export FLASK_APP=manage.py && flask initdb`

Start the flask server
`export FLASK_APP=manage.py && flask run`


## Deployment
Lamda

Has issues with sqlite at the moment. Pg Support should work.

Zappa needs your virtualenv set up correctly forwarning.

`pip install awscli`

`aws configure`

...

```

AWS Access Key ID: foo
AWS Secret Access Key: bar
...
```

`zappa deploy api`

`zappa tail api`

`zappa undeploy api`

`zappa update api`

`zappa deploy production`

`zappa update api or deploy`


```
(Werkzeug 0.12.2 (/Users/ncrmro/.virtualenvs/hs-events-venv/lib/python3.5/site-packages), Requirement.parse('Werkzeug==0.12'), {'zappa'})
Calling update for stage sync_api..
Downloading and installing dependencies..
Packaging project as zip..
Uploading dev-sync-hs-events-api-sync-api-1495380831.zip (8.1MiB)..
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 8.47M/8.47M [00:01<00:00, 4.56MB/s]
Updating Lambda function code..
Updating Lambda function configuration..
Uploading dev-sync-hs-events-api-sync-api-template-1495380844.json (1.7KiB)..
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1.70K/1.70K [00:00<00:00, 6.33KB/s]
Deploying API Gateway..
Your updated Zappa deployment is live!: https://09gi23fqn1.execute-api.us-east-1.amazonaws.com/api
```

Check the url. For instance
/api/groups will return the meetup groups for instance



### GraphQL needs pg database at the moment.
Graphql API is available at /graphql with graphiql support.

Here is an example query
'''
{
  allMeetupGroups{
    edges{
      node{
        id
        name
      }
    }
  }
}'''