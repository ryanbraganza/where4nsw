"""
http://popcnt.org/2008/05/google-app-engine-tips.html
"""
if os.environ.get('SERVER_SOFTWARE','').startswith('Devel'):
    HOST='local'
elif os.environ.get('SERVER_SOFTWARE','').startswith('Goog'):
    HOST='google'
else:
    # logging.error('Unknown server. Production/development?')
    HOST='unknown'
