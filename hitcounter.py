from flask import Flask
from redis import Redis
import os

hitcounter = Flask(__name__)
redis = Redis(host='redis', port=6379)
who = os.getenv('WHO', 'World')

@hitcounter.route('/')
def hello():
    redis.incr('hits')
    return 'Hello %s! I have been seen %s times.' % (who,redis.get('hits'))

if __name__ == "__main__":
    hitcounter.run(host="0.0.0.0", port=80)
