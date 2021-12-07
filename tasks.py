from invoke import task

@task
def start(ctx):
    ctx.run("python src/index.py")


@task
def db(ctx):
    ctx.run("python src/initialize_database.py")


@task
def test(ctx):
    ctx.run("pytest src")


@task
def lint(ctx):
    ctx.run("pylint src")


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")


@task(coverage)
def coveragereport(ctx):
    ctx.run("coverage html")