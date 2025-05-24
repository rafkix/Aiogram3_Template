from .throttling import ThrottlingMiddleware

def setup_middlewares(router):
    router.message.middleware(ThrottlingMiddleware())
