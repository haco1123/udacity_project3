**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation

*TODO:* run `kubectl` command to show the running pods and services for all components. Take a screenshot of the output and include it here to verify the installation
- For all pods see screenshot `answer-img/all_pods.png`
- For all services see scrrenshot `answer-img/all_services.png`

## Setup the Jaeger and Prometheus source
*TODO:* Expose Grafana to the internet and then setup Prometheus as a data source. Provide a screenshot of the home page after logging into Grafana.
- see `answer-img/grafana_homepage.png`

## Create a Basic Dashboard
*TODO:* Create a dashboard in Grafana that shows Prometheus as a source. Take a screenshot and include it here.
- see `answer-img/grafana_firstBasicDashoboard.png`

## Describe SLO/SLI
*TODO:* Describe, in your own words, what the SLIs are, based on an SLO of *monthly uptime* and *request response time*.
- SLIs are measurable values, that specify the performance of a servie in ration to the SLO. 
- Possible SLIs could be:
  1. The percentage of time a service is running over a specific month
  2. The average time of a service to respond ot a request

## Creating SLI metrics.
*TODO:* It is important to know why we want to measure certain metrics for our customer. Describe in detail 5 metrics to measure these SLIs. 
1. Uptime Percentage:
    - Description: Measures the percentage of time the service is running and available within a given month.
    - Reason: This directly reflects the reliability of the service and ensures it meets the SLO for uptime.
2. Average Response Time:
    - Description: Calculates the average time taken by the service to respond to requests over a specific period.
    - Reason: Helps evaluate the performance of the service and ensures it meets the SLO for request response time.
3. Error Rate:
    - Description: The ratio of failed requests (e.g., HTTP 4xx and 5xx errors) to total requests.
    - Reason: Indicates the stability of the service and helps identify issues affecting uptime or response time.
4. 95th Percentile Response Time:
    - Description: Measures the response time below which 95% of all requests are completed.
    - Reason: Captures outliers and ensures the service performs well for the majority of users.
5. Request Throughput:
    - Description: The number of requests handled by the service per minute.
    - Reason: Ensures the service can handle the expected load without degrading performance or uptime.

## Create a Dashboard to measure our SLIs
*TODO:* Create a dashboard to measure the uptime of the frontend and backend services. We will also want to measure 40x and 50x errors. Create a dashboard that show these values over a 24 hour period and take a screenshot.
- see `answer-img/uptime_errors.png`

## Tracing our Flask App
*TODO:*  We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here. Also provide a (screenshot) sample Python file containing a trace and span code used to perform Jaeger traces on the backend service.
- screenshot for backend span, see `answer-img/backend_span1.png` and `answer-img/backend_span2.png`
- for the example python file, see `app/example-python.py`

## Jaeger in Dashboards
*TODO:* Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.
- see `answer-img/dashboard_with_trace.png`

## Report Error
*TODO:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue also include a screenshot of the tracer span to demonstrate how we can user a tracer to locate errors easily.

TROUBLE TICKET

Name: Backend Service Monitoring Issue

Date: April 16, 2025

Subject: High Latency and wrong span tags in Backend Service

Affected Area: Backend Service 

Severity: High

Description:
We are experiencing high latency and wrong span tags in the Backend Service. The issue appears to be related to the backend service, as indicated by the Jaeger trace spans. All backend routes are reachable, but have the wrong pang tags for logging

Steps to Reproduce:
1. Access the Backend service via localhost:8081.
2. Request localhost:8081/api.
3. Observe the latency and error rates in the Jaeger trace spans.

Recommended Actions:
1. Update the `app.py` file to ensure the tag names matche the content or update the resonse content reguaring the name.

- see `answer-img/report_error_spans.png`


## Creating SLIs and SLOs
*TODO:* We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name four SLIs that you would use to measure the success of this SLO.
1. Uptime Percentage
2. Error Rate
3. Request Latency (95th Percentile)
4. Request Success Rate

## Building KPIs for our plan
*TODO*: Now that we have our SLIs and SLOs, create a list of 2-3 KPIs to accurately measure these metrics as well as a description of why those KPIs were chosen. We will make a dashboard for this, but first write them down here.
1. Uptime Percentage
    - This KPI directly reflects the reliability of the service and ensures it meets the SLO of 99.95% uptime.
2. Error Rate
    - A high error rate indicates issues affecting service stability and availability, which could impact the SLO.
3. 95th Percentile Response Time
    - This KPI captures outliers and ensures the service performs well for the majority of users, aligning with performance-related SLIs.

## Final Dashboard
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  
- see `answer-img/final_dashboard.png`
- Description:
    1. Uptime Percentage: Displays the percentage of time the service was operational over the last 24 hours. This ensures the service meets the 99.95% uptime SLO.
    2. Error Rate: Shows the ratio of failed requests (HTTP 4xx and 5xx) to total requests, helping identify stability issues.
    3. 95th Percentile Response Time: Visualizes the response time for 95% of requests, ensuring performance consistency.
    4. Request Throughput: Tracks the number of requests handled per minute, ensuring the service can handle expected load.