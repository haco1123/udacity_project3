from flask import Flask, request, jsonify
import logging
import re

import pymongo
from flask_pymongo import PyMongo
from flask_opentracing import FlaskTracing
from jaeger_client import Config
from jaeger_client.metrics.prometheus import PrometheusMetricsFactory
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from prometheus_flask_exporter import PrometheusMetrics
import requests


logging.basicConfig(format="%(message)s", level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()

metrics = PrometheusMetrics(app)
# static information as metric
metrics.info("app_info", "Application info", version="1.0.3")

app.config["MONGO_DBNAME"] = "example-mongodb"
app.config[
    "MONGO_URI"
] = "mongodb://example-mongodb-svc.default.svc.cluster.local:27017/example-mongodb"

mongo = PyMongo(app)

def init_tracer(service):

    config = Config(
        config={
            "sampler": {"type": "const", "param": 1},
            "logging": True,
            "reporter_batch_size": 1,
            "local_agent": {
                "reporting_host": "localhost",  # Passe dies an, falls Jaeger nicht lokal läuft
                "reporting_port": 6831,
            },
        },
        service_name=service,
        validate=True,
        metrics_factory=PrometheusMetricsFactory(service_name_label=service),
    )

    # this call also sets opentracing.tracer
    return config.initialize_tracer()


tracer = init_tracer("backend")
flask_tracer = FlaskTracing(tracer, True, app)


@app.route("/")
def homepage():
    with tracer.start_span("homepage") as span:
        span.set_tag('http.method', 'Hello World')
        span.set_tag('http.status_code', 200)
    return "Hello World"


@app.route("/api")
def my_api():
    with tracer.start_span("my-api") as span:
        answer = "something"
        span.set_tag('http.method', answer)
        span.set_tag('http.status_code', 200)
        
    return jsonify(repsonse=answer)


@app.route("/star", methods=["POST"])
def add_star():
    with tracer.start_span("post-new-star") as span:
        span.set_tag('http.method;', 'save in database')
        with tracer.start_span('save-star') as site_span:
            star = mongo.db.stars
            name = request.json["name"]
            distance = request.json["distance"]
            star_id = star.insert({"name": name, "distance": distance})
            new_star = star.find_one({"_id": star_id})
            output = {"name": new_star["name"], "distance": new_star["distance"]}
            site_span.set_tag("http.status_code", 200)
    return jsonify({"result": output})

if __name__ == "__main__":
    app.run()
