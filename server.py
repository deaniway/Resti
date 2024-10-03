if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv('.env')

    from src._project_.wsgi import application
    from src._project_.settings import DEPLOY_PORT, DEPLOY_ADDRESS

    from waitress import serve
    import logging

    logging.basicConfig(
        filename='debug.log',
        encoding='utf-8',
        level=logging.DEBUG
    )

    serve(
        app=application,
        host=DEPLOY_ADDRESS,
        port=DEPLOY_PORT
    )
