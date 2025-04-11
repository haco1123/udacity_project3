from jaeger_client import Config
from opentracing.ext import tags
from opentracing.propagation import Format
import requests


def init_tracer(service):
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
tracer = init_tracer('backend-service')


def example():
    with tracer.start_span('ExampleSpan') as span:
        req = requests.get('https://backend-service:8081/')
        span.set_tag('http.method;', req)
        def format():
            with tracer.start_span('my-test-span') as span:
                try:
                    print("success!")
                except:
                    print("try again")


if __name__ == "__main__":
    example()