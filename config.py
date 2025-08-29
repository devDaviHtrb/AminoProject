class Config:
    from secrets import token_hex
    SESSION_KEY = token_hex(16)
    DEBUG = True
    SOCKETIO_ASYNC_MODE = "threading"
