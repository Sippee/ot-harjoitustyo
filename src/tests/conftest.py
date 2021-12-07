import initialize_database


def pytest_configure():
    initialize_database.delete_db()
    initialize_database.create_db()