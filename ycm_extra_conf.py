def Settings( **kwargs ):
    return {
        'flags': ['-Wall', '-Wextra', '-Werror', '-fsanitize=address,undefined'],
    }
