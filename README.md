# RabbitMQ Async Messenger

A task I was set, to complete in 3 hours, as part of a job application. It consists of four components:
* printer.py waits for and prints/logs any messages received
* alarm_server.py can be run independently with a time argument of how long to wait until a message is sent
* parameter_server.py asynchronously ping messages randomly and according to the output of a time conversion...
* time_server.py converts time into 'virtual time' (as specified in the spec for the task)

The project uses RabbitMQ, pika and asyncio. 

## Getting Started

Ensure RabbitMQ is installed and running https://www.rabbitmq.com/download.html

git clone https://github.com/zacclery/RabbitMQ-Async-Messenger.git && cd RabbitMQ-Async-Messenger
##### Create virtualenv and activate
pip install -r requirements.txt

python printer.py

python alarm_server.py 0.001

python alarm_server.py 0.0002

python time_server.py

## Authors

**Zac Clery**

## License

This project is licensed under the MIT License
