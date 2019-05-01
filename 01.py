import sys
import time
import logging
from jaeger_client import Config

def init_tracer(service):
    logging.getLogger('').handlers = []
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)

    config = Config(
        config={
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'logging': True,
        },
        service_name=service,
    )

    # this call also sets opentracing.tracer
    return config.initialize_tracer()

def say_hello(hello_to):
    with tracer.start_span('say-hello') as span:
        hello_str = 'Hello, %s!' % hello_to
        span.set_tag('hello-to', hello_to)
        print(hello_str)

tracer = init_tracer('hello-world')

hello_to = sys.argv[1]
say_hello(hello_to)

time.sleep(2)
tracer.close()