from flask_graphql import GraphQLView

from src import app, init_db, schema, db


@app.route('/', methods=['GET', 'POST'])
def lambda_handler(event=None, context=None):
    return 'hello from Flask!'

app.add_url_rule('/graphql',
                 view_func=GraphQLView.as_view('graphql', schema=schema,
                                               graphiql=True))

@app.cli.command()
def initdb():
    """Initialize the database."""
    init_db()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db.remove()


if __name__ == '__main__':
    init_db()
    app.run()
